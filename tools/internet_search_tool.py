from typing import Optional
from crewai_tools import BaseTool
from duckduckgo_search import DDGS
from crewai_tools import BaseTool
class InternetSearchTool(BaseTool):
    name = "internet_search_tool"
    description = (
        "Use this tool to search the internet using DuckDuckGo for up-to-date information. "
        "It returns relevant snippets from the top 5 results. Ideal for news, trends, or fact-checking."
    )

    def _run(self, query: str) -> str:
        try:
            ddgs = DDGS()
            results = ddgs.text(query, max_results=5)
            filtered_results = [result for result in results if 'body' in result]
            if not filtered_results:
                return "No relevant search results found."
            return "\n\n".join([f"📰 {r['title']}\n{r['body']}\n{r['href']}" for r in filtered_results])
        except Exception as e:
            return f"❌ Error during DuckDuckGo search: {e}"
