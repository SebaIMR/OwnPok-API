from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    db_pass: str
    db_name: str
    db_user: str
    instance_connection_name: str

    class Config:
        env_file = ".env"

# Instancia de settings para usar en toda la aplicación
settings = Settings()