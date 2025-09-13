from src.app.main.model.TodoList import TodoList
from src.app.main.dto.TodoListDtoIn import TodoListDtoIn
from src.app.main.dto.TodoListDtoOut import TodoListDtoOut

class TodoListMapper:
    
    def to_dto_in(self, todo_list:TodoList)->TodoListDtoIn:
        mapping = {
            "id_user": todo_list.id_user,
            "todolist_name": todo_list.todolist_name
        }
        
        return TodoListDtoIn.model_validate(mapping)
    
    def to_dto_out(self, todo_list:TodoList)->TodoListDtoOut:
        mapping = {
            "todolist_name": todo_list.todolist_name,
            "tasks": todo_list.tasks
        }
        return TodoListDtoOut.model_validate(mapping)
    
    def to_entity(self, todo_list_dto_in:TodoListDtoIn ):
        todo_list = TodoList()
        for field in ["todolist_name", "id_user"]:
            setattr(todo_list, field, getattr(todo_list_dto_in, field))
        return todo_list