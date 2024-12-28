from pydantic_ai import Agent
import logfire
from backend.core.model_config import ModelConfig

logfire.configure()

theme_remover_agent = Agent(
    model=ModelConfig.DEFAULT_MODEL,
    system_prompt="Remove the theme from the given story.",
)


@theme_remover_agent.system_prompt
def remove_theme() -> str:
    with logfire.span("theme_remover_agent:remove_theme"):
        logfire.info(
            "Removing theme from the story..., making sure to only provide the result!"
        )
    return "Make sure to only provide the result!"
