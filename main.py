from modules.parser import parse_prd
from modules.test_generator import generate_test_cases
from modules.code_generator import generate_code
from modules.validator import validate_scenarios
from utils.json_utils import safe_parse_json
from rag.knowledge import load_knowledge

load_knowledge()
prd = """
User can login using email and password.
If password is incorrect, show error message.
After 5 failed attempts, account is locked.
Successful login redirects to dashboard.
"""

print("=== PRD ===")
print(prd)

# Step 1: Parse PRD
raw_scenarios = parse_prd(prd)
scenarios = safe_parse_json(raw_scenarios)

print("\n=== SCENARIOS ===")
print(scenarios)

# Validation
issues = validate_scenarios(scenarios)
print("\n=== VALIDATION ===")
print(issues)

# Step 2: Generate Test Cases
raw_tests = generate_test_cases(raw_scenarios)
tests = safe_parse_json(raw_tests)

print("\n=== TEST CASES ===")
print(tests)

# Step 3: Generate Code
code = generate_code(raw_tests)

print("\n=== PLAYWRIGHT CODE ===")
print(code)