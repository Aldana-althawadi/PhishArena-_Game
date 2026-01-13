import ollama

response = ollama.chat(
    model='llama3.1',
    messages=[
        {'role': 'user', 'content': 'Is this email phishing: "Verify your account now!"'}
    ]
)

print(response['message']['content'])
