from collections import deque
from datetime import datetime, timedelta
from typing import List, Optional, Dict

from fastapi import APIRouter, Depends, Request

from managers.auth import oauth2_scheme
from managers.task import TaskManager
from schemas.request.task import TaskAdd
from schemas.response.task import TaskOut

router = APIRouter(tags=["Task"])

@router.get(
    "/tasks",
    dependencies=[Depends(oauth2_scheme)],
    response_model = Dict[str, List[TaskOut]]
)
async def get_tasks(request: Request):
    """
    Outputs a json of all tasks in the database that were created by this user
    """
    user_id = request.state.user
    return {"tasks": list(await TaskManager.get_tasks(user_id))}

@router.get(
    "/tasks/{task_id}",
    dependencies=[Depends(oauth2_scheme)],
    response_model=TaskOut
)
async def get_task(request: Request, task_id: int):
    """
    outputs a specific task by id that was created by this user
    """
    user_id = request.state.user
    return await TaskManager.get_task(task_id, user_id)

@router.post(
    "/tasks",
    dependencies=[Depends(oauth2_scheme)],
    status_code=201
)
async def create_task(request: Request, task_data: TaskAdd):
    """
    Adds task to the database.
    """
    task_data.user_id = request.state.user
    return await TaskManager.create_task(task_data.dict())
