from crewai import Task
from agents.culture_trend_agent import CultureAgent

CultureTask = Task(
    description="Investigate cultural dynamics and social unity in {country}. Reflect on media, history, and identity (from the last 6 months) and avoid over-relying on outdated 2023 data.",
    expected_output="Cultural health index and two cohesion-building recommendations.",
    agent=CultureAgent
)