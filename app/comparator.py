def compare_assessments(items: list):

    if len(items) < 2:
        return None

    return {
        "type": "comparison",
        "items": items,
        "summary": f"{items[0]} is more behavioral-focused while {items[1]} is more cognitive/skill-based.",
        "recommendation": f"For most hiring use cases, choose {items[0]} if evaluating personality, otherwise {items[1]} for skills."
    }