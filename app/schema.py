from pydantic import BaseModel
from typing import List, Optional

class Recommendation(BaseModel):
    name: str
    score: float
    match_score: int
    relevance: int
    popularity: int

class ChatResponse(BaseModel):
    reply: str
    recommendations: List[Recommendation] = []
    confidence: Optional[str] = "medium"
    end_of_conversation: bool = False