from crewai import Task
from agents.foreign_policy_agent import ForeignPolicyAgent

ForeignPolicyTask = Task(
    description=(
        "Evaluate {country}'s foreign relations, regional influence, and participation in international organizations or treaties. "
        "Analyze defense posture, including military spending and border security issues or conflicts. "
        "Assess soft power dynamics such as diplomatic initiatives, cultural influence, and media presence abroad. "
        "Identify global shifts that could impact national interests."
    ),
    expected_output=(
        "A comprehensive foreign affairs summary including:\n"
        "- Key bilateral and multilateral relationships\n"
        "- Military and strategic defense posture with spending insights\n"
        "- Ongoing or recent border conflicts\n"
        "- Soft power footprint (diplomacy, media, cultural influence)\n"
        "- 3 actionable geopolitical or diplomatic strategy suggestions"
    ),
    agent=ForeignPolicyAgent
)

