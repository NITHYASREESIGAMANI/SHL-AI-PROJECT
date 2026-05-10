import json


def load_catalog():

    with open("app/data/shl_catalog.json", "r", encoding="utf-8") as f:
        return json.load(f)


def recommend_assessments(query: str):

    query = query.lower()

    catalog = load_catalog()

    recommendations = []

    for item in catalog:

        score = 0

        # Match against skills
        for skill in item.get("skills", []):

            if skill.lower() in query:
                score += 5

        # Match against assessment name
        if any(word in item["name"].lower() for word in query.split()):
            score += 3

        if score > 0:

            recommendations.append({
                "name": item["name"],
                "url": item["url"],
                "test_type": item["test_type"],
                "score": score
            })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:5]