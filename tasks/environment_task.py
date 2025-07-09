from crewai import Task
from agents.environment_agent import EnvironmentAgent

EnvironmentTask = Task(
    description=(
        "Evaluate key environmental challenges in {country}, including air and water quality, deforestation, "
        "carbon emissions, biodiversity loss, and vulnerability to climate change. "
        "Identify high-risk ecological zones and assess policy effectiveness in environmental protection. "
        "Propose 3 practical and impactful green policy actions to improve environmental sustainability."
    ),
    expected_output=(
        "An environmental risk assessment including:\n"
        "- Summary of major environmental stressors and trends\n"
        "- Vulnerable ecosystems or geographic regions\n"
        "- 3 evidence-based policy actions for sustainability and climate adaptation"
    ),
    agent=EnvironmentAgent
)
