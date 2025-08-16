from src.app.main.model.User import User
from src.app.main.dto.UserDtoIn import UserDtoIn
from sqlmodel import select, delete, Session, exists
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
    
    def add_user(self, user:UserDtoIn):
        print("Adding user...")
        statement = select(exists().where(User.email == user.email))
        result = self.db_session.exec(statement).first()
        if result:
            print("User already exists")
            return None
        
        user_to_add : User = User(
            name=user.name,
            surname=user.surname,
            email=user.email,
            address=user.address,
            phone_number = user.phone_number,
            password=user.password
        )
        
        self.db_session.add(user_to_add)
        self.db_session.commit()
        self.db_session.refresh(user_to_add)
        
        return user_to_add