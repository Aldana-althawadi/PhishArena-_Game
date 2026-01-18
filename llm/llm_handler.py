import ollama
from llm.rag import retrieve_docs  

SYSTEM_PROMPT = """
You are a cybersecurity awareness assistant.

Your task:
1. Determine if the email is phishing or legitimate.
2. Identify phishing flags from this list:
F1 Urgency
F2 Impersonation
F3 Suspicious Link
F4 Request for Credentials
F5 Generic Greeting
F6 Unexpected Attachment
F7 Grammar Errors
F8 Financial Request
F9 Threatening Language
F10 Too Good To Be True

3. Use the provided context to justify your decision.

Output MUST be valid JSON only:
{
  "is_phishing": true/false,
  "flags": ["F1", "F3"],
  "explanation": "..."
}
"""
def analyze_email(email_text):
    # Step 1: retrieve relevant docs from RAG
    context_docs = retrieve_docs(email_text)

    context = "\n\n".join([doc.page_content for doc in context_docs])

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""
Email:
{email_text}

Relevant knowledge:
{context}
"""
        }
    ]

    response = ollama.chat(
        model="llama3.1",
        messages=messages
    )

    return response["message"]["content"]
