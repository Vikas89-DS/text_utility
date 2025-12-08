Text Utility API

A lightweight, modular, production-ready FastAPI service that provides essential NLP utilities like text summarization, sentiment analysis, wordcount, and keyword extraction, along with a clean Streamlit UI.

This project is designed to demonstrate practical use of:

Git & GitHub workflow (feature branching, PRs, merges)

GitHub Actions CI

Modular FastAPI architecture

Deployment on Render

Front-end + API integration using Streamlit

🔧 Features
Backend (FastAPI)

/summary – Returns a short summary of the input text

/sentiment – Classifies sentiment as positive, negative, or neutral

/wordcount – Returns total number of words

/keywords – Extracts unique keywords

All endpoints use unified BaseModel input and modular router architecture.

Frontend (Streamlit UI)

Clean and minimal UI

Connects to deployed FastAPI backend

Allows users to interact with all features in one place

Instant results with JSON output

🚀 Live Deployment
Backend (FastAPI):
https://text-utility-161s.onrender.com

Swagger Docs:
https://text-utility-161s.onrender.com/docs

Frontend (Streamlit):

(Will be added after UI deployment)

📁 Project Structure
text_utility/
│
├── src/
│   ├── main.py
│   ├── routes/
│   │     ├── summary.py
│   │     ├── sentiment.py
│   │     ├── wordcount.py
│   │     └── keywords.py
│   └── tests/
│
├── ui/
│   ├── app.py
│   └── requirements.txt
│
├── requirements.txt
├── README.md
└── .gitignore

🛠️ Tech Stack

FastAPI – Backend API

Pytest – Unit tests

Streamlit – UI frontend

Requests – API communication

GitHub Actions – CI pipeline

Render – Deployment

🧪 Running Backend Locally
Create environment
python -m venv venv
source venv/bin/activate  (Windows: venv\Scripts\activate)

Install requirements
pip install -r requirements.txt

Run server
uvicorn src.main:app --reload

🖥️ Running UI Locally
cd ui
pip install -r requirements.txt
streamlit run app.py

⚙️ CI / CD Pipeline

GitHub Actions automatically runs:

Test suite (pytest)

Linting

Build

Deployment trigger

Any PR merged into main triggers an auto-deploy on Render.

👨‍💻 Author

Vikas – Building practical GenAI & NLP applications with modern backend workflows.
