from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"

# Instancia de settings para usar en toda la aplicación
settings = Settings()

# Si necesitas imprimir el valor de `database_url` para depuración
print(settings.database_url)