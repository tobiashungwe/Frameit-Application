from sqlalchemy.orm import Session
from backend.infrastructure.repositories.material_repository import MaterialRepository


class MaterialService:
    def __init__(self, db: Session):
        self.db = db

    def list_materials(self):
        return MaterialRepository.list_materials(self.db)

    def get_material(self, material_id: int):
        return MaterialRepository.get_material(self.db, material_id)

    def create_material(self, name: str, category: str = None, user_id: int = None):
        return MaterialRepository.create_material(self.db, name, category, user_id)

    def update_material(
        self,
        material_id: int,
        name: str = None,
        category: str = None,
        is_active: bool = None,
    ):
        return MaterialRepository.update_material(
            self.db, material_id, name, category, is_active
        )

    def delete_material(self, material_id: int):
        return MaterialRepository.delete_material(self.db, material_id)
