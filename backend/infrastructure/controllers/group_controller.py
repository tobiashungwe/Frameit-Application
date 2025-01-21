from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.application.services.group_service import GroupService
from backend.core.database import get_db_session
from backend.infrastructure.models.responses.group_response import GroupResponse

router = APIRouter()


@router.get("/", response_model=List[GroupResponse])
def list_groups(db: Session = Depends(get_db_session)):
    service = GroupService(db)
    groups = service.list_groups()
    return [GroupResponse(id=g.id, name=g.name, is_active=g.is_active) for g in groups]


@router.post("/", response_model=GroupResponse)
def create_group(name: str, db: Session = Depends(get_db_session)):
    service = GroupService(db)
    new_group = service.create_group(name)
    return GroupResponse(
        id=new_group.id, name=new_group.name, is_active=new_group.is_active
    )


@router.get("/{group_id}", response_model=GroupResponse)
def get_group(group_id: int, db: Session = Depends(get_db_session)):
    service = GroupService(db)
    group = service.get_group(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return GroupResponse(id=group.id, name=group.name, is_active=group.is_active)


@router.put("/{group_id}", response_model=GroupResponse)
def update_group(
    group_id: int,
    name: str = None,
    is_active: bool = None,
    db: Session = Depends(get_db_session),
):
    service = GroupService(db)
    updated_group = service.update_group(group_id, name, is_active)
    if not updated_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return GroupResponse(
        id=updated_group.id, name=updated_group.name, is_active=updated_group.is_active
    )


@router.delete("/{group_id}", response_model=dict)
def delete_group(group_id: int, db: Session = Depends(get_db_session)):
    service = GroupService(db)
    success = service.delete_group(group_id)
    if not success:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"deleted": True}
