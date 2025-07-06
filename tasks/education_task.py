from crewai import Task
from agents.education_agent import EducationAgent

EducationTask = Task(
    description=(
        "Analyze the educational performance of {country} using historical and current data. "
        "Evaluate literacy rates, enrollment levels in primary, secondary, and tertiary education, "
        "education spending, and skills gaps related to employment. "
        "Identify 3 actionable reforms or investments to enhance the education system."
        "(from the last 6 months) and avoid over-relying on outdated 2023 data."
    ),
    expected_output="An education system summary with 3 key improvement strategies.",
    agent=EducationAgent
)
