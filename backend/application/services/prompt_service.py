from sqlalchemy.orm import Session
from backend.infrastructure.repositories.prompt_repository import PromptRepository


class PromptService:
    def __init__(self, db: Session):
        self.db = db

    def get_prompt_template(self, name: str) -> str:
        """Fetch a prompt template from the database."""
        prompt = PromptRepository.get_prompt_by_name(self.db, name)
        if not prompt:
            raise ValueError(f"Prompt template '{name}' not found.")
        return prompt.prompt_text

    def generate_dynamic_prompt(self, name: str, **variables) -> str:
        """
        Generate a dynamic prompt by injecting variables into a template.
        """
        template = self.get_prompt_template(name)
        try:
            return template.format(**variables)
        except KeyError as e:
            raise ValueError(f"Missing variable for prompt generation: {e}")
