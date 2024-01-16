from typing import Optional, Union

from dotenv import load_dotenv
from pydantic import BaseSettings, EmailStr

load_dotenv()


class Settings(BaseSettings):
    app_title: str = "Кошачий благотворительный фонд (0.1.0)"
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"
    secret: str = "SECRET"
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Union[None, str] = None
    project_id: Union[None, str] = None
    private_key_id: Union[None, str] = None
    private_key: Union[None, str] = None
    client_email: Union[None, str] = None
    client_id: Union[None, str] = None
    auth_uri: Union[None, str] = None
    token_uri: Union[None, str] = None
    auth_provider_x509_cert_url: Union[None, str] = None
    client_x509_cert_url: Union[None, str] = None
    email: Union[None, str] = None

    class Config:
        env_file = ".env"


settings = Settings()
