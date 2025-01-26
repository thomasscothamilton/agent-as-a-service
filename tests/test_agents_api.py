# coding: utf-8

from fastapi.testclient import TestClient


from typing import List  # noqa: F401
from openapi_server.models.agent import Agent  # noqa: F401


def test_create_agent(client: TestClient):
    """Test case for create_agent

    Create a new agent
    """
    agent = {"system_message":"system_message","name":"name","id":"id"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/agents",
    #    headers=headers,
    #    json=agent,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_agents(client: TestClient):
    """Test case for get_agents

    Get all agents
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/agents",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

