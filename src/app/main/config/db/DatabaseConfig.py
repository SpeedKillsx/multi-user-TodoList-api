import os
from dotenv import load_dotenv

from sqlmodel import create_engine, SQLModel, Session
from src.app.main.model import User, TodoList, Task
class DatabaseConfig():
    load_dotenv()
    def __init__(self, database_name:str, database_password:str):
        
        self.database_name = database_name
        self.database_password = database_password
        self.env_db = self.get_db_env()
        self.database_url = f"postgresql+psycopg2://postgres:{self.database_password}@{self.env_db}:5432/{self.database_name}"
        self.engine = create_engine(self.database_url)
        print(f"Connecting to database with user  = {self.env_db}")
    
    def create_all_tables(self):
        print("Creating database..")
        SQLModel.metadata.create_all(self.engine)
    
    def get_session(self):
        with Session(self.engine) as session:
            return session
        
    def get_db_env(self):
        env_db = os.getenv("APP_ENV", "local")
        return "localhost" if env_db == "local" else "postgres"