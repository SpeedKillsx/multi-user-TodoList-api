from sqlmodel import Session
from src.app.main.repository.TaskRepository import TaskRepository
from src.app.main.model.Task import Task
from src.app.main.dto.TaskDtoIn import TaskDtoIn
from src.app.main.mappers.TaskMapper import TaskMapper

class TaskService:
    def __init__(self, task_repository:TaskRepository):
        self.task_mapper = TaskMapper()
        self.task_repository  = task_repository
    def add_task(self, task_dto_in:TaskDtoIn)->Task:
        task_entity:Task = self.task_mapper.to_entity(task_dto_in)
        
        task_db = self.task_repository.insert_task(task_entity)
        
        return task_db
        