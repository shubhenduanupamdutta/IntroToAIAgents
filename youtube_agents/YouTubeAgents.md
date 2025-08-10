# YoutubeAgents Crew

Welcome to the YoutubeAgents Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/youtube_agents/config/agents.yaml` to define your agents
- Modify `src/youtube_agents/config/tasks.yaml` to define your tasks
- Modify `src/youtube_agents/crew.py` to add your own logic, tools and specific args
- Modify `src/youtube_agents/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the youtube_agents Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The youtube_agents Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the YoutubeAgents Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

---

## Youtube Agents

---

### For search feature I am using SerperDevTool

For this you need to get API key from [Serper](https://serper.dev)
and set it in your `.env` file as `SERPER_API_KEY`

Then you can create a search tool and pass it to your agent:

```python
search_tool = SerperDevTool()

# ... rest of code

    @agent
    def researcher(self) -> Agent:
        """Return the researcher agent."""
        return Agent(
            config=self.agents_config["researcher"],  # type: ignore[index]
            verbose=True,
            llm=llm,
            tools=[search_tool],  # Add the search tool to the agent
        )
```
