from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from app.schemas.person_validator import PersonData
from app.schemas.organization_validator import OrganizationData
from app.settings import settings

router = APIRouter(
    prefix="/validate",
    tags=["Validate_Data"]
)


@router.post("/person", status_code=200)
async def validate_person(PersonData: PersonData, Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    return {
        "message": "Данные физ.лица валидны",
        "user_data": PersonData.model_dump()
    }


@router.post("/organization", status_code=200)
async def validate_organization(OrganizationData: OrganizationData, Authorize: AuthJWT = Depends()):
    if settings.ENABLE_SECURITY:
        Authorize.jwt_required()

    return {
        "message": "Данные юр.лица валидны",
        "user_data": OrganizationData.model_dump()
    }
