from crewai import Task
from agents.coordinator_agent import CoordinatorAgent

CoordinatorTask = Task(
    description=(
        "You are the final synthesizer. Review the findings from all domain-specific agents analyzing {country}.\n\n"
        "Context:\n{context}\n\n"
        "Your goal is to integrate these findings into a cohesive national development summary. "
        "Identify recurring themes, strategic challenges, and synergistic opportunities across domains. "
        "Avoid duplication, resolve conflicting insights, and ensure that all recommendations align toward a coherent policy vision.\n\n"
        "Summarize the results in markdown under the following 3 sections:\n"
        "- **Key Insights** (max 10 bullet points)\n"
        "- **Policy Recommendations** (max 10 bullet points)\n"
        "- **Risks to Watch** (max 10 bullet points)\n\n"
    ),
    expected_output=(
        "A well-structured markdown report including:\n"
        "### 📌 Key Insights\n"
        "Highlight recurring trends, critical issues, or breakthrough observations.\n\n"
        "### 🛠️ Recommendations\n"
        "Actionable, non-overlapping and synergistic strategies.\n\n"
        "### ⚠️ Risks to Watch\n"
        "Potential threats, implementation bottlenecks, or cross-sector vulnerabilities.\n\n"
        # "**End your report with:** `— Report compiled successfully.`"
    ),
    agent=CoordinatorAgent,
    context=[  # You can dynamically add task outputs from other agents
        # e.g. economic_analysis_task.output, healthcare_task.output, etc.
    ]
)

