from fastapi import Depends, APIRouter
from src.app.main.model.TodoList import TodoList
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoOut import TodoListDtoOut
from src.app.main.dependancy.database_dependancy import get_session
from src.app.main.service.TodoListService import TodoListService
from src.app.main.repository.TodoListRepository import TodoListRepository
from sqlmodel import Session
class TodoListResource:
    def __init__(self):
        self.todo_router = APIRouter(prefix="/todo")
        self.todo_router.add_api_route('/add',endpoint= self.add_todoList, methods=['POST'], response_model=TodoListDtoOut)
        
    def _get_service(self, session:Session):
        repository = TodoListRepository(session)
        service = TodoListService(repository)
        return service
    def get_router(self):
        return self.todo_router
    async def add_todoList(self, todoList_dto_in:TodoListDtoIn, session=Depends(get_session))->TodoListDtoOut:
        _service = self._get_service(session)
        
        todoList:TodoListDtoOut = _service.insert_todo(todoList_dto_in) 
        return todoList