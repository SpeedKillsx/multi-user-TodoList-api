from sqlmodel import SQLModel
class TodoListDtoOut(SQLModel):
    description:str = None
    is_done:bool=False

    