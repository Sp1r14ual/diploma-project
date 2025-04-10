from app.db.organization.organization_insert import insert_in_Organization
from app.db.organization.organization_update import update_in_Organization
from app.db.organization.organization_delete import delete_from_Organization
from app.schemas.organization_schema import AddOrganizationSchema, EditOrganizationSchema, DeleteOrganizationSchema
from app.logger import logger
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/db/organization",
    tags=["DB_Organization"]
)


@router.post("/insert", status_code=201)
async def db_create_organization(AddOrganizationSchema: AddOrganizationSchema) -> dict:
    id = insert_in_Organization(**AddOrganizationSchema.dict())

    logger.info(f"Insert in Organization: Success; ID: {id}")

    return {'id_organization': id, 'Result': 'Created'}


@router.put("/update", status_code=200)
async def db_update_organization(EditOrganizationSchema: EditOrganizationSchema) -> dict:
    result = update_in_Organization(**EditOrganizationSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Update In Organization: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Update in Organization: Success")

    return {'Result': 'Updated'}


@router.delete('/delete', status_code=200)
async def db_delete_organization(DeleteOrganizationSchema: DeleteOrganizationSchema) -> dict:
    result = delete_from_Organization(**DeleteOrganizationSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Delete From Organization: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Delete From Organization: Success")

    return {"Result": "Deleted"}
