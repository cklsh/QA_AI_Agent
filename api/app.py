from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from pipeline import run_pipeline
from rag.knowledge import init_knowledge, retrieve_context
from llm.client import call_llm
from models.schema import GenerateRequest, AskRequest
import shutil
import os

from utils.document_loader import load_pdf
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load RAG memory once
init_knowledge()

@app.get("/")
def root():
    return {
        "message": "QA AI Agent API Running"
    }


@app.post("/generate")
def generate(request: GenerateRequest):

    try:
        result = run_pipeline(request.prd_text)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
    
@app.post("/generate-pdf")
async def generate_pdf(
    file: UploadFile = File(...)
):

    try:

        # Ensure uploads folder exists
        os.makedirs("uploads", exist_ok=True)

        # Save uploaded file
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"✅ Uploaded: {file.filename}")

        # Extract PDF text
        prd_text = load_pdf(file_path)

        print("\n=== EXTRACTED TEXT ===")
        print(prd_text[:1000])

        # Run pipeline
        result = run_pipeline(prd_text)

        return {
            "success": True,
            "filename": file.filename,
            "extracted_length": len(prd_text),
            "data": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

@app.post("/ask")
def ask_question(request: AskRequest):

    context = retrieve_context(request.question)

    context_text = "\n".join(context)

    prompt = f"""
        Answer the question based on context.

        Context:
        {context_text}

        Question:
        {request.question}
        """

    answer = call_llm(prompt)

    return {
        "success": True,
        "answer": answer,
        "context": context
    }

@app.get("/health")
def health():
    return {"status": "ok"}