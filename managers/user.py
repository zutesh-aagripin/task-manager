from asyncpg import UniqueViolationError
from fastapi import HTTPException
from passlib.context import CryptContext

from db import database
from managers.auth import AuthManager
from models.user import user
from schemas.response.user import UserOut

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserManager:
    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data["password"])
        try:
            id_ = await database.execute(user.insert().values(**user_data))
        except UniqueViolationError as e:
            raise HTTPException(400, "This username already exists")
        return id_

    @staticmethod
    async def login(user_data):
        user_exists = await database.fetch_one(
            user.select().where(user.c.username == user_data["username"])
        )
        if not user_exists:
            raise HTTPException(400, "Wrong username")
        elif not pwd_context.verify(user_data["password"], user_exists["password"]):
            raise HTTPException(401, "Wrong password")
        return AuthManager.encode_token(user_exists)

    @staticmethod
    async def get_user_profile(user_id):
        return await database.fetch_one(user.select().where(user.c.id == user_id))

