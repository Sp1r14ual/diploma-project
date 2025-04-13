from pydantic import BaseModel


class AddHouseSchemaForPerson(BaseModel):
    adress: str
    cadastr_number: str
    id_client: int
    is_actual: int


class AddHouseSchemaForOrganization(BaseModel):
    adress: str
    cadastr_number: str
    id_organization: int
    is_actual: int


class EditHouseSchemaForPerson(BaseModel):
    id_house: int
    adress: str
    cadastr_number: str
    id_client: int
    is_actual: int


class EditHouseSchemaForOrganization(BaseModel):
    id_house: int
    adress: str
    cadastr_number: str
    id_organization: int
    is_actual: int


class DeleteHouseSchema(BaseModel):
    id_house: int


class GetAllHousesSchemaForPerson(BaseModel):
    id_client: int


class GetAllHousesSchemaForOrganization(BaseModel):
    id_organization: int
