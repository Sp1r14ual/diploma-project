from app.settings import settings


def add_crm_contact(params: dict = {"LAST_NAME": "Тестов", "NAME": "Тест", "SECOND_NAME": "Тестович"}):
    res = settings.BITRIX.call('crm.contact.add', {"fields": params})
    print(res)
