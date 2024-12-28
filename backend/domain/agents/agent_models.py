from sqlalchemy import Column, Integer, String, Boolean
from backend.core.database import Base


class AgentEntity(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(512), nullable=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<AgentEntity id={self.id} name={self.name}>"
