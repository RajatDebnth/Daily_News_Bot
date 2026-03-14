import feedparser
import urllib.parse

TOPICS = {
    "AI & Data Science": ["Agentic AI", "Generative AI Architecture", "MLOps", "AI Ethics"],
    "Robotics": ["Embodied AI", "Semiconductors", "Embedded Systems", "Sensors"],
    "Tech Career": ["Tech Job Roles", "Tech Hubs", "Skill Demand"],
    "World Affairs": ["Geopolitics of Tech", "Supply Chain", "Global Macroeconomics"]
}

def fetch_news():
    news_data = {}
    for category, subtopics in TOPICS.items():
        news_data[category] = []
        for sub in subtopics:
            query = urllib.parse.quote(sub)
            # Fetching news from the last 24 hours
            url = f"https://news.google.com/rss/search?q={query}+when:24h&hl=en-US&gl=US&ceid=US:en"
            feed = feedparser.parse(url)
            for entry in feed.entries[:2]: # Top 2 per subtopic
                news_data[category].append({
                    "subtopic": sub,
                    "title": entry.title,
                    "link": entry.link
                })
    return news_data