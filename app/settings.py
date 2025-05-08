from typing import ClassVar
from sqlalchemy import create_engine, Engine
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import secrets
import os
from fast_bitrix24 import Bitrix
from fastapi_jwt_auth import AuthJWT
from datetime import timedelta


BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'), override=True)

class SecuritySettings(BaseSettings):
    authjwt_secret_key: str = os.getenv("JWT_SECRET_KEY") or str(
        secrets.SystemRandom().getrandbits(128))
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_secure: bool = True
    authjwt_cookie_csrf_protect: bool = False
    # authjwt_cookie_samesite: str = 'lax'

    access_token_expire_time: timedelta = timedelta(hours=1)
    refresh_token_expire_time: timedelta = timedelta(days=1)

class Settings(BaseSettings):
    # HOST: str = os.getenv("HOST") or "0.0.0.0"
    # PORT: int = os.getenv("PORT") or 5000

    # DEBUG: bool = False if not os.getenv("FLASK_DEBUG") else True    

    DADATA_TOKEN: str = os.getenv("DADATA_TOKEN") or ""
    DADATA_SECRET: str = os.getenv("DADATA_SECRET") or ""

    DB_ENGINE_STRING: str = os.getenv("DB_ENGINE_STRING") or ""

    ENGINE: ClassVar[Engine] = create_engine(DB_ENGINE_STRING, echo=True)

    BITRIX_WEBHOOK: str = os.getenv("BITRIX_WEBHOOK") or ""

    BITRIX: ClassVar[Bitrix] = Bitrix(BITRIX_WEBHOOK)

    GETGEO_API_KEY: str = os.getenv("GETGEO_API_KEY") or ""

    iblockID: int = 15

    ENABLE_SECURITY: bool = True

@AuthJWT.load_config
def get_config():
    return SecuritySettings()

settings = Settings()
security_settings = SecuritySettings()