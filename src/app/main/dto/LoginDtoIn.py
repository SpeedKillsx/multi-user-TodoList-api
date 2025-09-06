from sqlmodel import SQLModel

class LoginDtoIn(SQLModel):
    email:str
    password:str