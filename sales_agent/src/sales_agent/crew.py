"""Building the SalesAgent crew from the configurations."""

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class SalesAgent:
    """SalesAgent crew."""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        """Researcher agent for gathering information."""
        return Agent(
            config=self.agents_config["researcher"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def newsletter_writer(self) -> Agent:
        """Newsletter writer agent for creating engaging content.

        Returns:
            Agent: The newsletter writer agent.

        """
        return Agent(
            config=self.agents_config["newsletter_writer"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def newsletter_editor(self) -> Agent:
        """Newsletter editor agent for overseeing content quality.

        Returns:
            Agent: The newsletter editor agent.

        """
        return Agent(
            config=self.agents_config["newsletter_editor"],  # type: ignore[index]
            verbose=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        """Research task for gathering information.

        Returns:
            Task: The research task.

        """
        return Task(
            config=self.tasks_config["research_task"],  # type: ignore[index]
        )

    @task
    def newsletter_task(self) -> Task:
        """Newsletter task for creating engaging content.

        Returns:
            Task: The newsletter writing task.

        """
        return Task(
            config=self.tasks_config["newsletter_task"],  # type: ignore[index]
        )

    @task
    def newsletter_edit_task(self) -> Task:
        """Newsletter task for editing content.

        Returns:
            Task: The newsletter editing task.

        """
        return Task(
            config=self.tasks_config["newsletter_edit_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Create the SalesAgent crew."""
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
