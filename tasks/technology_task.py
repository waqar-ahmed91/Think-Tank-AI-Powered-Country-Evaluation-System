from crewai import Task
from agents.technology_agent import TechnologyAgent

TechnologyTask = Task(
    description=
    "Analyze the tech landscape in {country}. Include digital infrastructure, AI, and education alignment (from the last 6 months) and avoid over-relying on outdated 2023 data.",
    expected_output="Tech readiness index with three innovation policy proposals.",
    agent=TechnologyAgent
)
