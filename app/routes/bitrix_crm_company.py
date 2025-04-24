from app.bitrix.crm_company import add_crm_company, get_crm_company, list_crm_companies, update_crm_company, delete_crm_company
from fastapi import APIRouter

router = APIRouter(
    prefix="/bitrix/company",
    tags=["Bitrix_CRM_Company"]
)

# Перевезти всё на post-методы с передачей параметров для фильтров


@router.get("/create", status_code=201)
async def bitrix_create_company():
    add_crm_company()
    return "OK"


@router.get("/get", status_code=200)
async def bitrix_get_company():
    return await get_crm_company()


@router.get("/list", status_code=200)
async def bitrix_list_companies():
    return await list_crm_companies()


@router.get("/update", status_code=201)
async def bitrix_update_company():
    update_crm_company()
    return "OK"


@router.get("/delete", status_code=200)
async def bitrix_delete_company():
    delete_crm_company()
    return "OK"


# @router.get("/get_fields", status_code=200)
# async def bitrix_get_company_fields():
#     return await get_crm_company_fields()
