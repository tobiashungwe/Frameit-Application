from sqlalchemy.orm import Session
from backend.infrastructure.repositories.translation_repository import (
    TranslationRepository,
)


class TranslationService:
    """
    Service class for managing translations pure for the UI elements to enhance maintainability for 188n module.
    """

    def __init__(self, db: Session):
        self.db = db

    def fetch_translations(self, language: str):
        translations = TranslationRepository.get_translations_by_language(
            self.db, language
        )
        return {translation.key: translation.value for translation in translations}
