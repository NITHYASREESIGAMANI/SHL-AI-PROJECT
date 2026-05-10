def score_assessment(match_score: int, relevance: int, popularity: int):
    """
    Simple weighted scoring system for SHL recommendations
    """

    return (0.5 * match_score) + (0.3 * relevance) + (0.2 * popularity)


def rank_assessments(assessments: list):
    """
    Expects list of dicts like:
    {name, match_score, relevance, popularity}
    """

    for a in assessments:
        a["score"] = score_assessment(
            a.get("match_score", 0),
            a.get("relevance", 0),
            a.get("popularity", 0)
        )

    return sorted(assessments, key=lambda x: x["score"], reverse=True)