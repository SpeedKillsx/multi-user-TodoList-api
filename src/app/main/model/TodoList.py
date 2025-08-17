from sqlmodel import SQLModel, Field

class TodoList(SQLModel, table=True):
    id:int|None = Field(default=None, primary_key=True, unique=True)
    id_user:int = Field(foreign_key="user.id", default=None)