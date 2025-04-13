import requests

PEOPLE_URL = 'http://127.0.0.1:8000/db/person/get_all_people'
ORGANIZATIONS_URL = 'http://127.0.0.1:8000/db/organization/get_all_organizations'


def test_get_all_people():
    response = requests.get(PEOPLE_URL)
    assert response.status_code == 200, response.json()
    assert response.json()


def test_get_all_organizations():
    response = requests.get(ORGANIZATIONS_URL)
    assert response.status_code == 200, response.json()
    assert response.json()
