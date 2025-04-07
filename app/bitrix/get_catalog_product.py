from app.settings import settings


def get_catalog_product_by_id(params: dict = {"id": 5}):
    """
    Получить товар по id
    params: список полей, которые надо достать
    """
    return settings.BITRIX.get_all('catalog.product.get', params)
