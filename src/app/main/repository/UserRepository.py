from src.app.main.model.User import User
from src.app.main.dto.UserDtoIn import UserDtoIn
from sqlmodel import select, delete, Session
class UserRepository():
    def __init__(self, db_session:Session):
        self.db_session = db_session
    
    def get_user(self, id:int)-> User|None:
        statement = select(User).where(User.id == id)
        user:User = self.db_session.exec(statement).first()
        if user is None:
            print(f"No User fond")
            return None
        return user
    def add_user(user:User, db_session):
        print("Adding user")
        pass