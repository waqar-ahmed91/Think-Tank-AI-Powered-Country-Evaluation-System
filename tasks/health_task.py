from crewai import Task
from agents.health_agent import HealthAgent

HealthTask = Task(
    description="Review the healthcare system of {country}. Include disease prevalence, healthcare spending, and reform suggestions (from the last 6 months) and avoid over-relying on outdated 2023 data.",
    expected_output="A public health summary and three key health policy recommendations.",
    agent=HealthAgent
)
