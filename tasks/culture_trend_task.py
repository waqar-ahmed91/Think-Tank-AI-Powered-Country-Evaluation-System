from crewai import Task
from agents.culture_trend_agent import CultureAgent

CultureTask = Task(
    description=(
        "Analyze the cultural landscape of {country}, focusing on social unity, national identity, "
        "media narratives, historical context, and cultural values. Identify factors that support or threaten cohesion."
    ),
    expected_output=(
        "A structured output that includes:\n"
        "- **Cultural Health Index** (brief qualitative or quantitative score)\n"
        "- **Three actionable recommendations** to strengthen social cohesion and cultural integration."
    ),
    agent=CultureAgent
)