from pydantic import BaseModel


class AddHouseEquipSchemaForPerson(BaseModel):
    id_client: int
    id_house: int
    id_type_house_equip: int
    year_produce: int
    remark: str


class AddHouseEquipSchemaForOrganization(BaseModel):
    id_organization: int
    id_house: int
    id_type_house_equip: int
    year_produce: int
    remark: str


class EditHouseEquipSchema(BaseModel):
    id_house: int
    id_type_house_equip: int
    year_produce: int
    remark: str
    id_house_equip: int


class DeleteHouseEquipSchema(BaseModel):
    id_house_equip: int
    id_house: int


class GetAllHouseEquipSchema(BaseModel):
    id_house: int
