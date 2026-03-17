import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from data.emails import EMAILS
from mail.smtp_sender import send_email_smtp

# Fixed mixed order for the training inbox
SEND_ORDER = [
    "E10", "E03", "E14", "E01",
    "E12", "E06", "E16", "E05",
    "E09", "E07", "E13", "E04",
    "E11", "E08", "E15", "E02"
]

RECIPIENT = "bob@emailme.com"


def get_email_by_id(email_id):
    for email in EMAILS:
        if email["id"] == email_id:
            return email
    return None


def main():
    sent_count = 0

    for email_id in SEND_ORDER:
        email = get_email_by_id(email_id)
        if not email:
            print(f"Skipping missing email ID: {email_id}")
            continue

        subject = f"[{email['id']}] {email['subject']}"

        send_email_smtp(
            sender=email["sender"],
            recipient=RECIPIENT,
            subject=subject,
            body=email["body"],
            smtp_host="localhost",
            smtp_port=25
        )

        print(f"Sent: {email['id']} -> {RECIPIENT}")
        sent_count += 1

    print(f"\nDone. Sent {sent_count} emails to {RECIPIENT}.")


if __name__ == "__main__":
    main()