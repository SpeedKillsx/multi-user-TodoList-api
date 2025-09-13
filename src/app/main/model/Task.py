from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Task(SQLModel, table=True):
    id:int|None = Field(default=None, primary_key=True, unique=True)
    description:Optional[str] = None
    is_done: bool = Field(default=False)
    id_todo_list:int = Field(foreign_key="todolist.id", default=None)
    
    todo_list: "TodoList" = Relationship(back_populates="tasks")