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

```
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
