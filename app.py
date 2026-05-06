from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from email.utils import parseaddr
import webbrowser
import threading
import os
import json

from cases.profiles import CASES
from cases.helpers import (
    get_progress_summary,
    get_case_by_id,
    get_cases_by_level_sorted,
    can_open_case,
    get_next_case_in_level,
    get_available_active_cases_for_player,
    LEVEL_ORDER,
    get_unlocked_levels,
    advance_case,
    reset_active_cases,
)
from logs.log_reader import read_game_logs
from logs.game_logger import log_game_event
from mail.mail_reader import get_latest_email
from mail.smtp_sender import send_email_smtp
from llm.checker import check_email_against_case


app = Flask(__name__)
app.secret_key = "stoe"

PLAYER_EMAIL = "player1@emailme.com"
PLAYER_USERNAME = "player1"

# True = browser-based submission for testing
# False = original Thunderbird/email mode
WEB_SUBMISSION_MODE = False 

PROGRESS_FILE = "logs/player_progress.json"


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")


# =========================
# Shared progress helpers
# =========================

def load_player_progress():
    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(PROGRESS_FILE):
        return {}

    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_player_progress(progress_data):
    os.makedirs("logs", exist_ok=True)

    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress_data, f, indent=2)


def get_completed_case_ids_for_player(player_email):
    progress_data = load_player_progress()
    return set(progress_data.get(player_email, []))


def mark_case_completed_for_player(player_email, case_id):
    progress_data = load_player_progress()
    completed = set(progress_data.get(player_email, []))
    completed.add(case_id)
    progress_data[player_email] = list(completed)
    save_player_progress(progress_data)


# =========================
# Routes
# =========================

@app.route("/")
def home():
    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)

    completed_case_ids = get_completed_case_ids_for_player(PLAYER_EMAIL)
    progress["total_completed_cases"] = len(completed_case_ids)

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


@app.route("/rules")
def rules():
    return render_template(
        "rules.html",
        username=PLAYER_USERNAME,
        player_email=PLAYER_EMAIL,
    )


@app.route("/levels")
def levels():
    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)

    selected_level = request.args.get("level", "Junior")
    level_cases = get_cases_by_level_sorted(selected_level)

    completed_case_ids = get_completed_case_ids_for_player(PLAYER_EMAIL)

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
    progress["completed_case_ids"] = list(completed_case_ids)
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

    completed_case_ids = get_completed_case_ids_for_player(PLAYER_EMAIL)
    case_completed = case_id in completed_case_ids

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
        web_submission_mode=WEB_SUBMISSION_MODE,
    )


@app.post("/case/<case_id>/process")
def process_case(case_id):
    """
    Original email-based mode.
    Reads the latest email from Maildir for the target mailbox.
    """
    case = get_case_by_id(case_id)
    if not case:
        return jsonify({"ok": False, "message": "Case not found."}), 404

    completed_case_ids = get_completed_case_ids_for_player(PLAYER_EMAIL)

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


@app.post("/case/<case_id>/submit-text")
def submit_text_case(case_id):
    """
    Web submission mode for multi-device testing.
    """
    case = get_case_by_id(case_id)
    if not case:
        return jsonify({"ok": False, "message": "Case not found."}), 404

    completed_case_ids = get_completed_case_ids_for_player(PLAYER_EMAIL)

    if not can_open_case(case, completed_case_ids):
        return jsonify({"ok": False, "message": "This case is locked right now."}), 403

    user_text = request.form.get("email_text", "").strip()

    if not user_text:
        return jsonify({"ok": False, "message": "Please write your message first."}), 400

    result = check_email_against_case(user_text, case)

    if not result or "status" not in result or "msg" not in result:
        return jsonify({"ok": False, "message": "Checker returned invalid result."}), 500

    log_game_event(
        player=PLAYER_EMAIL,
        target=case["target_email"],
        case_id=case["case_id"],
        level=case.get("level", ""),
        status=result["status"],
        flag=case.get("flag", "") if result["status"] else "",
        message=result["msg"],
        scores=result.get("scores")
    )

    if result["status"]:
        game_message = "Your message was accepted. The flag has been revealed below. Submit it to unlock the next case."
        revealed_flag = case.get("flag", "")
    else:
        game_message = result["msg"]
        revealed_flag = None

    session[f"feedback_{case_id}"] = {
        "status": result["status"],
        "message": game_message,
        "scores": result.get("scores"),
        "revealed_flag": revealed_flag
    }

    return jsonify({
        "ok": True,
        "status": "success" if result["status"] else "failed",
        "message": game_message,
        "redirect_url": url_for("case_page", case_id=case_id)
    })


@app.route("/dashboard")
def dashboard():
    log_rows = read_game_logs()
    progress = get_progress_summary(log_rows, PLAYER_EMAIL)
    active_cases = get_available_active_cases_for_player(log_rows, PLAYER_EMAIL)

    player_logs = [
        row for row in log_rows
        if str(row.get("player", "")).strip().lower() == PLAYER_EMAIL.lower()
    ]

    total_attempts = len(player_logs)
    total_success = sum(
        1 for row in player_logs
        if str(row.get("status", "")).strip().upper() == "SUCCESS"
    )
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
    completed_case_ids = get_completed_case_ids_for_player(PLAYER_EMAIL)

    return {
        "player": PLAYER_EMAIL,
        "log_count": len(log_rows),
        "logs": log_rows,
        "shared_completed_case_ids": list(completed_case_ids),
        "collected_flags": list(progress["collected_flags"]),
        "levels": progress["levels"],
    }


@app.route("/reset-game")
def reset_game():
    reset_active_cases()

    if os.path.exists("logs/game_log.csv"):
        os.remove("logs/game_log.csv")

    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)

    session.clear()

    return redirect(url_for("home"))
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)


@app.route("/submit_flag/<case_id>", methods=["POST"])
def submit_flag(case_id):
    user_flag = request.form.get("flag", "").strip()

    case = get_case_by_id(case_id)
    if not case:
        return "Case not found", 404

    if user_flag != case.get("flag", ""):
        session[f"feedback_{case_id}"] = {
            "status": False,
            "message": "Incorrect flag. Please try again.",
            "scores": None,
            "revealed_flag": case.get("flag", "") if WEB_SUBMISSION_MODE else None
        }
        return redirect(url_for("case_page", case_id=case_id))

    mark_case_completed_for_player(PLAYER_EMAIL, case_id)
    advance_case(case["target_email"])

    session[f"feedback_{case_id}"] = {
        "status": True,
        "message": "Correct flag submitted. The next case is now unlocked.",
        "scores": None,
        "revealed_flag": None
    }

    return redirect(url_for("case_page", case_id=case_id))


if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, host="0.0.0.0", port=5000)