from fastapi import FastAPI
from src.app.main.resource.UserResource import UserResource
from src.app.main.dependancy.database_dependancy import database_config, get_session
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    database_config.create_all_tables()
    yield

app = FastAPI(lifespan=lifespan)
user_resource = UserResource()
app.include_router(user_resource.get_router())