from llm_handler import analyze_email

email = """
Subject: Account Security Alert

Your Facebook account will be suspended in 24 hours.
Click the link below to verify your identity immediately:
http://facebook-secure-login.com
"""

result = analyze_email(email)
print(result)
