from modules.parser import parse_prd
from modules.test_generator import generate_test_cases
from modules.validator import validate_scenarios
from utils.json_utils import safe_parse_json
from utils.chunker import chunk_text
from rag.knowledge import add_knowledge

from helper import retry_llm_call
import json

def run_pipeline(prd_text):

    result = {
        "scenarios": None,
        "test_cases": None,
        "code": None,
        "issues": []
    }
    
    print("→ Chunking PRD...")

    chunks = chunk_text(prd_text)

    print(f"Found {len(chunks)} chunks")

    all_scenarios = []

    for index, chunk in enumerate(chunks):

        print(f"\n→ Processing chunk {index + 1}/{len(chunks)}")

        raw = retry_llm_call(
            lambda: parse_prd(chunk)
        )
        print("\n=== RAW MODEL OUTPUT ===")
        print(raw)

        if not raw:
            print("Failed chunk")
            continue

        parsed = safe_parse_json(raw)

        if not parsed:
            print("Invalid JSON chunk")
            continue

        scenarios = parsed.get("scenarios", [])

        all_scenarios.extend(scenarios)


    if not all_scenarios:
        result["issues"].append(
            "No scenarios extracted"
        )
        return result

    scenarios = {
        "feature": "Merged PRD",
        "scenarios": all_scenarios
    }

    print(
        f"\nCollected {len(all_scenarios)} scenarios"
    )

    result["scenarios"] = scenarios

    # Validation
    issues = validate_scenarios(scenarios)
    result["issues"].extend(issues)

    # Step 2
    print("→ Generating test cases...")

    raw_tests = retry_llm_call(
        lambda: generate_test_cases(
            json.dumps(scenarios)
        )
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

    print(
        f"Total scenarios: {len(all_scenarios)}"
    )

    return result