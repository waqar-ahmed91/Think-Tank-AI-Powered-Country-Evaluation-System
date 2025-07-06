from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
RiskAgent = Agent(
    role="National Risk Strategist",
    goal="Identify cross-sectoral risks including financial, ecological, cyber, and political threats (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="Risk modeler synthesizing threat matrices and long-horizon resilience plans.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)