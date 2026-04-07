
---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend UI | Streamlit |
| Backend API | FastAPI |
| OCR Engine | Tesseract OCR |
| Embeddings | SentenceTransformers |
| Vector Database | FAISS |
| Local LLM | Ollama + TinyLlama |
| Language | Python |

---

## 🧠 How It Works

### Step 1 — File Upload  
Users upload multiple files through the Streamlit interface.

### Step 2 — Text Extraction  
The backend processes each file:  
- If the document is text-based → direct text extraction  
- If the document is scanned → OCR using Tesseract  

### Step 3 — Chunking & Embeddings  
Extracted text is split into overlapping chunks.  
Each chunk is converted into embeddings using SentenceTransformer.

### Step 4 — Vector Storage  
All embeddings are stored in a FAISS vector database for fast similarity search.

### Step 5 — Question Answering  
When a user asks a question:  
- The question is embedded  
- FAISS retrieves relevant chunks  
- Retrieved chunks are passed as context to TinyLlama via Ollama  
- The model generates an answer based only on retrieved content  

This forms a **true zero-shot RAG pipeline**.

---

## 📂 Backend Module Explanation

### app.py
Main FastAPI server.  
- `/upload` → handles document ingestion  
- `/chat` → handles question answering  
Acts as the bridge between frontend and backend logic.

### ingest.py
Handles text extraction.  
- Direct text extraction for normal documents  
- OCR using Tesseract for scanned documents  

### chunk_embed.py
Prepares data for retrieval.  
- Splits text into chunks  
- Generates embeddings  
- Stores vectors in FAISS  

### rag.py
Core RAG pipeline.  
- Retrieves relevant chunks from FAISS  
- Sends context to TinyLlama via Ollama  
- Returns generated answers  

---

## 🖥️ Frontend Explanation

### ui.py
Streamlit-based interface.  
- Upload documents  
- Trigger processing  
- Ask questions  
- Display answers  

---

## 🚀 Installation & Setup

### 1. Clone Repository


---

### 2. Install Python Dependencies


---

### 3. Install Tesseract OCR

Download and install:

https://github.com/tesseract-ocr/tesseract

Ensure Tesseract is added to system PATH.

---

### 4. Install Ollama

Download from:

https://ollama.com/download

After installation, download TinyLlama:


When the model loads, exit with:

/bye

Ollama runs in background automatically.

---

## ▶️ Running the Application

### Start Backend


Backend runs at:
http://127.0.0.1:8000/

---

### Start Frontend

Open a new terminal:

cd frontend
streamlit run ui.py

Frontend runs at:
http://localhost:8501

---

## 💬 Usage Flow

1. Upload multiple documents  
2. Click **Process**  
3. Ask questions  
4. Get answers from uploaded content  

---

## 🖥️ System Requirements

- Python 3.10+  
- 8 GB RAM recommended  
- Windows / Linux / macOS supported  

---

## 🎯 Highlights

- Fully offline  
- No paid APIs  
- Zero-shot reasoning  
- OCR-supported document ingestion  
- Multi-document conversational search  
- Local LLM inference  

---

## 📜 License

MIT License

---

## 👤 Author

Lakshmana Aditya Varma Vegesna

---

## 🤝 Acknowledgements

FastAPI • Streamlit • FAISS • SentenceTransformers • Tesseract OCR • Ollama




