import re
import json
from llm.llm_handler import ask_llm


def normalize(text):
    return text.lower().strip()


def check_required_info(email_text, required_info):
    missing = []
    email_text = normalize(email_text)

    for item in required_info:
        if item.lower() not in email_text:
            missing.append(item)

    return missing


def build_prompt(email_text, case):
    return f"""
You are a cybersecurity training evaluator.

A player is writing a social engineering email.

--- SCENARIO ---
{case['mission_brief']}

--- REQUIRED INFORMATION ---
{case['required_info']}

--- PLAYER EMAIL ---
{email_text}

--- TASK ---
Evaluate the email based on:

1. Professionalism (formal tone, structured writing)
2. Realism (believability, logical request)
3. Completeness (includes required context)

--- SCORING ---
Give each score from 0 to 10.

--- OUTPUT FORMAT (STRICT JSON ONLY) ---
{{
    "status": true or false,
    "scores": {{
        "professionalism": number,
        "realism": number,
        "completeness": number
    }},
    "reason": "short explanation"
}}
"""


def extract_json(text):
    try:
        return json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    return None


def check_email_against_case(email_text, case):
    # Step 1: basic length check
    if len(email_text.split()) < 20:
        return {
            "status": False,
            "msg": "Your email is too short. Please write a more complete and professional message.",
            "scores": None
        }

    # Step 2: required info check
    missing = check_required_info(email_text, case["required_info"])
    if missing:
        return {
            "status": False,
            "msg": f"Missing important details: {', '.join(missing)}.",
            "scores": None
        }

    # Step 3: AI scoring
    prompt = build_prompt(email_text, case)
    llm_response = ask_llm(prompt)

    result = extract_json(llm_response)

    if not result:
        return {
            "status": False,
            "msg": "Evaluation failed. Try again.",
            "scores": None
        }

    scores = result.get("scores", {})
    professionalism = scores.get("professionalism", 0)
    realism = scores.get("realism", 0)
    completeness = scores.get("completeness", 0)

    avg_score = (professionalism + realism + completeness) / 3

    # PASS condition
    passed = avg_score >= 6

    if passed:
        return {
            "status": True,
            "msg": f"""Hello,

Your request has been verified successfully.

FLAG: {case['flag']}

Best regards,
{case['owner_name']}
PhishArena""",
            "scores": scores
        }
    else:
        return {
            "status": False,
            "msg": f"""Hello,

Your request was not convincing enough.

Reason:
{result.get("reason", "Improve professionalism and realism.")}

Scores:
- Professionalism: {professionalism}/10
- Realism: {realism}/10
- Completeness: {completeness}/10

Please improve your email and try again.

Best regards,
{case['owner_name']}
PhishArena""",
            "scores": scores
        }