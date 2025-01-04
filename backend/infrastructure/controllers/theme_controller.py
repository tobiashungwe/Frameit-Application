from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.application.services.theme_service import ThemeService
from backend.core.database import get_db_session

from backend.infrastructure.models import ThemeResponse

router = APIRouter()


@router.get("/", response_model=List[ThemeResponse])
def list_themes(db: Session = Depends(get_db_session)):
    theme_service = ThemeService(db)
    themes = theme_service.list_themes()
    return themes


@router.post("/", response_model=ThemeResponse)
def create_theme(
    title: str, description: str = "", db: Session = Depends(get_db_session)
):
    theme_service = ThemeService(db)
    new_theme = theme_service.create_theme(title, description)
    return new_theme


@router.get("/{theme_id}", response_model=ThemeResponse)
def get_theme(theme_id: int, db: Session = Depends(get_db_session)):
    theme_service = ThemeService(db)
    theme = theme_service.get_theme(theme_id)
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return theme


@router.put("/{theme_id}", response_model=ThemeResponse)
def update_theme(
    theme_id: int,
    title: str = None,
    description: str = None,
    is_active: bool = None,
    db: Session = Depends(get_db_session),
):
    theme_service = ThemeService(db)
    updated_theme = theme_service.update_theme(
        theme_id, title=title, description=description, is_active=is_active
    )
    if not updated_theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return updated_theme


@router.delete("/{theme_id}", response_model=dict)
def delete_theme(theme_id: int, db: Session = Depends(get_db_session)):
    theme_service = ThemeService(db)
    success = theme_service.delete_theme(theme_id)
    if not success:
        raise HTTPException(status_code=404, detail="Theme not found")
    return {"deleted": True}
