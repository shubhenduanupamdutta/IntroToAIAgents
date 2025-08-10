#!/usr/bin/env python
"""Codes to run the Nutritional Plan crew."""

# ruff: noqa: BLE001, ERA001

import warnings

import streamlit as st
from crewai import CrewOutput

from health.crew import Health
from health.data_schemas import UserInfo

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run(user_info: UserInfo) -> CrewOutput | None:
    """Run the Nutritionist Advisor Crew."""
    inputs = user_info.model_dump()

    try:
        with st.spinner(
            "Our nutrition team is creating your personalized plan. This my take a few minutes...",
        ):
            result = Health().crew().kickoff(inputs=inputs)
    except Exception as e:
        msg = f"An error occurred while running the crew: {e}"
        st.error(msg)
        return None
    else:
        return result


# def train() -> None:
#     """Train the crew for a given number of iterations."""
#     inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}
#     try:
#         Health().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")


# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         Health().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")


# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}

#     try:
#         Health().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
