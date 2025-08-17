from src.app.main.repository.UserRepository import UserRepository
from src.app.main.model.User import User
from src.app.main.dto.UserDtoIn import UserDtoIn
from src.app.main.dto.UserDtoOut import UserDtoOut
from src.app.main.mappers.UserMapper import UserMapper
class UserService:
    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository
        self.user_mapper = UserMapper()
    
    def get_user(self, id:int)-> UserDtoOut:
        print("Looking for user in the database")
        user = self.user_repository.get_user(id)

        if user is None:
            user_none:User = User(
            id=-1,
            name="None",
            surname="None",
            email="None",
            phone_number="None",
            address="None"
        )
            return self.user_mapper.to_Dto_Out(user_none)
        user_dto_out = UserDtoOut(
            id=user.id,
            name=user.name,
            surname=user.surname,
            email=user.email,
            address=user.address,
            phone_number=user.phone_number
        )
        return user_dto_out
    
    def addUser(self, user:UserDtoIn)->UserDtoOut:
        user:User = self.user_repository.add_user(user)
        user_dto_out = self.user_mapper.to_Dto_Out(user)
        return user_dto_out