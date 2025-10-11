from sqlmodel import create_engine, SQLModel, Session
from src.app.main.model import User, TodoList, Task
class DatabaseConfig():
    def __init__(self, database_name:str, database_password:str):
        
        self.database_name = database_name
        self.database_password = database_password
        self.database_url = f"postgresql+psycopg2://postgres:{self.database_password}@postgres:5432/{self.database_name}"
        
        self.engine = create_engine(self.database_url)
    
    def create_all_tables(self):
        print("Creating database..")
        SQLModel.metadata.create_all(self.engine)
    
    def get_session(self):
        with Session(self.engine) as session:
            return session