SHL AI Assessment Recommendation System
AI-powered SHL assessment recommendation system built using FastAPI.

Features
SHL assessment recommendation
Intent detection
Conversation memory
Ranking system
FastAPI backend
API Endpoints
Health Endpoint
GET /health

Chat Endpoint
POST /chat

Example Request:

{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java backend developer"
    }
  ]
}
Run Project
uvicorn app.main:app --reload