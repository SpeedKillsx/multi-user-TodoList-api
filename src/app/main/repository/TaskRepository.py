from sqlmodel import Session, select, insert
from src.app.main.model.Task import Task
from src.app.main.dto.TaskDtoIn import TaskDtoIn
class TaskRepository:
    def __init__(self, session:Session):
        self.db_session=session
    
    def insert_task(self, task:Task):
        self.db_session.add(task)
        self.db_session.commit()
        self.db_session.flush(task)
        
        return task
    