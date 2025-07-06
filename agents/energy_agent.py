from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

# Shared LLM Configuration
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

EnergyAgent = Agent(
    role="Energy Systems Expert",
    goal="Evaluate energy security, renewable transitions, and grid resilience (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="Works on national energy audits, carbon transition roadmaps, and pricing models.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)
