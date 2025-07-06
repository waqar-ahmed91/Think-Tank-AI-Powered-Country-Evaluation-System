# Think Tank — AI-Powered Country Evaluation System

**Think Tank** is an AI-driven multi-agent system designed to perform comprehensive country evaluations across a wide range of indicators including political stability, economic health, institutional transparency, and social metrics. The system leverages autonomous agents, each representing specialized domains, to simulate a think tank's collaborative assessment process and generate actionable insights.

---

## 🚀 Project Overview

In an era of data-driven policymaking, **Think Tank** introduces a novel approach to evaluating national performance by:

- Integrating multiple AI agents representing economic, political, legal, environmental, and social expertise  
- Leveraging real-time and historical data sources, including news APIs and global indices  
- Delivering structured, comparative, and transparent country reports

---

## 🧠 System Architecture

**Think Tank** is built on the [CrewAI](https://crewai.com/) framework, allowing dynamic orchestration of autonomous agents. The architecture includes:

- **Country Analyst Agent** — Oversees data aggregation and triggers other agents  
- **Political Stability Agent** — Evaluates governance, electoral integrity, and institutional trust  
- **Economic Agent** — Assesses GDP trends, inflation, trade, and employment metrics  
- **Social Agent** — Considers healthcare, education, demographics, and public sentiment  
- **Legal & Corruption Agent** — Analyzes transparency, corruption indices, and rule of law  
- **Environmental Agent** *(optional)* — Reviews climate policy, resource use, and ecological footprints

Each agent queries relevant APIs, performs LLM-assisted reasoning, and contributes to a structured country evaluation.

---

## 📊 Key Features

- 🧩 **Multi-Agent Collaboration:** Each agent contributes independently to a shared analysis task  
- 📡 **Real-Time Data:** Connects to APIs like GNews, World Bank, and Transparency.org  
- 🧠 **LLM-Powered Reasoning:** Natural language reasoning to evaluate qualitative indicators  
- 📘 **Modular Reporting:** Outputs comparative country insights in report or dashboard form  
- 🔒 **Custom Filters:** Filter reports by timeframe, region, or evaluation category

---

## 🔧 Technologies Used

| Component       | Technology                                     |
|----------------|-------------------------------------------------|
| Core Framework | [CrewAI](https://github.com/joaomdmoura/crewai) |
| Language Model | OpenAI GPT-4o-mini / GPT-4                      |
| Data Sources   | GNews API, Google Search                        |
| Backend        | Python 3.11+                                    |
| Orchestration  | LangChain (optional), Asyncio                   |
| Output Format  | Markdown / JSON / PDF                           |

---
### 📌 Future Work
Integration with interactive dashboards (Streamlit or Dash)

Real-time sentiment analysis from social media

Enhanced geographical and geopolitical visualizations

Plugin support for new agents (e.g., Defense etc..)

### 🤝 Contributing
Contributions are welcome! If you'd like to improve or extend the system:

Fork this repository

Create a new feature branch (git checkout -b feature-name)

Commit your changes and push

Submit a pull request

Please ensure your code adheres to PEP8 and includes tests where applicable.

### 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

### 🙋 Contact
Waqar Ahmed
Github: https://github.com/waqar-ahmed91