from pipeline import run_pipeline
from utils.document_loader import load_pdf
from utils.text_cleaner import clean_text

import json
import time

start = time.time()

# Load PRD from PDF
prd_text = load_pdf("documents/sample_prd.pdf")
prd_text = clean_text(prd_text)

print("PDF length ", len(prd_text))

print("=== EXTRACTED TEXT ===")
print(prd_text[:1000])  # preview first 1000 chars

# Run AI pipeline
result = run_pipeline(prd_text)

print("\n=== RESULT ===\n")
print(json.dumps(result, indent=2))

print("\n⏱ Time:", time.time() - start)