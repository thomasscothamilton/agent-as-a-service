# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.document_api_base import BaseDocumentApi
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
from pydantic import StrictStr
from typing import Any, List
from openapi_server.models.document import Document


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/documents",
    responses={
        200: {"model": List[Document], "description": "A list of documents"},
    },
    tags=["document"],
    summary="Get all documents",
    response_model_by_alias=True,
)
async def documents_get(
        session: SessionDep
) -> List[Document]:
    if not BaseDocumentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentApi.subclasses[0]().documents_get(session)


@router.delete(
    "/documents/{document_id}",
    responses={
        204: {"description": "Document deleted"},
        404: {"description": "Document not found"},
    },
    tags=["document"],
    summary="Delete a document by ID",
    response_model_by_alias=True,
)
async def documents_id_delete(
    session: SessionDep,
    document_id: StrictStr = Path(..., description=""),
) -> None:
    if not BaseDocumentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentApi.subclasses[0]().documents_id_delete(session, document_id)


@router.get(
    "/documents/{document_id}",
    responses={
        200: {"model": Document, "description": "A single document"},
        404: {"description": "Document not found"},
    },
    tags=["document"],
    summary="Get a document by ID",
    response_model_by_alias=True,
)
async def documents_id_get(
    session: SessionDep,
    document_id: StrictStr = Path(..., description=""),
) -> Document:
    if not BaseDocumentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentApi.subclasses[0]().documents_id_get(session, document_id)


@router.put(
    "/documents/{document_id}",
    responses={
        200: {"model": Document, "description": "Document updated"},
        404: {"description": "Document not found"},
    },
    tags=["document"],
    summary="Update a document by ID",
    response_model_by_alias=True,
)
async def documents_id_put(
    session: SessionDep,
    document_id: StrictStr = Path(..., description=""),
    document: Document = Body(None, description=""),
) -> Document:
    if not BaseDocumentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentApi.subclasses[0]().documents_id_put(session, document_id, document)


@router.post(
    "/documents",
    responses={
        201: {"model": Document, "description": "Document created"},
    },
    tags=["document"],
    summary="Create a new document",
    response_model_by_alias=True,
)
async def documents_post(
    session: SessionDep,
    document: Document = Body(None, description=""),
) -> Document:
    if not BaseDocumentApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDocumentApi.subclasses[0]().documents_post(session, document)
