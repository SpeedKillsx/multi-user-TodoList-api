from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.app.main.resource.UserResource import UserResource
from src.app.main.resource.TodoListResource import TodoListResource
from src.app.main.dependancy.database_dependancy import database_config, get_session
from src.app.main.resource.TaskResource import TaskResource
@asynccontextmanager
async def lifespan(app: FastAPI):
    database_config.create_all_tables()
    yield

app = FastAPI(lifespan=lifespan)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user_resource = UserResource()
todoList_resource = TodoListResource()
task_resource = TaskResource()
app.include_router(user_resource.get_router())
app.include_router(todoList_resource.get_router())
app.include_router(task_resource.get_router())