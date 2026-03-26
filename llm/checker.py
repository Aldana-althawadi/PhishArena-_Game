def check_email_against_case(email_text, case):
    """
    Checks if the email satisfies the required conditions of a case.
    Returns:
        {
            "status": True/False,
            "msg": response message
        }
    """

    if not email_text or not case:
        return {
            "status": False,
            "msg": "Invalid input provided."
        }

    text = email_text.lower()

    required = case.get("required_info", [])
    flag = case.get("flag", "FLAG-XXXX")
    failure_msg = case.get("failure_msg", "Missing required information.")
    name = case.get("owner_name", "Raven Organization")
    role = case.get("owner_role", "Staff Member")
    department = case.get("owner_department", "Raven Organization")

    missing = [item for item in required if item.lower() not in text]

    if not missing:
        success_msg = f"""Hello,

Thank you. Your request has been verified successfully.

FLAG: {flag}

Best regards,
{name}
{role}
{department}
"""
        return {
            "status": True,
            "msg": success_msg
        }

    return {
        "status": False,
        "msg": failure_msg
    }