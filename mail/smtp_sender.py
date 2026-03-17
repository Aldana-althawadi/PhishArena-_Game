import smtplib
from email.message import EmailMessage

def send_email_smtp(sender: str, recipient: str, subject: str, body: str,
                    smtp_host: str = "localhost", smtp_port: int = 25) -> None:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.send_message(msg)