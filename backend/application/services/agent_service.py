from typing import List, Optional
from backend.domain.agents.agent_models import AgentEntity
from backend.infrastructure.repositories.agent_repository import AgentRepository


class AgentService:
    @staticmethod
    def create_agent(name: str, description: Optional[str] = None) -> AgentEntity:
        # TODO: Add validation and side effects
        new_agent = AgentRepository.create_agent(name, description)
        return new_agent

    @staticmethod
    def get_agent(agent_id: int) -> Optional[AgentEntity]:
        return AgentRepository.get_agent_by_id(agent_id)

    @staticmethod
    def list_agents() -> List[AgentEntity]:
        return AgentRepository.list_agents()

    @staticmethod
    def update_agent(agent_id: int, **kwargs) -> Optional[AgentEntity]:
        return AgentRepository.update_agent(agent_id, **kwargs)

    @staticmethod
    def delete_agent(agent_id: int) -> bool:
        return AgentRepository.delete_agent(agent_id)
