def unique_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def fix_output(result, email_text):
    """
    Improve LLM output:
    - ensure useful phishing flags
    - ensure explanation always exists
    - stabilize confidence
    """

    text = (email_text or "").lower()
    flags = result.get("flags", []) or []

    # F1: urgency / pressure
    urgency_words = ["urgent", "immediately", "within 24 hours", "asap", "now"]
    if any(word in text for word in urgency_words):
        if "F1" not in flags:
            flags.append("F1")

    # F3: suspicious link
    if "http://" in text or "https://" in text:
        if "F3" not in flags:
            flags.append("F3")

    # F4: credential / account request
    credential_words = ["password", "login", "verify", "account", "reset", "username"]
    if any(word in text for word in credential_words):
        if "F4" not in flags:
            flags.append("F4")

    # Explanation fix
    explanation = str(result.get("explanation", "")).strip()
    is_phishing = result.get("is_phishing")

    if not explanation or len(explanation) < 20:
        if is_phishing:
            explanation = (
                "The email contains phishing indicators such as urgency, suspicious links, "
                "or requests related to account verification."
            )
        else:
            explanation = (
                "The email appears legitimate because it does not show strong phishing indicators "
                "such as suspicious links or credential requests."
            )

    # Confidence fix
    confidence = result.get("confidence", 0.5)
    try:
        confidence = float(confidence)
    except (TypeError, ValueError):
        confidence = 0.5

    if is_phishing is True and confidence < 0.6:
        confidence = 0.7
    elif is_phishing is False and confidence > 0.6:
        confidence = 0.6

    return {
        "is_phishing": is_phishing,
        "phishing_type": result.get("phishing_type", ""),
        "flags": unique_keep_order(flags),
        "confidence": round(confidence, 2),
        "explanation": explanation
    }