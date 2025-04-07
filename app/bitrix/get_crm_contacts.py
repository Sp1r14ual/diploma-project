from app.settings import settings


def get_crm_contacts(select_params: list = ["*"], filter_params: dict = {}) -> list[str]:
    """
    Получение контактов методом list
    params: список полей, которые надо достать
    """
    return settings.BITRIX.get_all('crm.contact.list', {'select': select_params, 'filter': filter_params})
