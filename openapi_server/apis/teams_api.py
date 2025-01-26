# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.teams_api_base import BaseTeamsApi
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

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictInt
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.team import Team
from openapi_server.models.team_input import TeamInput
from openapi_server.models.team_update import TeamUpdate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/teams",
    responses={
        201: {"model": Team, "description": "Team created successfully"},
    },
    tags=["Teams"],
    summary="Create a new team",
    response_model_by_alias=True,
)
async def create_team(
    team_input: TeamInput = Body(None, description=""),
) -> Team:
    """Adds a new team to the system."""
    if not BaseTeamsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTeamsApi.subclasses[0]().create_team(team_input)


@router.delete(
    "/teams/{team_id}",
    responses={
        204: {"description": "Team deleted successfully"},
        404: {"description": "Team not found"},
    },
    tags=["Teams"],
    summary="Delete an existing team",
    response_model_by_alias=True,
)
async def delete_team(
    team_id: Annotated[StrictInt, Field(description="The ID of the team")] = Path(..., description="The ID of the team"),
) -> None:
    """Removes a team from the system by its ID."""
    if not BaseTeamsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTeamsApi.subclasses[0]().delete_team(team_id)


@router.get(
    "/teams/{team_id}",
    responses={
        200: {"model": Team, "description": "Team details"},
        404: {"description": "Team not found"},
    },
    tags=["Teams"],
    summary="Retrieve a specific team",
    response_model_by_alias=True,
)
async def get_team_by_id(
    team_id: Annotated[StrictInt, Field(description="The ID of the team")] = Path(..., description="The ID of the team"),
) -> Team:
    """Returns details about a particular team by its ID."""
    if not BaseTeamsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTeamsApi.subclasses[0]().get_team_by_id(team_id)


@router.get(
    "/teams",
    responses={
        200: {"model": List[Team], "description": "A list of teams"},
    },
    tags=["Teams"],
    summary="List all teams",
    response_model_by_alias=True,
)
async def list_teams(
    limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of teams to return.")] = Query(20, description="Maximum number of teams to return.", alias="limit", ge=1),
    offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")] = Query(0, description="Pagination offset.", alias="offset", ge=0),
) -> List[Team]:
    """Retrieves a list of all teams in the system."""
    if not BaseTeamsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTeamsApi.subclasses[0]().list_teams(limit, offset)


@router.patch(
    "/teams/{team_id}",
    responses={
        200: {"model": Team, "description": "Team updated successfully"},
        404: {"description": "Team not found"},
    },
    tags=["Teams"],
    summary="Update an existing team",
    response_model_by_alias=True,
)
async def update_team(
    team_id: Annotated[StrictInt, Field(description="The ID of the team")] = Path(..., description="The ID of the team"),
    team_update: TeamUpdate = Body(None, description=""),
) -> Team:
    """Allows partial updates to an existing team’s information."""
    if not BaseTeamsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTeamsApi.subclasses[0]().update_team(team_id, team_update)
