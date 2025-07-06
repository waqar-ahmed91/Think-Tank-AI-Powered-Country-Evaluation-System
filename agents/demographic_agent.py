from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

DemographicsAgent = Agent(
    role="Population Dynamics Analyst",
    goal="Examine population growth, migration, age structure, and demographic challenges (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="Tracks census data, fertility trends, and their policy implications.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)