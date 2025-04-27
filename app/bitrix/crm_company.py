from app.settings import settings


# async def get_crm_company_fields():
#     return await settings.BITRIX.call('crm.company.fields', {})

def get_crm_company(id: int = 1):
    return settings.BITRIX.call('crm.company.get', {"ID": id})


def list_crm_companies(
        select_params=["ID", "TITLE"],
        filter_params={}):
    return settings.BITRIX.call('crm.company.list',
                                {'select': select_params,
                                 'filter': filter_params})


def add_crm_company(params: dict = {"TITLE": "ИП Тестов", "COMPANY_TYPE": "CUSTOMER", "CURRENCY_ID": "RUB", "REVENUE": 3000000}):
    settings.BITRIX.call('crm.company.add', {"fields": params})


def update_crm_company(id: int = 1, params={"CURRENCY_ID": "USD", "REVENUE": 50000}):
    settings.BITRIX.call('crm.company.update', {"id": id, "fields": params})


def delete_crm_company(id: int = 1):
    settings.BITRIX.call('crm.company.delete', {"id": id})
