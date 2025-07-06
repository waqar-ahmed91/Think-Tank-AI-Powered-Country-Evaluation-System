from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

# Shared LLM Configuration
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# === AGENT ===
ForeignPolicyAgent = Agent(
    role="Foreign Affairs Analyst",
    goal="Analyze international relations, diplomacy, and geopolitical risk (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="A former diplomat and intelligence advisor focused on global alliances and emerging threats.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)