from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.llm import analyze_query
from app.recommender import recommend_assessments
from app.comparator import compare_assessments
from app.memory import ConversationMemory
from app.scorer import rank_assessments
from app.logger import log_event


# -----------------------------
# APP INIT
# -----------------------------
app = FastAPI(
    title="SHL AI Assessment Recommender",
    description="AI-powered SHL assessment recommendation system",
    version="1.0.0"
)

# -----------------------------
# MEMORY
# -----------------------------
memory = ConversationMemory()


# -----------------------------
# INVALID QUERY CHECK
# -----------------------------
def is_invalid_query(text: str):

    invalid_keywords = [
        "movie",
        "song",
        "weather",
        "cricket",
        "food",
        "recipe",
        "joke"
    ]

    return any(word in text.lower() for word in invalid_keywords)


# -----------------------------
# REQUEST MODELS
# -----------------------------
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


# -----------------------------
# HEALTH ENDPOINT
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -----------------------------
# CHAT ENDPOINT
# -----------------------------
@app.post("/chat")
def chat(request: ChatRequest):

    # -------------------------
    # VALIDATE INPUT
    # -------------------------
    if not request.messages or len(request.messages) == 0:

        return {
            "reply": "Please provide hiring requirements.",
            "recommendations": [],
            "end_of_conversation": False
        }

    # -------------------------
    # USER MESSAGE
    # -------------------------
    user_message = request.messages[-1].content.strip()

    log_event(f"User query: {user_message}")

    # -------------------------
    # OFF TOPIC CHECK
    # -------------------------
    if is_invalid_query(user_message):

        return {
            "reply": "This system only supports SHL assessments and hiring evaluations.",
            "recommendations": [],
            "end_of_conversation": True
        }

    # -------------------------
    # ANALYZE QUERY
    # -------------------------
    ai_data = analyze_query(user_message)

    log_event(f"Intent: {ai_data.get('intent', 'unknown')}")

    # -------------------------
    # UPDATE MEMORY
    # -------------------------
    memory.update(ai_data, user_message)

    context = memory.get_context()

    # -------------------------
    # COMPARISON FLOW
    # -------------------------
    if ai_data.get("intent") == "compare":

        comparison_items = ai_data.get("comparison_items", [])

        comparison = compare_assessments(comparison_items)

        if comparison:

            return {
                "reply": comparison["summary"],
                "comparison": comparison,
                "memory": context,
                "end_of_conversation": False
            }

    # -------------------------
    # BUILD SEARCH QUERY
    # -------------------------
    rewritten_query = ai_data.get("rewritten_query")

    if not rewritten_query:

        role = context.get("role", "")

        skills = " ".join(context.get("skills", []))

        rewritten_query = f"{role} {skills}"

    # -------------------------
    # GET RECOMMENDATIONS
    # -------------------------
    results = recommend_assessments(rewritten_query)

    # -------------------------
    # NO MATCHES FOUND
    # -------------------------
    if not results:

        return {
            "reply": "Can you specify role, skills, or experience level?",
            "recommendations": [],
            "confidence": "low",
            "memory": context,
            "end_of_conversation": False
        }

    # -------------------------
    # ENRICH RESULTS
    # -------------------------
    enriched_results = []

    for r in results:

        enriched_results.append({
            "name": r["name"],
            "url": r["url"],
            "test_type": r["test_type"],
            "match_score": 80,
            "relevance": 75,
            "popularity": 85
        })

    # -------------------------
    # RANK RESULTS
    # -------------------------
    ranked = rank_assessments(enriched_results)

    # -------------------------
    # FINAL RESPONSE
    # -------------------------
    return {
        "reply": f"Top SHL assessments for {context.get('role')} role.",
        "recommendations": ranked,
        "confidence": "high",
        "memory": context,
        "evaluation_report": {
            "role": context.get("role"),
            "skills_detected": context.get("skills"),
            "intent": ai_data.get("intent"),
            "model_confidence": "high",
            "recommendation_strategy": "memory + scoring + ranking"
        },
        "end_of_conversation": True
    }