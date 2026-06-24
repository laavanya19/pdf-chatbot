from fastapi import FastAPI, UploadFile, File
from pdf_processor import extract_text_from_pdf
from chunker import create_chunks
from vector_store import store_chunks
from vector_store import search_chunks
from chatbot import generate_answer
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "PDF Chatbot is running!"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    pages = extract_text_from_pdf(file_path)

    chunks = create_chunks(pages)

    store_chunks(chunks)

    return {
        "message": "PDF uploaded successfully",
        "pages": len(pages),
        "chunks": len(chunks),
        "first_chunk": chunks[0]["text"][:200] if chunks else ""
    }
@app.post("/ask")
async def ask_question(data: dict):

    question = data["question"]

    results = search_chunks(question)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = "\n\n".join(documents)

    answer = generate_answer(
        question,
        context
    )

    source_pages = [
        item["page"]
        for item in metadatas
    ]

    return {
        "answer": answer,
        "source_pages": source_pages,
        "excerpt": documents[0][:300]
    }