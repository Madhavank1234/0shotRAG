import faiss
import pickle
import requests
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index + chunks
def load_vector_store():
    index = faiss.read_index("vector_store/index.faiss")
    chunks = pickle.load(open("vector_store/chunks.pkl", "rb"))
    return index, chunks

# Retrieve relevant chunks
def retrieve(query, top_k=4):
    index, chunks = load_vector_store()
    q_emb = model.encode([query])
    D, I = index.search(q_emb, top_k)
    return [chunks[i] for i in I[0]]

# Generate answer using Ollama server API
def generate_answer(query):
    context = "\n".join(retrieve(query))

    prompt = f"""
You are a document assistant.
Answer ONLY from the context below.
If the answer is not present, say: Not found in document.

Context:
{context}

Question: {query}
"""

    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    }
)


    return response.json()["response"]
