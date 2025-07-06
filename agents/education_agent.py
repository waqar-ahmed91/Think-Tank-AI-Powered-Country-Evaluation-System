from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

EducationAgent = Agent(
    role='Education Analyst',
    goal='Analyze educational performance and suggest reforms to improve literacy and skills (from the last 6 months) and avoid over-relying on older outdated data',
    backstory='A veteran education policy researcher with expertise in UNESCO/OECD data.',
    verbose=True,
    tools=[news_search_tool],
    allow_delegation=False,
    llm=llm
)
