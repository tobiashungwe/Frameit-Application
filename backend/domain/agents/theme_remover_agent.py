from pydantic_ai import Agent
import logfire
from backend.core.model_config import ModelConfig
from backend.application.services.prompt_service import PromptService

logfire.configure()


class ThemeRemoverAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        base_prompt = self.prompt_service.get_prompt_template(
            "theme_remover_agent_base"
        )

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            system_prompt=base_prompt,
        )

        @self.agent.system_prompt
        def remove_theme() -> str:
            """Remove the theme from the given story."""
            with logfire.span("theme_remover_agent:remove_theme"):
                logfire.info(
                    "Removing theme from the story..., making sure to only provide the result!"
                )
                static_prompt = self.prompt_service.get_prompt_template(
                    "theme_remover_agent_static"
                )
                return static_prompt
