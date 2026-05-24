from llm.client import call_llm
from rag.knowledge import retrieve_context


def generate_test_cases(scenarios_json):

    context = retrieve_context(str(scenarios_json))

    print("\n=== RETRIEVED CONTEXT ===")
    print(context)

    context_text = "\n".join(context)

    prompt = f"""
Return valid JSON only.

Relevant QA knowledge:
{context_text}

Schema:
{{
  "test_cases": [
    {{
      "title": "string",
      "type": "positive or negative",
      "steps": ["step1", "step2"],
      "expected_result": "string"
    }}
  ]
}}

INPUT:
{scenarios_json}
"""

    return call_llm(prompt)