# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.list_agents_default_response import ListAgentsDefaultResponse  # noqa: F401
from openapi_server.models.team import Team  # noqa: F401
from openapi_server.models.team_input import TeamInput  # noqa: F401
from openapi_server.models.team_update import TeamUpdate  # noqa: F401


def test_create_team(client: TestClient):
    """Test case for create_team

    Create a new team
    """
    team_input = {"name":"name","description":"description"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/teams",
    #    headers=headers,
    #    json=team_input,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_team(client: TestClient):
    """Test case for delete_team

    Delete an existing team
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/teams/{team_id}".format(team_id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_team_by_id(client: TestClient):
    """Test case for get_team_by_id

    Retrieve a specific team
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/teams/{team_id}".format(team_id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_teams(client: TestClient):
    """Test case for list_teams

    List all teams
    """
    params = [("limit", 20),     ("offset", 0)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/teams",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_team(client: TestClient):
    """Test case for update_team

    Update an existing team
    """
    team_update = {"name":"name","description":"description"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/teams/{team_id}".format(team_id=56),
    #    headers=headers,
    #    json=team_update,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

