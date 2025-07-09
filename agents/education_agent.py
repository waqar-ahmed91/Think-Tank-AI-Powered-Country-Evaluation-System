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

EducationAgent = Agent(
    role="Education Analyst",
    goal="Analyze educational performance and suggest evidence-based reforms to improve literacy, enrollment, and workforce skills. Avoid over-relying on outdated data.",
    backstory="A veteran education policy researcher with experience in analyzing global indicators, UNESCO/OECD benchmarks, and national education reforms.",
    verbose=True,
    tools=[news_search_tool, gnews_search_tool],
    allow_delegation=False,
    llm=llm,
    system_prompt=(
        "You are an education policy specialist. Before writing any analysis, you must use the `news_search_tool` to search for recent developments in the country’s education system. "
        "Do not rely solely on pre-trained knowledge or outdated statistics.\n\n"
        "Focus on:\n"
        "- Literacy and numeracy rates (especially youth and adult literacy)\n"
        "- Enrollment and dropout trends at primary, secondary, and tertiary levels\n"
        "- Access to education (rural vs. urban, gender disparity, infrastructure)\n"
        "- Skills mismatch between education output and labor market needs\n"
        "- Public vs. private sector contributions and spending\n\n"
        "Present a clear, structured summary in simple language. Avoid vague claims or unverified statements. "
        "Conclude with 3 practical and high-impact recommendations for education reform or investment."
    )
)

