from app.settings import settings


def get_catalog_product_by_id(params: dict = {"id": 5}):
    """
    Получить товар по id
    params: список полей, которые надо достать
    """
    return settings.BITRIX.get_all('catalog.product.get', params)


def get_catalog_product_list(select_params: list = ['id', 'iblockId', 'name'], filter_params: dict = {"iblockId": 15, 'name': 'Товар2'}):
    return settings.BITRIX.get_all('catalog.product.list', {"select": select_params, "filter": filter_params})


def get_infoblocks_list(select_params: list = ['id', 'iblockId', 'name'], filter_params: dict = {}):
    return settings.BITRIX.get_all('catalog.catalog.list', {'select': select_params, 'filter': filter_params})
