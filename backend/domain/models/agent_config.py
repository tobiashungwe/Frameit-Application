from sqlalchemy import Column, Integer, String, Text, JSON
from backend.core.database import Base


class AgentConfig(Base):
    __tablename__ = "agent_configs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    model = Column(String(255), nullable=False)
    system_prompt = Column(Text, nullable=False)
    deps_type = Column(JSON, nullable=True)
    result_type = Column(JSON, nullable=True)
    model_settings = Column(JSON, nullable=True)
