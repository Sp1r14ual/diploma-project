from app.bitrix.crm_contact import add_crm_contact, get_crm_contacts, update_crm_contact, delete_crm_contact
from app.schemas.contact_schema import ContactSchema, UpdateContactSchema, DeleteContactSchema
from fastapi import APIRouter

router = APIRouter(
    prefix="/bitrix/contact",
    tags=["Bitrix_CRM_Contact"]
)


@router.post("/create", status_code=201)
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


@router.put("/update", status_code=200)
async def bitrix_update_contact(UpdateContactSchema: UpdateContactSchema):
    params = {
        "LAST_NAME": UpdateContactSchema.family_name,
        "NAME": UpdateContactSchema.name,
        "SECOND_NAME": UpdateContactSchema.patronimic_name,
        "BIRTHDATE": UpdateContactSchema.birthdate,
        "EMAIL": UpdateContactSchema.email,
        "PHONE": UpdateContactSchema.phone_number,
        "ADDRESS": UpdateContactSchema.reg_adress
    }

    update_crm_contact(id=UpdateContactSchema.id, params=params)

    return "OK"


@router.delete("/delete", status_code=200)
async def bitrix_delete_contact(DeleteContactSchema: DeleteContactSchema):

    delete_crm_contact(id=DeleteContactSchema.id)

    return "OK"


@router.post("/get", status_code=200)
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
