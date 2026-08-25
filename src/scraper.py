import feedparser
import urllib.parse
from datetime import datetime
import pytz

# TOPICS_EVEN = {
#     "Core AI & Agents": [
#         "Agentic AI & Multi-Agent Orchestration", 
#         "NCLC AI App Builders & Platform Updates", 
#         "Vector Databases & Scalable Backends"
#     ],
#     "Enterprise & Compliance": [
#         "AI Regulatory Compliance & Data Privacy",
#         "Citizen Development & Shadow IT Governance",
#         "AI Monetization & SaaS Pricing Models"
#     ]
# }

# TOPICS_ODD = {
#     "Edge & Architecture": [
#         "Small Language Models SLMs & Edge AI",
#         "API & Function Calling Enhancements",
#         "Generative AI Architecture"
#     ],
#     "Industry & UX": [
#         "Vertical AI & Industry-Specific Micro-SaaS",
#         "UI/UX for Generative Interfaces"
#     ]
# }

# All subtopics split into two sets for rotation

TOPICS_EVEN = {
    "AI Capabilities": [
        "Models: New LLMs, Reasoning, Multimodal & Small/Local Models",
        "Agents: Tool Use, Planning, Memory & Multi-Agent Systems",
        "RAG & Data: Retrieval, Databases, Long-Context & Knowledge Systems",
        "Voice & Vision: Speech, Real-Time AI & Image/Video Understanding"
    ]
}

TOPICS_ODD = {
    "AI Engineering & Application": [
        "Developer AI: Coding Agents, IDE Agents & Autonomous Development",
        "Infrastructure: Inference, Deployment, Observability & Evaluation",
        "Automation: AI Workflows, Integrations & Browser/Computer Use",
        "AI Products: New Patterns That Solve Real Business Problems"
    ]
}

def fetch_news():
    # Set timezone to IST for date checking
    ist = pytz.timezone('Asia/Kolkata')
    day = datetime.now(ist).day
    
    # Select topics based on Even/Odd day
    active_topics = TOPICS_EVEN if day % 2 == 0 else TOPICS_ODD
    
    news_data = {}
    for category, subtopics in active_topics.items():
        news_data[category] = []
        for sub in subtopics:
            query = urllib.parse.quote(sub)
            # Query the last 48h to cover the rotation gap
            url = f"https://news.google.com/rss/search?q={query}+when:48h&hl=en-US&gl=US&ceid=US:en"
            feed = feedparser.parse(url)
            
            # Limit to top 2 results per subtopic to save space
            for entry in feed.entries[:2]:
                news_data[category].append({
                    "subtopic": sub,
                    "title": entry.title,
                    "link": entry.link
                })
    return news_data
