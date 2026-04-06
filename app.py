from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from email.utils import parseaddr

from cases.profiles import CASES
from cases.helpers import (
    get_progress_summary,
    get_all_cases,
    get_case_by_id,
    get_cases_by_level_sorted,
    is_case_completed,
    get_first_incomplete_case_in_level,
    can_open_case,
    get_next_case_in_level,
    get_available_active_cases_for_player,
    LEVEL_ORDER,
    get_unlocked_levels,
    advance_case,
)
from logs.log_reader import read_game_logs
from logs.game_logger import log_game_event
from mail.mail_reader import get_latest_email
from mail.smtp_sender import send_email_smtp
from llm.checker import check_email_against_case

app = Flask(__name__)
app.secret_key="stoe"

PLAYER_EMAIL = "player1@emailme.com"
PLAYER_USERNAME = "player1"


@app.route("/")
def home():
    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)

    return render_template(
        "index.html",
        username=PLAYER_USERNAME,
        player_email=PLAYER_EMAIL,
        total_targets=len(CASES),
        total_cases=sum(len(profile.get("cases", [])) for profile in CASES.values()),
        total_levels=len(progress["levels"]),
        total_flags=progress["total_flags"],
        progress=progress,
    )


@app.route("/profiles")
def profiles():
    return render_template(
        "profiles.html",
        profiles=CASES
    )


@app.route("/levels")
def levels():
    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)

    selected_level = request.args.get("level", "Junior")
    level_cases = get_cases_by_level_sorted(selected_level)

    submitted_flags = session.get("submitted_flags", {})
    completed_case_ids = set(
        cid for cid, is_done in submitted_flags.items() if is_done
    )

    # level unlock still depends on completed levels
    unlocked_levels = get_unlocked_levels(completed_case_ids)
    selected_level_unlocked = selected_level in unlocked_levels

    if selected_level_unlocked:
        for case in level_cases:
            case["completed"] = case["case_id"] in completed_case_ids
            case["openable"] = can_open_case(case, completed_case_ids)
    else:
        for case in level_cases:
            case["completed"] = case["case_id"] in completed_case_ids
            case["openable"] = False

    # rebuild progress display using submitted flags
    levels_summary = []
    for level_name in LEVEL_ORDER:
        level_all_cases = get_cases_by_level_sorted(level_name)
        total_count = len(level_all_cases)
        done_count = sum(1 for c in level_all_cases if c["case_id"] in completed_case_ids)

        levels_summary.append({
            "level": level_name,
            "done": done_count,
            "total": total_count,
            "unlocked": level_name in unlocked_levels,
            "completed": total_count > 0 and done_count == total_count
        })

    progress["levels"] = levels_summary
    progress["completed_case_ids"] = completed_case_ids
    progress["unlocked_levels"] = unlocked_levels
    progress["total_completed_cases"] = len(completed_case_ids)

    return render_template(
        "levels.html",
        username=PLAYER_USERNAME,
        player_email=PLAYER_EMAIL,
        progress=progress,
        selected_level=selected_level,
        level_cases=level_cases,
        selected_level_unlocked=selected_level_unlocked,
    )

@app.route("/case/<case_id>")
def case_page(case_id):
    case = get_case_by_id(case_id)
    if not case:
        return "Case not found", 404

    # completion now depends on submitted flags, not only AI success
    submitted_flags = session.get("submitted_flags", {})
    case_completed = submitted_flags.get(case_id, False)

    # only allow opening the first incomplete case in a level
    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)

    # use submitted flags for real progress in UI
    completed_case_ids = set(
        cid for cid, is_done in submitted_flags.items() if is_done
    )

    case_openable = can_open_case(case, completed_case_ids)
    next_case = get_next_case_in_level(case)

    feedback = session.pop(f"feedback_{case_id}", None)

    return render_template(
        "case.html",
        username=PLAYER_USERNAME,
        player_email=PLAYER_EMAIL,
        case=case,
        case_completed=case_completed,
        case_openable=case_openable,
        next_case=next_case,
        feedback=feedback,
    )

