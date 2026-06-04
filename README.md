# AI QA Agent (Runs Locally)

A local AI-powered QA assistant that converts PRDs into structured test scenarios and test cases.

Runs fully offline using Ollama (no API keys, no token costs).

---

## Features

✅ Upload PRD as PDF

✅ Extract and process document content

✅ Generate structured test scenarios

✅ Generate detailed test cases

✅ Local RAG memory (FAISS)

✅ REST API with FastAPI

🚧 Playwright code generation (Work In Progress)

---

## Architecture

```text
PDF
 ↓
Text Extraction
 ↓
Text Cleaning
 ↓
Chunking
 ↓
Scenario Generation
 ↓
Test Case Generation
 ↓
RAG Memory Storage
```

---

## Tech Stack

- Python
- FastAPI
- Ollama
- Qwen 2.5 (7B)
- FAISS
- Sentence Transformers
- PDFPlumber

---

## Setup

### 1. Install Ollama

Download:

https://ollama.com

---

### 2. Pull Model

```bash
ollama pull qwen2.5:7b
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run API

```bash
uvicorn api.app:app --reload
```

---

### 5. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Available Endpoints

### Generate from Text

```http
POST /generate
```

Input:

```json
{
  "prd_text": "User can login using email and password."
}
```

---

### Generate from PDF

```http
POST /generate-pdf
```

Upload a PRD PDF document.

---

### Ask Questions

```http
POST /ask
```

Query previously stored knowledge using RAG.

---

## Example Workflow

```text
Upload PRD PDF
 ↓
AI extracts requirements
 ↓
Generate scenarios
 ↓
Generate test cases
 ↓
Store knowledge in FAISS
 ↓
Ask questions about requirements
```

---

## Example Output

### Scenario

```json
{
  "name": "Successful Login",
  "type": "positive"
}
```

### Test Case

```json
{
  "title": "Login with Valid Credentials",
  "steps": [
    "Navigate to login page",
    "Enter valid credentials",
    "Click Login"
  ],
  "expected_result": "User is redirected to dashboard"
}
```

---

## Current Limitations

- Complex enterprise PRDs may require prompt tuning
- PDF extraction quality depends on document structure
- Playwright generation is still under development
- Local model quality depends on hardware and model size

---

## Goal

Reduce manual QA effort by helping teams:

- Understand requirements faster
- Generate test cases quicker
- Reuse historical QA knowledge
- Accelerate automation design
