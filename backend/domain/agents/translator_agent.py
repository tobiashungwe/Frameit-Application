from pydantic_ai import Agent, RunContext
from backend.core.model_config import ModelConfig
from backend.infrastructure.models import TranslationDependencies, TranslationResult
import logfire
from backend.application.services.prompt_service import PromptService

logfire.configure()


class TranslatorAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template(
            "translator_agent_static"
        )

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=TranslationDependencies,
            result_type=TranslationResult,
            system_prompt=static_prompt,
        )

        @self.agent.system_prompt
        def translate_story(ctx: RunContext[TranslationDependencies]) -> str:
            """Translate the given story into the specified target language."""
            with logfire.span("translator_agent:translate_story"):
                logfire.info(f"Translating story to '{ctx.deps.target_language}'...")
                return self.prompt_service.generate_dynamic_prompt(
                    name="translator_agent_dynamic",
                    story=ctx.deps.story,
                    target_language=ctx.deps.target_language,
                )
