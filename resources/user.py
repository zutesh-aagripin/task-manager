from typing import List, Optional

from fastapi import APIRouter, Depends, Request

from managers.auth import oauth2_scheme
from managers.user import UserManager
from schemas.response.user import UserOut

router = APIRouter(tags=["User"])

@router.get(
    "/user/profile",
    dependencies=[Depends(oauth2_scheme)],
    response_model=UserOut,
)

async def get_user(request: Request):
    """
    Outputs the profile of current user
    """
    user_data = await UserManager.get_user_profile(request.state.user)
    return user_data
