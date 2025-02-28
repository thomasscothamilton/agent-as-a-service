# coding: utf-8

"""
    AutoGen Framework API

    API for managing agents, teams, and tasks in an AutoGen system.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from typing import Optional
from sqlmodel import SQLModel, Field


class TaskInput(SQLModel):
    name: str
    description: Optional[str] = None
    assigned_team_id: int
    priority: Optional[str] = Field(default="low", nullable=True)

