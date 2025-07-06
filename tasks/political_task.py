from crewai import Task
from agents.political_agent import PoliticalAgent

PoliticalTask = Task(
    description=(
        "Evaluate the current political landscape of {country}, including political stability, "
        "transparency, corruption perception, electoral integrity, and trust in public institutions. "
        "Review historical context and current events. Suggest 3 governance or policy reforms that could "
        "improve democratic functioning, reduce corruption, or increase political trust."
        "(from the last 6 months) and avoid over-relying on outdated 2023 data."
    ),
    expected_output="A detailed report on political health with 3 reform recommendations.",
    agent=PoliticalAgent
)
