from llm.client import call_llm
from rag.knowledge import retrieve_context


def generate_test_cases(scenarios_json):

    context = retrieve_context(str(scenarios_json))

    print("\n=== RETRIEVED CONTEXT ===")
    print(context)

    context_text = "\n".join(context)

    prompt = f"""
You are a Senior QA Test Designer.

Your task:
Convert BDD scenarios into detailed QA test cases.

IMPORTANT:
- Do not change the business behavior.
- Do not create new requirements.
- Keep Given When Then information from the scenario.
- Add QA information needed for execution.
- Return valid JSON only.

Relevant QA knowledge:
{context_text}

Schema:

{{
  "test_cases": [
    {{
      "id": "TC001",

      "scenario_id": "SC001",

      "title": "string",

      "type": "positive|negative",

      "priority": "High|Medium|Low",

      "preconditions": [
        "string"
      ],

      "test_data": {{
        "key": "value"
      }},

      "bdd": {{
        "given": [
          "string"
        ],

        "when": [
          "string"
        ],

        "then": [
          "string"
        ]
      }},

      "automation_candidate": true
    }}
  ]
}}

INPUT:

{scenarios_json}
"""

    return call_llm(prompt)