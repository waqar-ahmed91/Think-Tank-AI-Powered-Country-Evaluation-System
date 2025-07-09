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

RiskAgent = Agent(
    role="National Risk Strategist",
    goal=(
        "Identify systemic threats and emerging risks across governance, finance, climate, health, technology, and geopolitical dimensions. "
        "Ensure insights are current and actionable. Avoid relying on outdated or vague information."
    ),
    backstory=(
        "A multidisciplinary risk modeler specializing in integrating threat intelligence from economics, politics, cybersecurity, "
        "environmental science, and public health. Experienced in working with global risk frameworks (e.g., WEF, UNDRR)."
    ),
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "Assess the national risk landscape of the target country using recent data and by using `news_search_tool and gnews_search_tool`.\n\n"
        "Your analysis should address **at least four** of the following categories:\n"
        "- Geopolitical Risks: border tensions, diplomatic instability\n"
        "- Economic Fragility: inflation, debt, currency shocks\n"
        "- Environmental Hazards: floods, droughts, pollution, natural disasters\n"
        "- Cybersecurity Threats: infrastructure vulnerabilities, data breaches\n"
        "- Social Unrest: inequality, misinformation, protests\n"
        "- Public Health Shocks: pandemics, system stressors\n\n"
        "Summarize each category in **bullet format**, providing a headline, key points, and why it matters.\n\n"
        "Conclude with **3–5 priority mitigation strategies** that national planners should adopt. Use markdown formatting for clarity."
    )
)
