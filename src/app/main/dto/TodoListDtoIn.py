from sqlmodel import SQLModel
from typing import Optional, List
from src.app.main.dto.TaskDtoIn import TaskDtoIn
class TodoListDtoIn(SQLModel):
    id_user:int
    todolist_name:str

    