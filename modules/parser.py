from llm.client import call_llm

def parse_prd(prd_text):
    prompt = f"""
You are a QA system.

STRICT RULES:
- Return ONLY valid JSON
- Use DOUBLE QUOTES only
- Do NOT include comments
- Do NOT include explanations
- Do NOT include non-English characters
- Do NOT include trailing commas
- If unsure, return empty JSON structure

FORMAT:
{{
  "feature": "string",
  "scenarios": [
    {{
      "name": "string",
      "type": "positive|negative",
      "steps": ["step1", "step2", "step3"],
      "expected_result": "string"
    }}
  ]
}}

PRD:
{prd_text}
"""
    return call_llm(prompt)