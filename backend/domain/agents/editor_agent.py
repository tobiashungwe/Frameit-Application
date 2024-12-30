from pydantic_ai import Agent, RunContext
from backend.infrastructure.models import EditorDependencies
import logfire

from backend.core.model_config import ModelConfig
from backend.application.services.prompt_service import PromptService

logfire.configure()


class EditorAgent:
    def __init__(self, db):
        self.prompt_service = PromptService(db)

        static_prompt = self.prompt_service.get_prompt_template("editor_agent_static")

        self.agent = Agent(
            model=ModelConfig.DEFAULT_MODEL,
            deps_type=EditorDependencies,
            system_prompt=static_prompt,
        )

        @self.agent.system_prompt
        def refine_story(ctx: RunContext[EditorDependencies]) -> str:
            """Refine and polish a story for grammar, clarity, and readability."""
            with logfire.span("editor_agent:refine_story"):
                logfire.info("Refining story for grammar, clarity, and structure.")
                return self.prompt_service.generate_dynamic_prompt(
                    name="editor_agent_dynamic",
                    story=ctx.deps.story,
                )


# TODO: editor agent: Can edit specific lines of text that was generarated (Nice to have)
