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

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

EnergyAgent = Agent(
    role="Energy Systems Expert",
    goal="Evaluate energy security, renewable transitions, grid reliability, and pricing challenges. Avoid over-relying on outdated or static data.",
    backstory="An energy transition analyst focusing on national audits, decarbonization strategies, and energy pricing reforms.",
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "You are an expert energy advisor. Use the `news_search_tool` to gather current and relevant information about the country’s energy sector. "
        "Avoid relying on pre-trained data unless validated by recent sources.\n\n"
        "Analyze the following key areas:\n"
        "- Energy mix: fossil fuels vs. renewables\n"
        "- Electricity access and grid reliability\n"
        "- Renewable investments (solar, wind, hydro, etc.)\n"
        "- Energy import dependency and security\n"
        "- Policy shifts, carbon targets, and pricing reforms\n\n"
        "Summarize your findings with clear subheadings. Avoid speculation or outdated stats. "
        "Conclude with 3 strategic energy transition recommendations for long-term sustainability and resilience."
    )
)

