from app.models.person_model import Person as PersonMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def update_in_Person(**params):

    with Session(autoflush=False, bind=ENGINE) as db:

        person = db.query(PersonMD).filter(
            PersonMD.id == params["client_id"]).first()

        if not person:
            return "Error: Person does not exist"

        for key, value in params.items():
            if key == "client_id":
                continue
            if getattr(person, key) == value:
                continue
            else:
                setattr(person, key, value)

        db.commit()
