from fastapi import APIRouter, HTTPException
from app.logger import logger
from dadata import Dadata
from app.settings import settings
from app.db.house.house_insert import insert_in_House
from app.db.house.house_update import update_in_House
from app.db.house.house_delete import delete_from_House
from app.db.house.get_all_houses import select_all_from_house_by_id
from app.schemas.house_schema import AddHouseSchemaForPerson, AddHouseSchemaForOrganization, EditHouseSchemaForPerson, EditHouseSchemaForOrganization, DeleteHouseSchema, GetAllHousesSchemaForPerson, GetAllHousesSchemaForOrganization

router = APIRouter(
    prefix="/db/house",
    tags=["DB_House"]
)


def check_none(data):
    non_nullable_fields = ("town", "district", "street",
                           "house_number", "postal_index")

    for field in data.keys():
        if field in non_nullable_fields and not data[field]:
            abort(400, message=f"Error: Some fields are None: {
                  [key for key in data.keys() if not data[key]]}")


@router.post("/insert/for_person", status_code=201)
async def db_create_house_for_person(AddHouseSchemaForPerson: AddHouseSchemaForPerson) -> dict:
    global parsed_data
    parsed_data = dict()

    with Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET) as dd:
        try:
            parsed_address = dd.clean(
                "address", AddHouseSchemaForPerson.dict()["adress"])
        except:
            raise HTTPException(
                status_code=403, detail="DaData is out of credits")

        parsed_data["town"] = parsed_address["city"]
        parsed_data["district"] = parsed_address["city_district"]
        parsed_data["street"] = parsed_address["street"]
        parsed_data["house_number"] = parsed_address["house"]
        parsed_data["corpus_number"] = parsed_address["block"]
        parsed_data["flat_number"] = parsed_address["flat"]
        parsed_data["postal_index"] = parsed_address["postal_code"]

    check_none(parsed_data)

    # id = insert_in_House(**data)
    result = insert_in_House(
        **dict(AddHouseSchemaForPerson.dict(), **parsed_data))

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Insert In House: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Insert In House: Success; ID: {result}")

    return {'id_house': result, 'Result': 'Created'}


@router.post("/insert/for_organization", status_code=201)
async def db_create_house_for_organization(AddHouseSchemaForOrganization: AddHouseSchemaForOrganization) -> dict:
    global parsed_data
    parsed_data = dict()

    with Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET) as dd:
        try:
            parsed_address = dd.clean(
                "address", AddHouseSchemaForOrganization.dict()["adress"])
        except:
            raise HTTPException(
                status_code=403, detail="DaData is out of credits")

        parsed_data["town"] = parsed_address["city"]
        parsed_data["district"] = parsed_address["city_district"]
        parsed_data["street"] = parsed_address["street"]
        parsed_data["house_number"] = parsed_address["house"]
        parsed_data["corpus_number"] = parsed_address["block"]
        parsed_data["flat_number"] = parsed_address["flat"]
        parsed_data["postal_index"] = parsed_address["postal_code"]

    check_none(parsed_data)

    # id = insert_in_House(**data)
    result = insert_in_House(
        **dict(AddHouseSchemaForOrganization.dict(), **parsed_data))

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Insert In House: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Insert In House: Success; ID: {result}")

    return {'id_house': result, 'Result': 'Created'}


@router.put("/update/for_person", status_code=200)
async def db_update_house_for_person(EditHouseSchemaForPerson: EditHouseSchemaForPerson) -> dict:
    global parsed_data
    parsed_data = dict()

    with Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET) as dd:
        try:
            parsed_address = dd.clean(
                "address", EditHouseSchemaForPerson.dict()["adress"])
        except:
            raise HTTPException(
                status_code=403, detail="DaData is out of credits")
        parsed_data["town"] = parsed_address["city"]
        parsed_data["district"] = parsed_address["city_district"]
        parsed_data["street"] = parsed_address["street"]
        parsed_data["house_number"] = parsed_address["house"]
        parsed_data["corpus_number"] = parsed_address["block"]
        parsed_data["flat_number"] = parsed_address["flat"]

    check_none(parsed_data)

    result = update_in_House(
        **dict(EditHouseSchemaForPerson.dict(), **parsed_data))

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Update In House: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Update In House: Success")

    return {'Result': 'Updated'}


@router.put("/update/for_organization", status_code=200)
async def db_update_house_for_organization(EditHouseSchemaForOrganization: EditHouseSchemaForOrganization) -> dict:
    global parsed_data
    parsed_data = dict()

    with Dadata(settings.DADATA_TOKEN, settings.DADATA_SECRET) as dd:
        try:
            parsed_address = dd.clean(
                "address", EditHouseSchemaForOrganization.dict()["adress"])
        except:
            raise HTTPException(
                status_code=403, detail="DaData is out of credits")

        parsed_data["town"] = parsed_address["city"]
        parsed_data["district"] = parsed_address["city_district"]
        parsed_data["street"] = parsed_address["street"]
        parsed_data["house_number"] = parsed_address["house"]
        parsed_data["corpus_number"] = parsed_address["block"]
        parsed_data["flat_number"] = parsed_address["flat"]

    check_none(parsed_data)

    result = update_in_House(
        **dict(EditHouseSchemaForOrganization.dict(), **parsed_data))

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Update In House: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Update In House: Success")

    return {'Result': 'Updated'}


@router.delete("/delete", status_code=200)
async def db_delete_house(DeleteHouseSchema: DeleteHouseSchema) -> dict:
    result = delete_from_House(**DeleteHouseSchema.dict())

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Delete From House: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Delete From House: Success")

    return {'Result': 'Deleted'}


def process_get_all_houses(data):
    result = select_all_from_house_by_id(**data)

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Select From House: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Select From House: Success")

    return result


@router.post("/get_all_houses/for_person", status_code=200)
async def db_get_all_houses_by_id_for_person(GetAllHousesSchemaForPerson: GetAllHousesSchemaForPerson):
    return process_get_all_houses(GetAllHousesSchemaForPerson.dict())


@router.post("/get_all_houses/for_organization", status_code=200)
async def db_get_all_houses_by_id_for_organization(GetAllHousesSchemaForOrganization: GetAllHousesSchemaForOrganization):
    return process_get_all_houses(GetAllHousesSchemaForOrganization.dict())
