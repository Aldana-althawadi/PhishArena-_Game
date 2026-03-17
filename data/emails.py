EMAILS = [

    # ---------- PHISHING EMAILS ----------

    {
        "id": "E01",
        "title": "Outlook Account Security Alert",
        "sender": "security@outlook-alert.com",
        "subject": "Urgent: Verify your Outlook account immediately",
        "body": """Dear User,

We detected unusual activity on your Outlook account.

To prevent temporary suspension, please confirm your account information within 24 hours.

Verify your account here:
http://outlook-account-security-check.com

Microsoft Security Team""",
        "expected_is_phishing": True,
        "expected_type": "Credential Harvesting",
        "expected_flags": ["F1", "F2", "F3", "F4", "F5"],
        "difficulty": "easy"
    },

    {
        "id": "E02",
        "title": "Instagram Login Alert",
        "sender": "support@instagram-security.net",
        "subject": "Instagram: Suspicious login attempt",
        "body": """Hello,

We noticed a login attempt to your Instagram account from a new device.

To secure your account, please confirm your login details here:
http://instagram-security-login.net

Instagram Support""",
        "expected_is_phishing": True,
        "expected_type": "Credential Harvesting",
        "expected_flags": ["F3", "F4"],
        "difficulty": "easy"
    },

    {
        "id": "E03",
        "title": "PayPal Billing Notification",
        "sender": "billing@paypal-verification.com",
        "subject": "Payment issue detected",
        "body": """Dear Customer,

Your recent payment could not be processed successfully.

To avoid interruption of your account services, please update your billing information here:
http://paypal-billing00check.com

PayPal Billing Department""",
        "expected_is_phishing": True,
        "expected_type": "Financial Scam",
        "expected_flags": ["F3", "F4", "F5", "F8"],
        "difficulty": "medium"
    },

    {
        "id": "E04",
        "title": "University Portal Verification Notice",
        "sender": "admin@university-notice.net",
        "subject": "Important: Student portal update",
        "body": """Dear Student,

Due to a recent university portal upgrade, all students must verify their account details before access is restricted.

Please confirm your student credentials here:
http://university-portal-update.com

Student Services""",
        "expected_is_phishing": True,
        "expected_type": "Impersonation",
        "expected_flags": ["F2", "F3", "F4"],
        "difficulty": "medium"
    },

    {
        "id": "E05",
        "title": "DHL Delivery Attempt Notice",
        "sender": "delivery@dhl-tracking-support.com",
        "subject": "Package delivery failed",
        "body": """Dear Customer,

We attempted to deliver your package today, but the delivery could not be completed due to incomplete address information.

Please update your delivery details immediately:
http://dhl-tracking-upd@te-supp0rt998.com

DHL Delivery Service""",
        "expected_is_phishing": True,
        "expected_type": "Social Engineering",
        "expected_flags": ["F3", "F5", "F9"],
        "difficulty": "medium"
    },

    {
        "id": "E06",
        "title": "Bank Security Alert",
        "sender": "security@bank-alerts.net",
        "subject": "Unusual transaction detected",
        "body": """Dear Customer,

We detected an unusual transaction on your account.

To prevent temporary suspension, you must verify your banking identity immediately by confirming your account credentials at the link below:

http://bank-secure-verification.net

Failure to verify may result in temporary account restrictions.""",
        "expected_is_phishing": True,
        "expected_type": "Financial Scam",
        "expected_flags": ["F1", "F3", "F4", "F5", "F9"],
        "difficulty": "hard"
    },

    {
        "id": "E07",
        "title": "Amazon Rewards Notification",
        "sender": "reward@amazon-prize-center.com",
        "subject": "Congratulations! You won a $500 gift card",
        "body": """Congratulations!

You have been selected to receive a $500 Amazon gift card as part of our customer rewards event.

Claim your reward now:
http://amazon-reward-center.net

Amazon Rewards Team""",
        "expected_is_phishing": True,
        "expected_type": "Prize Scam",
        "expected_flags": ["F3", "F10"],
        "difficulty": "easy"
    },

    {
        "id": "E08",
        "title": "Corporate Password Reset Notice",
        "sender": "it-support@company-security.com",
        "subject": "Mandatory password reset",
        "body": """Hello Employee,

As part of our latest security improvements, all employees are required to reset their passwords today.

Reset your password here:
http://company-password-reset.net

IT Support Team""",
        "expected_is_phishing": True,
        "expected_type": "Credential Harvesting",
        "expected_flags": ["F2", "F3", "F4"],
        "difficulty": "medium"
    },

    # ---------- LEGITIMATE EMAILS ----------

    {
        "id": "E09",
        "title": "Microsoft Security Notification",
        "sender": "noreply@outlook.com",
        "subject": "Microsoft security notification",
        "body": """We detected a login to your Microsoft account from a new device.

You can review your recent activity here:
https://account.microsoft.com/security

If this was you, no action is required.
If this was not you, please change your password immediately.""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Notification",
        "expected_flags": [],
        "difficulty": "medium"
    },

    {
        "id": "E10",
        "title": "Course Registration Reminder",
        "sender": "admin@university.edu",
        "subject": "Reminder: Course registration deadline",
        "body": """Dear Student,

This is a reminder that course registration closes on Sunday.

Please review your schedule and confirm your courses here:
https://portal.university.edu/registration

Regards,
University Administration""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Notification",
        "expected_flags": [],
        "difficulty": "easy"
    },

    {
        "id": "E11",
        "title": "Team Meeting Reminder",
        "sender": "hr@company.com",
        "subject": "Team meeting tomorrow",
        "body": """Hello Team,

This is a reminder that we will have a project meeting tomorrow at 10 AM in Meeting Room B.

You can review the agenda here:
https://intranet.company.com/meetings/project-team

Best,
HR Department""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Communication",
        "expected_flags": [],
        "difficulty": "easy"
    },

    {
        "id": "E12",
        "title": "Amazon Order Shipment",
        "sender": "support@amazon.com",
        "subject": "Your order has been shipped",
        "body": """Hello,

Your Amazon order has been shipped and is on the way.

You can track your package here:
https://www.amazon.com/your-orders

Thank you for shopping with Amazon.""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Notification",
        "expected_flags": [],
        "difficulty": "easy"
    },

    {
        "id": "E13",
        "title": "LinkedIn Login Alert",
        "sender": "security-noreply@linkedin.com",
        "subject": "New login to your LinkedIn account",
        "body": """Hi,

We noticed a login to your LinkedIn account from a new device.

You can review this activity here:
https://www.linkedin.com/checkpoint/login

If this was you, no action is needed.
If this was not you, please secure your account from the official LinkedIn website or app.

Regards,
LinkedIn Security""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Notification",
        "expected_flags": [],
        "difficulty": "medium"
    },

    {
        "id": "E14",
        "title": "IT Maintenance Notification",
        "sender": "it-support@company.com",
        "subject": "Scheduled system maintenance",
        "body": """Dear Staff,

Our IT team will perform scheduled system maintenance tonight between 1 AM and 3 AM.

Service details are available here:
https://intranet.company.com/maintenance

During this time some internal systems may be temporarily unavailable.""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Notification",
        "expected_flags": [],
        "difficulty": "medium"
    },

    {
        "id": "E15",
        "title": "Library Due Reminder",
        "sender": "library@university.edu",
        "subject": "Library book due reminder",
        "body": """Dear Student,

This is a reminder that your borrowed library book is due tomorrow.

You can review your borrowed items here:
https://library.university.edu/account

Please return the book on time to avoid late fees.""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Notification",
        "expected_flags": [],
        "difficulty": "easy"
    },

    {
        "id": "E16",
        "title": "GitHub Login Alert",
        "sender": "support@github.com",
        "subject": "New device signed into your account",
        "body": """Hi,

A new device has signed into your GitHub account.

You can review your recent account activity here:
https://github.com/settings/security-log

If this was not you, please change your password and review your security settings.""",
        "expected_is_phishing": False,
        "expected_type": "Legitimate Notification",
        "expected_flags": [],
        "difficulty": "medium"
    }

]