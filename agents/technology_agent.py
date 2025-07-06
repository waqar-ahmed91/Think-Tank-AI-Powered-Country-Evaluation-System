from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

# Shared LLM Configuration
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

TechnologyAgent = Agent(
    role="Technology Strategist",
    goal="Evaluate digital infrastructure, AI readiness, and R&D ecosystems (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="An innovation policy specialist mapping the nation's tech competitiveness.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)
