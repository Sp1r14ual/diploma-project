from pydantic import BaseModel, EmailStr, validator, Field, field_validator
from typing import Optional
from datetime import datetime
import re
import requests
from app.settings import settings


class PersonData(BaseModel):
    family_name: str = Field(..., min_length=1,
                             max_length=50, examples=["Иванов"])
    name: str = Field(..., min_length=1, max_length=50, examples=["Иван"])
    patronimic_name: Optional[str] = Field(
        None, max_length=50, examples=["Иванович"])
    phone_number: str = Field(
        ...,
        pattern=r'^(\+7|8)\d{10}$',
        examples=["+79161234567"]
    )
    email: str = Field(
        ...,
        pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$',
        examples=["ivan.ivanov@gmail.com"],
        description="Email должен соответствовать RFC 5322"
    )  # email валидировать через GETGEO API !!!
    inn: str = Field(..., examples=["0000000000"])
    birth_date: str = Field(..., examples=[
                            "20.01.2001"], description="Дата в формате DD.MM.YYYY")
    ogrn: str = Field(..., examples=["1027700132195"],
                      description="ОГРН (13 или 15 цифр)")
    snils: str = Field(..., examples=[
                       "11223344595"], description="СНИЛС (11 цифр)")

    @field_validator('family_name')
    def validate_surname(cls, v: str) -> str:
        post_data = {
            "query": v,
            "count": 10,
            "parts": ["SURNAME"]
        }
        response = requests.post('https://api.gigdata.ru/api/v2/suggest/fio',
                                 json=post_data, headers={'Authorization': settings.GETGEO_API_KEY})


        if response.status_code == 422:
            raise ValueError('Фамилия не найдена')
        
        response = response.json()

        for suggestion in response["suggestions"]:
            if suggestion["value"].lower() == v.lower():
                return v

        raise ValueError('Фамилия не найдена')

    @field_validator('name')
    def validate_name(cls, v: str) -> str:
        post_data = {
            "query": v,
            "count": 10,
            "parts": ["NAME"]
        }
        response = requests.post('https://api.gigdata.ru/api/v2/suggest/fio',
                                 json=post_data, headers={'Authorization': settings.GETGEO_API_KEY})

        if response.status_code == 422:
            raise ValueError('Имя не найдено')

        response = response.json()

        for suggestion in response["suggestions"]:
            if suggestion["value"].lower() == v.lower():
                return v

        raise ValueError('Имя не найдено')

    @field_validator('patronimic_name')
    def validate_patronymic(cls, v: str) -> str:
        post_data = {
            "query": v,
            "count": 10,
            "parts": ["PATRONYMIC"]
        }
        response = requests.post('https://api.gigdata.ru/api/v2/suggest/fio',
                                 json=post_data, headers={'Authorization': settings.GETGEO_API_KEY})

        if response.status_code == 422:
            raise ValueError('Отчество не найдено')

        response = response.json()

        for suggestion in response["suggestions"]:
            if suggestion["value"].lower() == v.lower():
                return v

        raise ValueError('Отчество не найдено')

    @field_validator('snils')
    def validate_snils(cls, v: str) -> str:
        # Удаляем все нецифровые символы
        clean_snils = re.sub(r'\D', '', v)

        # Проверка длины
        if len(clean_snils) != 11:
            raise ValueError('СНИЛС должен содержать ровно 11 цифр')

        # Проверка что все символы цифры
        if not clean_snils.isdigit():
            raise ValueError('СНИЛС должен содержать только цифры')

        # Проверка контрольного числа
        def calculate_checksum(snils: str) -> str:
            total = 0
            for i, digit in enumerate(snils[:9], start=1):
                total += int(digit) * (10 - i)

            if total < 100:
                checksum = total
            elif total == 100 or total == 101:
                checksum = 0
            else:
                checksum = total % 101
                if checksum == 100:
                    checksum = 0

            return f"{checksum:02d}"

        expected_checksum = calculate_checksum(clean_snils)
        actual_checksum = clean_snils[9:]

        if actual_checksum != expected_checksum:
            raise ValueError(
                f'Неверное контрольное число СНИЛС. Ожидалось {expected_checksum}')

        return v

    @field_validator('ogrn')
    def validate_ogrn(cls, v: str) -> str:
        # Проверка длины и цифр
        if len(v) not in (13, 15) or not v.isdigit():
            raise ValueError('ОГРН должен содержать 13 или 15 цифр')

        # Контрольная сумма для ОГРН (13 цифр)
        if len(v) == 13:
            check = int(v[:12]) % 11
            check = 0 if check == 10 else check
            if check != int(v[12]):
                raise ValueError(
                    'Неверный ОГРН (не совпадает контрольная сумма)')

        # Контрольная сумма для ОГРНИП (15 цифр)
        elif len(v) == 15:
            check = int(v[:14]) % 13
            check = 0 if check == 10 else check
            if check != int(v[14]):
                raise ValueError(
                    'Неверный ОГРНИП (не совпадает контрольная сумма)')

        return v

    @field_validator('birth_date')
    def validate_birth_date(cls, v: str) -> str:
        # Проверка формата
        if not v or len(v) != 10 or v[2] != '.' or v[5] != '.':
            raise ValueError('Неверный формат даты. Используйте DD.MM.YYYY')

        try:
            day = int(v[:2])
            month = int(v[3:5])
            year = int(v[6:])
        except ValueError:
            raise ValueError('Дата должна содержать только цифры и точки')

        # Проверка валидности даты
        try:
            datetime(year=year, month=month, day=day)
        except ValueError as e:
            raise ValueError(f'Некорректная дата: {str(e)}')

        # Проверка что дата не в будущем
        if datetime(year, month, day) > datetime.now():
            raise ValueError('Дата рождения не может быть в будущем')

        return v

    @field_validator('inn')
    def validate_inn(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError('ИНН должен содержать только цифры')
        if len(v) not in (10, 12):
            raise ValueError('ИНН должен быть 10 или 12 цифр')

        # Проверка контрольной суммы
        def calculate_checksum(inn: str, weights: list[int]) -> int:
            return sum(int(digit) * weight for digit, weight in zip(inn, weights)) % 11 % 10

        if len(v) == 10:
            checksum = calculate_checksum(v[:9], [2, 4, 10, 3, 5, 9, 4, 6, 8])
            if checksum != int(v[9]):
                raise ValueError('Неверный ИНН')
        else:
            checksum1 = calculate_checksum(
                v[:10], [7, 2, 4, 10, 3, 5, 9, 4, 6, 8])
            checksum2 = calculate_checksum(
                v[:11], [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8])

            if checksum1 != int(v[10]) or checksum2 != int(v[11]):
                raise ValueError('Неверный ИНН')

        return v
