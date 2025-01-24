from pydantic_ai import Agent, RunContext
from backend.core.model_config import ModelConfig
from backend.infrastructure.models import AdapterDependencies, AdapterResponse
from typing import Dict
import logfire
from backend.application.services.prompt_service import PromptService

logfire.configure()


class AdapterAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template("adapter_agent_static")

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=AdapterDependencies,
            result_type=AdapterResponse,
            system_prompt=static_prompt,
            retries=3,
        )

        @self.agent.system_prompt
        def map_objects(ctx: RunContext[AdapterDependencies]) -> Dict[str, str]:
            """Map generic activity objects to equivalents in the given theme."""
            exercise = ctx.deps.exercise
            theme = ctx.deps.theme
            user_keywords = ", ".join(ctx.deps.user_keywords)
            with logfire.span("adapter_agent:map_objects"):
                logfire.info(
                    f"Mapping objects for activity '{exercise}' in theme '{theme}' with keywords: '{user_keywords}'"
                )
                return self.prompt_service.generate_dynamic_prompt(
                    name="adapter_agent_dynamic",
                    exercise=exercise,
                    theme=theme,
                    user_keywords=user_keywords,
                )


# Todo: Make sure to add a tool to extract the materials out of the document and other information!
