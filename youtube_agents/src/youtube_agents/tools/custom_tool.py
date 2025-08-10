"""Custom tool definitions for YouTube agents.

This module provides a custom tool and its input schema for use with CrewAI agents.
"""

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""

    argument: str = Field(..., description="Description of the argument.")


class MyCustomTool(BaseTool):
    """A custom tool for use with CrewAI agents.

    This tool demonstrates how to define a custom tool with an input schema.
    """

    name: str = "Name of my tool"
    description: str = "Clear description for what this tool is useful for, your agent will need this information to use it."  # noqa: E501
    args_schema: type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:  # noqa: ARG002
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
