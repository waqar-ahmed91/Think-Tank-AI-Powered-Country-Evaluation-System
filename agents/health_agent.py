from crewai import Agent, Task
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool

# Shared LLM Configuration
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# === AGENTS ===
HealthAgent = Agent(
    role="Health Policy Analyst",
    goal="Evaluate healthcare infrastructure, outcomes, and health-related policies (from the last 6 months) and avoid over-relying on older outdated data.",
    backstory="A seasoned public health researcher analyzing disease burden, hospital capacity, and public health initiatives.",
    tools=[news_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm
)