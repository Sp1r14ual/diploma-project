from app.bitrix.crm_company import add_crm_company, get_crm_company, list_crm_companies, update_crm_company, delete_crm_company
from app.bitrix.crm_requisite import add_crm_requisite, update_crm_requisite, delete_crm_requisite, get_crm_requisite, list_crm_requisite
from app.schemas.company_schema import CompanySchema, UpdateCompanySchema, DeleteCompanySchema, GetCompanySchema, ListCompanySchema
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from app.settings import settings
import time

router = APIRouter(
    prefix="/bitrix/company",
    tags=["Bitrix_CRM_Company"]
)


@router.post("/create", status_code=201)
async def bitrix_create_company(CompanySchema: CompanySchema, Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    company_params = {
        "TITLE": CompanySchema.name,
        "ADDRESS_LEGAL": CompanySchema.adress_jur,
        "ADDRESS": CompanySchema.adress_fact,
        "COMMENTS": CompanySchema.remark,
        "BANKING_DETAILS": f"{CompanySchema.bank};{CompanySchema.korr_acc};{CompanySchema.calc_acc}",
    }

    add_crm_company(params=company_params)

    time.sleep(2)

    company_awaited = None

    # С 1 раза не срабатывает, простукиваем 2 раза
    try:
        company_awaited = await list_crm_companies(filter_params={"TITLE": company_params["TITLE"]})
    finally:
        time.sleep(2)
        company_awaited = await list_crm_companies(filter_params={"TITLE": company_params["TITLE"]})

    print("COMPANY_AWAITED:", company_awaited)

    try:
        company_id = company_awaited[0]["ID"]
    except:
        company_id = company_awaited["ID"]

    requisite_params = {
        "ENTITY_TYPE_ID": 4,
        "ENTITY_ID": company_id,
        "PRESET_ID": 1,
        "NAME": f"Реквизиты {company_params["TITLE"]}",
        "RQ_INN": CompanySchema.inn,
        "RQ_KPP": CompanySchema.kpp,
        "RQ_BIN": CompanySchema.bik,
        "RQ_OGRN": CompanySchema.ogrn
    }

    add_crm_requisite(params=requisite_params)

    return "OK"


@router.post("/get", status_code=200)
async def bitrix_get_company(GetCompanySchema: GetCompanySchema, Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    company_id = GetCompanySchema.id
    company_awaited = await get_crm_company(id=company_id)
    company = company_awaited["order0000000000"]

    # time.sleep(2)

    requisite_coroutine = list_crm_requisite(
        filter_params={"ENTITY_ID": company_id})

    requisite_awaited = await requisite_coroutine

    try:
        requisite_id = requisite_awaited[0]["ID"]
    except:
        requisite_id = requisite_awaited["ID"]

    company_requisites_coroutine = get_crm_requisite(id=requisite_id)
    company_requisites_awaited = await company_requisites_coroutine

    company_requisites = company_requisites_awaited["order0000000000"]

    banking_details = company["BANKING_DETAILS"].split(";")

    return {
        "id": company_id,
        "requisite_id": requisite_id,
        "name": company["TITLE"],
        "adress_jur": company["ADDRESS_LEGAL"],
        "adress_fact": company["ADDRESS"],
        "remark": company["COMMENTS"],
        "inn": company_requisites["RQ_INN"],
        "kpp": company_requisites["RQ_KPP"],
        "bik": company_requisites["RQ_BIN"],
        "korr_acc": banking_details[1],
        "calc_acc": banking_details[2],
        "bank": banking_details[0],
        "ogrn": company_requisites["RQ_OGRN"]
    }


@router.post("/list", status_code=200)
async def bitrix_list_companies(ListCompanySchema: ListCompanySchema, Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    company_params = {
        "TITLE": ListCompanySchema.name,
        # "ADDRESS_LEGAL": CompanySchema.adress_jur,
        # "ADDRESS": CompanySchema.adress_fact,
        # "COMMENTS": CompanySchema.remark,
        # "BANKING_DETAILS": f"{CompanySchema.bank};{CompanySchema.korr_acc};{CompanySchema.calc_acc}",
    }

    return await list_crm_companies(filter_params=company_params)


@router.put("/update", status_code=200)
async def bitrix_update_company(UpdateCompanySchema: UpdateCompanySchema, Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    compamy_params = {
        "TITLE": UpdateCompanySchema.name,
        "ADDRESS_LEGAL": UpdateCompanySchema.adress_jur,
        "ADDRESS": UpdateCompanySchema.adress_fact,
        "COMMENTS": UpdateCompanySchema.remark,
        "BANKING_DETAILS": f"{UpdateCompanySchema.bank};{UpdateCompanySchema.korr_acc};{UpdateCompanySchema.calc_acc}",
    }

    requisite_params = {
        "ENTITY_TYPE_ID": 4,
        "ENTITY_ID": UpdateCompanySchema.id,
        "PRESET_ID": 1,
        "RQ_INN": UpdateCompanySchema.inn,
        "RQ_KPP": UpdateCompanySchema.kpp,
        "RQ_BIN": UpdateCompanySchema.bik,
        "RQ_OGRN": UpdateCompanySchema.ogrn
    }

    update_crm_company(id=UpdateCompanySchema.id, params=compamy_params)

    update_crm_requisite(id=UpdateCompanySchema.id, params=requisite_params)

    return "OK"


@router.delete("/delete", status_code=200)
async def bitrix_delete_company(DeleteCompanySchema: DeleteCompanySchema, Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    company_awaited = await list_crm_companies(
        filter_params={"ID": DeleteCompanySchema.id})

    company_id = None

    try:
        company_id = company_awaited[0]["ID"]
    except:
        company_id = company_awaited["ID"]

    requisite_id = list_crm_requisite(filter_params={"ENTITY_ID": company_id})

    delete_crm_requisite(id=requisite_id)
    delete_crm_company(id=company_id)
    return "OK"
