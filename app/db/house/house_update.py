from sqlalchemy import and_
from app.models.person_model import Person as PersonMD
from app.models.organization_model import Organization as OrganizationMD
from app.models.house_model import House as HouseMD
from app.models.house_owner_model import HouseOwner as HouseOwnerMD
from app.models.town_model import Town as TownMD
from app.models.district_model import District as DistrictMD
from app.models.street_model import Street as StreetMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def update_in_House(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        house = db.query(HouseMD).filter(
            HouseMD.id == params["id_house"]).first()

        house_owner = None

        if not house:
            return "Error: House does not exist"

        for key, value in params.items():
            if key == "id_house":
                continue

            if key == "adress":
                continue

            if key == "town":
                town = db.query(TownMD).filter(
                    TownMD.name == params["town"]).first()

                if not town:
                    return "Error: Town does not exist"

                if house.id_town == town.id:
                    continue
                else:
                    house.id_town = town.id
                    continue

            if key == "district":
                district = db.query(DistrictMD).filter(
                    DistrictMD.name == params["district"]).first()

                if not district:
                    return "Error: District does not exist"

                if house.id_district == district.id:
                    continue
                else:
                    house.id_district = district.id
                    continue

            if key == "street":
                street = db.query(StreetMD).filter(
                    StreetMD.name == params["street"]).first()

                if not street:
                    return "Error: Street does not exist"

                if house.id_street == street.id:
                    continue
                else:
                    house.id_street = street.id
                    continue

            if key == "id_organization":
                organization = db.query(OrganizationMD).filter(
                    OrganizationMD.id == params["id_organization"]).first()

                if not organization:
                    return "Error: Organization does not exist"

                continue

            if key == "id_client":
                person = db.query(PersonMD).filter(
                    PersonMD.id == params["id_client"]).first()

                if not person:
                    return "Error: Client does not exist"

                house_owner = db.query(HouseOwnerMD).filter(and_(
                    HouseOwnerMD.id_house == params["id_house"], HouseOwnerMD.id_person == params["id_client"])).first()

                if not house_owner:
                    return "Error: House Owner does not exist"

                continue

            if key == "is_actual":

                try:
                    params["id_client"]
                except KeyError:
                    house.is_actual = params["is_actual"]
                    continue

                house_owner = db.query(HouseOwnerMD).filter(and_(
                    HouseOwnerMD.id_house == params["id_house"], HouseOwnerMD.id_person == params["id_client"])).first()

                if not house_owner:
                    return "Error: House Owner does not exist"

                if getattr(house_owner, key) == value:
                    continue
                else:
                    setattr(house_owner, key, value)
                    continue

            if getattr(house, key) == value:
                continue
            else:
                setattr(house, key, value)

        db.commit()
