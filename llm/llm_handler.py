from langchain_ollama import OllamaLLM
import time

llm = OllamaLLM(model="llama3.2:1b")

def ask_llm(prompt: str):
    start_time = time.perf_counter()
    response = llm.invoke(prompt)
    end_time = time.perf_counter()

    response_time = end_time - start_time
    print(f"AI response time: {response_time:.2f} seconds")

    return response