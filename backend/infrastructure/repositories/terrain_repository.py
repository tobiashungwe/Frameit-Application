from sqlalchemy.orm import Session
from backend.domain.models.terrain import Terrain


class TerrainRepository:
    @staticmethod
    def list_terrains(db: Session):
        return db.query(Terrain).filter(Terrain.is_active.is_(True)).all()

    @staticmethod
    def get_terrain(db: Session, terrain_id: int):
        return db.query(Terrain).filter(Terrain.id == terrain_id).first()

    @staticmethod
    def create_terrain(db: Session, name: str, user_id: int = None):
        new_terrain = Terrain(name=name, user_id=user_id)
        db.add(new_terrain)
        db.commit()
        db.refresh(new_terrain)
        return new_terrain

    @staticmethod
    def update_terrain(
        db: Session, terrain_id: int, name: str = None, is_active: bool = None
    ):
        terrain = db.query(Terrain).filter(Terrain.id == terrain_id).first()
        if not terrain:
            return None
        if name is not None:
            terrain.name = name
        if is_active is not None:
            terrain.is_active = is_active
        db.commit()
        db.refresh(terrain)
        return terrain

    @staticmethod
    def delete_terrain(db: Session, terrain_id: int):
        terrain = db.query(Terrain).filter(Terrain.id == terrain_id).first()
        if not terrain:
            return False
        db.delete(terrain)
        db.commit()
        return True
