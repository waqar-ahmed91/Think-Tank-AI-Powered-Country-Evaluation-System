
from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
CultureAgent = Agent(
    role="Cultural Trends Advisor",
    goal="Analyze cultural influence, soft power, and public sentiment shifts (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="Combines historical context with media analytics to map social cohesion and narratives.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)