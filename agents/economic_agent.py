from crewai import Agent, LLM
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool
from tools.gnews_search_tool import gnews_search_tool
from langchain_ollama import OllamaLLM as Ollama
from tools.internet_search import internet_search_tool
# llm = LLM(
#     provider="ollama",
#     model="ollama/qwen2.5:7b",
#     base_url="http://localhost:11434",
#     temperature=0.3,
#     # system="Always respond using valid JSON. If a tool was called, wait for the tool result, then output a clean and final answer only — no thoughts, no planning.",
#     additional_kwargs={
#         "tool_choice": "auto",
#         "auto_continue": True,  # this is CRITICAL to continue after tool result
#         }
# )
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)


EconomicAgent = Agent(
    role="Economic Analyst",
    goal="Evaluate the country’s economic conditions using current data and provide strategic recommendations. Avoid relying on outdated information.",
    backstory="An expert economist tracking GDP, inflation, labor markets, trade balances, and fiscal policy to shape national strategies.",
    verbose=True,
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    llm=llm,
    system_prompt=(
        "You are an economic policy expert. Before writing any analysis, you must use the `news_search_tool` to gather the latest economic updates. "
        "Avoid relying only on your training data or prior knowledge.\n\n"
        "Focus your analysis on:\n"
        "- GDP growth trends and structure\n"
        "- Inflation, interest rates, and monetary policy\n"
        "- Labor market trends and employment\n"
        "- Key economic sectors (e.g., agriculture, services, manufacturing)\n"
        "- Trade balance and foreign investment\n\n"
        "After reviewing the news and data, write a structured analysis in plain English. Avoid vague claims or unsupported assumptions. "
        "Conclude with 2–3 strategic implications for economic planning (e.g., fiscal policy, labor force development, industrial focus)."
    )
)


