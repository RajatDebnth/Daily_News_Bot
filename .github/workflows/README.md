# 🤖 AI News Assistant (v1.0.0)

An automated news intelligence agent that scrapes high-signal technical news, processes it using **Gemini 2.5 Flash**, and dispatches a daily briefing to **Telegram**.

---

## 🚀 Overview
This project is a serverless news aggregator built for **Data Engineers** and **AI Architects**. It solves the problem of "information overload" by filtering global RSS feeds into a concise, actionable daily briefing.

### Key Features
* **Targeted Scraping**: Tracks AI, Robotics, Tech Careers, and World Affairs.
* **AI Synthesis**: Uses Google's **Gemini 2.5 Flash** for high-signal summarization.
* **Dual-Layer Automation**: Runs locally for testing and via **GitHub Actions** for 24/7 automation.
* **Zero Infrastructure**: Fully serverless; uses GitHub's cloud runners.

---

## 🛠️ Tech Stack
* **Language**: Python 3.12
* **AI Engine**: Google Gen AI SDK (`gemini-2.5-flash-lite`)
* **Data Source**: Feedparser (Google News RSS)
* **Delivery**: Telegram Bot API
* **Automation**: GitHub Actions (Cron: `08:00 AM IST`)

---

## 📁 Project Structure
```text
ai-news-assistant/
├── .github/workflows/
│   └── daily_news.yml      # GitHub Actions Automation config
├── src/
│   ├── scraper.py          # RSS feed logic
│   ├── brain.py            # AI Prompt Engineering & Processing
│   └── telegram_bot.py     # Telegram API integration
├── main.py                 # Application Entry Point
├── requirements.txt        # Pinned dependencies
├── .env                    # Local API Keys (HIDDEN)
└── test_setup.py           # Pre-flight diagnostic tool