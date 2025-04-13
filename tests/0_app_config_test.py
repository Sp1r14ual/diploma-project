from dadata import Dadata
from app.settings import settings
from sqlalchemy import text
from sqlalchemy.orm import Session
from fast_bitrix24 import Bitrix
import requests


def test_dadata_connection():
    try:
        Dadata(settings.DADATA_TOKEN,
               settings.DADATA_SECRET), "DaData Connection Failed"
    except:
        assert False, "Cannot establish DaData connection"

    assert True


def test_db_connection():
    try:
        Session(autoflush=False, bind=settings.ENGINE)
    except:
        assert False, "Cannot create session"

    assert True


def test_bitrix_connection():
    try:
        Bitrix(settings.BITRIX_WEBHOOK)
    except:
        assert False, "Cannot establish Bitrix connection"

    assert True


def test_server_connection():
    assert requests.get(
        "http://127.0.0.1:8000/").status_code == 200, "Start page is inaccessible"
    assert requests.get(
        "http://127.0.0.1:8000/docs").status_code == 200, "Docs page is inaccessible"
    assert requests.get("http://127.0.0.1:8000/random").status_code == 404
