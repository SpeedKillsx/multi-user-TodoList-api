from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.app.main.resource.UserResource import UserResource
from src.app.main.resource.TodoListResource import TodoListResource
from src.app.main.dependancy.database_dependancy import database_config, get_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    database_config.create_all_tables()
    yield

app = FastAPI(lifespan=lifespan)
user_resource = UserResource()
todoList_resource = TodoListResource()

app.include_router(user_resource.get_router())
app.include_router(todoList_resource.get_router())