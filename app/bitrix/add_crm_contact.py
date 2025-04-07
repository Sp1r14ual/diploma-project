from app.settings import settings


def add_crm_contact(params: dict = {"LAST_NAME": "Евпатеев", "NAME": "Евпатий", "SECOND_NAME": "Сергеевич"}):
    res = settings.BITRIX.call('crm.contact.add', {"fields": params})
    print(res)
