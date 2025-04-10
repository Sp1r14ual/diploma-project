from app.models.base_model import Base as BaseMD
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


def insert_in_House(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    house_params = dict()
    house_owner_params = dict()

    with Session(autoflush=False, bind=ENGINE) as db:
        for key, value in params.items():
            if key == "adress":
                continue
            elif key in ("id_client", "id_organization"):
                if key == "id_client":
                    person = db.query(PersonMD).filter(
                        PersonMD.id == params["id_client"]).first()

                    if not person:
                        return "Error: Client does not exist"

                    house_owner_params["id_person"] = value
                    house_owner_params["is_actual"] = params["is_actual"]

                    continue
                else:
                    organization = db.query(OrganizationMD).filter(
                        OrganizationMD.id == params["id_organization"]).first()

                    if not organization:
                        return "Error: Organization does not exist"

                    house_params["id_organization"] = organization.id
                    house_params["is_actual"] = params["is_actual"]

                    continue

            else:
                if key == "town":
                    town = db.query(TownMD).filter(
                        TownMD.name == params["town"]).first()

                    if not town:
                        return "Error: Town does not exist"

                    house_params["id_town"] = town.id

                    continue

                if key == "district":
                    district = db.query(DistrictMD).filter(
                        DistrictMD.name == params["district"]).first()

                    if not district:
                        return "Error: District does not exist"

                    house_params["id_district"] = district.id

                    continue

                if key == "street":
                    street = db.query(StreetMD).filter(
                        StreetMD.name == params["street"]).first()

                    if not street:
                        return "Error: Street does not exist"

                    house_params["id_street"] = street.id

                    continue

                if key == "postal_index":
                    house_params["postal_index"] = params["postal_index"]

                    continue

            house_params[key] = value

        house = HouseMD(**house_params)

        db.add(house)
        db.commit()

        try:
            params["id_client"]
        except KeyError:
            return house.id

        house_owner_params["id_house"] = house.id
        house_owner = HouseOwnerMD(**house_owner_params)

        db.add(house_owner)
        db.commit()

        return house.id
