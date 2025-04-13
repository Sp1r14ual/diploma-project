import requests
import importlib
import pytest
from app.settings import settings
house_test_module = importlib.import_module('tests.3_house_test')

IS_ACTIVE = False


def query_house_by_id_client():
    data_to_send = {'id_client': 46831}

    return requests.post(house_test_module.URL + '/get_all_houses/for_person', json=data_to_send)


def query_house_by_id_organization():
    data_to_send = {'id_organization': 3826}

    return requests.post(house_test_module.URL + '/get_all_houses/for_organization', json=data_to_send)


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_get_all_houses_for_person():

    house_test_module.test_insert_in_house_for_person()
    response = query_house_by_id_client()

    assert response.status_code == 200
    assert house_test_module.ITEM_ID in [
        item["id"] for item in response.json()]

    house_test_module.test_delete_from_house_for_person()
    response = query_house_by_id_client()

    if response.status_code == 400:
        assert True
        return

    assert response.status_code == 200
    assert not (house_test_module.ITEM_ID in [
                item["id"] for item in response.json()])


@pytest.mark.skipif(not (IS_ACTIVE and all((settings.DADATA_TOKEN, settings.DADATA_SECRET))), reason="prevent using dadata api")
def test_get_all_houses_for_organization():
    house_test_module.test_insert_in_house_for_organization()
    response = query_house_by_id_organization()

    assert response.status_code == 200
    assert house_test_module.ITEM_ID in [
        item["id"] for item in response.json()]

    house_test_module.test_delete_from_house_for_organization()
    response = query_house_by_id_organization()

    if response.status_code == 400:
        assert True
        return

    assert response.status_code == 200
    assert not (house_test_module.ITEM_ID in [
                item["id"] for item in response.json()])
