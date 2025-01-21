from sqlalchemy.orm import Session
from backend.domain.models.group import Group


class GroupRepository:
    @staticmethod
    def list_groups(db: Session):
        return db.query(Group).filter(Group.is_active.is_(True)).all()

    @staticmethod
    def get_group(db: Session, group_id: int):
        return db.query(Group).filter(Group.id == group_id).first()

    @staticmethod
    def create_group(db: Session, name: str):
        new_group = Group(name=name)
        db.add(new_group)
        db.commit()
        db.refresh(new_group)
        return new_group

    @staticmethod
    def update_group(
        db: Session, group_id: int, name: str = None, is_active: bool = None
    ):
        group = db.query(Group).filter(Group.id == group_id).first()
        if not group:
            return None
        if name is not None:
            group.name = name
        if is_active is not None:
            group.is_active = is_active
        db.commit()
        db.refresh(group)
        return group

    @staticmethod
    def delete_group(db: Session, group_id: int):
        group = db.query(Group).filter(Group.id == group_id).first()
        if not group:
            return False
        db.delete(group)
        db.commit()
        return True
