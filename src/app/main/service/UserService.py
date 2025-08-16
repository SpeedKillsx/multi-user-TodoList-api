from src.app.main.repository.UserRepository import UserRepository
from src.app.main.dto.UserDtoIn import UserDtoIn
from src.app.main.dto.UserDtoOut import UserDtoOut

class UserService:
    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository
    
    def get_user(self, id:int)-> UserDtoOut:
        print("Looking for user in the database")
        user = self.user_repository.get_user(id)

        if user is None:
            return UserDtoOut(
            id=-1,
            name="None",
            surname="None",
            email="None",
            phone_number="None",
            address="None"
        )
        user_dto_out = UserDtoOut(
            user.id,
            user.name,
            user.surname,
            user.email,
            user.address,
            user.phone_number
        )
        return user_dto_out