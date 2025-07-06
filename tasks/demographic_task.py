from crewai import Task
from agents.demographic_agent import DemographicsAgent

DemographicsTask = Task(
    description="Analyze demographic trends in {country}, focusing on age structure, migration, and labor force (from the last 6 months) and avoid over-relying on outdated 2023 data.",
    expected_output="Population dynamics report with policy insights.",
    agent=DemographicsAgent
)