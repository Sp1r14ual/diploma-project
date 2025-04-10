from app.models.house_model import House as HouseMD
from app.models.house_equip_model import HouseEquip as HouseEquipMD
from app.models.type_house_equip_model import TypeHouseEquip as TypeHouseEquipMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def update_in_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        house_equip = db.query(HouseEquipMD).filter(
            HouseEquipMD.id == params["id_house_equip"]).first()

        if not house_equip:
            return "Error: House Equip does not exist"

        for key, value in params.items():
            if key == "id_house_equip":
                continue
            if key == "id_house":
                house = db.query(HouseMD).filter(
                    HouseMD.id == params["id_house"])

                if not house:
                    return "Error: House does not exist"

                # house_equip.id_house = value
                continue

            if key == "id_type_house_equip":
                type_house_equip = db.query(TypeHouseEquipMD).filter(
                    TypeHouseEquipMD.id == params["id_type_house_equip"])

                if not type_house_equip:
                    return "Error: Type House Equip does not exist"

                # house_equip.id_type_house_equip = value

            if getattr(house_equip, key) == value:
                continue
            else:
                setattr(house_equip, key, value)

        db.commit()
