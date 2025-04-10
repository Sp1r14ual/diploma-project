from app.models.base_model import Base as BaseMD
from app.models.person_model import Person as PersonMD
from app.models.organization_model import Organization as OrganizationMD
from app.models.house_model import House as HouseMD
from app.models.house_equip_model import HouseEquip as HouseEquipMD
from app.models.type_house_equip_model import TypeHouseEquip as TypeHouseEquipMD
from app.models.abonent_model import Abonent as AbonentMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def insert_in_HouseEquip(**params):
    BaseMD.metadata.create_all(bind=ENGINE)

    abonent_params = dict()
    house_equip_params = dict()

    with Session(autoflush=False, bind=ENGINE) as db:

        for key, value in params.items():
            if key == "id_house":
                house = db.query(HouseMD).filter(
                    HouseMD.id == params["id_house"]).first()

                if not house:
                    return "Error: House does not exist"

                house_equip_params["id_house"] = house.id

            if key == "id_type_house_equip":
                type_house_equip = db.query(TypeHouseEquipMD).filter(
                    TypeHouseEquipMD.id == params["id_type_house_equip"])

                if not type_house_equip:
                    return "Error: Type House Equip does not exist"

                house_equip_params["id_type_house_equip"] = value

            if key == "id_client":
                person = db.query(PersonMD).filter(
                    PersonMD.id == params["id_client"])

                if not person:
                    return "Error: Client does not exist"

                house = db.query(HouseMD).filter(
                    HouseMD.id == params["id_house"]).first()

                if not house:
                    return "Error: House does not exist"

                abonent_params["id_person"] = value
                abonent_params["id_type_abonent"] = 1
                abonent_params["id_house"] = params["id_house"]

            elif key == "id_organization":
                organization = db.query(OrganizationMD).filter(
                    OrganizationMD.id == params["id_organization"])

                if not organization:
                    return "Error: Client does not exist"

                house = db.query(HouseMD).filter(
                    HouseMD.id == params["id_house"]).first()

                if not house:
                    return "Error: House does not exist"

                abonent_params["id_organization"] = value
                abonent_params["id_type_abonent"] = 2
                abonent_params["id_house"] = params["id_house"]

            else:
                house_equip_params[key] = value

        abonent = AbonentMD(**abonent_params)
        db.add(abonent)
        db.commit()

        house_equip_params["id_abonent"] = abonent.id
        house_equip = HouseEquipMD(**house_equip_params)

        db.add(house_equip)
        db.commit()
        return house_equip.id
