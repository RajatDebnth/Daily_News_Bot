from google import genai
import os
from datetime import datetime
import pytz

def summarize_news(raw_news):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    model_id = "gemini-2.5-flash-lite" 

    # Get correct date for IST
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    current_date = now.strftime('%A, %B %d, %Y')
    current_time = now.strftime('%I:%M %p')

    prompt = f"""
    Role: Senior AI Architect.
    Context: Deliver a high-signal briefing within Telegram's character limits.
    Data: {raw_news}

    Rules:
    - Date/Time: {current_date} at {current_time} IST.
    - Format: Telegram Markdown. No raw URLs. 
    - Links: Use strictly [Full Report ↗️](link).
    - Content: Merge similar stories. Max 2 bullets per sub-category.
    - Style: Concise, technical, and objective.

    Briefing Template:
    📅 **{current_date}** | 🕒 **{current_time} IST**
    ---
    **[CATEGORY]**
    • **[Title]**
      - 💡 *Impact:* [1 sentence technical insight]
      - 🔗 [Full Report ↗️](link)
    """

    try:
        response = client.models.generate_content(model=model_id, contents=prompt)
        return response.text
    except Exception as e:
        return f"⚠️ AI Summary Error: {str(e)}"