from src.app.main.repository.TodoListRepository import TodoListRepository
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoOut import TodoListDtoOut
from src.app.main.model.TodoList import TodoList
from src.app.main.mappers.TodoListMapper import TodoListMapper

class TodoListService:
    
    def __init__(self, todo_list_repository:TodoListRepository):
        self.todo_list_repository = todo_list_repository
        self.todo_list_mapper = TodoListMapper()
    def get_todo_list(self):
        pass
    
    def insert_todo(self, todolist_dto_in:TodoListDtoIn)->TodoListDtoOut:
        todolist:TodoList = self.todo_list_mapper.to_entity(todolist_dto_in)
        
        todolist_add = self.todo_list_repository.insert_todo(todolist)
        print("Todo Added")
        return self.todo_list_mapper.to_dto_out(todolist_add)

