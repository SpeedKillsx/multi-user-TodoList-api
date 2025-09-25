from sqlmodel import SQLModel

class TodoListNames(SQLModel):
    todolist_name: str