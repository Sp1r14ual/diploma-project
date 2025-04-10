from app.models.base_model import Base as BaseMD
from app.models.person_model import Person as PersonMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def insert_in_Person(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        person = PersonMD(**params)

        db.add(person)
        db.commit()
        return person.id
