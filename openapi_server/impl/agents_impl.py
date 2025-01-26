from typing import List, Optional
from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated
from openapi_server.apis.agents_api_base import BaseAgentsApi
from openapi_server.database import SessionDep
from openapi_server.models.agent import Agent
from openapi_server.models.agent_input import AgentInput
from openapi_server.models.agent_update import AgentUpdate


class AgentsImpl(BaseAgentsApi):
    async def create_agent(
        self,
        session: SessionDep,
        agent_input: AgentInput,
    ) -> Agent:
        """Adds a new agent to the system."""
        # Default fallback implementation
        return Agent(id=0, name="Default Agent", status="active", role="default")

    async def delete_agent(
        self,
        session: SessionDep,
        agent_id: Annotated[StrictInt, Field(description="The ID of the agent")],
    ) -> None:
        """Removes an agent from the system by its ID."""
        # Default fallback implementation
        print(f"Agent with ID {agent_id} deleted (default fallback).")

    async def get_agent_by_id(
        self,
        session: SessionDep,
        agent_id: Annotated[StrictInt, Field(description="The ID of the agent")],
    ) -> Agent:
        """Retrieves detailed information about an agent by its ID."""
        # Default fallback implementation
        return Agent(id=agent_id, name="Default Agent", status="active", role="default")

    async def list_agents(
        self,
        session: SessionDep,
        status: Annotated[Optional[StrictStr], Field(description="Filter agents by status.")] = None,
        role: Annotated[Optional[StrictStr], Field(description="Filter agents by role.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of agents to return.")] = 20,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")] = 0,
    ) -> List[Agent]:
        """Retrieves a list of all agents available in the system."""
        # Default fallback implementation
        return [Agent(id=i, name=f"Default Agent {i}", status="active", role="default") for i in range(offset, offset + limit)]

    async def update_agent(
        self,
        session: SessionDep,
        agent_id: Annotated[StrictInt, Field(description="The ID of the agent")],
        agent_update: AgentUpdate,
    ) -> Agent:
        """Allows partial updates to an existing agent's information."""
        # Default fallback implementation
        return Agent(id=agent_id, name=agent_update.name or "Updated Agent", status=agent_update.status or "active", role=agent_update.role or "default")