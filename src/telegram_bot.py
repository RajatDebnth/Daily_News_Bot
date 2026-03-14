import requests
import os

def send_to_telegram(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # Telegram has a 4096 character limit per message
    if len(message) > 4000:
        message = message[:3900] + "..."

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, data=payload)
    return response.status_code == 200