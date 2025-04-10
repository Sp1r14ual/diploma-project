from app.db.house_equip.house_equip_insert import insert_in_HouseEquip
from app.db.house_equip.house_equip_update import update_in_HouseEquip
from app.db.house_equip.house_equip_delete import delete_from_HouseEquip
from app.schemas.house_equip_schema import AddHouseEquipSchemaForPerson, AddHouseEquipSchemaForOrganization, EditHouseEquipSchema, DeleteHouseEquipSchema
from app.logger import logger
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/db/house_equip",
    tags=["DB_HouseEquip"]
)


@router.post("/insert/for_person", status_code=201)
async def db_create_house_equip_for_person(AddHouseEquipSchemaForPerson: AddHouseEquipSchemaForPerson) -> dict:
    id = insert_in_HouseEquip(**AddHouseEquipSchemaForPerson.dict())

    logger.info(f"Insert In HouseEquip: Success; ID: {id}")

    return {'id_house_equip': id, 'Result': 'Created'}


@router.post("/insert/for_organization", status_code=201)
async def db_create_house_equip_for_organization(AddHouseEquipSchemaForOrganization: AddHouseEquipSchemaForOrganization) -> dict:
    id = insert_in_HouseEquip(**AddHouseEquipSchemaForOrganization.dict())

    logger.info(f"Insert In HouseEquip: Success; ID: {id}")

    return {'id_house_equip': id, 'Result': 'Created'}


@router.put("/update", status_code=200)
async def db_update_house_equip(EditHouseEquipSchema: EditHouseEquipSchema) -> dict:
    result = update_in_HouseEquip(**EditHouseEquipSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Update In HouseEquip: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Update In HouseEquip: Success")

    return {'Result': 'Updated'}


@router.delete('/delete', status_code=200)
async def db_delete_house_equip(DeleteHouseEquipSchema: DeleteHouseEquipSchema) -> dict:
    result = delete_from_HouseEquip(**DeleteHouseEquipSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Delete From HouseEquip: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Delete From HouseEquip: Success")

    return {'Result': 'Deleted'}
