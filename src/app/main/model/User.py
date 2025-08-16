from sqlmodel import SQLModel, Field
class User(SQLModel, table = True):
    id:int | None = Field(default=None, primary_key=True, unique=True)
    name:str
    surname:str
    email:str
    address:str
    phone_number:str
    password:str