from app.models.person_model import Person as PersonMD
from sqlalchemy.orm import Session
from app.settings import settings


ENGINE = settings.ENGINE


def select_all_from_person():

    with Session(autoflush=False, bind=ENGINE) as db:

        people = db.query(PersonMD).all()
        # people = [people[i]
        #           for i in range(len(people) - 1, len(people) - 100, -1)]

        if not people:
            return "Error: Person table is empty"

        result = [{
            "id": person.id,
            "family_name": person.family_name,
            "birthdate": None if not person.birthdate else person.birthdate.strftime("%d.%m.%Y"),
            "phone_number": person.phone_number,
            "name": person.name,
            "patronimic_name": person.patronimic_name,
            "pasport_serial": person.pasport_serial,
            "pasport_number": person.pasport_number,
            "pasport_date": None if not person.pasport_date else person.pasport_date.strftime("%d.%m.%Y"),
            "pasport_place": person.pasport_place,
            "remark": person.remark,
            "dep_code": person.dep_code,
            "reg_adress": person.reg_adress,
            "reg_region": person.reg_region,
            "reg_raion": person.reg_raion,
            "reg_city": person.reg_city,
            "reg_street": person.reg_street,
            "reg_house": person.reg_house,
            "reg_flat": person.reg_flat,
            "postal_index": person.postal_index,
            "inn": person.inn,
            "ogrn": person.ogrn,
            "snils": person.snils,
            "email": person.email
        } for person in people]

        return result
