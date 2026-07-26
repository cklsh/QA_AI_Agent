def validate_scenarios(data):

    issues = []

    scenarios = data.get("scenarios", [])

    for scenario in scenarios:

        title = scenario.get("title")

        if not title:
            issues.append(
                "Scenario missing title"
            )

        if not scenario.get("given"):
            issues.append(
                f"Scenario '{title}' missing Given"
            )

        if not scenario.get("when"):
            issues.append(
                f"Scenario '{title}' missing When"
            )

        if not scenario.get("then"):
            issues.append(
                f"Scenario '{title}' missing Then"
            )

    return issues