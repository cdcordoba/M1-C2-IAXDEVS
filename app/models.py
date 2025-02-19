from pydantic import BaseModel, Field
from typing import Optional, List

class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    completed: bool = Field(default=False)


class UpdateTaskModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskList(BaseModel):
    tasks: List[Task]
