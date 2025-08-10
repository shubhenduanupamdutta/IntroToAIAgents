"""Custom tool for specific tasks."""

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""

    argument: str = Field(..., description="Description of the argument.")


class MyCustomTool(BaseTool):  # noqa: D101
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will "
        "need this information to use it."
    )
    args_schema: type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:  # noqa: ARG002
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
