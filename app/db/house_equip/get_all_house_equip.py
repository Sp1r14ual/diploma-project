from app.models.house_equip_model import HouseEquip as HouseEquipMD
from app.models.abonent_model import Abonent as AbonentMD
from sqlalchemy.orm import Session
from app.settings import settings


ENGINE = settings.ENGINE


def select_all_from_house_equip_by_id(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        house_equip = db.query(HouseEquipMD).filter(
            HouseEquipMD.id_house == params["id_house"]).all()
        # house_equip = [house_equip[i] for i in range(
        #     len(house_equip) - 1, len(house_equip) - 100, -1)]

        if not house_equip:
            return "Error: House Equip table is empty"

        result = list()

        for item in house_equip:
            try:
                id_client = db.query(AbonentMD).filter(
                    item.id_abonent == AbonentMD.id).first().id_person
            except AttributeError:
                id_client = None

            try:
                id_organization = db.query(AbonentMD).filter(
                    item.id_abonent == AbonentMD.id).first().id_organization
            except AttributeError:
                id_organization = None

            id = item.id
            id_house = item.id_house
            id_type_house_equip = item.id_type_house_equip
            year_produce = item.year_produce
            remark = item.remark

            data = {
                "id": id,
                "id_client": id_client,
                "id_organization": id_organization,
                "id_house": id_house,
                "id_type_house_equip": id_type_house_equip,
                "year_produce": year_produce,
                "remark": remark
            }

            result.append(data)

        return result


def select_all_from_house_equip():

    with Session(autoflush=False, bind=ENGINE) as db:

        house_equip = db.query(HouseEquipMD).all()
        # house_equip = [house_equip[i] for i in range(
        #     len(house_equip) - 1, len(house_equip) - 100, -1)]

        if not house_equip:
            return "Error: House Equip table is empty"

        result = list()

        for item in house_equip:
            try:
                id_client = db.query(AbonentMD).filter(
                    item.id_abonent == AbonentMD.id).first().id_person
            except AttributeError:
                id_client = None

            try:
                id_organization = db.query(AbonentMD).filter(
                    item.id_abonent == AbonentMD.id).first().id_organization
            except AttributeError:
                id_organization = None

            id_house = item.id_house
            id_type_house_equip = item.id_type_house_equip
            year_produce = item.year_produce
            remark = item.remark

            data = {
                "id_client": id_client,
                "id_organization": id_organization,
                "id_house": id_house,
                "id_type_house_equip": id_type_house_equip,
                "year_produce": year_produce,
                "remark": remark
            }

            result.append(data)

        return result
