from crewai import Task
from agents.energy_agent import EnergyAgent

EnergyTask = Task(
    description="Study the energy sector of {country}. Discuss renewables, fossil dependency, and access (from the last 6 months) and avoid over-relying on outdated 2023 data.",
    expected_output="Energy profile with three decarbonization strategies.",
    agent=EnergyAgent
)
