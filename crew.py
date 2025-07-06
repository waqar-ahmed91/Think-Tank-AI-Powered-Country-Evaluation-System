from crewai import Crew
from tasks.economic_task import EconomicTask
from tasks.education_task import EducationTask
from tasks.political_task import PoliticalTask
from tasks.coordinator_task import CoordinatorTask
from tasks.culture_trend_task import CultureTask
from tasks.technology_task import TechnologyTask
from tasks.health_task import HealthTask
from tasks.environment_task import EnvironmentTask
from tasks.energy_task import EnergyTask
from tasks.foreign_policy_task import ForeignPolicyTask
from tasks.demographic_task import DemographicsTask
from tasks.risk_analysis_task import RiskTask

from agents.coordinator_agent import CoordinatorAgent
from markdown import markdown
from weasyprint import HTML

def run_thinktank_pipeline(country: str):
    print(f"\n🧠 Starting Think Tank analysis for {country}...\n")

    # Step 1: Run domain-specific agents
    domain_crew = Crew(
        agents=[
            EconomicTask.agent,
            EducationTask.agent,
            PoliticalTask.agent,
            CultureTask.agent,
            TechnologyTask.agent,
            HealthTask.agent,
            EnvironmentTask.agent,
            EnergyTask.agent,
            ForeignPolicyTask.agent,
            DemographicsTask.agent,
            RiskTask.agent
        ],
        tasks=[
            EconomicTask,
            EducationTask,
            PoliticalTask,
            CultureTask,
            TechnologyTask,
            HealthTask,
            EnvironmentTask,
            EnergyTask,
            ForeignPolicyTask,
            DemographicsTask,
            RiskTask
        ],
        verbose=True
    )

    domain_crew.kickoff(inputs={"country": country})
    domain_outputs = {
        task.name or task.__class__.__name__: task.output
        for task in domain_crew.tasks if task.output
    }

    # Step 2: Create merged context
    merged_context = "\n\n".join(
        f"## {task_name} for {country}\n\n{output}"
        for task_name, output in domain_outputs.items()
    )

    # Step 3: Run the coordinator agent
    coordinator_crew = Crew(
        agents=[CoordinatorAgent],
        tasks=[CoordinatorTask],
        verbose=True
    )

    coordinator_crew.kickoff(inputs={
        "country": country,
        "context": merged_context
    })

    # ✅ Access clean final summary
    summary = CoordinatorTask.output

    # Step 4: Assemble markdown
    final_markdown = f"""# 🧠 Think Tank Strategic Report — {country}

{merged_context}

---

## 📌 Final Strategic Summary
{summary}
"""

    filename = f"{country.lower()}_thinktank_report.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_markdown)

    # Convert to HTML then PDF
    styled_html = """
    <style>
    body { font-family: Arial, sans-serif; padding: 40px; line-height: 1.6; }
    h1, h2, h3 { color: #2c3e50; }
    pre, code { background-color: #f4f4f4; padding: 8px; display: block; }
    </style>
    """ + markdown(final_markdown, extensions=["fenced_code", "tables"])

    filename_pdf = filename.replace(".md", ".pdf")
    HTML(string=styled_html).write_pdf(filename_pdf)

    print(f"\n✅ Report saved as:\n- Markdown: `{filename}`\n- PDF: `{filename_pdf}`")