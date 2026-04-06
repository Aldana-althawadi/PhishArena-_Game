from langchain_ollama import OllamaLLM

# Main model used for the  email challenge checker
llm = OllamaLLM(model="llama3.2:1b")
def ask_llm(prompt: str):
    return llm.invoke(prompt)