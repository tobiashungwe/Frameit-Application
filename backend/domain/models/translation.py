from sqlalchemy import Column, Integer, String, Text
from backend.core.database import Base


class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String(5), nullable=False)
    key = Column(String(255), nullable=False)
    value = Column(Text, nullable=False)
