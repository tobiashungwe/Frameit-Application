from fastapi import APIRouter, HTTPException
from typing import List
from backend.application.services.theme_service import ThemeService

# TODO: Make sure to use ThemeEntity with the theme controller so that it can also check the types and get the themes from the database
# from backend.domain.models import ThemeEntity

router = APIRouter()


@router.get("/", response_model=List[dict])
def list_themes():
    themes = ThemeService.list_themes()
    return [
        {"id": t.id, "title": t.title, "description": t.description} for t in themes
    ]


@router.post("/", response_model=dict)
def create_theme(title: str, description: str = ""):
    new_theme = ThemeService.create_theme(title, description)
    return {
        "id": new_theme.id,
        "title": new_theme.title,
        "description": new_theme.description,
    }


@router.get("/{theme_id}", response_model=dict)
def get_theme(theme_id: int):
    theme = ThemeService.get_theme(theme_id)
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return {"id": theme.id, "title": theme.title, "description": theme.description}


@router.put("/{theme_id}", response_model=dict)
def update_theme(
    theme_id: int, title: str = None, description: str = None, is_active: bool = None
):
    updated = ThemeService.update_theme(
        theme_id, title=title, description=description, is_active=is_active
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Theme not found")
    return {
        "id": updated.id,
        "title": updated.title,
        "description": updated.description,
    }


@router.delete("/{theme_id}", response_model=dict)
def delete_theme(theme_id: int):
    success = ThemeService.delete_theme(theme_id)
    if not success:
        raise HTTPException(status_code=404, detail="Theme not found")
    return {"deleted": True}
