from datetime import datetime
from pydantic import BaseModel

class TaskOut(BaseModel):
    id: int
    title: str
    created_at: datetime
    user_id: int