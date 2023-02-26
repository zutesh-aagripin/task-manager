from fastapi import HTTPException

from asyncpg import UniqueViolationError
from sqlalchemy import and_, func, select

from db import database
from models import task


class TaskManager:
    @staticmethod
    async def get_tasks(user_id):
        query = task.select().where(task.c.user_id == user_id)
        return await database.fetch_all(query)

    @staticmethod
    async def get_task(task_id, user_id):
        print(f"task_id is {task_id} and user_id is {user_id}")
        query = task.select().where(task.c.id == task_id and task.c.user_id == user_id)
        task_exists = await database.fetch_one(query)
        if not task_exists:
            raise HTTPException(400, "no such task")
        return task_exists

    @staticmethod
    async def create_task(task_data):
        try:
            task_id = await database.execute(task.insert().values(**task_data))
        except UniqueViolationError as e:
            raise HTTPException(400, "This task_name already exists")
        return {"id": task_id}



