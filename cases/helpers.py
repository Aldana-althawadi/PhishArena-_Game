from cases.profiles import CASES, ACTIVE_CASE

def get_profile(target_email: str):
    return CASES.get(target_email.lower())

def get_active_case(target_email: str):
    profile = get_profile(target_email)
    if not profile:
        return None

    idx = ACTIVE_CASE.get(target_email.lower(), 0)
    cases = profile.get("cases", [])

    if idx < 0 or idx >= len(cases):
        return None

    return cases[idx]

def advance_case(target_email: str):
    email = target_email.lower()
    profile = get_profile(email)

    if not profile:
        return False

    current = ACTIVE_CASE.get(email, 0)
    total = len(profile.get("cases", []))

    if current + 1 < total:
        ACTIVE_CASE[email] = current + 1
        return True
    else:
        return False   