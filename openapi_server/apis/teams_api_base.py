# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.team import Team
from openapi_server.models.team_input import TeamInput
from openapi_server.models.team_update import TeamUpdate


class BaseTeamsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTeamsApi.subclasses = BaseTeamsApi.subclasses + (cls,)
    async def create_team(
        self,
        team_input: TeamInput,
    ) -> Team:
        """Adds a new team to the system."""
        ...


    async def delete_team(
        self,
        team_id: Annotated[StrictInt, Field(description="The ID of the team")],
    ) -> None:
        """Removes a team from the system by its ID."""
        ...


    async def get_team_by_id(
        self,
        team_id: Annotated[StrictInt, Field(description="The ID of the team")],
    ) -> Team:
        """Returns details about a particular team by its ID."""
        ...


    async def list_teams(
        self,
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of teams to return.")],
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")],
    ) -> List[Team]:
        """Retrieves a list of all teams in the system."""
        ...


    async def update_team(
        self,
        team_id: Annotated[StrictInt, Field(description="The ID of the team")],
        team_update: TeamUpdate,
    ) -> Team:
        """Allows partial updates to an existing team’s information."""
        ...
