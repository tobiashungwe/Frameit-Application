from sqlalchemy.orm import Session
from backend.domain.models.theme import ThemeEntity


class ThemeRepository:
    @staticmethod
    def get_theme_by_title(db: Session, title: str) -> ThemeEntity:
        return db.query(ThemeEntity).filter(ThemeEntity.title == title).first()

    @staticmethod
    def list_themes(db: Session):
        return db.query(ThemeEntity).all()

    @staticmethod
    def create_theme(
        db: Session, title: str, description: str = None, is_active: bool = True
    ):
        new_theme = ThemeEntity(
            title=title, description=description, is_active=is_active
        )
        db.add(new_theme)
        db.commit()
        db.refresh(new_theme)
        return new_theme

    @staticmethod
    def update_theme(
        db: Session,
        theme_id: int,
        title: str = None,
        description: str = None,
        is_active: bool = None,
    ):
        theme = db.query(ThemeEntity).filter(ThemeEntity.id == theme_id).first()
        if not theme:
            return None
        if title is not None:
            theme.title = title
        if description is not None:
            theme.description = description
        if is_active is not None:
            theme.is_active = is_active
        db.commit()
        db.refresh(theme)
        return theme

    @staticmethod
    def delete_theme(db: Session, theme_id: int):
        theme = db.query(ThemeEntity).filter(ThemeEntity.id == theme_id).first()
        if not theme:
            return False
        db.delete(theme)
        db.commit()
        return True
