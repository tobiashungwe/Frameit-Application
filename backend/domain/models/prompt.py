from sqlalchemy import Column, Integer, String, Text
from backend.core.database import Base


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    prompt_text = Column(Text, nullable=False)
    type = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
