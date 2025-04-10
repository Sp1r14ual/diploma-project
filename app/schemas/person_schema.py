from pydantic import BaseModel


class AddPersonSchema(BaseModel):
    family_name: str
    birthdate: str | None = None
    phone_number: str | None = None
    name: str
    patronimic_name: str | None = None
    pasport_serial: str | None = None
    pasport_number: str | None = None
    pasport_date: str | None = None
    pasport_place: str | None = None
    remark: str | None = None
    dep_code: str | None = None
    reg_adress: str | None = None
    reg_region: str | None = None
    reg_raion: str | None = None
    reg_city: str | None = None
    reg_street: str | None = None
    reg_house: str | None = None
    postal_index: str | None = None
    inn: str | None = None
    ogrn: str | None = None
    snils: str | None = None
    email: str | None = None


class EditPersonSchema(BaseModel):
    client_id: int
    family_name: str
    name: str
    birthdate: str | None = None
    phone_number: str | None = None
    patronimic_name: str | None = None
    pasport_serial: str | None = None
    pasport_number: str | None = None
    pasport_date: str | None = None
    pasport_place: str | None = None
    remark: str | None = None
    dep_code: str | None = None
    reg_adress: str | None = None
    reg_region: str | None = None
    reg_raion: str | None = None
    reg_city: str | None = None
    reg_street: str | None = None
    reg_house: str | None = None
    postal_index: str | None = None
    inn: str | None = None
    ogrn: str | None = None
    snils: str | None = None
    email: str | None = None


class DeletePersonSchema(BaseModel):
    id_client: int
