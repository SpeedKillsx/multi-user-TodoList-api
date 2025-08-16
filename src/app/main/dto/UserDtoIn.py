from sqlmodel import SQLModel

class UserDtoIn(SQLModel):
    name:str
    surname:str
    email:str
    address:str
    phone_number:str
    password:str