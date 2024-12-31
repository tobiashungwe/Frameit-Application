from sqlalchemy.orm import Session
from backend.domain.models.translation import Translation


class TranslationRepository:
    @staticmethod
    def get_translations_by_language(db: Session, language: str):
        return db.query(Translation).filter(Translation.language == language).all()

    @staticmethod
    def add_translation(db: Session, language: str, key: str, value: str):
        translation = Translation(language=language, key=key, value=value)
        db.add(translation)
        db.commit()
        return translation
