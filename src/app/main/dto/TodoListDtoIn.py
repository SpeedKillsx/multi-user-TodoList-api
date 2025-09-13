from sqlmodel import SQLModel
from typing import Optional


class TodoListDtoIn(SQLModel):
    id_user:int
    todolist_name:str

    