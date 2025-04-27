from app.settings import settings


def add_crm_requisite(params: dict):
    settings.BITRIX.call('crm.requisite.add', {"fields": params})


def update_crm_requisite(id: int, params: dict):
    settings.BITRIX.call('crm.requisite.update', {"id": id, "fields": params})


def get_crm_requisite(id: int):
    return settings.BITRIX.call('crm.requisite.get', {"id": id})


def list_crm_requisite(select_params: list = ["ENTITY_TYPE_ID", "ENTITY_ID", "ID", "NAME"],
                       filter_params: dict = {}):
    return settings.BITRIX.call('crm.requisite.list', {
        "select": select_params, "filter":  filter_params})


def delete_crm_requisite(id: int):
    settings.BITRIX.call('crm.requisite.delete', {"id": id})
