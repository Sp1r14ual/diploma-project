from app.models.base_model import Base as BaseMD
from app.models.organization_model import Organization as OrganizationMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def insert_in_Organization(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        organization = OrganizationMD(**params)

        db.add(organization)
        db.commit()
        return organization.id
