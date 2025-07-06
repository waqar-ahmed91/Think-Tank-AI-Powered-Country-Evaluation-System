from crewai import Task
from agents.economic_agent import EconomicAgent

EconomicTask = Task(
    description=(
        "Analyze the current and historical economic data of {country}, "
        "including GDP, inflation, income inequality, and trade performance. "
        "Recommend economic policies to improve fiscal stability and growth."
        "(from the last 6 months) and avoid over-relying on outdated 2023 data."
    ),
    expected_output="Detailed economic assessment with 3 key policy recommendations.",
    agent=EconomicAgent
)
