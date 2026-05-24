# AI QA Agent (Runs Locally)
A mini project that converts PRDs into test cases and Playwright automation code.
Runs fully locally using Ollama 
---

## What it does
Input:
* PRD (plain text)

Output:
* Test scenarios (JSON)
* Test cases (positive / negative / edge)
* Playwright (TypeScript) code
---

## Flow
```text
PRD → Scenarios → Test Cases → Playwright Code
```

Optional:

```text
+ RAG (reuse QA knowledge)
```
---

## Tech
* Python
* Ollama (local LLM)
* Qwen 2.5 (7B)
* FAISS (RAG)
---

## Setup

### 1. Install Ollama

Download:
https://ollama.com

---

### 2. Pull model

```bash
ollama pull qwen2.5:3b
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run API

```bash
uvicorn api.app:app --reload
```

---

### 5. Open Swagger Docs

http://127.0.0.1:8000/docs
---

## Example PRD
```text
User can login using email and password.
If password is wrong → show error.
After 5 failed attempts → lock account.
```
---

## Output
* Structured test scenarios
* Detailed test cases
* Playwright test code
---

## Notes
* Fully offline (no tokens / API)
* Output quality depends on prompt + model
* Designed as MVP (not production-ready)
---

## Goal
Speed up QA work:
* faster test design
* faster automation
* reusable knowledge (RAG)
---
