from sentence_transformers import SentenceTransformer
import faiss, os, pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

def build_faiss(chunks):
    if len(chunks) == 0:
        raise ValueError("No text extracted from documents. OCR or extraction failed.")

    embeddings = model.encode(chunks)

    if len(embeddings) == 0:
        raise ValueError("Embedding model returned empty embeddings.")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    os.makedirs("vector_store", exist_ok=True)
    faiss.write_index(index, "vector_store/index.faiss")
    pickle.dump(chunks, open("vector_store/chunks.pkl", "wb"))
