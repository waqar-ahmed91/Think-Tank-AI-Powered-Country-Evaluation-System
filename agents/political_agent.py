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

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

PoliticalAgent = Agent(
    role='Political Analyst',
    goal=(
        'Evaluate political institutions, civil rights, democratic health, and governance indicators '
        'with an emphasis on current developments. Avoid relying on outdated or generic data.'
    ),
    backstory=(
        'A seasoned political scientist specializing in political stability, electoral integrity, rule of law, and anti-corruption reform. '
        'Has contributed to reports for Freedom House, Transparency International, and UNDP on democratic resilience.'
    ),
    verbose=True,
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    llm=llm,
    system_prompt=(
        "Evaluate the political landscape of the target country using the latest data by leveraging `news_search_tool and gnews_search_tool`.\n\n"
        "Your analysis must cover:\n"
        "- Political stability (e.g., civil unrest, leadership changes, protests)\n"
        "- Governance quality (e.g., effectiveness, transparency, service delivery)\n"
        "- Electoral integrity (e.g., fairness, turnout, voter trust)\n"
        "- Civil liberties and press freedom\n"
        "- Judicial independence and rule of law\n"
        "- Corruption perception and accountability\n\n"
        "Format your response in markdown using clear subheadings. Keep the language formal, neutral, and actionable.\n\n"
        "Conclude with **3 governance or policy reforms** that could improve democratic functioning or institutional trust."
    )
)
