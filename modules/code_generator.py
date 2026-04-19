from llm.client import call_llm

def generate_code(test_cases_json):
    prompt = f"""
You are a QA automation engineer.

TASK:
Convert test cases into Playwright TypeScript.

STRICT RULES:
- Use test.describe and test()
- Use page.locator()
- Include expect() assertions
- Keep code clean and simple
- Do NOT explain

INPUT:
{test_cases_json}
"""
    return call_llm(prompt)