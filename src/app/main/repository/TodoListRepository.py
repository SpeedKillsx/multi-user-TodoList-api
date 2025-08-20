from src.app.main.model.TodoList import TodoList
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from sqlmodel import select, delete, Session, exists

class TodoListRepository:
    def __init__(self, session_db:Session):
        self.session_db = session_db
    
    def insert_todo(self, todo_list:TodoList)->TodoList:
        self.session_db.add(todo_list)
        self.session_db.commit()
        self.session_db.flush(todo_list)
        return todo_list