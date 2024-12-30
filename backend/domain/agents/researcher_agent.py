from pydantic_ai import Agent, RunContext
from backend.core.model_config import ModelConfig
from backend.application.services.prompt_service import PromptService
from backend.infrastructure.models import ResearchDependencies, ResearchResponse
import logfire


logfire.configure()


class ResearchAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template("research_theme_static")

        # Initialize the Agent with a default system prompt
        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=ResearchDependencies,
            result_type=ResearchResponse,
            system_prompt=static_prompt,
        )

        @self.agent.system_prompt
        def research_theme(ctx: RunContext[ResearchDependencies]) -> str:
            """Research theme by using a dynamic prompt from the database."""
            theme = ctx.deps.theme
            user_keywords = ", ".join(ctx.deps.user_keywords)
            with logfire.span("researcher_agent:research_theme"):
                logfire.info(
                    f"Researching theme for query: '{theme}' with keywords: '{user_keywords}'"
                )
                return self.prompt_service.generate_dynamic_prompt(
                    name="research_theme_dynamic",
                    theme=theme,
                    user_keywords=user_keywords,
                )
