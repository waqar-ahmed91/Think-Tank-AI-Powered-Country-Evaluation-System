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

CultureAgent = Agent(
    role="Cultural Trends Advisor",
    goal="Analyze cultural influence, soft power, and public sentiment shifts in {country}, avoiding reliance on outdated data.",
    backstory="Combines historical context with media analytics to map social cohesion and cultural narratives.",
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "You are a cultural trends expert. You must use the `news_search_tool` at least once to retrieve the most recent insights. "
        "Do not rely solely on prior knowledge.\n\n"
        "Focus your analysis on:\n"
        "- Social cohesion and national identity\n"
        "- Ethnic and religious diversity\n"
        "- Media narratives and public sentiment\n"
        "- Cultural values, traditions, and tensions\n\n"
        "After using the tool, synthesize the findings into clear, concise insights. "
        "Avoid speculation or outdated references. "
        "Conclude with a summary of cultural strengths and emerging tensions."
    )
)