import requests
import pytest
import time
from datetime import datetime

PRODUCT_ID = None

DATA_FOR_CREATE = {
    "name": "Navien-24",
    "year_produce": 2077,
    "remark": "bimbimbim"
}


DATA_FOR_UPDATE = {
    "name": "Navien-18",
    "year_produce": 2069,
    "remark": "bambambam"
}

URL = 'http://127.0.0.1:8000/bitrix/catalog/product'


def test_create_product():

    response = requests.post(URL + '/create', json=DATA_FOR_CREATE)

    assert response.status_code == 201

    time.sleep(2)


def test_find_product():

    global PRODUCT_ID

    response = requests.post(
        URL + '/list', json=DATA_FOR_CREATE)

    assert response.status_code == 200
    assert response.json(), "Contact not found"

    PRODUCT_ID = int(response.json()[0]["id"])


def test_update_product():
    response = requests.put(
        URL + '/update', json={**DATA_FOR_UPDATE, "id": PRODUCT_ID})

    assert response.status_code == 200
    assert response.json() == "OK"

    time.sleep(2)

    response = requests.post(
        URL + '/list', json=DATA_FOR_UPDATE)

    assert response.status_code == 200

    updated_data = {
        "name": response.json()[0]["name"],
        "remark": response.json()[0]["previewText"],
        "year_produce": int(datetime.fromisoformat(response.json()[0]["dateCreate"]).date().strftime('%Y'))
        # танцы с бубнами
    }

    assert updated_data == DATA_FOR_UPDATE


def test_delete_product():
    response = requests.delete(URL + '/delete', json={"id": PRODUCT_ID})

    assert response.status_code == 200
    assert response.json() == "OK"

    time.sleep(2)

    response = requests.post(
        URL + '/list', json=DATA_FOR_UPDATE)

    assert response.status_code == 200
    assert not response.json()
