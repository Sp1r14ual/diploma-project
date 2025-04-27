import requests
import pytest
import time

COMPANY_ID = None
COMPANY_REQUISITE_ID = None

DATA_FOR_CREATE = {
    "name": "ООО Рога и Копыта",
    "adress_jur": "640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь",
    "adress_fact": "640098, Новосибирская область, г Новосибирск, Октябрьская ул, д. 42, этаж цоколь",
    "remark": "blabla",
    "inn": "4444444",
    "kpp": "5555555",
    # "from_1c": 0,
    "bik": "6666666",
    "korr_acc": "252525",
    "calc_acc": "262626",
    "bank": "Levoberezhniy",
    "ogrn": "123456789"
}

DATA_FOR_UPDATE = {
    "name": "ООО Уши и Лапы",
    "adress_jur": "640099, Омская область, г Омск, Ленинская ул, д. 45, этаж цоколь",
    "adress_fact": "640099, Омская область, г Омск, Ленинская ул, д. 45, этаж цоколь",
    "remark": "bimbimbim",
    "inn": "4564564565",
    "kpp": "345345335",
    # "from_1c": 1,
    "bik": "222333444",
    "korr_acc": "252525",
    "calc_acc": "262626",
    "bank": "Alfa Group",
    "ogrn": "2565121024"
}


URL = 'http://127.0.0.1:8000/bitrix/company'


def test_create_company():

    response = requests.post(URL + '/create', json=DATA_FOR_CREATE)

    assert response.status_code == 201

    # time.sleep(2)


def test_find_company():
    global COMPANY_ID

    response = requests.post(URL + '/list', json={"name": "ООО Рога и Копыта"})

    COMPANY_ID = int(response.json()["ID"])

    response = requests.post(URL + '/get', json={"id": COMPANY_ID})

    assert response.status_code == 200
    assert response.json(), "Company not found"

    COMPANY_ID = response.json()["id"]
    COMPANY_REQUISITE_ID = response.json()["requisite_id"]


def test_update_company():
    response = requests.put(
        URL + '/update', json={**DATA_FOR_UPDATE, "id": COMPANY_ID})

    assert response.status_code == 200
    assert response.json() == "OK"

    time.sleep(2)

    # response = requests.post(URL + '/get', json={"id": COMPANY_ID})

    # assert response.status_code == 200

    # updated_data = response.json()

    # assert updated_data == DATA_FOR_UPDATE


def test_delete_contact():
    response = requests.delete(URL + '/delete', json={"id": COMPANY_ID})

    assert response.status_code == 200
    assert response.json() == "OK"

    time.sleep(2)

    # response = requests.post(URL + '/get', json={"id": COMPANY_ID})

    # assert response.status_code == 200
    # assert not response.json()
