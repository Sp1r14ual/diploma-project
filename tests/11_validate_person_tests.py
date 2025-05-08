import requests
import pytest
from app.settings import settings

VALID_DATA = {
    "family_name": "Иванов",
    "name": "Иван",
    "patronimic_name": "Иванович",
    "phone_number": "+79161234567",
    "email": "ivan.ivanov@gmail.com",
    "inn": "0000000000",
    "birth_date": "20.01.2001",
    "ogrn": "1027700132195",
    "snils": "11223344595"
}

INVALID_DATA = {
    "family_name": "Булщитов",
    "name": "Булщит",
    "patronimic_name": "Булщитович",
    "phone_number": "999999999",
    "email": "bullshit@bullshit.com",
    "inn": "1231231231",
    "birth_date": "77.88.9999",
    "ogrn": "1027700666666",
    "snils": "11223344333"
}

URL = 'http://127.0.0.1:8000/validate'

IS_ACTIVE = False


@pytest.mark.skipif(not (IS_ACTIVE and settings.GETGEO_API_KEY), reason="prevent using getgeo api")
def test_valid_person():
    response = requests.post(URL + '/person', json=VALID_DATA)

    assert response.status_code == 200
    assert "Данные физ.лица валидны" in response.json().values()


@pytest.mark.skipif(not (IS_ACTIVE and settings.GETGEO_API_KEY), reason="prevent using getgeo api")
def test_invalid_person():
    response = requests.post(URL + '/person', json=INVALID_DATA)

    assert response.status_code == 422
