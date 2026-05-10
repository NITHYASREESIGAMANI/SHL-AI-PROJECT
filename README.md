# SHL AI Assessment Recommendation System

AI-powered SHL Assessment Recommendation System built using FastAPI, Python, LLM integration, memory handling, ranking logic, and assessment recommendation engine.

---

# Live Deployment URL

## Render Live URL

[SHL AI Project Live Demo](https://shl-ai-project-561w.onrender.com?utm_source=chatgpt.com)

---

# GitHub Repository

## GitHub Source Code

[SHL AI Project GitHub Repository](https://github.com/NITHYASREESIGAMANI/SHL-AI-PROJECT?utm_source=chatgpt.com)

---

# Features

- SHL assessment recommendation
- AI-based intent detection
- Conversation memory
- Assessment comparison
- Ranking and scoring system
- FastAPI backend
- REST API support
- Render cloud deployment

---

# Tech Stack

- Python
- FastAPI
- Uvicorn
- Google Gemini API
- Pydantic
- Requests
- BeautifulSoup
- JSON
- Render

---

# Project Structure

```bash
SHL-AI-PROJECT/
│
├── app/
│   ├── main.py
│   ├── llm.py
│   ├── recommender.py
│   ├── comparator.py
│   ├── scorer.py
│   ├── memory.py
│   ├── prompts.py
│   ├── logger.py
│   ├── scraper.py
│   ├── schema.py
│   └── data/
│       └── shl_catalog.json
│
├── requirements.txt
├── README.md
└── .gitignore
API Endpoints
1. Health Check API
Endpoint
GET /health
Live API URL
https://shl-ai-project-561w.onrender.com/health
Sample Response
{
    "status": "ok"
}
2. Chat Recommendation API
Endpoint
POST /chat
Live API URL
https://shl-ai-project-561w.onrender.com/docs
Request Body
Use this JSON body inside POST request
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java backend developer"
    }
  ]
}
Sample Response
{
    "reply": "Top SHL assessments for developer role.",
    "recommendations": [
        {
            "name": "Core Java Entry Level",
            "url": "https://www.shl.com/",
            "test_type": "K",
            "match_score": 80,
            "relevance": 75,
            "popularity": 85,
            "score": 79.5
        },
        {
            "name": "Java 8 (New)",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/java-8-new/",
            "test_type": "K",
            "match_score": 80,
            "relevance": 75,
            "popularity": 85,
            "score": 79.5
        },
        {
            "name": "Full Stack Developer Test",
            "url": "https://www.shl.com/",
            "test_type": "K",
            "match_score": 80,
            "relevance": 75,
            "popularity": 85,
            "score": 79.5
        }
    ],
    "confidence": "high",
    "memory": {
        "role": "developer",
        "skills": [
            "java"
        ],
        "intent": "recommend",
        "history": [
            "Hiring Java backend developer"
        ]
    },
    "evaluation_report": {
        "role": "developer",
        "skills_detected": [
            "java"
        ],
        "intent": "recommend",
        "model_confidence": "high",
        "recommendation_strategy": "memory + scoring + ranking"
    },
    "end_of_conversation": true
}
How to Run Locally
1. Clone Repository
git clone https://github.com/NITHYASREESIGAMANI/SHL-AI-PROJECT.git
2. Move Into Project Folder
cd SHL-AI-PROJECT
3. Create Virtual Environment
python -m venv venv
4. Activate Virtual Environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
6. Run FastAPI Server
uvicorn app.main:app --reload
Local Server URL
http://127.0.0.1:8000
Swagger API Documentation
http://127.0.0.1:8000/docs
Deployment Platform

Project deployed using:

Render Cloud Platform
Author

NITHYASREE S

inside readme file give everything properly give
SHL AI Assessment Recommendation System

AI-powered SHL Assessment Recommendation System built using FastAPI, Python, LLM integration, memory handling, ranking logic, and assessment recommendation engine.

Live Deployment URL
Render Live URL

SHL AI Project Live Demo

GitHub Repository
Source Code

SHL AI Project GitHub Repository

Features
AI-based SHL assessment recommendation
Intent detection using LLM
Conversation memory handling
Assessment ranking and scoring
SHL assessment comparison
REST API support
FastAPI backend
Render cloud deployment
Tech Stack
Python
FastAPI
Uvicorn
Google Gemini API
Pydantic
Requests
BeautifulSoup
JSON
Render
Project Structure
SHL-AI-PROJECT/
│
├── app/
│   ├── main.py
│   ├── llm.py
│   ├── recommender.py
│   ├── comparator.py
│   ├── scorer.py
│   ├── memory.py
│   ├── prompts.py
│   ├── logger.py
│   ├── scraper.py
│   ├── schema.py
│   └── data/
│       └── shl_catalog.json
│
├── requirements.txt
├── README.md
└── .gitignore
API Endpoints
1. Health Check API
Endpoint
GET /health
Live URL
https://shl-ai-project-561w.onrender.com/health
Response
{
    "status": "ok"
}
2. Chat Recommendation API
Endpoint
POST /chat
Live URL
https://shl-ai-project-561w.onrender.com/chat
POST Request Body

Use the following JSON body inside POST request.

{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java backend developer"
    }
  ]
}
Sample API Response
{
    "reply": "Top SHL assessments for developer role.",
    "recommendations": [
        {
            "name": "Core Java Entry Level",
            "url": "https://www.shl.com/",
            "test_type": "K",
            "match_score": 80,
            "relevance": 75,
            "popularity": 85,
            "score": 79.5
        },
        {
            "name": "Java 8 (New)",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/java-8-new/",
            "test_type": "K",
            "match_score": 80,
            "relevance": 75,
            "popularity": 85,
            "score": 79.5
        },
        {
            "name": "Full Stack Developer Test",
            "url": "https://www.shl.com/",
            "test_type": "K",
            "match_score": 80,
            "relevance": 75,
            "popularity": 85,
            "score": 79.5
        }
    ],
    "confidence": "high",
    "memory": {
        "role": "developer",
        "skills": [
            "java"
        ],
        "intent": "recommend",
        "history": [
            "Hiring Java backend developer"
        ]
    },
    "evaluation_report": {
        "role": "developer",
        "skills_detected": [
            "java"
        ],
        "intent": "recommend",
        "model_confidence": "high",
        "recommendation_strategy": "memory + scoring + ranking"
    },
    "end_of_conversation": true
}
How to Run the Project Locally
Step 1 — Clone Repository
git clone https://github.com/NITHYASREESIGAMANI/SHL-AI-PROJECT.git
Step 2 — Move to Project Folder
cd SHL-AI-PROJECT
Step 3 — Create Virtual Environment
python -m venv venv
Step 4 — Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Step 5 — Install Dependencies
pip install -r requirements.txt
Step 6 — Run FastAPI Server
uvicorn app.main:app --reload
Local Development URLs
Local Server
http://127.0.0.1:8000
Swagger Documentation
http://127.0.0.1:8000/docs
Testing API Using Swagger UI
Step 1

Open Swagger documentation:

http://127.0.0.1:8000/docs
Step 2

Click:

POST /chat
Step 3

Click:

Try it out
Step 4

Paste this request body:

{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java backend developer"
    }
  ]
}
Step 5

Click:

Execute
Step 6

View AI-generated SHL assessment recommendations.

Deployment

Project deployed using Render Cloud Platform.

Author

NITHYASREE S
