# coding: utf-8

"""
    AutoGen Framework API

    API for managing agents, teams, and tasks in an AutoGen system.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class Task(SQLModel, table=True):
    task_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    status: Optional[str] = Field(default="pending", nullable=True)
    assigned_team_id: Optional[int] = Field(default=None, foreign_key="team.team_id")
    priority: Optional[str] = Field(default="low", nullable=True)
    created_at: Optional[datetime] = None
