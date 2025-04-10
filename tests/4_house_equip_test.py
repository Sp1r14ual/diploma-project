import requests
import json

URL = 'http://127.0.0.1:8000/db/house_equip'
ITEM_ID = None
ID_HOUSE = 140029
ID_PERSON = 623
ID_ORGANIZATION = 3848


def test_insert_in_house_equip_for_person():
    global ITEM_ID

    data_to_send = {'id_client': ID_PERSON, 'id_house': ID_HOUSE, 'id_type_house_equip': 4,
                    'year_produce': 2077, 'remark': 'blablabla'}

    response = requests.post(URL + '/insert/for_person', json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_house_equip"]

    assert response_json["id_house_equip"] is not None
    assert response.status_code == 201, response_json


def test_update_in_house_equip_for_person():
    data_to_send = {'id_house_equip': ITEM_ID, 'id_house': ID_HOUSE, 'id_type_house_equip': 3,
                    'year_produce': 2069, 'remark': 'bimbimbimbambambam'}

    response = requests.put(URL + '/update', json=data_to_send)

    assert response.status_code == 200, response.json()


def test_delete_from_house_equip_for_person():
    data_to_send = {'id_house_equip': ITEM_ID, 'id_house': ID_HOUSE}

    response = requests.delete(URL + '/delete', json=data_to_send)

    assert response.status_code == 200, response.json()


def test_insert_in_house_equip_for_organization():
    global ITEM_ID

    data_to_send = {'id_organization': ID_ORGANIZATION, 'id_house': ID_HOUSE, 'id_type_house_equip': 4,
                    'year_produce': 2077, 'remark': 'blablabla'}

    response = requests.post(
        URL + '/insert/for_organization', json=data_to_send)

    response_json = response.json()
    ITEM_ID = response_json["id_house_equip"]

    assert response_json["id_house_equip"] is not None
    assert response.status_code == 201, response_json


def test_update_in_house_equip_for_organization():
    data_to_send = {'id_house_equip': ITEM_ID, 'id_house': ID_HOUSE, 'id_type_house_equip': 3,
                    'year_produce': 2069, 'remark': 'bimbimbimbambambam'}

    response = requests.put(URL + '/update', json=data_to_send)

    assert response.status_code == 200, response.json()


def test_delete_from_house_equip_for_organization():
    data_to_send = {'id_house_equip': ITEM_ID, 'id_house': ID_HOUSE}

    response = requests.delete(URL + '/delete', json=data_to_send)

    assert response.status_code == 200, response.json()
