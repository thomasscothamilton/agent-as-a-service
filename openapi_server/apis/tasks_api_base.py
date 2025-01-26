# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.task import Task
from openapi_server.models.task_agent_assignment import TaskAgentAssignment
from openapi_server.models.task_agent_assignment_input import TaskAgentAssignmentInput
from openapi_server.models.task_input import TaskInput
from openapi_server.models.task_update import TaskUpdate


class BaseTasksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTasksApi.subclasses = BaseTasksApi.subclasses + (cls,)
    async def add_agent_to_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
        task_agent_assignment_input: TaskAgentAssignmentInput,
    ) -> TaskAgentAssignment:
        """An alternative approach to assigning an agent to a task using a nested subresource."""
        ...


    async def assign_agent_to_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
        task_agent_assignment_input: TaskAgentAssignmentInput,
    ) -> None:
        """Associates an agent with a specific task, including the agent&#39;s role in that task."""
        ...


    async def create_task(
        self,
        task_input: TaskInput,
    ) -> Task:
        """Adds a new task to the system."""
        ...


    async def delete_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
    ) -> None:
        """Removes a task from the system by its ID."""
        ...


    async def get_task_by_id(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
    ) -> Task:
        """Returns details about a particular task by its ID."""
        ...


    async def list_agents_for_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
    ) -> List[TaskAgentAssignment]:
        """Retrieves a list of agents (and their roles) assigned to a particular task."""
        ...


    async def list_tasks(
        self,
        status: Annotated[Optional[StrictStr], Field(description="Filter tasks by status.")],
        priority: Annotated[Optional[StrictStr], Field(description="Filter tasks by priority.")],
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of tasks to return.")],
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")],
    ) -> List[Task]:
        """Retrieves a list of all tasks in the system."""
        ...


    async def remove_agent_from_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
        agent_id: Annotated[StrictInt, Field(description="The ID of the agent")],
    ) -> None:
        """Deletes the agent-to-task assignment for a specified task and agent."""
        ...


    async def update_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
        task_update: TaskUpdate,
    ) -> Task:
        """Allows partial updates to an existing task’s information."""
        ...
