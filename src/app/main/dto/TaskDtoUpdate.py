from sqlmodel import SQLModel

class TaskDtoUpdate(SQLModel):
    task_id: int
    state: bool