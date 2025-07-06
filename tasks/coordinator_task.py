from crewai import Task
from agents.coordinator_agent import CoordinatorAgent

CoordinatorTask = Task(
    description=(
        "Review the analyses provided by the economic, education, and political agents for {country}. "
        "Identify recurring themes, strategic challenges, and synergistic opportunities. "
        "Summarize their findings in a markdown-ready format under 3 sections: Key Insights, Policy Recommendations, and Risks to Watch. "
        "Ensure the recommendations are coherent and non-conflicting across sectors."
    ),
    expected_output=(
        "A markdown summary with:\n"
        "- **Key Insights** (max 5 bullet points)\n"
        "- **Policy Recommendations** (max 5 bullet points)\n"
        "- **Risks to Watch** (max 3 bullet points)"
    ),
    agent=CoordinatorAgent,
    context=[
        # Add dependent tasks' outputs here dynamically in your code
    ]
)
