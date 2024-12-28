from fastapi import APIRouter, HTTPException
from typing import List
from backend.application.services.agent_service import AgentService

# TODO: Make sure to use agententity with the agent controller so that it can also check the types
# from backend.domain.agents.agent_models import AgentEntity

router = APIRouter()


@router.get("/", response_model=List[dict])  # Or a Pydantic schema
def list_agents():
    agents = AgentService.list_agents()
    # Convert to basic dict if not using Pydantic
    return [{"id": a.id, "name": a.name, "description": a.description} for a in agents]


@router.post("/", response_model=dict)
def create_agent(name: str, description: str = None):
    agent = AgentService.create_agent(name, description)
    return {"id": agent.id, "name": agent.name, "description": agent.description}


@router.get("/{agent_id}", response_model=dict)
def get_agent(agent_id: int):
    agent = AgentService.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"id": agent.id, "name": agent.name, "description": agent.description}


@router.put("/{agent_id}", response_model=dict)
def update_agent(
    agent_id: int, name: str = None, description: str = None, is_active: bool = None
):
    updated = AgentService.update_agent(
        agent_id, name=name, description=description, is_active=is_active
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"id": updated.id, "name": updated.name, "description": updated.description}


@router.delete("/{agent_id}", response_model=dict)
def delete_agent(agent_id: int):
    success = AgentService.delete_agent(agent_id)
    if not success:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"deleted": True}
