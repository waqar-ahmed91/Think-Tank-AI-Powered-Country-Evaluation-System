from crewai.tools import tool
import os
import requests
from dotenv import load_dotenv

load_dotenv()

@tool("gnews_search_tool")
def gnews_search_tool(query: str) -> str:
    """
    Search GNews API for recent news articles.
    Input: query string (e.g., 'Pakistan politics')
    """
    api_key = os.getenv("GNEWS_API_KEY")
    if not api_key:
        return "❌ GNEWS_API_KEY not found in environment variables."

    url = "https://gnews.io/api/v4/search"
    params = {
        "q": query,
        "lang": "en",
        "max": 3,
        "token": api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if not data.get("articles"):
            return "No articles found."

        return "\n\n".join(
            f"📰 **{a['title']}**\n{a['url']}\n{a.get('description', '')}"
            for a in data["articles"]
        )

    except Exception as e:
        return f"❌ Error fetching news: {e}"
