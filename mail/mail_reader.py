import os
import email
from email import policy

MAILBOXES = {
    "alice@emailme.com": "/home/alice/Maildir",
    "bob@emailme.com": "/home/bob/Maildir"
}


def read_latest_from_folder(folder_path):
    if not os.path.exists(folder_path):
        return None

    files = sorted(os.listdir(folder_path), reverse=True)
    if not files:
        return None

    latest_file = os.path.join(folder_path, files[0])

    with open(latest_file, "rb") as f:
        msg = email.message_from_binary_file(f, policy=policy.default)

    subject = str(msg.get("Subject", ""))
    from_email = str(msg.get("From", "")).lower()
    to_email = str(msg.get("To", "")).lower()

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_content()
                break
    else:
        body = msg.get_content()

    return {
        "subject": subject,
        "from": from_email,
        "to": to_email,
        "body": body
    }


def get_latest_email():
    latest_candidates = []

    for _, base_path in MAILBOXES.items():
        for subfolder in ["new", "cur"]:
            folder = os.path.join(base_path, subfolder)
            if not os.path.exists(folder):
                continue

            files = [
                os.path.join(folder, f)
                for f in os.listdir(folder)
            ]

            for f in files:
                if os.path.isfile(f):
                    latest_candidates.append(f)

    if not latest_candidates:
        return None

    latest_file = max(latest_candidates, key=os.path.getmtime)

    with open(latest_file, "rb") as f:
        msg = email.message_from_binary_file(f, policy=policy.default)

    subject = str(msg.get("Subject", ""))
    from_email = str(msg.get("From", "")).lower()
    to_email = str(msg.get("To", "")).lower()

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_content()
                break
    else:
        body = msg.get_content()

    return {
        "subject": subject,
        "from": from_email,
        "to": to_email,
        "body": body
    }