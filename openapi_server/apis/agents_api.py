# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.agents_api_base import BaseAgentsApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.database import SessionDep
from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.agent import Agent
from openapi_server.models.agent_input import AgentInput
from openapi_server.models.agent_update import AgentUpdate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/agents",
    responses={
        201: {"model": Agent, "description": "Agent created successfully"},
    },
    tags=["Agents"],
    summary="Create a new agent",
    response_model_by_alias=True,
)
async def create_agent(
    session: SessionDep,
    agent_input: AgentInput = Body(None, description=""),
) -> Agent:
    """Adds a new agent to the system."""
    if not BaseAgentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAgentsApi.subclasses[0]().create_agent(session, agent_input)


@router.delete(
    "/agents/{agent_id}",
    responses={
        204: {"description": "Agent deleted successfully"},
        404: {"description": "Agent not found"},
    },
    tags=["Agents"],
    summary="Delete an agent",
    response_model_by_alias=True,
)
async def delete_agent(
    session: SessionDep,
    agent_id: Annotated[StrictInt, Field(description="The ID of the agent")] = Path(..., description="The ID of the agent"),
) -> None:
    """Removes an agent from the system by its ID."""
    if not BaseAgentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAgentsApi.subclasses[0]().delete_agent(session, agent_id)


@router.get(
    "/agents/{agent_id}",
    responses={
        200: {"model": Agent, "description": "Agent details"},
        404: {"description": "Agent not found"},
    },
    tags=["Agents"],
    summary="Get details of a specific agent",
    response_model_by_alias=True,
)
async def get_agent_by_id(
    session: SessionDep,
    agent_id: Annotated[StrictInt, Field(description="The ID of the agent")] = Path(..., description="The ID of the agent"),
) -> Agent:
    """Retrieves detailed information about an agent by its ID."""
    if not BaseAgentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAgentsApi.subclasses[0]().get_agent_by_id(session, agent_id)


@router.get(
    "/agents",
    responses={
        200: {"model": List[Agent], "description": "A list of agents"},
    },
    tags=["Agents"],
    summary="List all agents",
    response_model_by_alias=True,
)
async def list_agents(
    session: SessionDep,
    status: Annotated[Optional[StrictStr], Field(description="Filter agents by status.")] = Query(None, description="Filter agents by status.", alias="status"),
    role: Annotated[Optional[StrictStr], Field(description="Filter agents by role.")] = Query(None, description="Filter agents by role.", alias="role"),
    limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of agents to return.")] = Query(20, description="Maximum number of agents to return.", alias="limit", ge=1),
    offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")] = Query(0, description="Pagination offset.", alias="offset", ge=0),
) -> List[Agent]:
    """Retrieves a list of all agents available in the system."""
    if not BaseAgentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAgentsApi.subclasses[0]().list_agents(session, status, role, limit, offset)


@router.patch(
    "/agents/{agent_id}",
    responses={
        200: {"model": Agent, "description": "Agent updated successfully"},
        404: {"description": "Agent not found"},
    },
    tags=["Agents"],
    summary="Update an existing agent",
    response_model_by_alias=True,
)
async def update_agent(
    session: SessionDep,
    agent_id: Annotated[StrictInt, Field(description="The ID of the agent")] = Path(..., description="The ID of the agent"),
    agent_update: AgentUpdate = Body(None, description=""),
) -> Agent:
    """Allows partial updates to an existing agent&#39;s information."""
    if not BaseAgentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAgentsApi.subclasses[0]().update_agent(session, agent_id, agent_update)
