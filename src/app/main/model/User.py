from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table = True):
    id:int | None = Field(default=None, primary_key=True, unique=True)
    name:str
    surname:str
    email:str = Field(default=None, unique=True)
    address:str
    phone_number:str
    password:str
    
    todos: list["TodoList"] | None = Relationship(back_populates="user")