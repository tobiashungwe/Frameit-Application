from sqlalchemy.orm import Session
from backend.domain.models.prompt import Prompt


class PromptRepository:
    @staticmethod
    def get_prompt_by_name(db: Session, name: str) -> Prompt:
        return db.query(Prompt).filter(Prompt.name == name).first()

    @staticmethod
    def list_prompts(db: Session):
        return db.query(Prompt).all()

    @staticmethod
    def create_prompt(db: Session, name: str, prompt_text: str, version: int = 1):
        new_prompt = Prompt(name=name, prompt_text=prompt_text, version=version)
        db.add(new_prompt)
        db.commit()
        db.refresh(new_prompt)
        return new_prompt
