from fastapi import APIRouter, HTTPException
from app.schemas.person_validator import PersonData
from app.schemas.organization_validator import OrganizationData

router = APIRouter(
    prefix="/validate",
    tags=["Validate_Data"]
)


@router.post("/person", status_code=200)
async def validate_person(PersonData: PersonData):
    return {
        "message": "Данные физ.лица валидны",
        "user_data": PersonData.model_dump()
    }


@router.post("/organization", status_code=200)
async def validate_organization(OrganizationData: OrganizationData):
    return {
        "message": "Данные юр.лица валидны",
        "user_data": OrganizationData.model_dump()
    }
