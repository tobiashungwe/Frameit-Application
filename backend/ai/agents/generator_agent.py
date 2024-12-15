from pydantic_ai import Agent, RunContext
from models.dependencies import ThemeDependencies
from models.result_models import ThemeResult
from logger_config import logger

generator_agent = Agent(
    "groq:llama-3.3-70b-versatile",
    deps_type=ThemeDependencies,
    result_type=ThemeResult,
    system_prompt=(
        "Create an engaging story for children that incorporates the activity '{activity_description}', "
        "the theme '{theme}', and the following keywords: {user_keywords}."
    ),
)


@generator_agent.tool
async def create_story(ctx: RunContext[ThemeDependencies]) -> str:
    logger.info(
        f"Generator Agent: Creating story for theme '{ctx.deps.theme}' and activity '{ctx.deps.activity_description}'"
    )
    return f"In the {ctx.deps.theme}, {', '.join(ctx.deps.user_keywords)} engage in {ctx.deps.activity_description}. It is an exciting adventure!"
