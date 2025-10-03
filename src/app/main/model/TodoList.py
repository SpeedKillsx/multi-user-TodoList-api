from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date
class TodoList(SQLModel, table=True):
    id:int|None = Field(default=None, primary_key=True, unique=True)
    todolist_name : str
    creation_date: date
    id_user:int = Field(foreign_key="user.id", default=None)
    
    tasks: list['Task']| None = Relationship(back_populates="todo_list")
    user: "User" = Relationship(back_populates="todos")