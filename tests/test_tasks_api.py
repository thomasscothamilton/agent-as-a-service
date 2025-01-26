# coding: utf-8

from fastapi.testclient import TestClient


from typing import List  # noqa: F401
from openapi_server.models.task import Task  # noqa: F401


def test_create_task(client: TestClient):
    """Test case for create_task

    Create a new task
    """
    task = {"description":"description","id":"id","title":"title"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/tasks",
    #    headers=headers,
    #    json=task,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_tasks(client: TestClient):
    """Test case for get_tasks

    Get all tasks
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/tasks",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

