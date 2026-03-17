from pathlib import Path
from email import policy
from email.parser import BytesParser
from typing import List, Dict

def read_maildir(user_home: str, box: str = "new", limit: int = 20) -> List[Dict]:
    maildir_path = Path(user_home) / "Maildir" / box
    if not maildir_path.exists():
        return []

    files = sorted(maildir_path.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]
    out = []

    for f in files:
        raw = f.read_bytes()
        msg = BytesParser(policy=policy.default).parsebytes(raw)

        subject = str(msg.get("Subject", ""))
        from_ = str(msg.get("From", ""))
        to_ = str(msg.get("To", ""))
        date_ = str(msg.get("Date", ""))

        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = (part.get_content() or "").strip()
                    break
        else:
            body = (msg.get_content() or "").strip()

        out.append({
            "file": f.name,
            "subject": subject,
            "from": from_,
            "to": to_,
            "date": date_,
            "body": body,
        })

    return out