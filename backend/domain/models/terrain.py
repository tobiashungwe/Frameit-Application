from sqlalchemy import Column, Integer, String, Boolean
from backend.core.database import Base


class Terrain(Base):
    __tablename__ = "terrains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=False, index=True)
    is_active = Column(Boolean, default=True)
