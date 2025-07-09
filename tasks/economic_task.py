from crewai import Task
from agents.economic_agent import EconomicAgent

EconomicTask = Task(
    description=(
        "Analyze the current and historical economic landscape of {country}, "
        "focusing on GDP growth trends, inflation control, income distribution, fiscal balance, and trade performance. "
        "Assess structural challenges and identify sectors driving or hindering growth. "
        "Recommend strategic economic policies that enhance fiscal stability and long-term development."
    ),
    expected_output=(
        "An in-depth economic report including:\n"
        "- Major economic indicators and performance trends\n"
        "- Key challenges and sectoral opportunities\n"
        "- 3 evidence-based policy recommendations to boost stability and growth"
    ),
    agent=EconomicAgent
)
