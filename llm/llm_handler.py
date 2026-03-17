from langchain_ollama import OllamaLLM
from llm.rag import retrieve_context

llm = OllamaLLM(model="qwen2.5:3b")

def analyze_email_raw(email_text: str) -> str:
    context = retrieve_context(email_text)

    prompt = f"""
You are a cybersecurity phishing detection system.

Your task is to analyze a single email and determine whether it is phishing or legitimate.

Follow the rules below carefully.

---------------------------------------------------
Classification Rules
---------------------------------------------------

Use evidence-based reasoning when determining whether an email is phishing.

Strong phishing indicators include:

- Suspicious or unofficial login / verification / payment links
- Requests for credentials or personal information
- Impersonation of organizations through unofficial sender or domain
- Pressure or threats requiring immediate action
- Messages asking the user to click links to verify accounts

Legitimate emails may contain:

- login notifications
- security alerts
- new device warnings
- general account activity updates

These alone are NOT phishing unless the email asks the user to submit credentials
or directs the user to an unofficial link.

If an email asks the user to verify credentials through an external link that
does not clearly belong to the official organization, treat this as strong phishing evidence.

If the email is purely informational (announcement, meeting reminder, receipt,
notification without credential request), classify it as legitimate.

If evidence is weak or uncertain, classify as legitimate with low confidence.

---------------------------------------------------
Phishing Flag Definitions
---------------------------------------------------

Assign flags ONLY if there is clear evidence in the email text.

F1 (Urgency) – explicit pressure such as:
"act now", "immediately", "within 24 hours", deadlines, or urgent warnings.

F2 (Impersonation) – the sender pretends to represent a trusted organization
(bank, university, company IT, social media platform).

F3 (Suspicious Link) – the email contains a URL that appears unofficial,
unusual, shortened, or unrelated to the claimed organization.

F4 (Credential Request) – the email asks the user to enter or confirm
passwords, login credentials, verification codes, or identity details.

F5 (Generic Greeting) – vague greetings such as
"Dear user", "Dear customer", "Dear employee".

F6 (Unexpected Attachment) – attachments that the recipient did not request.

F7 (Grammar Errors) – noticeable spelling mistakes or unnatural phrasing.

F8 (Financial Request) – requests for payments, banking information, or transfers.

F9 (Threat / Pressure) – warnings of consequences such as
account suspension, penalties, legal action, or service interruption.

F10 (Too Good To Be True) – unrealistic prizes, rewards, or gift cards.

---------------------------------------------------
Analysis Procedure
---------------------------------------------------

Before producing the final JSON output:

1. Identify any suspicious indicators in the email.
2. Check if the sender or link appears unofficial.
3. Determine if credentials or financial information are requested.
4. Determine whether the email is informational or requesting action.
5. Assign flags ONLY if the evidence clearly exists in the email.

Do NOT invent evidence that does not appear in the email text.

---------------------------------------------------
Output Requirements
---------------------------------------------------

Respond ONLY in valid JSON.

Do NOT include explanations outside the JSON.

The JSON MUST contain all fields.

If "is_phishing" is true:
- "phishing_type" MUST NOT be empty
- "flags" MUST contain at least TWO relevant flags
- "confidence" MUST be between 0.6 and 1.0
- explanation must reference evidence from the email

If "is_phishing" is false:
- "flags" MUST be an empty list
- "confidence" MUST be between 0.0 and 0.6

Flags must be a list of strings like:

["F1","F3"]

Do NOT return objects inside the flags list.
If "is_phishing" is false:
- "flags" MUST be an empty list
- "confidence" MUST be between 0.0 and 0.6
- "explanation" MUST contain at least 1 sentence explaining why the email appears legitimate
- The explanation should mention the absence of phishing evidence such as suspicious links, credential requests, threats, impersonation, or unusual pressure

---------------------------------------------------
Output Format
---------------------------------------------------

{{
  "is_phishing": true or false,
  "phishing_type": "",
  "flags": [],
  "confidence": 0.0,
  "explanation": ""
}}

Important:
Use ONLY evidence present in the current email text.

Do NOT assume the presence of links, credential requests, sender mismatch,
attachments, urgency, or threats unless they are explicitly visible.

Do NOT copy information from the reference examples into the email analysis

For legitimate emails, do not leave the explanation empty.
Always explain why the message appears legitimate based on visible evidence in the email.

Phishing reference examples:
{context}

Email to analyze:
{email_text}
"""

    return llm.invoke(prompt)
