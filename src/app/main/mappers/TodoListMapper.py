from src.app.main.model.TodoList import TodoList
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoOut import TodoListDtoOut

class TodoListMapper:
    
    def to_dto_in(self, todo_list:TodoList)->TodoListDtoIn:
        mapping = {
            "description":todo_list.description,
            "is_done": todo_list.is_done,
            "id_user": todo_list.id_user,
        }
        
        return TodoListDtoIn.model_validate(mapping)
    
    def to_dto_out(self, todo_list:TodoList)->TodoListDtoOut:
        mapping = {
            "description": todo_list.description,
            "is_done": todo_list.is_done
        }
        return TodoListDtoOut.model_validate(mapping)
    
    def to_entity(self, todo_list_dto_in:TodoListDtoIn ):
        todo_list = TodoList()
        for field in ["description","is_done", "id_user"]:
            setattr(todo_list, field, getattr(todo_list_dto_in, field))
        return todo_list