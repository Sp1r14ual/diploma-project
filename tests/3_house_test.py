import requests
import json
import pytest
from app.settings import settings

URL = 'http://127.0.0.1:8000/db/house'
ITEM_ID = None

IS_ACTIVE = False


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_insert_in_house_for_person():
    global ITEM_ID

    data_to_send = {'adress': '640978, Новосибирск, ул. Ватутина 12а к67 кв 87',
                    'cadastr_number': '123123123', 'id_client': 46831, 'is_actual': 0}

    response = requests.post(URL + '/insert/for_person', json=data_to_send)

    response_json = response.json()

    assert response.status_code == 201, response_json

    ITEM_ID = response_json["id_house"]

    assert response_json["id_house"] is not None


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_update_in_house_for_person():
    data_to_send = {'id_house': ITEM_ID, 'adress': '640978, Новосибирск, ул. Ватутина 12б к69 кв 88',
                    'cadastr_number': '123223223', 'id_client': 46831, 'is_actual': 1}

    response = requests.put(URL + '/update/for_person', json=data_to_send)

    assert response.status_code == 200, response.json()


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_delete_from_house_for_person():
    data_to_send = {'id_house': ITEM_ID}

    response = requests.delete(URL + '/delete', json=data_to_send)

    assert response.status_code == 200, response.json()


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_insert_in_house_for_organization():
    global ITEM_ID

    data_to_send = {'adress': '640978, Новосибирск, ул. Ватутина 12а к67 кв 87',
                    'cadastr_number': '123123123', 'id_organization': 3826, 'is_actual': 0}

    response = requests.post(
        URL + '/insert/for_organization', json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_house"]

    assert response_json["id_house"] is not None
    assert response.status_code == 201, response_json


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_update_in_house_for_organization():
    data_to_send = {'id_house': ITEM_ID, 'adress': '640978, Новосибирск, ул. Ватутина 12б к69 кв 88',
                    'cadastr_number': '123223223', 'id_organization': 3826, 'is_actual': 1}

    response = requests.put(
        URL + '/update/for_organization', json=data_to_send)

    assert response.status_code == 200, response.json()


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_delete_from_house_for_organization():
    data_to_send = {'id_house': ITEM_ID}

    response = requests.delete(URL + '/delete', json=data_to_send)

    assert response.status_code == 200, response.json()
