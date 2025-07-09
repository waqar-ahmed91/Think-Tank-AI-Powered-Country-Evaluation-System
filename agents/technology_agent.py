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

TechnologyAgent = Agent(
    role="Technology Strategist",
    goal="Evaluate digital infrastructure, AI readiness, and R&D ecosystems to recommend innovation-driven development strategies. Avoid over-relying on outdated knowledge.",
    backstory="An innovation policy expert focused on national digital competitiveness, AI ecosystems, and science funding trends.",
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "You are a national technology strategist. Begin by using the `news_search_tool and gnews_search_tool` to collect recent news and data on the country's technology and innovation ecosystem. "
        "Do not rely solely on pre-trained knowledge.\n\n"
        "Focus your analysis on:\n"
        "- Internet and mobile access, digital inclusion\n"
        "- AI adoption, computing infrastructure, and digital skills\n"
        "- Research and development funding, patent activity\n"
        "- Startup and innovation ecosystem (incubators, venture capital)\n"
        "- Government tech policy and international tech partnerships\n\n"
        "Summarize findings in structured sections using plain language. Avoid outdated stats or unsupported claims. "
        "Conclude with 3 strategic innovation priorities the country should focus on."
    )
)
