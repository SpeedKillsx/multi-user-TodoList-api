from sqlmodel import SQLModel

class UserDtoOut(SQLModel):
    id:int
    name:str
    surname:str
    email:str
    address:str
    phone_number:str