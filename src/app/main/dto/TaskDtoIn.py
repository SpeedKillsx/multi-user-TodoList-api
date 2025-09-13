from sqlmodel import SQLModel

class TaskDtoIn(SQLModel):
    description:str
    is_done:bool
    id_todo_list: int