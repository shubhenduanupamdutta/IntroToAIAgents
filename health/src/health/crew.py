"""Healthy Diet Plans - Crew, Agents and Tasks."""

# ruff: noqa: ERA001

import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# Define llm

# # Locally running
# llm = LLM(
#     model="ollama/llama3.1:8b",  # Specify the model you want to use
#     api_base="http://localhost:11434",  # Ollama API base URL
# )

# With OpenRouter
llm = LLM(
    api_base="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_KEY"),
    model="openai/gpt-oss-120b",
)

search_tool = SerperDevTool()


@CrewBase
class Health:
    """Healthy Diet Plans Creation Crew."""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def nutritionist(self) -> Agent:
        """Nutritionist Agent."""
        return Agent(
            config=self.agents_config["nutritionist"],  # type: ignore[index]
            verbose=True,
            llm=llm,
            tools=[search_tool],
        )

    @agent
    def medical_specialist(self) -> Agent:
        """Medical Specialist Agent."""
        return Agent(
            config=self.agents_config["medical_specialist"],  # type: ignore[index]
            verbose=True,
            llm=llm,
            tools=[search_tool],
        )

    @agent
    def diet_planner(self) -> Agent:
        """Therapeutic Diet Planner Agent."""
        return Agent(
            config=self.agents_config["diet_planner"],  # type: ignore[index]
            verbose=True,
            llm=llm,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def demographic_research(self) -> Task:
        """Research nutritional needs based on demographics."""
        return Task(
            config=self.tasks_config["demographic_research"],  # type: ignore[index]
        )

    @task
    def medical_analysis(self) -> Task:
        """Analyze medical conditions and adjust nutritional recommendations."""
        return Task(
            config=self.tasks_config["medical_analysis"],  # type: ignore[index]
            context=[self.demographic_research()],
        )

    @task
    def diet_plan(self) -> Task:
        """Create the comprehensive diet plan."""
        return Task(
            config=self.tasks_config["diet_plan"],  # type: ignore[index]
            context=[self.demographic_research(), self.medical_analysis()],
        )

    @crew
    def crew(self) -> Crew:
        """Create the Nutritional Plan crew with CrewAI."""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead  # noqa: ERA001
            # https://docs.crewai.com/how-to/Hierarchical/
        )
