from src.app.main.model.TodoList import TodoList
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListNames import TodoListNames
from sqlmodel import select, delete, Session, exists
import logging

logger = logging.getLogger("myapp")

class TodoListRepository:
    def __init__(self, session_db:Session):
        self.session_db = session_db
    
    def insert_todo(self, todo_list:TodoList)->TodoList:
        self.session_db.add(todo_list)
        self.session_db.commit()
        self.session_db.flush(todo_list)
        return todo_list
    
    def find_todolist_by_id(self, id_todolist:int)->TodoList:
        statement = select(TodoList).where(TodoList.id == id_todolist)
        todo:TodoList = self.session_db.exec(statement=statement).first()
        return todo
    
    def find_todolist_by_user(self, user_id:int):
        logger.info("FFF")
        statement = select(TodoList.todolist_name).where(TodoList.id_user == user_id)
        result = self.session_db.exec(statement).all()
        todos:list[TodoListNames] = [TodoListNames(todolist_name=name) for name in result]
        logger.info(f"Todos names = {todos}")
        return todos   