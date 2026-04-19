from llm.client import call_llm
from rag.knowledge import retrieve_context

def generate_test_cases(scenarios_json):
    context = retrieve_context(scenarios_json)

    context_text = "\n".join(context)

    prompt = f"""
You are a QA system.

Use the following knowledge to improve test quality:
{context_text}

TASK:
Generate detailed test cases.

STRICT RULES:
- Include positive, negative, edge cases
- Use knowledge if relevant
- Return ONLY JSON

INPUT:
{scenarios_json}
"""
    return call_llm(prompt)