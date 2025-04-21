import requests
import pytest
from datetime import datetime
import time

CONTACT_ID = None
DATA_FOR_CREATE = {
    "family_name": "Дрозденко",
    "name": "Сергей",
    "patronimic_name": "Леонидович",
    "birthdate": "04.07.2001"
    # "phone_number": "88005553535"
}
DATA_FOR_UPDATE = {
    "family_name": "Панасенко",
    "name": "Сергей",
    "patronimic_name": "Дмитриевич",
    "birthdate": "20.01.2001"
    # "phone_number": "89137776655"
}
URL = 'http://127.0.0.1:8000/bitrix/contact'


def test_create_contact():

    response = requests.post(URL + '/create', json=DATA_FOR_CREATE)

    assert response.status_code == 201

    time.sleep(2)


def test_find_contact():
    global CONTACT_ID

    response = requests.post(URL + '/get', json=DATA_FOR_CREATE)

    assert response.status_code == 200
    assert response.json() != [], "Contact not found"

    CONTACT_ID = int(response.json()[0]["ID"])


def test_update_contact():
    response = requests.put(
        URL + '/update', json={**DATA_FOR_UPDATE, "id": CONTACT_ID})

    assert response.status_code == 200
    assert response.json() == "OK"

    time.sleep(2)

    response = requests.post(URL + '/get', json=DATA_FOR_UPDATE)

    assert response.status_code == 200

    updated_data = {
        "family_name": response.json()[0]["LAST_NAME"],
        "name": response.json()[0]["NAME"],
        "patronimic_name": response.json()[0]["SECOND_NAME"],
        "birthdate": datetime.fromisoformat(response.json()[0]["BIRTHDATE"]).date().strftime('%d.%m.%Y')
        # танцы с бубнами
    }

    assert updated_data == DATA_FOR_UPDATE


def test_delete_contact():
    response = requests.delete(URL + '/delete', json={"id": CONTACT_ID})

    assert response.status_code == 200
    assert response.json() == "OK"

    time.sleep(2)

    response = requests.post(URL + '/get', json=DATA_FOR_UPDATE)

    assert response.status_code == 200
    assert not response.json()
