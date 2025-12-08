<h1 align="center">Text Utility API</h1>

<p align="center">
  <strong>A lightweight, modular, production-ready FastAPI service</strong> that provides essential NLP utilities like text summarization, sentiment analysis, wordcount, and keyword extraction, along with a clean Streamlit UI.
</p>

<p align="center">
  This project is designed to demonstrate practical use of:<br>
  Git & GitHub workflow (feature branching, PRs, merges) • GitHub Actions CI • Modular FastAPI architecture • Deployment on Render • Front-end + API integration using Streamlit
</p>

<h2>🔧 Features</h2>

<h3>Backend (FastAPI)</h3>
<ul>
  <li><code>/summary</code> – Returns a short summary of the input text</li>
  <li><code>/sentiment</code> – Classifies sentiment as positive, negative, or neutral</li>
  <li><code>/wordcount</code> – Returns total number of words</li>
  <li><code>/keywords</code> – Extracts unique keywords</li>
</ul>
<p><strong>All endpoints use unified BaseModel input and modular router architecture.</strong></p>

<h3>Frontend (Streamlit UI)</h3>
<ul>
  <li>Clean and minimal UI</li>
  <li>Connects to deployed FastAPI backend</li>
  <li>Allows users to interact with all features in one place</li>
  <li>Instant results with JSON output</li>
</ul>

<h2>🚀 Live Deployment</h2>

<strong>Backend (FastAPI):</strong><br>
<a href="https://text-utility-161s.onrender.com">https://text-utility-161s.onrender.com</a><br><br>

<strong>Swagger Docs:</strong><br>
<a href="https://text-utility-161s.onrender.com/docs">https://text-utility-161s.onrender.com/docs</a><br><br>

<strong>Frontend (Streamlit):</strong><br>
(Will be added after UI deployment)

<h2>📁 Project Structure</h2>

<pre>
text_utility/
│
├── src/
│   ├── main.py
│   ├── routes/
│   │   ├── summary.py
│   │   ├── sentiment.py
│   │   ├── wordcount.py
│   │   └── keywords.py
│   └── tests/
│
├── ui/
│   ├── app.py
│   └── requirements.txt
│
├── requirements.txt
├── README.md
└── .gitignore
</pre>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>FastAPI – Backend API</li>
  <li>Pytest – Unit tests</li>
  <li>Streamlit – UI frontend</li>
  <li>Requests – API communication</li>
  <li>GitHub Actions – CI pipeline</li>
  <li>Render – Deployment</li>
</ul>

<h2>🧪 Running Backend Locally</h2>

<pre>
# Create environment
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run server
uvicorn src.main:app --reload
</pre>

<h2>🖥️ Running UI Locally</h2>

<pre>
cd ui
pip install -r requirements.txt
streamlit run app.py
</pre>

<h2>⚙️ CI / CD Pipeline</h2>
<p>GitHub Actions automatically runs:</p>
<ul>
  <li>Test suite (pytest)</li>
  <li>Linting</li>
  <li>Build</li>
  <li>Deployment trigger</li>
</ul>
<p><strong>Any PR merged into main triggers an auto-deploy on Render.</strong></p>

<h2>👨‍💻 Author</h2>
<p><strong>Vikas</strong> – Building practical GenAI & NLP applications with modern backend workflows.</p>

<p align="center">
  <i>Made with ❤️ and lots of coffee</i>
</p>
