from sqlmodel import SQLModel
from src.app.main.model.Task import Task

class TodoListDtoOut(SQLModel):
    _id:int
    todolist_name:str
    tasks:list[Task]

    