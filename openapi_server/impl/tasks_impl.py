from typing import List, Optional
from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated
from openapi_server.apis.tasks_api_base import BaseTasksApi
from openapi_server.models.task import Task
from openapi_server.models.task_input import TaskInput
from openapi_server.models.task_update import TaskUpdate


class TasksImpl(BaseTasksApi):
    async def create_task(
        self,
        task_input: TaskInput,
    ) -> Task:
        """Adds a new task to the system."""
        # Default fallback implementation
        return Task(id=0, title="Default Task", status="active", description="Default task description")

    async def delete_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
    ) -> None:
        """Removes a task from the system by its ID."""
        # Default fallback implementation
        print(f"Task with ID {task_id} deleted (default fallback).")

    async def get_task_by_id(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
    ) -> Task:
        """Retrieves detailed information about a task by its ID."""
        # Default fallback implementation
        return Task(id=task_id, title="Default Task", status="active", description="Default task description")

    async def list_tasks(
        self,
        status: Annotated[Optional[StrictStr], Field(description="Filter tasks by status.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Maximum number of tasks to return.")] = 20,
        offset: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="Pagination offset.")] = 0,
    ) -> List[Task]:
        """Retrieves a list of all tasks available in the system."""
        # Default fallback implementation
        return [Task(id=i, title=f"Default Task {i}", status="active", description="Default task description") for i in range(offset, offset + limit)]

    async def update_task(
        self,
        task_id: Annotated[StrictInt, Field(description="The ID of the task")],
        task_update: TaskUpdate,
    ) -> Task:
        """Allows partial updates to an existing task's information."""
        # Default fallback implementation
        return Task(id=task_id, title=task_update.title or "Updated Task", status=task_update.status or "active", description=task_update.description or "Updated task description")