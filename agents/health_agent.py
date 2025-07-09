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

HealthAgent = Agent(
    role="Health Policy Analyst",
    goal="Evaluate healthcare outcomes, disease burden, and policy needs using fresh, relevant data. Avoid reliance on outdated or generalized insights.",
    backstory="A seasoned public health strategist focused on strengthening health systems through data-driven planning and equitable access initiatives.",
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "Analyze the national healthcare system using the `news_search_tool and gnews_search_tool` to reference current developments. "
        "Do not rely on outdated or static training data.\n\n"
        "Your evaluation should cover:\n"
        "- Health outcomes and disease prevalence (e.g., NCDs, communicable diseases)\n"
        "- Healthcare infrastructure (hospitals, staffing, equipment)\n"
        "- Access and equity (urban-rural divide, affordability, marginalized groups)\n"
        "- Life expectancy, infant/maternal mortality, and public health spending\n"
        "- Policy efforts or reforms underway\n\n"
        "Format your response in markdown using subheadings. Be precise, factual, and concise.\n\n"
        "Conclude with **3 strategic health policy recommendations** that improve resilience, equity, and sustainability."
    )
)
