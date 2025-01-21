from sqlalchemy.orm import Session
from backend.infrastructure.repositories.terrain_repository import TerrainRepository


class TerrainService:
    def __init__(self, db: Session):
        self.db = db

    def list_terrains(self):
        return TerrainRepository.list_terrains(self.db)

    def get_terrain(self, terrain_id: int):
        return TerrainRepository.get_terrain(self.db, terrain_id)

    def create_terrain(self, name: str, user_id: int = None):
        return TerrainRepository.create_terrain(self.db, name, user_id)

    def update_terrain(self, terrain_id: int, name: str = None, is_active: bool = None):
        return TerrainRepository.update_terrain(self.db, terrain_id, name, is_active)

    def delete_terrain(self, terrain_id: int):
        return TerrainRepository.delete_terrain(self.db, terrain_id)
