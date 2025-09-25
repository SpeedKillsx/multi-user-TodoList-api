from fastapi import Depends, APIRouter
from src.app.main.model.TodoList import TodoList
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoOut import TodoListDtoOut
from src.app.main.dependancy.database_dependancy import get_session
from src.app.main.service.TodoListService import TodoListService
from src.app.main.repository.TodoListRepository import TodoListRepository
from src.app.main.dto.TodoListNames import TodoListNames
from sqlmodel import Session
from typing import List
class TodoListResource:
    def __init__(self):
        self.todo_router = APIRouter(prefix="/todo")
        self.todo_router.add_api_route('/add',endpoint= self.add_todoList, methods=['POST'], response_model=TodoListDtoOut)
        self.todo_router.add_api_route('/{id}',endpoint= self.get_todolist, methods=['GET'], response_model=TodoListDtoOut)
        self.todo_router.add_api_route('/user/{user_id}',endpoint= self.get_user_todolist, methods=['GET'], response_model=List[TodoListNames])
        
        
        
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
    
    async def get_todolist(self, id:int, session:Session=Depends(get_session))->TodoListDtoOut:
        _service = self._get_service(session)
        
        return _service.find_by_id(id)
    
    async def get_user_todolist(self, user_id:int, session:Session=Depends(get_session))->List[TodoListNames]:
        print("Route hit!") 
        _service = self._get_service(session)
        
        return _service.find_user_todolist(user_id)
        