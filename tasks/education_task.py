from crewai import Task
from agents.education_agent import EducationAgent

EducationTask = Task(
    description=(
        "Evaluate the educational performance of {country} using historical and recent data. "
        "Analyze literacy trends, enrollment rates at primary, secondary, and tertiary levels, "
        "government spending on education, and alignment of education with labor market needs. "
        "Identify systemic gaps, challenges in access or quality, and regional disparities. "
        "Recommend 3 strategic reforms or investments to improve educational outcomes and employability."
    ),
    expected_output=(
        "A concise education sector analysis including:\n"
        "- Key indicators and challenges\n"
        "- Gaps in access, quality, or relevance\n"
        "- 3 targeted improvement strategies or reforms"
    ),
    agent=EducationAgent
)
