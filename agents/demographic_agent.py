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
#     # Optional, but strongly recommended for Ollama tool support:
#     additional_kwargs={
#         "tool_choice": "auto",
#         "auto_continue": True,  # this is CRITICAL to continue after tool result
#         }
# )
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)


DemographicsAgent = Agent(
    role="Population Dynamics Analyst",
    goal="Examine population growth, migration, age structure, and demographic challenges in {country}, avoiding over-reliance on outdated data.",
    backstory="Tracks census data, fertility trends, migration, and age structures to assess national development capacity and risks.",
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "You are a demographic expert. You must use the `news_search_tool` to gather up-to-date insights before writing your analysis. "
        "Do not rely solely on prior knowledge.\n\n"
        "Your analysis should include:\n"
        "- Population growth trends\n"
        "- Age structure and working-age population share\n"
        "- Labor force trends and challenges\n"
        "- Migration patterns (internal and external)\n\n"
        "After using the tool, summarize the demographic trajectory using clear, plain language. "
        "Avoid speculation. Conclude with demographic implications for national development, including labor policy or urban planning considerations."
    )
)
