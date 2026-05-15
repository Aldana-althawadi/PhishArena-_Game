# hybird evaluation engine  
import re
import json
from llm.llm_handler import ask_llm


def normalize(text):
    if not text:
        return ""

    text = text.lower().strip()
    text = re.sub(r"[_\-]+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def check_required_info(email_text, required_info): 
    missing = []
    normalized_email = normalize(email_text)

    for item in required_info:
        if isinstance(item, str):
            if normalize(item) not in normalized_email:
                missing.append(item)

        elif isinstance(item, list):
            found = False
            for phrase in item:
                if normalize(phrase) in normalized_email:
                    found = True
                    break

            if not found:
                missing.append(" / ".join(item))

    return missing


def score_professionalism(email_text):
    score = 4
    lowered = email_text.lower()

    greetings = ["hi ", "hello ", "dear "]
    closings = ["best regards", "regards", "sincerely", "thank you"]
    polite_words = ["please", "kindly", "appreciate", "thank you"]

    if any(g in lowered for g in greetings):
        score += 2

    if any(c in lowered for c in closings):
        score += 2

    if any(w in lowered for w in polite_words):
        score += 1

    if len(email_text.split()) >= 35:
        score += 1

    return min(score, 10)


def score_realism(email_text):
    score = 4
    lowered = email_text.lower()

    if "subject:" not in lowered:
        score += 1

    if any(word in lowered for word in ["please", "assist", "confirm", "verify", "request"]):
        score += 2

    if len(email_text.split()) >= 30:
        score += 2

    if "\n" in email_text:
        score += 1

    return min(score, 10)


def score_completeness(email_text, required_info):
    total = len(required_info)

    if total == 0:
        return 10

    missing = check_required_info(email_text, required_info)
    matched = total - len(missing)

    score = round((matched / total) * 10, 1)
    return max(0, min(score, 10))


def build_prompt(email_text, case, local_scores):
    return f"""
You are evaluating a training-game email submission.

Case mission:
{case.get('mission_brief', '')}

Expected from player:
{case.get('expected_from_player', '')}

Required information:
{case.get('required_info', [])}

Player email:
{email_text}

Local pre-scores:
- professionalism: {local_scores['professionalism']}
- realism: {local_scores['realism']}
- completeness: {local_scores['completeness']}

Instructions:
- Be fair and game-friendly.
- Accept similar wording, not only exact phrases.
- Do not be overly strict.
- If the email is reasonable for a student training game, score it fairly.
- Keep scores between 0 and 10.
- Return ONLY valid JSON.
- Do not use markdown.
- Do not add any explanation outside the JSON.
- The JSON must start with {{ and end with }}.
- Do not omit closing brackets.

Return exactly:
{{
  "status": true,
  "scores": {{
    "professionalism": 0,
    "realism": 0,
    "completeness": 0
  }},
  "reason": "short explanation"
}}
"""


def extract_json(text):
    """
    Extract JSON from LLM output and repair simple incomplete JSON when possible.
    """
    if not text:
        return None

    text = text.strip()
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except Exception:
        pass

    match = re.search(r"\{.*", text, re.DOTALL)
    if not match:
        return None

    candidate = match.group().strip()

    try:
        return json.loads(candidate)
    except Exception:
        pass

    open_braces = candidate.count("{")
    close_braces = candidate.count("}")

    if open_braces > close_braces:
        candidate = candidate + ("}" * (open_braces - close_braces))

    try:
        return json.loads(candidate)
    except Exception:
        return None


def safe_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default


def merge_scores(local_scores, ai_scores):
    ai_prof = safe_float(ai_scores.get("professionalism"), local_scores["professionalism"])
    ai_real = safe_float(ai_scores.get("realism"), local_scores["realism"])
    ai_comp = safe_float(ai_scores.get("completeness"), local_scores["completeness"])

    final_scores = {
        "professionalism": round((local_scores["professionalism"] * 0.6) + (ai_prof * 0.4), 1),
        "realism": round((local_scores["realism"] * 0.6) + (ai_real * 0.4), 1),
        "completeness": round((local_scores["completeness"] * 0.7) + (ai_comp * 0.3), 1),
    }

    return final_scores


def get_pass_threshold(case):
    level = case.get("level", "Junior")

    thresholds = {
        "Junior": 5.0,
        "Senior": 5.5,
        "Head": 6.0,
        "Chief": 6.5,
        "CEO": 7.0,
    }

    return thresholds.get(level, 6.0)


def build_success_message(case):
    return f"""Hello,

Your request has been verified successfully.

FLAG: {case['flag']}

Best regards,
{case['owner_name']}
PhishArena"""


def build_failure_message(case, reason, professionalism, realism, completeness):
    return f"""Hello,

Your request was not convincing enough.

Reason:
{reason}

Scores:
- Professionalism: {professionalism}/10
- Realism: {realism}/10
- Completeness: {completeness}/10

Please improve your email and try again.

Best regards,
{case['owner_name']}
PhishArena"""


def check_email_against_case(email_text, case):
    try:
        if len(email_text.split()) < 20:
            return {
                "status": False,
                "msg": "Your email is too short. Please write a more complete and professional message.",
                "scores": None
            }

        missing = check_required_info(email_text, case.get("required_info", []))
        if missing:
            return {
                "status": False,
                "msg": f"Missing important details: {', '.join(missing)}.",
                "scores": None
            }

        local_scores = {
            "professionalism": score_professionalism(email_text),
            "realism": score_realism(email_text),
            "completeness": score_completeness(email_text, case.get("required_info", []))
        }

        final_scores = local_scores.copy()
        final_reason = "Local evaluation used."
        ai_status = False

        try:
            prompt = build_prompt(email_text, case, local_scores)
            llm_response = ask_llm(prompt)

            print("\n[DEBUG] Raw LLM response:\n", llm_response)

            result = extract_json(llm_response)

            if result:
                ai_scores = result.get("scores", {})
                final_scores = merge_scores(local_scores, ai_scores)
                final_reason = result.get("reason", "AI-assisted evaluation used.")
                ai_status = bool(result.get("status", False))
            else:
                print("[DEBUG] Invalid AI JSON. AI evaluation rejected.")

                final_scores = {
                    "professionalism": 0,
                    "realism": 0,
                    "completeness": 0
                }

                final_reason = "AI response could not be parsed correctly, so the AI evaluation was rejected."
                ai_status = False

        except Exception as ai_error:
            print("[DEBUG] AI evaluation error:", str(ai_error))

            final_scores = {
                "professionalism": 0,
                "realism": 0,
                "completeness": 0
            }

            final_reason = "AI evaluation error occurred, so the AI evaluation was rejected."
            ai_status = False

        professionalism = safe_float(final_scores.get("professionalism"), 0)
        realism = safe_float(final_scores.get("realism"), 0)
        completeness = safe_float(final_scores.get("completeness"), 0)

        avg_score = round((professionalism + realism + completeness) / 3, 2)
        required_avg = get_pass_threshold(case)

        final_reason = (
            f"Average score is {avg_score}/10. "
            f"Required score is {required_avg}/10. "
            f"{final_reason}"
        )

        passed = (avg_score >= required_avg) and ai_status

        if passed:
            return {
                "status": True,
                "msg": build_success_message(case),
                "scores": {
                    "professionalism": professionalism,
                    "realism": realism,
                    "completeness": completeness
                }
            }

        return {
            "status": False,
            "msg": build_failure_message(
                case,
                final_reason,
                professionalism,
                realism,
                completeness
            ),
            "scores": {
                "professionalism": professionalism,
                "realism": realism,
                "completeness": completeness
            }
        }

    except Exception as e:
        print("[ERROR] check_email_against_case:", str(e))
        return {
            "status": False,
            "msg": "Temporary evaluation error. Please try again.",
            "scores": None
        }