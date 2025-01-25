# coding: utf-8
from http.client import HTTPException

from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session

from openapi_server.apis.document_api_base import BaseDocumentApi
from openapi_server.database import engine, SessionDep
from openapi_server.models.document import Document
from typing import List, Annotated


class DocumentImpl(BaseDocumentApi):

    async def documents_get(self, session: SessionDep) -> List[Document]:
        return session.exec(select(Document).offset(100).limit(100)).all()

    async def documents_id_delete(self, document_id: str, session: SessionDep) -> None:
        document = session.query(Document).filter(Document.id == document_id).first()
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
        session.delete(document)
        session.commit()

    async def documents_id_get(self, document_id: str, session: SessionDep) -> Document:
        # Retrieve a document by ID
        document = session.query(Document).filter(Document.id == document_id).first()
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
        return document

    async def documents_id_put(self, document_id: str, document: Document,
                               session: SessionDep) -> Document:
        # Update a document by ID
        existing_document = session.query(Document).filter(Document.id == document_id).first()
        if not existing_document:
            raise HTTPException(status_code=404, detail="Document not found")

        # Update fields
        for key, value in document.dict().items():
            setattr(existing_document, key, value)

        session.add(existing_document)
        session.commit()
        session.refresh(existing_document)  # Refresh to get the updated object
        return existing_document

    async def documents_post(self, document: Document, session: SessionDep) -> Document:
        # Create a new document
        session.add(document)
        session.commit()
        session.refresh(document)  # Refresh to get the persisted object
        return document
