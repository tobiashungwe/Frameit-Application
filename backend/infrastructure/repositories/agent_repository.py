from typing import List, Optional
from sqlalchemy.orm import Session
from backend.domain.agents.agent_models import AgentEntity
from backend.core.database import get_db_session


class AgentRepository:
    @staticmethod
    def create_agent(name: str, description: Optional[str]) -> AgentEntity:
        session: Session = get_db_session()
        new_agent = AgentEntity(name=name, description=description)
        session.add(new_agent)
        session.commit()
        session.refresh(new_agent)
        return new_agent

    @staticmethod
    def get_agent_by_id(agent_id: int) -> Optional[AgentEntity]:
        session: Session = get_db_session()
        return session.query(AgentEntity).filter(AgentEntity.id == agent_id).first()

    @staticmethod
    def list_agents() -> List[AgentEntity]:
        session: Session = get_db_session()
        return session.query(AgentEntity).all()

    @staticmethod
    def update_agent(agent_id: int, **kwargs) -> Optional[AgentEntity]:
        session: Session = get_db_session()
        agent = session.query(AgentEntity).filter(AgentEntity.id == agent_id).first()
        if not agent:
            return None
        for key, value in kwargs.items():
            setattr(agent, key, value)
        session.commit()
        session.refresh(agent)
        return agent

    @staticmethod
    def delete_agent(agent_id: int) -> bool:
        session: Session = get_db_session()
        agent = session.query(AgentEntity).filter(AgentEntity.id == agent_id).first()
        if agent:
            session.delete(agent)
            session.commit()
            return True
        return False
