from llm.pipeline import analyze_email_pipeline

def generate_ai_reply(email_text: str) -> dict:
    """
    Returns:
      {
        "analysis": {...pipeline output...},
        "reply_text": "..."
      }
    """
    analysis = analyze_email_pipeline(email_text)

    is_phish = analysis.get("is_phishing")
    flags = analysis.get("flags", [])
    phish_type = analysis.get("phishing_type", "")
    confidence = analysis.get("confidence", 0.0)

    if is_phish:
        reply = (
            "Hi,\n\n"
            "I can’t proceed with this request because this email appears suspicious.\n"
            f"Reason: {phish_type} | Flags: {', '.join(flags)} | Confidence: {confidence:.2f}\n\n"
            "Please contact the organization using the official website/app (not via links in the email).\n\n"
            "Regards"
        )
    else:
        reply = (
            "Hi,\n\n"
            "Thanks for your email. I received it and will review it shortly.\n\n"
            "Regards"
        )

    return {"analysis": analysis, "reply_text": reply}