from sqlalchemy.orm import Session
from backend.infrastructure.repositories.theme_repository import ThemeRepository


class ThemeService:
    """
    Service class for managing themes using the ThemeRepository.
    This class provides basic CRUD operations for themes.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_theme_by_title(self, title: str):
        return ThemeRepository.get_theme_by_title(self.db, title)

    def list_themes(self):
        return ThemeRepository.list_themes(self.db)

    def create_theme(self, title: str, description: str = None, is_active: bool = True):
        return ThemeRepository.create_theme(self.db, title, description, is_active)

    def update_theme(
        self,
        theme_id: int,
        title: str = None,
        description: str = None,
        is_active: bool = None,
    ):
        return ThemeRepository.update_theme(
            self.db, theme_id, title, description, is_active
        )

    def delete_theme(self, theme_id: int):
        return ThemeRepository.delete_theme(self.db, theme_id)
