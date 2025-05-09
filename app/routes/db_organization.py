from app.db.organization.organization_insert import insert_in_Organization
from app.db.organization.organization_update import update_in_Organization
from app.db.organization.organization_delete import delete_from_Organization
from app.db.organization.get_all_organizations import select_all_from_organization
from app.schemas.organization_schema import AddOrganizationSchema, EditOrganizationSchema, DeleteOrganizationSchema
from app.logger import logger
from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from app.settings import settings

router = APIRouter(
    prefix="/db/organization",
    tags=["DB_Organization"]
)


@router.post("/insert", status_code=201)
async def db_create_organization(AddOrganizationSchema: AddOrganizationSchema, Authorize: AuthJWT = Depends()) -> dict:
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    id = insert_in_Organization(**AddOrganizationSchema.dict())

    logger.info(f"Insert in Organization: Success; ID: {id}")

    return {'id_organization': id, 'Result': 'Created'}


@router.put("/update", status_code=200)
async def db_update_organization(EditOrganizationSchema: EditOrganizationSchema, Authorize: AuthJWT = Depends()) -> dict:
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    result = update_in_Organization(**EditOrganizationSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Update In Organization: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Update in Organization: Success")

    return {'Result': 'Updated'}


@router.delete('/delete', status_code=200)
async def db_delete_organization(DeleteOrganizationSchema: DeleteOrganizationSchema, Authorize: AuthJWT = Depends()) -> dict:
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    result = delete_from_Organization(**DeleteOrganizationSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Delete From Organization: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Delete From Organization: Success")

    return {"Result": "Deleted"}


@router.get('/get_all_organizations', status_code=200)
async def db_get_all_organizations(Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    result = select_all_from_organization()

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Select From Organization: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Select From Organization: Success")

    return result
