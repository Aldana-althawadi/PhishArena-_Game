from langchain_community.llms import Ollama
from llm.rag import retrieve_context

llm = Ollama(model="llama3.1")

def analyze_email_raw(email_text: str) -> str:
    context = retrieve_context(email_text)

    prompt = f"""
You are a cybersecurity phishing detection system.

Decision rules:
1) Mark "is_phishing": true ONLY if there is clear evidence such as:
   - credential request (password, OTP, login)
   - suspicious or mismatched link/domain
   - unexpected attachment with pressure to open
   - urgent financial transfer request
2) If the email is purely informational (meeting reminder, announcement, receipt),
   mark it as legitimate.
3) Only assign a flag if the email contains direct evidence of it.
4) If unsure, set is_phishing=false and use low confidence (<0.6).

Flag definitions:
F1 Urgency – short deadlines, pressure to act fast  
F2 Impersonation – pretending to be a brand/person  
F3 Suspicious Link – strange or obfuscated URL  
F4 Credential Request – asks for password or login  
F5 Generic Greeting – “Dear user”, “Dear employee”  
F6 Unexpected Attachment – invoice/pdf you did not request  
F7 Grammar Errors – spelling or awkward language  
F8 Financial Request – transfer money, pay urgently  
F9 Threat/Pressure – suspension, punishment, legal threat  
F10 Too Good To Be True – prizes, free gifts, rewards  

Rules:
- Respond ONLY in valid JSON.
- Do not add any text outside JSON.
- Use this exact format:

{{
  "is_phishing": true or false,
  "phishing_type": "",
  "flags": [],
  "confidence": 0.0,
  "explanation": ""
}}

Important:
- "flags" MUST be a list of strings like ["F1","F3"].
- Do NOT return objects/dictionaries inside "flags".
- Respond ONLY in valid JSON. No extra text.

Phishing reference examples:
{context}

Email to analyze:
{email_text}
"""

    return llm.invoke(prompt)
