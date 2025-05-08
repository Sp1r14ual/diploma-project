from pydantic import BaseModel, Field, field_validator
from typing import Optional
from difflib import SequenceMatcher
import requests
from app.settings import settings
from fastapi import HTTPException


class OrganizationData(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, examples=[
        "ООО 'Ромашка'"], description="Наименование организации")
    adress_jur: str = Field(..., min_length=5, max_length=255, examples=[
                            "г. Москва, ул. Ленина, д. 1"], description="Юридический адрес")
    adress_fact: str = Field(..., min_length=5, max_length=255, examples=[
                             "г. Москва, ул. Пушкина, д. 42"], description="Фактический адрес")
    remark: Optional[str] = Field(None, max_length=1000, examples=[
                                  "Дополнительная информация"], description="Комментарий")
    inn: str = Field(..., examples=["7707083893"],
                     description="ИНН (10 или 12 цифр)")
    kpp: str = Field(..., examples=["773601001"], description="КПП (9 цифр)")
    bik: str = Field(..., examples=["044525225"], description="БИК (9 цифр)")
    korr_acc: str = Field(..., examples=[
                          "30101810400000000225"], description="Корр. счет (20 цифр)")
    calc_acc: str = Field(..., examples=[
                          "40702810000000012345"], description="Расчетный счет (20 цифр)")
    bank: str = Field(..., examples=["ПАО 'Сбербанк'"],
                      description="Наименование банка")
    ogrn: str = Field(..., examples=[
                      "1027700132195"], description="ОГРН (13 цифр)")

    @field_validator('inn')
    def validate_inn(cls, v: str) -> str:

        # Костыль
        # Не ясно, почему игнорируется флаг ENABLE_SECURITY на уровне эндпоинта
        if settings.ENABLE_SECURITY:
            raise HTTPException(status_code=401, detail="Unauthorized")

        if len(v) not in (10, 12) or not v.isdigit():
            raise ValueError("ИНН должен содержать 10 или 12 цифр")

        # Контрольная сумма для ИНН
        def checksum(inn: str, coefficients: list[int]) -> int:
            return sum(int(c) * k for c, k in zip(inn, coefficients)) % 11 % 10

        if len(v) == 10:
            if checksum(v[:9], [2, 4, 10, 3, 5, 9, 4, 6, 8]) != int(v[9]):
                raise ValueError("Неверная контрольная сумма ИНН")
        else:
            if (checksum(v[:10], [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]) != int(v[10]) or
               checksum(v[:11], [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]) != int(v[11])):
                raise ValueError("Неверная контрольная сумма ИНН")
        return v

    @field_validator('kpp')
    def validate_kpp(cls, v: str) -> str:
        if len(v) != 9 or not v.isdigit():
            raise ValueError("КПП должен содержать ровно 9 цифр")
        return v

    @field_validator('bik')
    def validate_bik(cls, v: str) -> str:
        if len(v) != 9 or not v.isdigit():
            raise ValueError("БИК должен содержать ровно 9 цифр")
        return v

    @field_validator('korr_acc', 'calc_acc')
    def validate_account(cls, v: str) -> str:
        if len(v) != 20 or not v.isdigit():
            raise ValueError("Счет должен содержать ровно 20 цифр")
        return v

    @field_validator('ogrn')
    def validate_ogrn(cls, v: str) -> str:
        if (len(v) not in (13, 15) or not v.isdigit() or
            (len(v) == 13 and int(v[:12]) % 11 % 10 != int(v[12])) or
                (len(v) == 15 and int(v[:14]) % 13 % 10 != int(v[14]))):
            raise ValueError("Неверный формат ОГРН")
        return v

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio() >= 0.8

    def query_getgeo(cls, param, value):
        post_data = {
            "query": value,
            "count": 10
        }

        response = requests.post(f'https://api.gigdata.ru/api/v2/suggest/{param}',
                                 json=post_data, headers={'Authorization': settings.GETGEO_API_KEY}).json()

        for suggestion in response["suggestions"]:

            if cls.similar(suggestion["value"].lower(), value.lower()):
                return value

        raise ValueError(f"Указанный {param} не найден")

    @field_validator('name')
    def validate_name(cls, v: str) -> str:
        return cls.query_getgeo(cls=cls, param="party", value=v)

    @field_validator('adress_jur')
    def validate_jur_address(cls, v: str) -> str:
        return cls.query_getgeo(cls=cls, param="address", value=v)

    @field_validator('adress_fact')
    def validate_fact_address(cls, v: str) -> str:
        return cls.query_getgeo(cls=cls, param="address", value=v)
