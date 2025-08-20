from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class TodoList(SQLModel, table=True):
    id:int|None = Field(default=None, primary_key=True, unique=True)
    description:Optional[str] = None
    is_done: bool = Field(default=False)
    id_user:int = Field(foreign_key="user.id", default=None)
    
    user: "User" = Relationship(back_populates="todos")