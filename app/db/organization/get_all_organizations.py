from app.models.organization_model import Organization as OrganizationMD
from sqlalchemy.orm import Session
from app.settings import settings


ENGINE = settings.ENGINE


def select_all_from_organization():

    with Session(autoflush=False, bind=ENGINE) as db:

        organizations = db.query(OrganizationMD).all()
        # organizations = [organizations[i] for i in range(
        #     len(organizations) - 1, len(organizations) - 100, -1)]

        if not organizations:
            return "Error: Organization table is empty"

        result = [{
            "id": organization.id,
            "name": organization.name,
            "adress_jur": organization.adress_jur,
            "zip_code_jur": organization.zip_code_jur,
            "adress_fact": organization.adress_fact,
            "zip_code_fact": organization.zip_code_fact,
            "is_coop": organization.is_coop,
            "is_pir": organization.is_pir,
            "is_smr_gvd_gnd": organization.is_smr_gvd_gnd,
            "is_smr_vdgo": organization.is_smr_vdgo,
            "is_to_gvd_gnd": organization.is_to_gvd_gnd,
            "remark": organization.remark,
            "inn": organization.inn,
            "kpp": organization.kpp,
            "bik": organization.bik,
            "korr_acc": organization.korr_acc,
            "calc_acc": organization.calc_acc,
            "bank": organization.bank,
            "is_gro": organization.is_gro,
            "ogrn": organization.ogrn,
            "from_1c": organization.from_1c,
            "to_rg": organization.to_rg,
            "to_ggs": organization.to_ggs,
            "to_gss": organization.to_gss,
            "to_ggsi": organization.to_ggsi,
            "to_ggss": organization.to_ggss,
            "to_rgs": organization.to_rgs
        } for organization in organizations]

        return result
