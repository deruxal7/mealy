from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    app_name: str = Field(..., description="Name of the application")
    fastapi_env: str = Field(..., description="Environment for FastAPI application")
    log_level: str = Field(..., description="Logging level for the application")
    db_url: PostgresDsn = Field(..., description="Database connection URL")
    api_base_url: str = Field(..., description="Base URL for the API endpoints")
    secret_key: str = Field(..., description="Secret key for the application")

    class Config:
        env_file = ".env"

settings = Settings()
