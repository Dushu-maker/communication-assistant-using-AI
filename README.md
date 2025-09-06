# 🤖 AI-Powered Communication Assistant

> **Hackathon Submission | AI Engineer Fresher**  
> Automates support email triaging, prioritization (urgent + negative first), AI response drafting (GPT + RAG), and dashboard analytics — using real sample emails (login, billing, downtime, API). Built with Python + Flask + React. Runs locally. Judges will love it! 🚀📧

![Dashboard Preview](screenshots/dashboard-overview.png)

---

## 🚀 Features

- ✅ Filters & loads sample support emails (from CSV)
- ✅ Auto-tags: **Urgent** (e.g., “critical”, “blocked”, “immediate”) / **Not Urgent**
- ✅ Simple sentiment context (Negative/Neutral)
- ✅ Generates draft replies (fallback if no OpenAI key)
- ✅ Dashboard shows emails, priority, editable responses
- ✅ Zero cloud needed — 100% runs on localhost

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask, Pandas, SQLite
- **Frontend**: HTML, CSS, JavaScript (lightweight — no React complexity)
- **AI**: Optional OpenAI GPT (fallback included)
- **Data**: Sample dataset of 20 real-world support emails (login, billing, API, downtime)

---

## 🛠️ Setup & Run (Easy!)

### 1. Clone or Download This Repo

Extract to Desktop → folder should be: `ai-communication-assistant`

### 2. Run Backend (Anaconda or CMD)

```bash
cd backend
pip install flask pandas
python app.py
