from pydantic import BaseModel


class CompanySchema(BaseModel):
    name: str
    adress_jur: str
    adress_fact: str
    remark: str
    inn: str
    kpp: str
    # from_1c: int | None = 0
    bik: str
    korr_acc: str
    calc_acc: str
    bank: str
    ogrn: str


class UpdateCompanySchema(CompanySchema):
    id: int


class DeleteCompanySchema(BaseModel):
    id: int


class GetCompanySchema(BaseModel):
    id: int


class ListCompanySchema(BaseModel):
    name: str
