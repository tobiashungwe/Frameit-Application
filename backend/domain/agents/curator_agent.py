from pydantic_ai import Agent, RunContext
from backend.application.services.prompt_service import PromptService
from backend.core.model_config import ModelConfig
from backend.infrastructure.models import ThemeDependencies
from typing import List
import logfire

logfire.configure()


class CuratorAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template("curator_agent_static")

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=ThemeDependencies,
            system_prompt=static_prompt,
        )

        @self.agent.system_prompt
        def suggest_themes(ctx: RunContext[ThemeDependencies]) -> List[str]:
            """Suggest standalone themes suitable for children’s activities."""
            with logfire.span("curator_agent:suggest_themes"):
                logfire.info(f"Generating themes for query: '{ctx.deps.theme}'")
                theme = ctx.deps.theme
                response = self.prompt_service.generate_dynamic_prompt(
                    name="curator_agent_dynamic",
                    theme=theme,
                )
            return [
                theme.strip() for theme in response.data.split("\n") if theme.strip()
            ]
