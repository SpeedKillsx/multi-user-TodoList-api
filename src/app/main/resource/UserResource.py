from src.app.main.dto.UserDtoIn import UserDtoIn
from src.app.main.dto.UserDtoOut import UserDtoOut
from src.app.main.service.UserService import UserService
from src.app.main.repository.UserRepository import UserRepository
from src.app.main.dependancy.database_dependancy import get_session
from fastapi import APIRouter, Depends
from sqlmodel import Session
class UserResource:
    def __init__(self):
        self.router = APIRouter(prefix="/user")
        self.router.add_api_route("/{id}", self.get_user, methods=["GET"], response_model=UserDtoOut)
        self.router.add_api_route("/add", self.add_user, methods=["POST"], response_model=UserDtoOut)
        
    def get_router(self):
        return self.router
    
    def _get_service(self, session: Session):
        repository = UserRepository(session)
        service = UserService(repository)
        return service
    
    async def get_user(self, id:int, session:Session=Depends(get_session))->UserDtoOut:
        service = self._get_service(session)
        return service.get_user(id)
    
    async def add_user(self, user:UserDtoIn, session:Session=Depends(get_session)):
        service = self._get_service(session)
        added_user = service.addUser(user)
        return added_user
    