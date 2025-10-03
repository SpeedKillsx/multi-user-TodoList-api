from sqlmodel import SQLModel
from datetime import date

class TaskDtoIn(SQLModel):
    description:str
    is_done:bool
    creation_date:date
    id_todo_list: int