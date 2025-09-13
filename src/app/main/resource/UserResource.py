from src.app.main.dto.UserDtoIn import UserDtoIn
from src.app.main.dto.UserDtoOut import UserDtoOut
from src.app.main.dto.UserLogInDtoOut import UserLogInDtouOut
from src.app.main.dto.LoginDtoIn import LoginDtoIn
from src.app.main.service.UserService import UserService
from src.app.main.repository.UserRepository import UserRepository
from src.app.main.dependancy.database_dependancy import get_session
from fastapi import APIRouter, Depends
from fastapi import Security
from sqlmodel import Session
from src.app.main.config.auth.auth_bearer import JWTBearer
class UserResource:
    def __init__(self):
        self.router = APIRouter(prefix="/user")
        self.router.add_api_route("/", self.get_user, methods=["GET"], response_model=UserDtoOut)
        self.router.add_api_route("/add", self.add_user, methods=["POST"], response_model=UserDtoOut)
        self.router.add_api_route("/connect", self.user_connection, methods=["POST"], response_model=UserLogInDtouOut)
        
    def get_router(self):
        return self.router
    
    def _get_service(self, session: Session):
        repository = UserRepository(session)
        service = UserService(repository)
        return service
    
    async def get_user(self, session:Session=Depends(get_session), payload = Security(JWTBearer()))->UserDtoOut:
        service = self._get_service(session)
        user_id = payload['user_id']
        return service.get_user(user_id)
    
    async def add_user(self, user:UserDtoIn, session:Session=Depends(get_session))->UserDtoOut:
        service = self._get_service(session)
        added_user = service.addUser(user)
        return added_user
    
    async def user_connection(self, login_dto_in:LoginDtoIn, session:Session=Depends(get_session)):
        service = self._get_service(session=session)
        connected_user:UserLogInDtouOut = service.connect_user(login_dto_in=login_dto_in)
        return connected_user
    