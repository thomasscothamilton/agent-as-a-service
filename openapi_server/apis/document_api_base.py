# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictStr
from typing import Any, List

from openapi_server.models.document import Document
from openapi_server.database import SessionDep


class BaseDocumentApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDocumentApi.subclasses = BaseDocumentApi.subclasses + (cls,)

    async def documents_get(
            self,
            session: SessionDep
    ) -> List[Document]:
        ...

    async def documents_id_delete(
            self,
            session: SessionDep,
            document_id: StrictStr,
    ) -> None:
        ...

    async def documents_id_get(
            self,
            session: SessionDep,
            document_id: StrictStr,
    ) -> Document:
        ...

    async def documents_id_put(
            self,
            session: SessionDep,
            document_id: StrictStr,
            document: Document,
    ) -> Document:
        ...

    async def documents_post(
            self,
            session: SessionDep,
            document: Document,
    ) -> Document:
        ...
