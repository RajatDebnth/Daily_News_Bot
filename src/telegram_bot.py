import requests
import os

def send_to_telegram(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # Final safety truncate
    if len(message) > 4050:
        message = message[:4000] + "\n\n*(Briefing truncated to fit Telegram limit)*"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True # Keeps the message compact
    }
    
    response = requests.post(url, data=payload)
    return response.status_code == 200