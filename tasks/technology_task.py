from crewai import Task
from agents.technology_agent import TechnologyAgent

TechnologyTask = Task(
    description=(
        "Evaluate the technological landscape of {country}. "
        "Include assessment of:\n"
        "- **Digital Infrastructure**: broadband access, 5G rollout, and connectivity gaps\n"
        "- **Emerging Technologies**: AI, cybersecurity, robotics, and frontier tech adoption\n"
        "- **Innovation Ecosystem**: research output, startup support, tech investment, and regulation\n"
        "- **Education Alignment**: tech skills in education, STEM pipelines, and workforce readiness\n\n"
        "Highlight strengths and bottlenecks in the country's path toward digital transformation. "
        "Support analysis with recent available data and global benchmarks."
    ),
    expected_output=(
        "A structured tech readiness report including:\n"
        "- A qualitative or indexed assessment of national tech capacity\n"
        "- Three innovation policy recommendations for accelerating digital growth"
    ),
    agent=TechnologyAgent
)
