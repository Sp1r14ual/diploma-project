from typing import ClassVar
from sqlalchemy import create_engine, Engine
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
# import secrets
import os
from fast_bitrix24 import Bitrix

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'), override=True)


class Settings(BaseSettings):
    HOST: str = os.getenv("HOST") or "0.0.0.0"
    PORT: int = os.getenv("PORT") or 5000

    DEBUG: bool = False if not os.getenv("FLASK_DEBUG") else True

    # JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY") or str(
    #     secrets.SystemRandom().getrandbits(128))

    DADATA_TOKEN: str = os.getenv("DADATA_TOKEN") or ""
    DADATA_SECRET: str = os.getenv("DADATA_SECRET") or ""

    ENGINE: ClassVar[Engine] = create_engine(
        'mssql+pyodbc://DESKTOP-OE5G1EA\\SQLEXPRESS/ggs_stud?driver=SQL+Server+Native+Client+11.0', echo=True)

    BITRIX_WEBHOOK: str = os.getenv("BITRIX_WEBHOOK")

    BITRIX: ClassVar[Bitrix] = Bitrix(BITRIX_WEBHOOK)


settings = Settings()
