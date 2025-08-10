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

