from sqlmodel import SQLModel, Field

class TaskDtoIn(SQLModel):
    description:str
    is_done: bool=False
    id_todo_list: int