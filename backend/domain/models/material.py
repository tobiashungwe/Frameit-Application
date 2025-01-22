from sqlalchemy import Column, Integer, String, Boolean
from backend.core.database import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=False, index=True)
    category = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
