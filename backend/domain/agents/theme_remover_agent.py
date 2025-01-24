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
            model=ModelConfig.DEFAULT_MODEL, system_prompt=base_prompt, retries=3
        )
