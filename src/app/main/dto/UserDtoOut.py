from sqlmodel import SQLModel
from src.app.main.dto.TodoListDtoOut import TodoListDtoOut
class UserDtoOut(SQLModel):
    id:int
    name:str
    surname:str
    email:str
    address:str
    phone_number:str
    todos:list[TodoListDtoOut]