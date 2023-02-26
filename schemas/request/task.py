from pydantic import BaseModel

class TaskAdd(BaseModel):
    title: str
    user_id: int = None