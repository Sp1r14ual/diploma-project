from pydantic import BaseModel


class ContactSchema(BaseModel):
    family_name: str
    name: str
    patronimic_name: str
    birthdate: str | None = None
    phone_number: str
    email: str | None = None
    pasport_serial: str | None = None
    pasport_number: str | None = None
    pasport_date: str | None = None
    pasport_place: str | None = None
    remark: str | None = None
    dep_code: str | None = None
    reg_adress: str | None = None
    inn: str | None = None
    ogrn: str | None = None
    snils: str | None = None
