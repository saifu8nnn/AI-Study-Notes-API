# AI Study Notes API 📚🤖

A production-ready REST API for managing study notes with AI-powered summarization. Built with FastAPI, PostgreSQL, and Groq AI.

**Live API:** https://ai-study-notes-api.onrender.com/

**Interactive Docs:** https://ai-study-notes-api.onrender.com/docs

---

## Features

- Full CRUD operations for study notes
- AI-powered automatic summarization using Groq (LLaMA 3.3 70B)
- PostgreSQL database for persistent storage
- SQLAlchemy ORM for database management
- Pydantic validation for request/response models
- Dockerized for easy deployment

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **AI:** Groq API (LLaMA 3.3 70B)
- **Validation:** Pydantic
- **Containerization:** Docker + Docker Compose
- **Deployment:** Render

---

## How to Use (No Setup Required)

The API is live and ready to use. The easiest way to interact with it is through the interactive docs.

### Option 1 — Interactive Docs (Recommended)

Visit: **https://ai-study-notes-api.onrender.com/docs**

This opens a Swagger UI where you can test all endpoints directly in your browser — no Postman or setup needed.

### Option 2 — Postman or any HTTP client

Use the base URL: `https://ai-study-notes-api.onrender.com`

---

## API Endpoints

### Create a Note
```
POST /notes
```
**Request Body:**
```json
{
  "title": "Machine Learning Basics",
  "content": "Machine learning is a subset of AI that enables systems to learn from data without being explicitly programmed."
}
```
**Response:** Returns the created note with an AI-generated summary automatically attached.

---

### Get All Notes
```
GET /notes
```
**Response:** Returns a list of all saved notes.

---

### Get a Single Note
```
GET /notes/{id}
```
**Response:** Returns the note with the matching ID or 404 if not found.

---

### Update a Note
```
PUT /notes/{id}
```
**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content goes here."
}
```
**Response:** Returns the updated note.

---

### Delete a Note
```
DELETE /notes/{id}
```
**Response:** 204 No Content if deleted, 404 if not found.

---

## Run Locally

### Prerequisites
- Python 3.12+
- PostgreSQL
- Docker (optional)

### Without Docker

1. Clone the repo:
```bash
git clone https://github.com/saifu8nnn/AI-Study-Notes-API.git
cd AI-Study-Notes-API
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root:
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost/study_notes
GROQ_API_KEY=your_groq_api_key
```

5. Run the server:
```bash
uvicorn app.main:app --reload
```

### With Docker

1. Clone the repo and create `.env` file as above

2. Run with Docker Compose:
```bash
docker-compose up --build
```

API will be available at `http://localhost:8000`

---

## Project Structure

```
study-notes-api/
├── app/
│   ├── main.py          # FastAPI routes
│   ├── models.py        # Pydantic + SQLAlchemy models
│   ├── database.py      # Database connection and session
│   └── ai_services.py   # Groq AI integration
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env                 # Not committed to GitHub
```

---

## Author

**Saif** — 3rd year CS Engineering student at Bansal College of Engineering

Building backends, one project at a time. 🚀

Connect on LinkedIn: https://www.linkedin.com/in/saifu8n/