from src.app.main.model.User import User
from src.app.main.dto.UserDtoIn import UserDtoIn
from sqlmodel import select, delete, Session, exists, and_
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
    def _get_session(self):
        return self.db_session
    def get_user_by_email(self, email:str)->User:
        statement = select(User).where(User.email == email)
        result = self.db_session.exec(statement).first()
        return result
        
    def add_user(self, user:User)->User:
        print("Adding user...")
        self.db_session.add(user)
        self.db_session.commit()
        self.db_session.refresh(user)
        return user
    
    def find_user_by_credentials(self, user:User)->User:
        statement = select(User).where(
            and_(
                User.email == user.email,
                User.password == user.password
            )
        )
        
        user:User = self.db_session.exec(statement=statement).first()
        
        return user
    
    def find_todolist_by_userId(self, id:int):
        pass