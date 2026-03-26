from email.utils import parseaddr
from mail.mail_reader import get_latest_email
from cases.helpers import get_active_case, advance_case
from cases.profiles import CASES
from llm.checker import check_email_against_case
from mail.smtp_sender import send_email_smtp
from logs.game_logger import log_game_event


def main():
    email_data = get_latest_email()

    if not email_data:
        print("No email found.")
        return

    sender_name, sender_email = parseaddr(email_data["from"])
    sender_email = sender_email.strip().lower()

    receiver = email_data["to"].strip().lower()
    subject = email_data["subject"]
    body = email_data["body"]

    print("\n=== CURRENT CASE ===")
    print(f"Target: {receiver}")
    case = get_active_case(receiver)

    if not case:
        print(f"No active case found for: {receiver}")
        return

    print(f"Case ID: {case['case_id']}")
    print(f"Title: {case['title']}")
    print(f"Level: {CASES[receiver]['level']}")
    print("====================\n")

    result = check_email_against_case(body, case)

    if result is None:
        print("ERROR: checker returned no result")
        return

    print("=== GAME RESULT ===")
    print(f"Player: {sender_email}")
    print(f"Target: {receiver}")
    print(f"Case: {case['case_id']}")
    print(f"Status: {'SUCCESS ✅' if result['status'] else 'FAILED ❌'}")
    print("Message:")
    print(result["msg"])
    print("===================\n")

    if result["status"]:
        advanced = advance_case(receiver)

        if advanced:
            print("➡ Moving to next case...\n")
        else:
            print("🎉 All cases completed!\n")

    log_game_event(
         player=sender_email,
         target=receiver,
         case_id=case["case_id"],
         status=result["status"],
         message=result["msg"])              
             

    try:
        send_email_smtp(
            sender=receiver,
            recipient=sender_email,
            subject=f"Re: {subject}" if subject else "Re: Your Request",
            body=result["msg"],
            smtp_host="localhost",
            smtp_port=25
        )
        print("Reply sent successfully.")
    except Exception as e:
        print("Reply could not be delivered through mail.")
        print("Delivery error:", e)


if __name__ == "__main__":
    main()