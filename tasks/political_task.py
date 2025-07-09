from crewai import Task
from agents.political_agent import PoliticalAgent

PoliticalTask = Task(
    description=(
        "Evaluate the political landscape of {country}, focusing on political stability, institutional transparency, "
        "corruption perception, rule of law, electoral integrity, and public trust in government. "
        "Include analysis of civil society engagement, freedom of press, and judicial independence. "
        "Incorporate historical trends, recent developments, and regional context. "
        "Recommend 3 governance or policy reforms that could strengthen democratic resilience, reduce corruption, "
        "or rebuild institutional trust."
    ),
    expected_output=(
        "A concise report on political system health, including:\n"
        "- Assessment of political risks, freedoms, and institutional integrity\n"
        "- Notable events or shifts in governance, media, or legal frameworks\n"
        "- Three actionable reform suggestions to improve political accountability and democratic function"
    ),
    agent=PoliticalAgent
)

