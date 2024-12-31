from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db_session
from backend.application.services.translation_service import TranslationService

router = APIRouter()


@router.get("/{language}")
def get_translations(language: str, db: Session = Depends(get_db_session)):
    service = TranslationService(db)
    translations = service.fetch_translations(language)
    return {"language": language, "translations": translations}
