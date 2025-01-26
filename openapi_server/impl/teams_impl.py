from typing import List, Optional
from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated
from openapi_server.apis.teams_api_base import BaseTeamsApi
from openapi_server.models.team import Team
from openapi_server.models.team_input import TeamInput
from openapi_server.models.team_update import TeamUpdate


class TeamsImpl(BaseTeamsApi):
    async def create_team(
        self,
        team_input: TeamInput,
    ) -> Team:
        """Adds a new team to the system."""
        # Default fallback implementation
        return Team(id=0, name="Default Team", description="Default team description")

    async def delete_team(
        self,
        team_id: Annotated[StrictInt, Field(description="The ID of the team")],
    ) -> None:
        """Removes a team from the system by its ID."""
        # Default fallback implementation
        print(f"Team with ID {team_id} deleted (default fallback).")

    async def get_team_by_id(
        self,
        team_id: Annotated[StrictInt, Field(description="The ID of the team")],
    ) -> Team:
        """Retrieves detailed information about a team by its ID."""
        # Default fallback implementation
        return Team(id=team_id, name="Default Team", description="Default team description")

    async def list_teams(
        self,
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of teams to return.")] = 20,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")] = 0,
    ) -> List[Team]:
        """Retrieves a list of all teams available in the system."""
        # Default fallback implementation
        return [Team(id=i, name=f"Default Team {i}", description="Default team description") for i in range(offset, offset + limit)]

    async def update_team(
        self,
        team_id: Annotated[StrictInt, Field(description="The ID of the team")],
        team_update: TeamUpdate,
    ) -> Team:
        """Allows partial updates to an existing team's information."""
        # Default fallback implementation
        return Team(id=team_id, name=team_update.name or "Updated Team", description=team_update.description or "Updated team description")