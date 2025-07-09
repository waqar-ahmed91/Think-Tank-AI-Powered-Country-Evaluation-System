from crewai import Task
from agents.energy_agent import EnergyAgent

EnergyTask = Task(
    description=(
        "Assess the energy landscape of {country}, including reliance on fossil fuels, development of renewable sources, "
        "energy production and consumption trends, and population access to electricity. "
        "Highlight infrastructure gaps, energy security risks, and barriers to clean energy transition. "
        "Recommend 3 viable decarbonization or energy diversification strategies."
    ),
    expected_output=(
        "A concise energy sector analysis including:\n"
        "- Overview of current energy mix and accessibility\n"
        "- Challenges in sustainability and infrastructure\n"
        "- 3 actionable strategies to reduce carbon emissions and improve energy resilience"
    ),
    agent=EnergyAgent
)
