from crewai import Agent, LLM
from langchain_openai import ChatOpenAI
from tools.news_search_tool import news_search_tool
from tools.internet_search import internet_search_tool
from langchain_ollama import OllamaLLM as Ollama


# llm = LLM(
#     provider="ollama",
#     model="ollama/qwen2.5:7b",
#     base_url="http://localhost:11434",
#     temperature=0.6,
#     system="You are a concise expert. Output final answers only.",
#     additional_kwargs={
#         "tool_choice": "auto",
#         "auto_continue": True,
#         }
# )
# llm = Ollama(
#     base_url="http://localhost:11434",
#     model="llama3.2:latest",
#     api_key="1234",
#     temperature=0.6
# )
# llm = Ollama(
#     model="llama3.2",
#     base_url="http://localhost:11434",
#     temperature=0.6
# )

# print(llm.call("What's the capital of France?"))

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)


CoordinatorAgent = Agent(
    role="Coordinator Analyst",
    goal=(
        "Synthesize and align insights from all domain-specific agents into a unified, high-level "
        "strategic report to guide national development planning and policy coordination."
    ),
    backstory=(
        "A seasoned national strategy consultant known for translating complex, multi-sector data "
        "into coherent, cross-functional policy blueprints. Expert in reconciling conflicting analyses "
        "and ensuring recommendations align with broader development goals."
    ),
    system_prompt=(
        "You will be given summaries from domain-specific expert agents.\n\n"
        "Your task is to:\n"
        "- Extract only the most impactful and relevant insights from each.\n"
        "- Eliminate duplicate or conflicting recommendations.\n"
        "- Integrate them into a structured, markdown-ready final report.\n\n"
        "**Your output must be structured into the following sections:**\n"
        "1. **Key Insights** (max 10 concise bullet points)\n"
        "2. **Recommendations** (max 10 high-level actions)\n"
        "3. **Risks to Watch** (max 10 potential issues or blind spots)\n\n"
        "Be clear, professional, and to the point. Do not explain your reasoning or mention that you are processing findings.\n"
        "**End your output with:** '— Final report compiled successfully.'"
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm,
    # tools=[news_search_tool]  # Optional, if needed later
)


# from crewai import Task, Crew

# agent = Agent(
#     role='News Analyst',
#     goal='Fetch real-time news and provide structured summaries using tools',
#     backstory='You are skilled at finding reliable news using online tools and summarizing the key points.',
#     verbose=True,
#     debug=True,
#     allow_delegation=False,
#     llm=llm,
#     # tools=[internet_search_tool],
#     system_prompt=system_msg
# )


# test_task = Task(
#     description=(
#         "Use tools to find the latest news about technology. "
#         "Return only the tool-based output — do not guess."
#     ),
#     expected_output="list the main points from the news.",
#     agent=agent
# )

# crew = Crew(
#     agents=[agent],
#     tasks=[test_task],
#     verbose=True
# )

# crew.kickoff()
