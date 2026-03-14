import os
from dotenv import load_dotenv
from src.scraper import fetch_news
from src.brain import summarize_news
from src.telegram_bot import send_to_telegram

# Load variables from .env if running locally on your ASUS
if os.path.exists(".env"):
    load_dotenv()

def run_assistant():
    print("🚀 Starting Daily News Assistant...")
    
    # 1. Scrape data from Google News RSS
    print("📡 Scraping news feeds...")
    raw_data = fetch_news()
    if not raw_data:
        print("❌ No news found in the last 24 hours.")
        return

    # 2. Process with Gemini AI
    print("🧠 Summarizing with Gemini 2.0...")
    report = summarize_news(raw_data)
    
    # 3. Check for valid report and send
    if report and "AI Summary Error" not in report:
        print("📲 Sending to Telegram...")
        if send_to_telegram(report):
            print("✅ Success! Message delivered.")
        else:
            print("❌ Telegram delivery failed. Check your Token/ChatID.")
    else:
        print(f"❌ AI Processing failed: {report}")

if __name__ == "__main__":
    run_assistant()