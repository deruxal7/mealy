from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    VERSION: str = Field("0.01")
    RELOAD: bool = True
    API_BASE_URL: str
    DB_URL: PostgresDsn

    class Config:
        env_file = ".env"

settings = Settings()
