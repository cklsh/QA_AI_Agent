from modules.parser import parse_prd
from modules.test_generator import generate_test_cases
from modules.validator import validate_scenarios
from utils.json_utils import safe_parse_json
from rag.knowledge import add_knowledge

from helper import retry_llm_call


def run_pipeline(prd_text):

    result = {
        "scenarios": None,
        "test_cases": None,
        "code": None,
        "issues": []
    }

    # Step 1
    print("→ Parsing PRD...")

    raw_scenarios = retry_llm_call(
        lambda: parse_prd(prd_text)
    )

    if not raw_scenarios:
        result["issues"].append("Failed to generate scenarios")
        return result

    scenarios = safe_parse_json(raw_scenarios)

    if not scenarios:
        result["issues"].append("Invalid scenario JSON")
        return result

    result["scenarios"] = scenarios

    # Validation
    issues = validate_scenarios(scenarios)
    result["issues"].extend(issues)

    # Step 2
    print("→ Generating test cases...")

    raw_tests = retry_llm_call(
        lambda: generate_test_cases(raw_scenarios)
    )

    if not raw_tests:
        result["issues"].append("Failed to generate test cases")
        return result

    test_cases = safe_parse_json(raw_tests)

    if not test_cases:
        result["issues"].append("Invalid test case JSON")
        return result

    result["test_cases"] = test_cases

    # Save good knowledge only
    add_knowledge([
        str(test_cases)
    ])

    # Step 3: Generate Code
    # print("→ Generating code...")
    # code = generate_code(raw_tests)
    # result["code"] = code

    return result