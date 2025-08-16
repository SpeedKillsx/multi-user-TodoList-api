from src.app.main.config.db.DatabaseConfig import DatabaseConfig

database_config = DatabaseConfig('TODO', 'postgres')

def get_session():
    yield database_config.get_session()