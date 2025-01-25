# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.chat_api_base import BaseChatApi
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
from openapi_server.models.chat import Chat


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/chat",
    responses={
        200: {"model": Chat, "description": "A Chat response"},
    },
    tags=["chat"],
    summary="A chat response",
    response_model_by_alias=True,
)
async def chat(
) -> Chat:
    if not BaseChatApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseChatApi.subclasses[0]().chat()
