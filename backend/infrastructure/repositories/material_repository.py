from sqlalchemy.orm import Session
from backend.domain.models.material import Material


class MaterialRepository:
    @staticmethod
    def list_materials(db: Session):
        return db.query(Material).filter(Material.is_active.is_(True)).all()

    @staticmethod
    def get_material(db: Session, material_id: int):
        return db.query(Material).filter(Material.id == material_id).first()

    @staticmethod
    def create_material(
        db: Session, name: str, category: str = None, user_id: int = None
    ):
        new_material = Material(name=name, category=category, user_id=user_id)
        db.add(new_material)
        db.commit()
        db.refresh(new_material)
        return new_material

    @staticmethod
    def update_material(
        db: Session,
        material_id: int,
        name: str = None,
        category: str = None,
        is_active: bool = None,
    ):
        material = db.query(Material).filter(Material.id == material_id).first()
        if not material:
            return None
        if name is not None:
            material.name = name
        if category is not None:
            material.category = category
        if is_active is not None:
            material.is_active = is_active
        db.commit()
        db.refresh(material)
        return material

    @staticmethod
    def delete_material(db: Session, material_id: int):
        material = db.query(Material).filter(Material.id == material_id).first()
        if not material:
            return False
        db.delete(material)
        db.commit()
        return True
