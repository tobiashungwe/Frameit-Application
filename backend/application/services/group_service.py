from sqlalchemy.orm import Session
from backend.infrastructure.repositories.group_repository import GroupRepository


class GroupService:
    def __init__(self, db: Session):
        self.db = db

    def list_groups(self):
        return GroupRepository.list_groups(self.db)

    def get_group(self, group_id: int):
        return GroupRepository.get_group(self.db, group_id)

    def create_group(self, name: str):
        return GroupRepository.create_group(self.db, name)

    def update_group(self, group_id: int, name: str = None, is_active: bool = None):
        return GroupRepository.update_group(self.db, group_id, name, is_active)

    def delete_group(self, group_id: int):
        return GroupRepository.delete_group(self.db, group_id)
