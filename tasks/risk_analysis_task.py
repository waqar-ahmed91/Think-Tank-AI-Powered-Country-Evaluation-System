from crewai import Task
from agents.risk_analysis_agent import RiskAgent

RiskTask = Task(
    name="National Risk Analysis",
    description=(
        "Develop a comprehensive national risk profile for {country}. "
        "Analyze vulnerabilities across four key domains:\n"
        "- **Cybersecurity**: digital infrastructure threats, data breaches, and resilience\n"
        "- **Political Stability**: governance risks, civil unrest, and institutional trust\n"
        "- **Environmental Hazards**: climate shocks, natural disasters, and resource degradation\n"
        "- **Economic Fragility**: inflation, sovereign debt, unemployment, inequality, and trade imbalance\n\n"
        "Draw insights from global indices, risk reports, and recent news developments. "
        "Identify 3 to 5 critical risk mitigation strategies that national policymakers should prioritize."
    ),
    expected_output=(
        "A structured risk intelligence report organized into:\n"
        "- Four categorized risk summaries (Cyber, Political, Environmental, Economic)\n"
        "- A prioritized list of 3–5 mitigation strategies tailored for national resilience"
    ),
    agent=RiskAgent
)
