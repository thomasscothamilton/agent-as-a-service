# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated

from openapi_server.database import SessionDep
from openapi_server.models.agent import Agent
from openapi_server.models.agent_input import AgentInput
from openapi_server.models.agent_update import AgentUpdate


class BaseAgentsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAgentsApi.subclasses = BaseAgentsApi.subclasses + (cls,)
    async def create_agent(
        self,
        session: SessionDep,
        agent_input: AgentInput,
    ) -> Agent:
        """Adds a new agent to the system."""
        ...


    async def delete_agent(
        self,
        session: SessionDep,
        agent_id: Annotated[StrictInt, Field(description="The ID of the agent")],
    ) -> None:
        """Removes an agent from the system by its ID."""
        ...


    async def get_agent_by_id(
        self,
        session: SessionDep,
        agent_id: Annotated[StrictInt, Field(description="The ID of the agent")],
    ) -> Agent:
        """Retrieves detailed information about an agent by its ID."""
        ...


    async def list_agents(
        self,
        session: SessionDep,
        status: Annotated[Optional[StrictStr], Field(description="Filter agents by status.")],
        role: Annotated[Optional[StrictStr], Field(description="Filter agents by role.")],
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of agents to return.")],
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")],
    ) -> List[Agent]:
        """Retrieves a list of all agents available in the system."""
        ...


    async def update_agent(
        self,
        session: SessionDep,
        agent_id: Annotated[StrictInt, Field(description="The ID of the agent")],
        agent_update: AgentUpdate,
    ) -> Agent:
        """Allows partial updates to an existing agent&#39;s information."""
        ...
