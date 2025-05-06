from fastapi import APIRouter, HTTPException
from app.schemas.person_validator import PersonData

router = APIRouter(
    prefix="/validate",
    tags=["Validate_Data"]
)


@router.post("/person", status_code=200)
async def db_create_person(PersonData: PersonData):
    return {
        "message": "Данные пользователя валидны",
        "user_data": PersonData.model_dump()
    }
