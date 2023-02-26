from schemas.base import UserBase
from pydantic import BaseModel
class UserOut(UserBase):
    id: int
    first_name: str
    last_name: str