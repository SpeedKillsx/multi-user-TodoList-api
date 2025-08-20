from sqlmodel import SQLModel
from typing import Optional


class TodoListDtoIn(SQLModel):
    description:Optional[str] = None
    is_done:bool=False
    id_user:int

    