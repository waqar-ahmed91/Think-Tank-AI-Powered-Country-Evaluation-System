from crewai import Task
from agents.environment_agent import EnvironmentAgent

EnvironmentTask = Task(
    description="Assess environmental challenges in {country}. Cover air quality, emissions, land use, and climate risk (from the last 6 months) and avoid over-relying on outdated 2023 data.",
    expected_output="Sustainability status and three green policy actions.",
    agent=EnvironmentAgent
)