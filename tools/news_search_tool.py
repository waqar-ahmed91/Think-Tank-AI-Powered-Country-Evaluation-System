# tools/news_search_tool.py
from crewai.tools import tool, BaseTool
from serpapi import GoogleSearch
import os
import requests
from dotenv import load_dotenv
from ddgs import DDGS
from datetime import datetime, timedelta

load_dotenv()

@tool("news_search_tool")
def news_search_tool(query: str) -> str:
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

# def search_duckduckgo_news(query: str, max_results: int = 15, months: int = 12) -> str:
#     cutoff = datetime.utcnow() - timedelta(days=30 * months)

#     with DDGS() as ddgs:
#         results = ddgs.news(query, max_results=max_results)
#         if not results:
#             return "No news found."

#         # Filter news items by date within the specified range
#         fresh_results = [
#             r for r in results
#             if isinstance(r.get("date"), datetime) and r["date"] > cutoff
#         ]

#         if not fresh_results:
#             return f"No news found from the past {months} month(s)."

#         return "\n\n".join(
#             f"📰 **{r['title']}**\n{r['url']}\n{r.get('snippet', '')}" for r in fresh_results
#         )

# @tool("news_search_tool")
# def news_search_tool(query: str) -> str:
#     """
#     Search DuckDuckGo News for articles from the past 12 months.
#     """
#     return search_duckduckgo_news(query, months=12)


# @tool
# def news_search_tool(query: str, recency: str = "d", num_results: int = 5) -> str:
#     """
#     Search Google News for recent articles using SerpAPI.

#     Parameters:
#     - query: Search term (e.g., "Pakistan inflation").
#     - recency: 'd' for day, 'w' for week, 'm' for month, '' for no filter.
#     - num_results: Number of articles to return (default: 5).
#     """
#     api_key = os.getenv("SERPAPI_API_KEY")
#     if not api_key:
#         return "❌ SERPAPI_API_KEY not found."

#     params = {
#         "engine": "google",
#         "q": query,
#         "tbm": "nws",
#         "api_key": api_key
#     }

#     if recency:
#         params["tbs"] = f"qdr:{recency}"

#     try:
#         search = GoogleSearch(params)
#         results = search.get_dict()
#         articles = results.get("news_results", [])[:num_results]
#         if not articles:
#             return "No news found."

#         return "\n\n".join(
#             f"📰 {a['title']}\n{a['link']}\n{a.get('snippet', '')}" for a in articles
#         )

#     except Exception as e:
#         return f"❌ Error during search: {e}"
