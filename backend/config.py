from typing import List
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "E-Commerce Control"
    API: str = "/api"
    API_V1: str = "/api/v1"

    CORS_ORIGIN: List[str] = ["*"]

    database_name: str
    database_host: str
    database_port: int
    database_user: str
    database_password: str

    jwt_secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def get_db_url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+psycopg2",
                username=self.database_user,
                password=self.database_password,
                host=self.database_host,
                port=self.database_port,
                path=self.database_name
            )
        )


settings = Settings()
