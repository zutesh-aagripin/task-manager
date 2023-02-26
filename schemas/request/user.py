from schemas.base import UserBase

class UserRegisterIn(UserBase):
    first_name: str
    last_name: str