@app.post("/case/<case_id>/process")
def process_case(case_id):
    case = get_case_by_id(case_id)
    if not case:
        return jsonify({"ok": False, "message": "Case not found."}), 404

    submitted_flags = session.get("submitted_flags", {})
    completed_case_ids = set(cid for cid, is_done in submitted_flags.items() if is_done)

    if not can_open_case(case, completed_case_ids):
        return jsonify({"ok": False, "message": "This case is locked right now."}), 403

    email_data = get_latest_email(
        sender_filter=PLAYER_EMAIL,
        receiver_filter=case["target_email"]
    )

    if not email_data:
        return jsonify({
            "ok": False,
            "message": f"No matching email found from {PLAYER_EMAIL} to {case['target_email']}."
        }), 404

    sender_name, sender_email = parseaddr(email_data.get("from", ""))
    sender_email = sender_email.strip().lower()

    receiver = email_data.get("to", "").strip().lower()
    subject = email_data.get("subject", "")
    body = email_data.get("body", "")

    if sender_email != PLAYER_EMAIL:
        return jsonify({
            "ok": False,
            "message": f"Email sender mismatch. Found: {sender_email}, expected: {PLAYER_EMAIL}"
        }), 400

    if receiver != case["target_email"]:
        return jsonify({
            "ok": False,
            "message": f"Email receiver mismatch. Found: {receiver}, expected: {case['target_email']}"
        }), 400

    result = check_email_against_case(body, case)

    if not result:
        return jsonify({"ok": False, "message": "Checker returned no result."}), 500

    if "status" not in result or "msg" not in result:
        return jsonify({
            "ok": False,
            "message": f"Checker returned invalid result: {result}"
        }), 500

    log_game_event(
        player=sender_email,
        target=receiver,
        case_id=case["case_id"],
        level=case.get("level", ""),
        status=result["status"],
        flag=case.get("flag", "") if result["status"] else "",
        message=result["msg"],
        scores=result.get("scores")
    )

    try:
        send_email_smtp(
            sender=receiver,
            recipient=sender_email,
            subject=f"Re: {subject}" if subject else "Re: Your Request",
            body=result["msg"],
            smtp_host="localhost",
            smtp_port=25
        )
    except Exception as e:
        return jsonify({
            "ok": False,
            "message": f"SMTP failed: {str(e)}"
        }), 500

    if result["status"]:
        game_message = "Your email was accepted. Check your inbox for the staff response and submit the flag."
    else:
        game_message = result["msg"]

    session[f"feedback_{case_id}"] = {
        "status": result["status"],
        "message": game_message,
        "scores": result.get("scores")
    }

    return jsonify({
        "ok": True,
        "status": "success" if result["status"] else "failed",
        "message": game_message,
        "redirect_url": url_for("case_page", case_id=case_id)
    })


@app.route("/rules")
def rules():
    return render_template(
        "rules.html",
        username=PLAYER_USERNAME,
        player_email=PLAYER_EMAIL,
    )

@app.route("/dashboard")
def dashboard():
    import json

    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)
    active_cases = get_available_active_cases_for_player(log_rows, PLAYER_EMAIL)

    player_logs = [
        row for row in log_rows
        if str(row.get("player", "")).strip().lower() == PLAYER_EMAIL.lower()
    ]

    total_attempts = len(player_logs)
    total_success = sum(1 for row in player_logs if str(row.get("status", "")).strip().upper() == "SUCCESS")
    total_failed = total_attempts - total_success

    professionalism_scores = []
    realism_scores = []
    completeness_scores = []

    level_stats = {}

    for row in player_logs:
        level = row.get("level", "Unknown")
        if level not in level_stats:
            level_stats[level] = {"attempts": 0, "success": 0}

        level_stats[level]["attempts"] += 1
        if str(row.get("status", "")).strip().upper() == "SUCCESS":
            level_stats[level]["success"] += 1

        raw_scores = row.get("scores", "")
        if raw_scores:
            try:
                scores = json.loads(raw_scores)
                professionalism_scores.append(scores.get("professionalism", 0))
                realism_scores.append(scores.get("realism", 0))
                completeness_scores.append(scores.get("completeness", 0))
            except Exception:
                pass

    def avg(values):
        return round(sum(values) / len(values), 2) if values else 0

    analytics = {
        "total_attempts": total_attempts,
        "total_success": total_success,
        "total_failed": total_failed,
        "avg_professionalism": avg(professionalism_scores),
        "avg_realism": avg(realism_scores),
        "avg_completeness": avg(completeness_scores),
        "level_stats": level_stats
    }

    return render_template(
        "dashboard.html",
        username=PLAYER_USERNAME,
        player_email=PLAYER_EMAIL,
        progress=progress,
        active_cases=active_cases,
        analytics=analytics
    )


@app.route("/debug-progress")
def debug_progress():
    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)

    return {
        "player": PLAYER_EMAIL,
        "log_count": len(log_rows),
        "logs": log_rows,
        "completed_case_ids": list(progress["completed_case_ids"]),
        "collected_flags": list(progress["collected_flags"]),
        "levels": progress["levels"],
    }   


@app.route("/reset-game")
def reset_game():
    import os
    from cases.helpers import reset_active_cases

    reset_active_cases()

    if os.path.exists("logs/game_log.csv"):
        os.remove("logs/game_log.csv")

    session.clear()

    return redirect(url_for("home"))    


@app.route("/submit_flag/<case_id>", methods=["POST"])
def submit_flag(case_id):
    user_flag = request.form.get("flag", "").strip()

    case = get_case_by_id(case_id)
    if not case:
        return "Case not found", 404

    if user_flag != case.get("flag", ""):
        session[f"feedback_{case_id}"] = {
            "status": False,
            "message": "Incorrect flag. Please check your email reply and try again."
        }
        return redirect(url_for("case_page", case_id=case_id))

    # mark completed in session
    completed_flags = session.get("submitted_flags", {})
    completed_flags[case_id] = True
    session["submitted_flags"] = completed_flags

    # now move to next active case
    advance_case(case["target_email"])

    session[f"feedback_{case_id}"] = {
        "status": True,
        "message": "Correct flag submitted. The next case is now unlocked."
    }

    return redirect(url_for("case_page", case_id=case_id))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)