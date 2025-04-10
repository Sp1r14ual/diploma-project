from app.settings import settings


def get_crm_contacts(select_params: list = ["*"], filter_params: dict = {}) -> list[str]:
    """
    Получение списка контактов
    select_params: выбирать только указанные поля, по умолчанию все
    filter_params: фильтрация по значениям полей, по умолчанию без фильтров
    """
    return settings.BITRIX.get_all('crm.contact.list', {'select': select_params, 'filter': filter_params})
