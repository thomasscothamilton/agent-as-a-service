# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.tasks_api_base import BaseTasksApi
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
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.task import Task
from openapi_server.models.task_agent_assignment import TaskAgentAssignment
from openapi_server.models.task_agent_assignment_input import TaskAgentAssignmentInput
from openapi_server.models.task_input import TaskInput
from openapi_server.models.task_update import TaskUpdate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/tasks/{task_id}/agents",
    responses={
        201: {"model": TaskAgentAssignment, "description": "Agent added to task successfully"},
        404: {"description": "Task or agent not found"},
    },
    tags=["Tasks"],
    summary="Add an agent to a task (nested subresource style)",
    response_model_by_alias=True,
)
async def add_agent_to_task(
    task_id: Annotated[StrictInt, Field(description="The ID of the task")] = Path(..., description="The ID of the task"),
    task_agent_assignment_input: TaskAgentAssignmentInput = Body(None, description=""),
) -> TaskAgentAssignment:
    """An alternative approach to assigning an agent to a task using a nested subresource."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().add_agent_to_task(task_id, task_agent_assignment_input)


@router.post(
    "/tasks/{task_id}/assign-agent",
    responses={
        200: {"description": "Agent assigned to task successfully"},
        404: {"description": "Task or agent not found"},
    },
    tags=["Tasks"],
    summary="Assign an agent to a task",
    response_model_by_alias=True,
)
async def assign_agent_to_task(
    task_id: Annotated[StrictInt, Field(description="The ID of the task")] = Path(..., description="The ID of the task"),
    task_agent_assignment_input: TaskAgentAssignmentInput = Body(None, description=""),
) -> None:
    """Associates an agent with a specific task, including the agent&#39;s role in that task."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().assign_agent_to_task(task_id, task_agent_assignment_input)


@router.post(
    "/tasks",
    responses={
        201: {"model": Task, "description": "Task created successfully"},
    },
    tags=["Tasks"],
    summary="Create a new task",
    response_model_by_alias=True,
)
async def create_task(
    task_input: TaskInput = Body(None, description=""),
) -> Task:
    """Adds a new task to the system."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().create_task(task_input)


@router.delete(
    "/tasks/{task_id}",
    responses={
        204: {"description": "Task deleted successfully"},
        404: {"description": "Task not found"},
    },
    tags=["Tasks"],
    summary="Delete an existing task",
    response_model_by_alias=True,
)
async def delete_task(
    task_id: Annotated[StrictInt, Field(description="The ID of the task")] = Path(..., description="The ID of the task"),
) -> None:
    """Removes a task from the system by its ID."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().delete_task(task_id)


@router.get(
    "/tasks/{task_id}",
    responses={
        200: {"model": Task, "description": "Task details"},
        404: {"description": "Task not found"},
    },
    tags=["Tasks"],
    summary="Retrieve a specific task",
    response_model_by_alias=True,
)
async def get_task_by_id(
    task_id: Annotated[StrictInt, Field(description="The ID of the task")] = Path(..., description="The ID of the task"),
) -> Task:
    """Returns details about a particular task by its ID."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().get_task_by_id(task_id)


@router.get(
    "/tasks/{task_id}/agents",
    responses={
        200: {"model": List[TaskAgentAssignment], "description": "A list of agent assignments"},
        404: {"description": "Task not found"},
    },
    tags=["Tasks"],
    summary="List agents assigned to a specific task",
    response_model_by_alias=True,
)
async def list_agents_for_task(
    task_id: Annotated[StrictInt, Field(description="The ID of the task")] = Path(..., description="The ID of the task"),
) -> List[TaskAgentAssignment]:
    """Retrieves a list of agents (and their roles) assigned to a particular task."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().list_agents_for_task(task_id)


@router.get(
    "/tasks",
    responses={
        200: {"model": List[Task], "description": "A list of tasks"},
    },
    tags=["Tasks"],
    summary="List all tasks",
    response_model_by_alias=True,
)
async def list_tasks(
    status: Annotated[Optional[StrictStr], Field(description="Filter tasks by status.")] = Query(None, description="Filter tasks by status.", alias="status"),
    priority: Annotated[Optional[StrictStr], Field(description="Filter tasks by priority.")] = Query(None, description="Filter tasks by priority.", alias="priority"),
    limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of tasks to return.")] = Query(20, description="Maximum number of tasks to return.", alias="limit", ge=1),
    offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")] = Query(0, description="Pagination offset.", alias="offset", ge=0),
) -> List[Task]:
    """Retrieves a list of all tasks in the system."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().list_tasks(status, priority, limit, offset)


@router.delete(
    "/tasks/{task_id}/agents/{agent_id}",
    responses={
        204: {"description": "Agent removed from the task successfully"},
        404: {"description": "Task or agent not found"},
    },
    tags=["Tasks"],
    summary="Remove an agent from a task",
    response_model_by_alias=True,
)
async def remove_agent_from_task(
    task_id: Annotated[StrictInt, Field(description="The ID of the task")] = Path(..., description="The ID of the task"),
    agent_id: Annotated[StrictInt, Field(description="The ID of the agent")] = Path(..., description="The ID of the agent"),
) -> None:
    """Deletes the agent-to-task assignment for a specified task and agent."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().remove_agent_from_task(task_id, agent_id)


@router.patch(
    "/tasks/{task_id}",
    responses={
        200: {"model": Task, "description": "Task updated successfully"},
        404: {"description": "Task not found"},
    },
    tags=["Tasks"],
    summary="Update an existing task",
    response_model_by_alias=True,
)
async def update_task(
    task_id: Annotated[StrictInt, Field(description="The ID of the task")] = Path(..., description="The ID of the task"),
    task_update: TaskUpdate = Body(None, description=""),
) -> Task:
    """Allows partial updates to an existing task’s information."""
    if not BaseTasksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTasksApi.subclasses[0]().update_task(task_id, task_update)
