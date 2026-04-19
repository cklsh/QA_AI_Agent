from llm.client import call_llm

def parse_prd(prd_text):
    prompt = f"""
You are a QA system.

TASK:
Convert PRD into structured test scenarios.

STRICT RULES:
- Return ONLY valid JSON
- No explanation
- Each scenario must have at least 3 steps
- Include BOTH positive and negative scenarios

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