from sqlmodel import SQLModel

class UserLogInDtouOut(SQLModel):
    email: str
    access_token:str
    type_token:str