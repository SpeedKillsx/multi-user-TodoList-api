from src.app.main.repository.UserRepository import UserRepository
from src.app.main.model.User import User
from src.app.main.dto.UserDtoIn import UserDtoIn
from src.app.main.dto.UserDtoOut import UserDtoOut
from src.app.main.mappers.UserMapper import UserMapper
from src.app.main.dto.LoginDtoIn import LoginDtoIn
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
        user_dto_out = self.user_mapper.to_Dto_Out(user)
        return user_dto_out
    
    def addUser(self, userIn:UserDtoIn)->UserDtoOut:
        
        exist:User = self.user_repository.get_user_by_email(userIn.email)
        
        if exist:
            raise Exception("L'utilisateur existe deja")
        
        user:User = self.user_mapper.to_Entity(user_dto=userIn)
        
        user_add = self.user_repository.add_user(user)
        user_dto_out = self.user_mapper.to_Dto_Out(user_add)
        
        return user_dto_out
    
    def connect_user(self, login_dto_in: LoginDtoIn)->UserDtoOut:
        user_exist:User = self.user_repository.get_user_by_email(login_dto_in.email)
        if not user_exist:
            raise Exception(f"No user found with email : {login_dto_in.email}")
        user:User = self.user_repository.find_user_by_credentials(user=user_exist)
        
        if not user:
            raise Exception("Could not connect to the application")
            
        user_dto_out:UserDtoOut = self.user_mapper.to_Dto_Out(user_entity=user)
        return user_dto_out