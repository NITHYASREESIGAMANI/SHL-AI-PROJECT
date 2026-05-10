def analyze_query(user_query: str):

    query = user_query.lower()

    intent = "recommend"

    # detect clarification need
    needs_clarification = False

    if len(query.split()) < 2:
        needs_clarification = True

    # detect intent
    if "compare" in query:
        intent = "compare"

    elif "weather" in query or "movie" in query:
        intent = "off_topic"

    # detect skills
    skills = []

    if "java" in query:
        skills.append("java")

    if "python" in query:
        skills.append("python")

    if "sales" in query:
        skills.append("sales")

    if "manager" in query:
        skills.append("management")

    # detect role
    role = None

    if "developer" in query:
        role = "developer"

    elif "engineer" in query:
        role = "engineer"

    elif "manager" in query:
        role = "manager"

    elif "analyst" in query:
        role = "analyst"

    return {
        "intent": intent,
        "role": role,
        "skills": skills,
        "experience_level": "",
        "needs_clarification": needs_clarification
    }