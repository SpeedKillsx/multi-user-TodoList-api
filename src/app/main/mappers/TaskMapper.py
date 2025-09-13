from src.app.main.model.Task import Task
from src.app.main.dto.TaskDtoIn import TaskDtoIn

class TaskMapper:
    def to_entity(self, task_dto_in:TaskDtoIn):
        task = Task()
        for field in ["is_done", "description", "id_todo_list"]:
            setattr(task, field, getattr(task_dto_in, field))
        
        return task
    
    