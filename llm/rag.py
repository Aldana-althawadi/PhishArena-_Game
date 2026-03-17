import os
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings



# CONFIG – absolute paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DOCS_FOLDER = os.path.join(PROJECT_DIR, "KnowledgeBase", "RAG_Docs")
VECTOR_DB_DIR = os.path.join(PROJECT_DIR, "KnowledgeBase", "vector_db")
COLLECTION_NAME = "phishing_kb"


# Load documents
docs = []
for file_name in os.listdir(DOCS_FOLDER):
    if file_name.endswith(".txt"):
        file_path = os.path.join(DOCS_FOLDER, file_name)
        loader = TextLoader(file_path)
        docs.extend(loader.load())

print(f"[INFO] Loaded {len(docs)} documents from {DOCS_FOLDER}")


# Split documents into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs_split = splitter.split_documents(docs)

print(f"[INFO] Split documents into {len(docs_split)} chunks")


# Create embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text") 
vector_db = Chroma.from_documents(
    docs_split,
    embeddings,
    collection_name=COLLECTION_NAME,
    persist_directory=VECTOR_DB_DIR
)


# Persist the vector DB
vector_db.persist()
#print(f"[INFO] RAG knowledge base created and saved at {VECTOR_DB_DIR}")


# Quick verification 
results = vector_db.similarity_search("suspicious link in email", k=2)
#print("\n[INFO] Sample search results:")
#for i, r in enumerate(results, 1):
   # print(f"--- Result {i} ---")
    #print(r.page_content[:200], "...\n")

def retrieve_docs(query, k=3):
    return vector_db.similarity_search(query, k=k)


# retrival function
def retrieve_context(query, k=3):
    results = vector_db.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in results])

