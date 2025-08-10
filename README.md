# Crew AI Project

---

## Setup Crew AI CLI

---

### 1. Download and Install `uv` if not installed

[Installing uv](https://docs.astral.sh/uv/getting-started/installation/)

### 2. Install crew ai on your computer

```bash
uv tool install crewai
```

If you encounter a `PATH` warning

```bash
uv tool update-shell
```

### 3. Verify installation

```bash
uv tool list
```

### 4. To upgrade the crew ai tool

```bash
uv tool install crewai --upgrade
```

---

## Using Crew AI

---

### 1. Generate project scaffolding

Run crewai CLI command:

```bash
crewai create crew <your-project-name>
```

Then you need to choose options as asked. Then a scaffolded project will be created in the specified directory.

### 2. Customize your project

You can customize your project by modifying the generated files and folders according to your requirements. This may include updating configuration files, adding new components, or changing the project structure.

Few important files and folders are:

#### agents.yaml

##### Location: `src\sales_agent\config\agents.yaml`

This file contains the configuration for the agents used in the sales process. You can define the agent's behavior, capabilities, and other settings here.

All agents are defined in this file, for example

```yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.

newsletter_writer:
  role: >
    {topic} Newsletter Writer
  goal: >
    Create engaging newsletters that inform and educate subscribers about {topic}
  backstory: >
    You're a creative writer with a passion for storytelling. You have a knack for
    turning complex topics into engaging narratives that resonate with your audience.

newsletter_editor:
  role: >
    {topic} Newsletter Editor
  goal: >
    Oversee the content and ensure the quality of newsletters related to {topic}
  backstory: >
    You're an experienced editor with a keen eye for detail. You excel at refining
    content to ensure clarity, coherence, and engagement for the audience.
```

#### tasks.yaml

##### Location: `src\sales_agent\config\tasks.yaml`

Defines the tasks that the agents can perform during the sales process. Each task can be associated with specific agents and may include details such as the task description, required skills, and any relevant context.

For example

```yaml
research_task:
  description: >
    Conduct a thorough research about {topic}
    Make sure you find any interesting and relevant information given
    the current year is {current_year}.
  expected_output: >
    A list with 10 bullet points of the most relevant information about {topic}
  agent: researcher

newsletter_task:
  description: >
    Create a newsletter about {topic} that highlights the key developments and insights.
  expected_output: >
    A well-structured newsletter that includes an introduction, key points, and a conclusion.
  agent: newsletter_writer

newsletter_edit_task:
  description: >
    Review and edit the newsletter about {topic} to ensure clarity and engagement.
  expected_output: >
    A polished version of the newsletter with improvements in structure, clarity, and engagement.
  agent: newsletter_editor
```

#### .env

##### Location: `.env`

`.env` file contains environment variables that are used to configure the application. You can define variables such as API keys, database connection strings, and other settings that may vary between different environments (e.g., development, testing, production). In our case our `MODEL` and `OPENAI_API_KEY` are defined here.

#### main.py

##### Location: `src\sales_agent\main.py`

Entry point for the sales agent application. This file is usually used to initializes the application, loads configuration settings, and starts the main event loop. In our case, this will run the entire project for you. It already has some boilerplate code to get you started.

We can define what should happen, when we run, train, replay or test the crew.

#### crew.py

##### Location: `src\sales_agent\crew.py`

Defines the agents and tasks that make up the sales process. This file is responsible for orchestrating the interactions between different agents and tasks, ensuring that the sales process runs smoothly and efficiently.

Here we process the config in `agents.yaml` and `tasks.yaml` and while building the agent, we provide these config to them. And build the crew out of all the agents.

#### tools/

##### Location: `src\sales_agent\tools\`

Here is where you can define your custom tools which can be used by the agents in your crew.
An example custom tool could be a web scraper that gathers information from specific websites or a data analysis tool that processes and visualizes sales data.

#### Knowledge

##### Location: `knowledge\`

Essentially this maintains some external knowledge, this can be your FAQs, documentation or any other relevant information that can assist the agents in their tasks.

### 3. Run the project

To run the project, first you need to run the following at the root of your crew project

```bash
crew install
```

And then you can run your project

```bash
crew run
```

---

## Integrating Open Source LLM running locally

---

I am using `ollama` with `llama3.1:1.8b` since I am working on lower capacity hardware.

- Download and Install Ollama on platform from [ollama](https://ollama.com/)
- Install \

  ```bash
  ollama run llama3.1:8b
  ```

  This will install and run the model locally.

- Update the `.env` file in your project root to use the local model

  ```bash
  MODEL=ollama/llama3.1
  API_BASE=http://localhost:11434
  ```

- Update the `crew.py` file to use the local model

  ```python
  llm = LLM(
      model="ollama/llama3.1:8b",  # Specify the model you want to use
      api_base="http://localhost:11434",  # Ollama API base URL
  )

  @CrewBase
  class DefaultProject:
      """DefaultProject crew"""

      agents: List[BaseAgent]
      tasks: List[Task]

      # Learn more about YAML configuration files here:
      # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
      # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

      # If you would like to add tools to your agents, you can learn more about it here:
      # https://docs.crewai.com/concepts/agents#agent-tools
      @agent
      def researcher(self) -> Agent:
          return Agent(
              config=self.agents_config["researcher"],  # type: ignore[index]
              verbose=True,
              llm=llm,
          )

      @agent
      def reporting_analyst(self) -> Agent:
          return Agent(
              config=self.agents_config["reporting_analyst"],  # type: ignore[index]
              verbose=True,
              llm=llm,
          )
  ```

- Now you can run the crew with the following command:

  You need to make sure that ollama is running with llama3.1:8b

  ```bash
  crewai install
  crewai run
  ```
