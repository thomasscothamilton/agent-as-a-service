# coding: utf-8

"""
    Document Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from sqlmodel import SQLModel, Field

class Document(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field()
    content: str = Field()
