from app.models.organization_model import Organization as OrganizationMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def update_in_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        organization = db.query(OrganizationMD).filter(
            OrganizationMD.id == params["organization_id"]).first()

        if not organization:
            return "Error: Organization does not exist"

        for key, value in params.items():
            if key == "organization_id":
                continue
            if getattr(organization, key) == value:
                continue
            else:
                setattr(organization, key, value)

        db.commit()
