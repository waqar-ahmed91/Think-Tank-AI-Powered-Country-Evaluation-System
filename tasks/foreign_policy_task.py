from crewai import Task
from agents.foreign_policy_agent import ForeignPolicyAgent

ForeignPolicyTask = Task(
    description="Evaluate {country}'s foreign relations, defense posture, and major international agreements (from the last 6 months) and avoid over-relying on outdated 2023 data.",
    expected_output="Foreign affairs summary with three geopolitical strategy suggestions.",
    agent=ForeignPolicyAgent
)