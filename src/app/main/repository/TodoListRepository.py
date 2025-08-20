from app.main.model.TodoList import TodoList
from sqlmodel import select, delete, Session, exists

class TodoListRepository:
    def __init__(self, session_db:Session):
        self.session_db = session_db
    
    def insert_todo(self, ):
        pass
    pass