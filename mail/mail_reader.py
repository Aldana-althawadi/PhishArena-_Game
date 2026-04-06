import os
import email
from email import policy
from email.utils import parseaddr

MAILBOXES = {
    "alice@emailme.com": "/home/alice/Maildir",
    "bob@emailme.com": "/home/bob/Maildir",
    "charlie@emailme.com": "/home/charlie/Maildir",
    "steven@emailme.com": "/home/steven/Maildir",
    "eve@emailme.com": "/home/eve/Maildir",
    "david@emailme.com": "/home/david/Maildir",
    "sophia@emailme.com": "/home/sophia/Maildir",
    "michael@emailme.com": "/home/michael/Maildir",
    "olivia@emailme.com": "/home/olivia/Maildir",
    "daniel@emailme.com": "/home/daniel/Maildir",
    "player1@emailme.com": "/home/player1/Maildir"
}


def extract_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    return part.get_content()
                except Exception:
                    continue
        return ""
    try:
        return msg.get_content()
    except Exception:
        return ""


def normalize_email(value):
    """
    Extract only the email address part from headers like:
    'Player One <player1@emailme.com>'
    """
    _, addr = parseaddr(str(value))
    return addr.strip().lower()


def get_latest_email(sender_filter=None, receiver_filter=None, case_id_filter=None):
    sender_filter = sender_filter.strip().lower() if sender_filter else None
    receiver_filter = receiver_filter.strip().lower() if receiver_filter else None
    case_id_filter = case_id_filter.strip().lower() if case_id_filter else None

    if receiver_filter not in MAILBOXES:
        return None

    base_path = MAILBOXES[receiver_filter]
    candidates = []

    for subfolder in ["new", "cur"]:
        folder = os.path.join(base_path, subfolder)
        if not os.path.exists(folder):
            continue

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if not os.path.isfile(file_path):
                continue

            try:
                with open(file_path, "rb") as f:
                    msg = email.message_from_binary_file(f, policy=policy.default)
            except Exception:
                continue

            from_email = normalize_email(msg.get("From", ""))
            to_email = normalize_email(msg.get("To", ""))
            subject = str(msg.get("Subject", "")).strip().lower()

            if sender_filter and from_email != sender_filter:
                continue

            if receiver_filter and to_email != receiver_filter:
                continue

            if case_id_filter and case_id_filter not in subject:
                continue

            candidates.append((file_path, msg))

    if not candidates:
        return None

    latest_file, latest_msg = max(candidates, key=lambda item: os.path.getmtime(item[0]))

    return {
        "subject": str(latest_msg.get("Subject", "")),
        "from": normalize_email(latest_msg.get("From", "")),
        "to": normalize_email(latest_msg.get("To", "")),
        "body": extract_body(latest_msg)
    }