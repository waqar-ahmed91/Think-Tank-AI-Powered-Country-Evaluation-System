from crewai import Task
from agents.risk_analysis_agent import RiskAgent

RiskTask = Task(
    name="National Risk Analysis",  # Optional, improves logging
    description=(
        "Construct a comprehensive risk profile for {country}. "
        "Include assessment of:\n"
        "- Cybersecurity threats and digital vulnerabilities\n"
        "- Political instability (governance, protests, trust)\n"
        "- Environmental and climate-related shocks (e.g., floods, droughts)\n"
        "- Economic fragility (inflation, debt, inequality, trade balance)\n\n"
        "Use data from global organizations and recent news to support insights. "
        "Suggest 3–5 strategic mitigation priorities."
        "(from the last 6 months) and avoid over-relying on outdated 2023 data."
    ),
    expected_output="A structured national risk report with four risk categories and corresponding mitigation priorities.",
    agent=RiskAgent
)
