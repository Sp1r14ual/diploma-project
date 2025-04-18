from app.bitrix.add_crm_contact import add_crm_contact
from app.bitrix.get_crm_contacts import get_crm_contacts
from app.schemas.contact_schema import ContactSchema
from fastapi import APIRouter

router = APIRouter(
    prefix="/bitrix/contact",
    tags=["Bitrix_CRM_Contact"]
)

# Сделать post с передачей параметров


@router.post("/create")
async def bitrix_create_contact(ContactSchema: ContactSchema):
    params = {
        "LAST_NAME": ContactSchema.family_name,
        "NAME": ContactSchema.name,
        "SECOND_NAME": ContactSchema.patronimic_name,
        "BIRTHDATE": ContactSchema.birthdate,
        "EMAIL": ContactSchema.email,
        "PHONE": ContactSchema.phone_number,
        "ADDRESS": ContactSchema.reg_adress
    }

    add_crm_contact(params=params)
    return "OK"

# сделать фильтрацию по параметрам через post метод


@router.post("/get")
async def bitrix_get_contacts(ContactSchema: ContactSchema):
    received = {
        "LAST_NAME": ContactSchema.family_name,
        "NAME": ContactSchema.name,
        "SECOND_NAME": ContactSchema.patronimic_name,
        "BIRTHDATE": ContactSchema.birthdate,
        "EMAIL": ContactSchema.email,
        "PHONE": ContactSchema.phone_number,
        "ADDRESS": ContactSchema.reg_adress
    }

    params = {k: v for k, v in received.items() if v is not None}

    return await get_crm_contacts(filter_params=params)
