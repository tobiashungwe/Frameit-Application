from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.application.services.material_service import MaterialService
from backend.core.database import get_db_session
from backend.infrastructure.models.responses.material_response import MaterialResponse

router = APIRouter()


@router.get("/", response_model=List[MaterialResponse])
def list_materials(db: Session = Depends(get_db_session)):
    service = MaterialService(db)
    materials = service.list_materials()
    return [
        MaterialResponse(
            id=m.id,
            name=m.name,
            category=m.category,
            is_active=m.is_active,
            user_id=m.user_id,
        )
        for m in materials
    ]


@router.get("/{material_id}", response_model=MaterialResponse)
def get_material(material_id: int, db: Session = Depends(get_db_session)):
    service = MaterialService(db)
    material = service.get_material(material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return MaterialResponse(
        id=material.id,
        name=material.name,
        category=material.category,
        is_active=material.is_active,
        user_id=material.user_id,
    )


@router.post("/", response_model=MaterialResponse)
def create_material(
    name: str,
    category: str = None,
    user_id: int = None,
    db: Session = Depends(get_db_session),
):
    service = MaterialService(db)
    new_material = service.create_material(name, category, user_id)
    return MaterialResponse(
        id=new_material.id,
        name=new_material.name,
        category=new_material.category,
        is_active=new_material.is_active,
        user_id=new_material.user_id,
    )


@router.put("/{material_id}", response_model=MaterialResponse)
def update_material(
    material_id: int,
    name: str = None,
    category: str = None,
    is_active: bool = None,
    db: Session = Depends(get_db_session),
):
    service = MaterialService(db)
    updated_material = service.update_material(material_id, name, category, is_active)
    if not updated_material:
        raise HTTPException(status_code=404, detail="Material not found")
    return MaterialResponse(
        id=updated_material.id,
        name=updated_material.name,
        category=updated_material.category,
        is_active=updated_material.is_active,
        user_id=updated_material.user_id,
    )


@router.delete("/{material_id}", response_model=dict)
def delete_material(material_id: int, db: Session = Depends(get_db_session)):
    service = MaterialService(db)
    success = service.delete_material(material_id)
    if not success:
        raise HTTPException(status_code=404, detail="Material not found")
    return {"deleted": True}
