from fastapi import APIRouter

from resources import auth, task, user

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(user.router)
api_router.include_router(task.router)
