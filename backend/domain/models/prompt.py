from sqlalchemy import Column, Integer, String, Text
from backend.core.database import Base


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    prompt_text = Column(Text, nullable=False)
    version = Column(Integer, default=1)
    context = Column(String(512), nullable=True)  # E.g., 'agent_name' or 'use_case'
