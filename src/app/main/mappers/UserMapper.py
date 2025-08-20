from src.app.main.model.User import User
from src.app.main.dto.UserDtoOut import UserDtoOut
from src.app.main.dto.UserDtoIn import UserDtoIn

class UserMapper:
    
    def to_Dto_In(self, user_entity:User)->UserDtoIn:
        data= {
        "name": user_entity.name,
        "surname": user_entity.surname,
        "email": user_entity.email,
        "address": user_entity.address,
        "phone_number": user_entity.phone_number
        }
        return UserDtoIn.model_validate(data)
    
    def to_Dto_Out(self, user_entity:User)->UserDtoOut:
        data= {
        "id": user_entity.id,
        "name": user_entity.name,
        "surname": user_entity.surname,
        "email": user_entity.email,
        "address": user_entity.address,
        "phone_number": user_entity.phone_number,
        "todos": user_entity.todos
        }
        return UserDtoOut.model_validate(data)
        
    def to_Entity(self, user_dto:UserDtoIn):
        user = User()
        for field in ["name", "surname", "email", "address", "phone_number", "password"]:
            setattr(user, field, getattr(user_dto, field))
        return user