from app.settings import settings


def get_catalog_product_by_id(id: int):
    return settings.BITRIX.get_all('catalog.product.get', {"id": id})


def get_catalog_product_list(select_params: list = ['id', 'iblockId', 'name', 'dateCreate', 'previewText'], filter_params: dict = {}):
    return settings.BITRIX.get_all('catalog.product.list', {"select": select_params, "filter": filter_params})


def get_infoblocks_list(select_params: list = ['id', 'iblockId', 'name', 'dateCreate', 'previewText'], filter_params: dict = {}):
    return settings.BITRIX.get_all('catalog.catalog.list', {'select': select_params, 'filter': filter_params})


def add_catalog_product(params: dict = {}):
    settings.BITRIX.call('catalog.product.add', {"fields": params})


def update_catalog_product(id: int, params: dict = {}):
    settings.BITRIX.call('catalog.product.update', {
                         "id": id, "fields": params})


def delete_catalog_product(id: int):
    settings.BITRIX.call('catalog.product.delete', {"id": id})
