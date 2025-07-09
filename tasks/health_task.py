from crewai import Task
from agents.health_agent import HealthAgent

HealthTask = Task(
    description=(
        "Review the healthcare system of {country}, focusing on disease prevalence, healthcare infrastructure, spending patterns, "
        "and access disparities. Highlight challenges in service delivery, public health outcomes, and recent reforms. "
        "Identify opportunities for systemic improvements or targeted interventions."
    ),
    expected_output=(
        "A concise public health status report including:\n"
        "- Overview of disease burden and major health risks\n"
        "- Key metrics on access, spending, and infrastructure\n"
        "- Three strategic health policy recommendations for improvement"
    ),
    agent=HealthAgent
)
