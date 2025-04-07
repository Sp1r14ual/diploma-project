from app.bitrix.add_crm_contact import add_crm_contact
from app.bitrix.get_crm_contacts import get_crm_contacts
from fastapi import APIRouter

router = APIRouter(
    prefix="/bitrix/contact"
)

# Сделать post с передачей параметров


@router.get("/create")
async def bitrix_create_contact():
    add_crm_contact()
    return "OK"

# сделать фильтрацию по параметрам через post метод


@router.get("/get")
async def bitrix_get_contacts():
    return await get_crm_contacts()
