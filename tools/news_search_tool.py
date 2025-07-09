# tools/news_search_tool.py
from crewai.tools import tool
from serpapi import GoogleSearch
import os
import requests
from dotenv import load_dotenv
from ddgs import DDGS
from datetime import datetime, timedelta

load_dotenv()

# @tool("gnews_search_tool")
# def gnews_search_tool(query: str) -> str:
#     """
#     Search GNews API for recent news articles.
#     Input: query string (e.g., 'Pakistan politics')
#     """
#     api_key = os.getenv("GNEWS_API_KEY")
#     if not api_key:
#         return "❌ GNEWS_API_KEY not found in environment variables."

#     url = "https://gnews.io/api/v4/search"
#     params = {
#         "q": query,
#         "lang": "en",
#         "max": 3,
#         "token": api_key
#     }

#     try:
#         response = requests.get(url, params=params)
#         data = response.json()

#         if not data.get("articles"):
#             return "No articles found."

#         return "\n\n".join(
#             f"📰 **{a['title']}**\n{a['url']}\n{a.get('description', '')}"
#             for a in data["articles"]
#         )

#     except Exception as e:
#         return f"❌ Error fetching news: {e}"


def search_duckduckgo_news(query: str, max_results: int = 5) -> str:
    try:
        with DDGS() as ddgs:
            results = ddgs.news(query, max_results=max_results)
            if not results:
                return "No news found."

            return "\n\n".join(
                f"📰 **{r['title']}**\n{r['url']}\n{r.get('snippet', '')}" for r in results
            )
    except Exception as e:
        return f"❌ Error during news search: {e}"

@tool("news_search_tool")
def news_search_tool(query: str) -> str:
    """
    Search DuckDuckGo News for recent articles.

    Parameters:
    - query (str): The search query string (e.g., "Pakistan education").

    Returns:
    - str: A list of recent news headlines with URLs.

    Usage:
    news_search_tool(query="Pakistan education")
    """
    return search_duckduckgo_news(query)


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
