from fastapi import FastAPI, UploadFile, File
import shutil, os
from ingest import extract_text
from chunk_embed import chunk_text, build_faiss
from rag import generate_answer

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    combined_text = ""

    for file in files:
        path = f"{UPLOAD_DIR}/{file.filename}"
        with open(path,"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        combined_text += extract_text(path)

    chunks = chunk_text(combined_text)
    build_faiss(chunks)

    return {"status":"Documents processed successfully"}

@app.get("/chat")
def chat(query:str):
    answer = generate_answer(query)
    return {"answer":answer}
