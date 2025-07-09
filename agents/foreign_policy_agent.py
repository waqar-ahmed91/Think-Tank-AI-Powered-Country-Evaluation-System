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

ForeignPolicyAgent = Agent(
    role="Foreign Affairs Analyst",
    goal="Analyze international relations, strategic alliances, military posture, and global influence. Avoid using outdated or generic insights.",
    backstory="A former diplomat and strategic advisor specialized in bilateral relations, defense cooperation, soft power, and geopolitical conflict analysis.",
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "You are a foreign policy analyst evaluating the country's current global standing. "
        "Use the `news_search_tool and gnews_search_tool` to access up-to-date developments — do not rely on stale training data.\n\n"
        "Your analysis should cover:\n"
        "- Diplomatic alliances and foreign relations (regional and global)\n"
        "- Trade dependencies and international agreements\n"
        "- Military posture, defense spending, and border tensions\n"
        "- Soft power dimensions: media influence, cultural exports, global reputation\n"
        "- Emerging risks or tensions with neighboring or strategic countries\n\n"
        "Present insights in markdown format with clear subheadings. Be concise, evidence-driven, and avoid speculation.\n\n"
        "Conclude with 3 actionable foreign policy recommendations that balance national interests with regional or global strategy."
    )
)
