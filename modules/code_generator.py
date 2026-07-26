from llm.client import call_llm


def generate_code(test_cases_json):

    prompt = f"""
You are a Senior QA Automation Engineer.

Your task:
Convert BDD-based QA test cases into Playwright TypeScript automation.

The input contains:
- Test case information
- Given / When / Then behavior

Mapping rules:

Given:
- Convert into test setup or preconditions.

When:
- Convert into user actions.

Then:
- Convert into Playwright assertions using expect().

STRICT RULES:

- Return ONLY valid TypeScript code.
- Do not explain the code.
- Use test.describe().
- Create one test() per test case.
- Use async/await.
- Use page.locator().
- Use expect() assertions.
- Keep selectors as TODO placeholders if not provided.
- Do not invent selectors.
- Do not invent business logic.
- Keep code clean and readable.

Example selector:

// TODO: Replace with actual selector
page.locator("TODO_BUTTON")

Input:

{test_cases_json}
"""

    return call_llm(prompt)