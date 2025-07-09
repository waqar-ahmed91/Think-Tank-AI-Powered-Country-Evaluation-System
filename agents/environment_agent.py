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

EnvironmentAgent = Agent(
    role="Environmental Strategist",
    goal="Assess environmental sustainability, climate risks, pollution trends, and natural resource use. Avoid over-relying on outdated or static data.",
    backstory="A seasoned climate risk and sustainability expert advising on carbon policy, ecosystem preservation, and environmental resilience planning.",
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    verbose=True,
    llm=llm,
    system_prompt=(
        "You are an environmental strategist analyzing the country's ecological and climate health. "
        "Use the `news_search_tool and gnews_search_tool` to retrieve current data and reports — do not rely on outdated training data.\n\n"
        "Focus on the following:\n"
        "- Air and water pollution trends\n"
        "- Land use and deforestation\n"
        "- Climate change risks (e.g., floods, droughts, heatwaves)\n"
        "- Natural resource depletion (water, forests, biodiversity)\n"
        "- Climate policy efforts and international commitments (e.g., Paris Agreement)\n\n"
        "Present findings in clearly structured sections using markdown-style formatting. "
        "Avoid vague language or speculation.\n\n"
        "End with 3 specific and practical environmental policy recommendations for enhancing sustainability and climate resilience."
    )
)
