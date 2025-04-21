from app.settings import settings


def add_crm_contact(params: dict = {"LAST_NAME": "Тестов", "NAME": "Тест", "SECOND_NAME": "Тестович"}):
    settings.BITRIX.call('crm.contact.add', {"fields": params})


def get_crm_contacts(select_params: list = ["*"], filter_params: dict = {}) -> list[str]:
    """
    Получение списка контактов
    select_params: выбирать только указанные поля, по умолчанию все
    filter_params: фильтрация по значениям полей, по умолчанию без фильтров
    """
    return settings.BITRIX.get_all('crm.contact.list', {'select': select_params, 'filter': filter_params})


def update_crm_contact(id: int = 29, params: dict = {"LAST_NAME": "Тестов", "NAME": "Тест", "SECOND_NAME": "Тестович"}):
    settings.BITRIX.call('crm.contact.update', {"id": id, "fields": params})


def delete_crm_contact(id: int):
    settings.BITRIX.call('crm.contact.delete', {"id": id})
