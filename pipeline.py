from modules.parser import parse_prd
from modules.test_generator import generate_test_cases
from modules.validator import validate_scenarios

from utils.json_utils import safe_parse_json
from utils.chunker import chunk_text

from rag.knowledge import add_knowledge

from helper import retry_llm_call

import json
import time


def run_pipeline(prd_text):
    start_time = time.time()
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
    feature = "Merged PRD"


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


        # Keep feature from parser output
        if feature == "Merged PRD" and parsed.get("feature"):
            feature = parsed["feature"]


        scenarios = parsed.get("scenarios", [])

        all_scenarios.extend(scenarios)



    if not all_scenarios:

        result["issues"].append(
            "No scenarios extracted"
        )

        return result



    scenarios = {
        "feature": feature,
        "scenarios": all_scenarios
    }


    print(
        f"\nCollected {len(all_scenarios)} scenarios"
    )


    result["scenarios"] = scenarios



    # Validation

    issues = validate_scenarios(scenarios)

    result["issues"].extend(issues)


    # Save good knowledge only

    add_knowledge(
        [
            str(scenarios)
        ]
    )



    # Step 2: Generate Code (disabled for now)

    # print("→ Generating code...")
    # code = generate_code(raw_tests)
    # result["code"] = code



    print(
        f"Total scenarios: {len(all_scenarios)}"
    )

    elapsed_time = time.time() - start_time

    print(
        f"\n✅ Pipeline completed in {elapsed_time:.2f} seconds"
    )

    return result