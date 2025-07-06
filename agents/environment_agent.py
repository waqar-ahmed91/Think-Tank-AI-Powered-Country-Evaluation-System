from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

# Shared LLM Configuration
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# === AGENTS ===
EnvironmentAgent = Agent(
    role="Environmental Strategist",
    goal="Assess environmental sustainability, climate policy, and natural resource management (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="Expert in climate risk, carbon policy, and ecological trends.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)