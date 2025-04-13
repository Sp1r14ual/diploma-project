from app.db.person.person_insert import insert_in_Person
from app.db.person.person_update import update_in_Person
from app.db.person.person_delete import delete_from_Person
from app.db.person.get_all_people import select_all_from_person
from app.schemas.person_schema import AddPersonSchema, EditPersonSchema, DeletePersonSchema
from fastapi import APIRouter, HTTPException
from app.logger import logger


router = APIRouter(
    prefix="/db/person",
    tags=["DB_Person"]
)


@router.post("/insert", status_code=201)
async def db_create_person(AddPersonSchema: AddPersonSchema):

    id = insert_in_Person(**AddPersonSchema.dict())

    logger.info(f"Insert in Person: Success; ID: {id}")

    return {'id_client': id, "Result": "Created"}


@router.put("/update", status_code=200)
async def db_update_person(EditPersonSchema: EditPersonSchema):
    result = update_in_Person(**EditPersonSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Update In Person: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Update in Person: Success")

    return {"Result": "Updated"}


@router.delete("/delete", status_code=200)
async def db_delete_person(DeletePersonSchema: DeletePersonSchema):
    result = delete_from_Person(**DeletePersonSchema.dict())
    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Delete From Person: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Delete From Person: Success")

    return {"Result": "Deleted"}


@router.get("/get_all_people", status_code=200)
async def db_get_all_people():
    result = select_all_from_person()

    if isinstance(result, str) and result.startswith("Error"):
        logger.error(f"Select From Person: {result}")
        raise HTTPException(status_code=400, detail=result)

    logger.info(f"Select From Person: Success")

    return result
