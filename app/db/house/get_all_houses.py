from app.models.house_model import House as HouseMD
from app.models.house_owner_model import HouseOwner as HouseOwnerMD
from app.models.town_model import Town as TownMD
from app.models.district_model import District as DistrictMD
from app.models.street_model import Street as StreetMD
from sqlalchemy.orm import Session
from app.settings import settings


ENGINE = settings.ENGINE


def prepare_return_value(houses):
    result = list()

    with Session(autoflush=False, bind=ENGINE) as db:

        for house in houses:

            try:
                town = db.query(TownMD).filter(
                    house.id_town == TownMD.id).first().name
            except AttributeError:
                town = None

            try:
                district = db.query(DistrictMD).filter(
                    house.id_district == DistrictMD.id).first().name
            except AttributeError:
                district = None

            try:
                street = db.query(StreetMD).filter(
                    house.id_street == StreetMD.id).first().name
            except AttributeError:
                street = None

            try:
                id_client = db.query(HouseOwnerMD).filter(
                    HouseOwnerMD.id_house == house.id).first().id_person
                is_actual = db.query(HouseOwnerMD).filter(
                    HouseOwnerMD.id_house == house.id).first().is_actual
            except AttributeError:
                id_client = None
                is_actual = house.is_actual

            id = house.id
            id_organization = house.id_organization
            house_number = house.house_number
            corpus_number = house.corpus_number
            flat_number = house.flat_number
            cadastr_number = house.cadastr_number
            postal_index = house.postal_index

            data = {
                "id": id,
                "adress": f"почтовый индекс {postal_index}, город {town}, район {district}, улица {street}, дом {house_number}, корпус {corpus_number}, квартира {flat_number}",
                "id_organization": id_organization,
                # "town": town,
                # "district": district,
                # "street": street,
                # "house_number": house_number,
                # "corpus_number": corpus_number,
                # "flat_number": flat_number,
                "cadastr_number": cadastr_number,
                "id_client": id_client,
                "is_actual": is_actual
            }

            result.append(data)

        return result


def select_all_from_house_by_id(**params):

    with Session(autoflush=False, bind=ENGINE) as db:

        is_person = "id_client" in params

        houses = list()

        if is_person:
            house_owner_data = db.query(HouseOwnerMD).filter(
                HouseOwnerMD.id_person == params["id_client"]).all()
            house_ids = [
                house_owner.id_house for house_owner in house_owner_data]

            for house_id in house_ids:
                house = db.query(HouseMD).filter(
                    HouseMD.id == house_id).first()
                houses.append(house)

        else:
            houses = db.query(HouseMD).filter(
                HouseMD.id_organization == params["id_organization"]).all()

        if not houses:
            return "Error: House table is empty"

        return prepare_return_value(houses)


def select_all_from_house():

    with Session(autoflush=False, bind=ENGINE) as db:

        houses = db.query(HouseMD).all()
        # houses = [houses[i]
        #           for i in range(len(houses) - 1, len(houses) - 100, -1)]

        if not houses:
            return "Error: House table is empty"

        return prepare_return_value(houses)
