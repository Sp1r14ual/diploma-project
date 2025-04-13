import requests
import importlib
import pytest
from app.settings import settings
house_equip_test_module = importlib.import_module('tests.4_house_equip_test')


def query_house_equip_by_id_house():
    data_to_send = {'id_house': house_equip_test_module.ID_HOUSE}

    return requests.post(house_equip_test_module.URL + '/get_all_house_equip', json=data_to_send)


def test_get_all_house_equip_for_person():
    house_equip_test_module.test_insert_in_house_equip_for_person()
    response = query_house_equip_by_id_house()

    assert response.status_code == 200
    assert house_equip_test_module.ITEM_ID in [
        item["id"] for item in response.json()]

    house_equip_test_module.test_delete_from_house_equip_for_person()
    response = query_house_equip_by_id_house()

    if response.status_code == 400:
        assert True
        return

    assert response.status_code == 200
    assert not (house_equip_test_module.ITEM_ID in [
                item["id"] for item in response.json()])


def test_get_all_house_equip_for_organization():
    house_equip_test_module.test_insert_in_house_equip_for_organization()
    response = query_house_equip_by_id_house()

    assert response.status_code == 200
    assert house_equip_test_module.ITEM_ID in [
        item["id"] for item in response.json()]

    house_equip_test_module.test_delete_from_house_equip_for_organization()
    response = query_house_equip_by_id_house()

    if response.status_code == 400:
        assert True
        return

    assert response.status_code == 200
    assert not (house_equip_test_module.ITEM_ID in [
                item["id"] for item in response.json()])
