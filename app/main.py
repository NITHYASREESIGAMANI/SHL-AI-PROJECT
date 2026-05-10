from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content.lower()

    if "java" in latest_message:
        return {
            "reply": "Here are SHL assessments for Java developer.",
            "recommendations": [
                {
                    "name": "Java 8 (New)",
                    "url": "https://www.shl.com",
                    "test_type": "K"
                }
            ],
            "end_of_conversation": True
        }

    return {
        "reply": "Please specify role, experience, and skills.",
        "recommendations": [],
        "end_of_conversation": False
    }