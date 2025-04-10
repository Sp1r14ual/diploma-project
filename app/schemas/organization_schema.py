from pydantic import BaseModel


class AddOrganizationSchema(BaseModel):
    name: str
    adress_jur: str
    adress_fact: str
    remark: str
    inn: str
    kpp: str
    from_1c: int
    bik: str | None = None
    korr_acc: str | None = None
    calc_acc: str | None = None
    bank: str | None = None
    ogrn: str | None = None


class EditOrganizationSchema(BaseModel):
    organization_id: int
    name: str
    from_1c: int
    zip_code_jur: str | None = None
    zip_code_fact: str | None = None
    adress_jur: str | None = None
    adress_fact: str | None = None
    remark: str | None = None
    inn: str | None = None
    kpp: str | None = None
    bik: str | None = None
    korr_acc: str | None = None
    calc_acc: str | None = None
    bank: str | None = None
    ogrn: str | None = None


class DeleteOrganizationSchema(BaseModel):
    id_organization: int
