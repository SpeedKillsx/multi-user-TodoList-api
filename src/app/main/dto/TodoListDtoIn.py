from sqlmodel import SQLModel
from typing import Optional, List
from src.app.main.dto.TaskDtoIn import TaskDtoIn
from datetime import date
class TodoListDtoIn(SQLModel):
    id_user:int
    todolist_name:str
    creation_date:date


    