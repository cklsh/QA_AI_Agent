from fastapi import FastAPI

from pipeline import run_pipeline
from rag.knowledge import init_knowledge, retrieve_context
from llm.client import call_llm
from models.schema import GenerateRequest, AskRequest

app = FastAPI()

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