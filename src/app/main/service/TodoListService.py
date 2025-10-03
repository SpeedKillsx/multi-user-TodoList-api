from src.app.main.repository.TodoListRepository import TodoListRepository
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoOut import TodoListDtoOut
from src.app.main.dto.TodoListNames import TodoListNames
from src.app.main.model.TodoList import TodoList
from src.app.main.mappers.TodoListMapper import TodoListMapper

class TodoListService:
    
    def __init__(self, todo_list_repository:TodoListRepository):
        self.todo_list_repository = todo_list_repository
        self.todo_list_mapper = TodoListMapper()
    
    
    def insert_todo(self, todolist_dto_in:TodoListDtoIn)->TodoListDtoOut:
        todolist:TodoList = self.todo_list_mapper.to_entity(todolist_dto_in)
        
        todolist_add = self.todo_list_repository.insert_todo(todolist)
        
        return self.todo_list_mapper.to_dto_out(todolist_add)

    def find_by_id(self, id:int)->TodoListDtoOut:
        todolist:TodoList = self.todo_list_repository.find_todolist_by_id(id)
        if todolist is None:
            return None

        return self.todo_list_mapper.to_dto_out(todolist)
    
    def find_user_todolist(self, user_id:int)->list[TodoListNames]:
        todos_names:list[TodoListNames] = self.todo_list_repository.find_todolist_by_user(user_id)
        if len(todos_names) == 0:
            return {"message":"Not found"}
        
        return todos_names
            
