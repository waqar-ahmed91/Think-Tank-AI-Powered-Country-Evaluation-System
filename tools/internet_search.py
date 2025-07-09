# tools/internet_search.py
from crewai.tools import BaseTool
from ddgs import DDGS

class InternetSearchTool(BaseTool):
    name: str = "news_search_tool"
    description: str = "Useful for finding recent news articles from the internet"

    def _run(self, query: str) -> str:
        try:
            with DDGS() as ddgs:
                results = ddgs.text(query, max_results=5)
                summaries = [r.get("body", "") or r.get("snippet", "") for r in results]
                return "\n".join(summaries) if summaries else "No results found."
        except Exception as e:
            return f"Error during search: {str(e)}"

# Export the tool instance
internet_search_tool = InternetSearchTool()
