from sqlmodel import SQLModel

class TodoListNames(SQLModel):
    id:int
    todolist_name: str
    