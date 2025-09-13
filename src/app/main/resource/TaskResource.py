from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.app.main.repository.TaskRepository import TaskRepository
from src.app.main.service.TaskService import TaskService
from src.app.main.model.Task import Task
from src.app.main.dto.TaskDtoIn import TaskDtoIn
from src.app.main.dependancy.database_dependancy import get_session

class TaskResource:
    
    def __init__(self):
        self.router = APIRouter(prefix="/task")
        self.router.add_api_route("/add", self.create_task, methods=["POST"], response_model=Task)
    
    def get_router(self):
        return self.router
    
    def _get_service(self, session: Session):
        repository = TaskRepository(session)
        service = TaskService(repository)
        return service
    async def create_task(self, task_dto_in:TaskDtoIn, session:Session=Depends(get_session))->Task:
        _service = self._get_service(session=session)
        
        task = _service.add_task(task_dto_in=task_dto_in)
        return task