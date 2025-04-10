from app.models.house_equip_model import HouseEquip as HouseEquipMD
from app.models.abonent_model import Abonent as AbonentMD
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.settings import settings

ENGINE = settings.ENGINE


def delete_from_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        house_equip = db.query(HouseEquipMD).filter(and_(
            HouseEquipMD.id == params["id_house_equip"], HouseEquipMD.id_house == params["id_house"])).first()

        if not house_equip:
            return "Error: House Equip does not exist"

        abonent = db.query(AbonentMD).filter(and_(house_equip.id_abonent ==
                                                  AbonentMD.id, house_equip.id_house == AbonentMD.id_house)).first()

        # Сомнительно, но окей
        if not abonent:
            return "Error: Abonent does not exist"

        db.delete(house_equip)

        db.commit()

        db.delete(abonent)

        db.commit()
