from google import genai
import os

def summarize_news(raw_news):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    model_id = "gemini-2.5-flash-lite" 

    # Compact High-Density Prompt
    prompt = f"""
    Role: Elite Tech Analyst for C-suite Executives.
    Task: Synthesize news metadata into a high-signal Telegram briefing.
    Data: {raw_news}

    Guidelines:
    - Merge duplicates; prioritize high-impact stories.
    - Style: Professional, objective, technical (e.g., use 'latency', 'RAG', 'scalability').
    - Format: Telegram Markdown (**Bold**, *Italic*).
    - Limit: Max 3 items per category.

    Structure:
    📅 **[Current Date] | Daily Intel Brief**

    **[CATEGORY NAME]**
    • **[Title]**
      - 💡 *Impact:* [Technical 'So What?' in 1 sentence].
      - 🔗 [Link]

    Execute Briefing:
    """

    try:
        response = client.models.generate_content(model=model_id, contents=prompt)
        return response.text
    except Exception as e:
        return f"⚠️ AI Summary Error: {str(e)}"