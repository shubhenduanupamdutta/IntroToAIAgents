#!/usr/bin/env python

"""Main entry point for sales agent application."""
# ruff: noqa: BLE001, B904, TRY002

import sys
import warnings
from datetime import datetime

from sales_agent.crew import SalesAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run() -> None:
    """Run the crew."""
    inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}  # noqa: DTZ005

    try:
        SalesAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        msg = f"An error occurred while running the crew: {e}"
        raise Exception(msg)


def train() -> None:
    """Train the crew for a given number of iterations."""
    inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}  # noqa: DTZ005
    try:
        SalesAgent().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )

    except Exception as e:
        msg = f"An error occurred while training the crew: {e}"
        raise Exception(msg)


def replay() -> None:
    """Replay the crew execution from a specific task."""
    try:
        SalesAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        msg = f"An error occurred while replaying the crew: {e}"
        raise Exception(msg)


def test() -> None:
    """Test the crew execution and returns the results."""
    inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}  # noqa: DTZ005

    try:
        SalesAgent().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs,
        )

    except Exception as e:
        msg = f"An error occurred while testing the crew: {e}"
        raise Exception(msg)
