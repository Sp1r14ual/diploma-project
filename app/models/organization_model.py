from sqlalchemy import Column, Integer, CHAR, VARCHAR
from app.models.base_model import Base


class Organization(Base):
    __tablename__ = 'organization'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(1024), nullable=False, default="DEFAULT_COMPANY")
    adress_jur = Column(VARCHAR(1024), nullable=True)
    zip_code_jur = Column(VARCHAR(6), nullable=True)
    adress_fact = Column(VARCHAR(1024), nullable=True)
    zip_code_fact = Column(VARCHAR(6), nullable=True)
    is_coop = Column(Integer, nullable=False, default=0)
    is_pir = Column(Integer, nullable=False, default=0)
    is_smr_gvd_gnd = Column(Integer, nullable=False, default=0)
    is_smr_vdgo = Column(Integer, nullable=False, default=0)
    is_to_gvd_gnd = Column(Integer, nullable=False, default=0)
    remark = Column(VARCHAR(1024), nullable=True)
    inn = Column(CHAR(12), nullable=True)
    kpp = Column(CHAR(9), nullable=True)
    bik = Column(CHAR(9), nullable=True)
    korr_acc = Column(CHAR(20), nullable=True)
    calc_acc = Column(CHAR(20), nullable=True)
    bank = Column(VARCHAR(128), nullable=True)
    is_gro = Column(Integer, nullable=True)
    ogrn = Column(VARCHAR(32), nullable=True)
    from_1c = Column(Integer, nullable=False, default=0)
    to_rg = Column(Integer, nullable=False, default=0)
    to_ggs = Column(Integer, nullable=False, default=0)
    to_gss = Column(Integer, nullable=False, default=0)
    to_ggsi = Column(Integer, nullable=False, default=0)
    to_ggss = Column(Integer, nullable=False, default=0)
    to_rgs = Column(Integer, nullable=False, default=0)
