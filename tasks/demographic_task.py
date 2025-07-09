from crewai import Task
from agents.demographic_agent import DemographicsAgent

DemographicsTask = Task(
    description=(
        "Analyze demographic trends in {country}, focusing on age structure, migration flows, fertility rates, and labor force composition. "
        "Ensure a multi-year perspective, identifying patterns and shifts over time rather than focusing on a single year like 2023."
    ),
    expected_output=(
        "A concise population dynamics report including:\n"
        "- Key trends in population growth, aging, youth bulge, and migration\n"
        "- Implications for labor force development\n"
        "- 2–3 policy insights to address demographic challenges and opportunities"
    ),
    agent=DemographicsAgent
)