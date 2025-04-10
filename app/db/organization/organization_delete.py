from app.models.organization_model import Organization as OrganizationMD
from sqlalchemy.orm import Session
from app.settings import settings

ENGINE = settings.ENGINE


def delete_from_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        organization = db.query(OrganizationMD).filter(
            OrganizationMD.id == params["id_organization"]).first()

        if not organization:
            return "Error: Organization does not exist"

        db.delete(organization)
        db.commit()
