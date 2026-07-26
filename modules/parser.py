from llm.client import call_llm


def parse_prd(prd_text):

    prompt = f"""
You are a Senior QA Engineer specializing in BDD (Behavior Driven Development).

Your task:
Analyze the PRD and convert business requirements into BDD test scenarios.

IMPORTANT:
- A scenario describes WHAT behavior should be tested.
- Do NOT create detailed test execution steps.
- Do NOT create test cases.
- Do NOT invent requirements that are not mentioned in the PRD.

Return valid JSON only.

Rules:
- No markdown
- No explanation
- Use double quotes only
- Include positive scenarios when the requirement succeeds
- Include negative scenarios when validation or failure behavior exists
- Focus on user behavior and system response

Use Given When Then format:

Given:
The initial condition or precondition.

When:
The user action or event.

Then:
The expected system behavior.

Schema:

{{
  "feature": "string",

  "scenarios": [
    {{
      "id": "SC001",
      "title": "string",
      "type": "positive|negative",

      "given": [
        "string"
      ],

      "when": [
        "string"
      ],

      "then": [
        "string"
      ]
    }}
  ]
}}

PRD:

{prd_text}
"""

    return call_llm(prompt)