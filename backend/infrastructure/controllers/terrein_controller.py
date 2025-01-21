from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.application.services.terrain_service import TerrainService
from backend.core.database import get_db_session
from backend.infrastructure.models.responses.terrain_response import TerrainResponse

router = APIRouter()


@router.get("/", response_model=List[TerrainResponse])
def list_terrains(db: Session = Depends(get_db_session)):
    service = TerrainService(db)
    terrains = service.list_terrains()
    return [
        TerrainResponse(id=t.id, name=t.name, is_active=t.is_active, user_id=t.user_id)
        for t in terrains
    ]


@router.get("/{terrain_id}", response_model=TerrainResponse)
def get_terrain(terrain_id: int, db: Session = Depends(get_db_session)):
    service = TerrainService(db)
    terrain = service.get_terrain(terrain_id)
    if not terrain:
        raise HTTPException(status_code=404, detail="Terrain not found")
    return TerrainResponse(
        id=terrain.id,
        name=terrain.name,
        is_active=terrain.is_active,
        user_id=terrain.user_id,
    )


@router.post("/", response_model=TerrainResponse)
def create_terrain(
    name: str, user_id: int = None, db: Session = Depends(get_db_session)
):
    service = TerrainService(db)
    new_terrain = service.create_terrain(name, user_id)
    return TerrainResponse(
        id=new_terrain.id,
        name=new_terrain.name,
        is_active=new_terrain.is_active,
        user_id=new_terrain.user_id,
    )


@router.put("/{terrain_id}", response_model=TerrainResponse)
def update_terrain(
    terrain_id: int,
    name: str = None,
    is_active: bool = None,
    db: Session = Depends(get_db_session),
):
    service = TerrainService(db)
    updated_terrain = service.update_terrain(terrain_id, name, is_active)
    if not updated_terrain:
        raise HTTPException(status_code=404, detail="Terrain not found")
    return TerrainResponse(
        id=updated_terrain.id,
        name=updated_terrain.name,
        is_active=updated_terrain.is_active,
        user_id=updated_terrain.user_id,
    )


@router.delete("/{terrain_id}", response_model=dict)
def delete_terrain(terrain_id: int, db: Session = Depends(get_db_session)):
    service = TerrainService(db)
    success = service.delete_terrain(terrain_id)
    if not success:
        raise HTTPException(status_code=404, detail="Terrain not found")
    return {"deleted": True}
