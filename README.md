# 🐦 AI Tweet Generator (FastAPI + LLaMA 3)

An AI-powered web application that generates 10 human-like tweets based on a given topic or context. The system uses real-time web search and a large language model to produce natural, news-inspired tweets.

## 🚀 Features

* 🔍 Real-time web search using Serper API
* 🤖 Tweet generation using LLaMA 3.3 (70B) via Groq API
* ✍️ Generates exactly 10 unique tweets
* 🧠 Each tweet is inspired by a different source
* ⚡ Fast and lightweight backend built with FastAPI
* 🎨 Simple and clean frontend using HTML, CSS, JavaScript
* 📄 Interactive API documentation via Swagger UI

## 🛠️ Tech Stack

### Backend
* Python
* FastAPI
* Groq API (LLaMA 3.3 – 70B)
* Serper API (Google Search)
* Uvicorn
* Pydantic

### Frontend
* HTML
* CSS
* JavaScript (Fetch API)

## 📂 Project Structure

```
tweet-generator/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── services/
│   │       └── tweet_service.py
│   ├── requirements.txt
│   └── .env (ignored)
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
└── README.md
```

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/tweet-generator.git
cd tweet-generator
```

### 2️⃣ Backend Setup

**Create virtual environment:**

```bash
python -m venv env
```

**Activate (Windows):**

```bash
env\Scripts\activate
```

**Activate (macOS/Linux):**

```bash
source env/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Create `.env` file:**

```env
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

**Run the server:**

```bash
uvicorn app.main:app --reload
```

Backend will run at: `http://127.0.0.1:8000`

Swagger UI: `http://127.0.0.1:8000/docs`

### 3️⃣ Frontend Setup

Open `index.html` using:
* VS Code Live Server
* or any browser

Frontend communicates with backend at: `http://127.0.0.1:8000/generate_tweets`

## 🔁 API Endpoint

### `POST /generate_tweets`

**Request Body:**

```json
{
  "topic": "AI in healthcare"
}
```

**Response:**

```json
{
  "tweets": [
    "AI is quietly transforming diagnostics by catching patterns doctors might miss.",
    "Hospitals using AI tools are seeing faster workflows and fewer errors.",
    "..."
  ]
}
```

## 🎯 Use Case Examples

* Social media content generation
* News-based tweet inspiration
* AI + Web Search applications
* Learning project for FastAPI & LLM integration

## 🧠 What I Learned

* Designing REST APIs using FastAPI
* Integrating large language models via external APIs
* Combining web search with LLM context building
* Handling CORS and frontend-backend communication
* Writing clean, modular backend services

## 🔒 Security Notes

* API keys are stored in `.env` (not committed)
* Virtual environments are excluded via `.gitignore`

## 👤 Author

**Suguna**  
Python Developer | FastAPI | AI & LLM Projects

---

⭐ If you found this project helpful, please consider giving it a star!
