import requests
import pytest
from app.settings import settings


VALID_DATA = {
    "name": "ООО Стилвуд",
    "adress_jur": "г Новосибирск, ул. Полякова, д 14",
    "adress_fact": "г Новосибирск, ул. Полякова, д 14",
    "remark": "Дополнительная информация",
    "inn": "7707083893",
    "kpp": "773601001",
    "bik": "044525225",
    "korr_acc": "30101810400000000225",
    "calc_acc": "40702810000000012345",
    "bank": "ПАО 'Сбербанк'",
    "ogrn": "1027700132195"
}

INVALID_DATA = {
    "name": "ООО НЕСУЩЕСТВУЕТ",
    "adress_jur": "г Готем, ул. Рандомная, д 99999",
    "adress_fact": "г Готем, ул. Рандомная, д 99999",
    "remark": "Дополнительная информация",
    "inn": "7707083888",
    "kpp": "773601111",
    "bik": "888525225",
    "korr_acc": "12301810400000000225",
    "calc_acc": "32102810000000012345",
    "bank": "ПАО 'Сбербанк'",
    "ogrn": "1234700132195"
}

URL = 'http://127.0.0.1:8000/validate'

IS_ACTIVE = False


@pytest.mark.skipif(not (IS_ACTIVE and settings.GETGEO_API_KEY), reason="prevent using getgeo api")
def test_valid_person():
    response = requests.post(URL + '/organization', json=VALID_DATA)

    assert response.status_code == 200
    assert "Данные юр.лица валидны" in response.json().values()


@pytest.mark.skipif(not (IS_ACTIVE and settings.GETGEO_API_KEY), reason="prevent using getgeo api")
def test_invalid_person():
    response = requests.post(URL + '/organization', json=INVALID_DATA)

    assert response.status_code == 422
