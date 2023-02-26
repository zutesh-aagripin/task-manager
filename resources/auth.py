from fastapi import APIRouter

from managers.user import UserManager
from schemas.request.user import UserRegisterIn
from schemas.base import UserBase

router = APIRouter(tags=["Auth"])

@router.post(
    "/user/sign-up",
    status_code=201
)
async def register(user_data: UserRegisterIn):
    """
    User registration Returns user id
    """
    user_id = await UserManager.register(user_data.dict())
    return {"id": user_id}


@router.post(
    "/user/token"
)
async def login(user_data: UserBase):
    """
    User logging in using JWT. Returns token
    with 120 minutes duration.
    """
    token = await UserManager.login(user_data.dict())
    return {"access_token": token}
