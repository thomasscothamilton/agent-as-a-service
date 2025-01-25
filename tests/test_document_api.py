# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictStr  # noqa: F401
from typing import Any, List  # noqa: F401
from openapi_server.models.document import Document  # noqa: F401


def test_documents_get(client: TestClient):
    """Test case for documents_get

    Get all documents
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/documents",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_documents_id_delete(client: TestClient):
    """Test case for documents_id_delete

    Delete a document by ID
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/documents/{document_id}".format(document_id='document_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_documents_id_get(client: TestClient):
    """Test case for documents_id_get

    Get a document by ID
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/documents/{document_id}".format(document_id='document_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_documents_id_put(client: TestClient):
    """Test case for documents_id_put

    Update a document by ID
    """
    document = {"id":"id","title":"title","content":"content"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/documents/{document_id}".format(document_id='document_id_example'),
    #    headers=headers,
    #    json=document,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_documents_post(client: TestClient):
    """Test case for documents_post

    Create a new document
    """
    document = {"id":"id","title":"title","content":"content"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/documents",
    #    headers=headers,
    #    json=document,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

