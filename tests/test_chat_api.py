# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.chat import Chat  # noqa: F401


def test_chat(client: TestClient):
    """Test case for chat

    A chat response
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/chat",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

