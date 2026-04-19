def validate_scenarios(data):
    issues = []

    if not data:
        return ["Invalid JSON"]

    for s in data.get("scenarios", []):
        if len(s.get("steps", [])) < 3:
            issues.append(f"Scenario '{s.get('name')}' too shallow")

    return issues