from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

EconomicAgent = Agent(
    role='Economic Analyst',
    goal='Evaluate the country’s economic conditions and provide strategic suggestions (from the last 6 months) and avoid over-relying on older outdated data',
    backstory='An expert economist tracking GDP, trade, inflation, and fiscal policy.',
    verbose=True,
    tools=[news_search_tool],
    allow_delegation=False,
    llm=llm
)


