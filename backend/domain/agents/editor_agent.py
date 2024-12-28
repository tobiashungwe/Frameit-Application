from pydantic_ai import Agent, RunContext
from backend.infrastructure.models import EditorDependencies
import logfire

from backend.core.model_config import ModelConfig

logfire.configure()


# TODO: editor agent: Can edit specific lines of text that was generarated (Nice to have)
# Define the Editor Agent
editor_agent = Agent(
    model=ModelConfig.DEFAULT_MODEL,
    deps_type=EditorDependencies,
    system_prompt="You are a professional content editor. Refine and improve the following story "
    "to ensure it is engaging, cohesive, and free of errors. "
    "Fix grammar, improve clarity, and enhance flow while preserving the original meaning.",
)


@editor_agent.tool
async def refine_story(ctx: RunContext[EditorDependencies]) -> str:
    """
    Tool to refine and polish a story for grammar, clarity, and readability.
    Args:
        story (str): The raw story text that needs refinement.

    Returns:
        str: The refined and polished story.
    """
    with logfire.span("editor_agent:refine_story"):
        logfire.info("Refining story for grammar, clarity, and structure.")
        # Run the editor tool
        response = await ctx.agent.run(
            f"Refine and improve the following story:\n\n{ctx.deps.story}"
        )
        refined_story = response.data.strip()
        logfire.info("Story refinement completed successfully.")
        return refined_story
