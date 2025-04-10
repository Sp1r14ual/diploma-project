from sqlalchemy import Column, Integer, DateTime, VARCHAR
from app.models.base_model import Base


class Person(Base):
    __tablename__ = 'person'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)
    family_name = Column(VARCHAR(1024), nullable=False, default="Doe")
    birthdate = Column(DateTime, nullable=True)
    phone_number = Column(VARCHAR(16), nullable=True)
    name = Column(VARCHAR(1024), nullable=False, default="John")
    patronimic_name = Column(VARCHAR(1024), nullable=True)
    pasport_serial = Column(VARCHAR(6), nullable=True)
    pasport_number = Column(VARCHAR(12), nullable=True)
    pasport_date = Column(DateTime, nullable=True)
    pasport_place = Column(VARCHAR(512), nullable=True)
    remark = Column(VARCHAR(512), nullable=True)
    dep_code = Column(VARCHAR(6), nullable=True)
    reg_adress = Column(VARCHAR(1024), nullable=True)
    reg_region = Column(VARCHAR(200), nullable=True)
    reg_raion = Column(VARCHAR(200), nullable=True)
    reg_city = Column(VARCHAR(200), nullable=True)
    reg_street = Column(VARCHAR(200), nullable=True)
    reg_house = Column(VARCHAR(200), nullable=True)
    reg_flat = Column(VARCHAR(20), nullable=True)
    postal_index = Column(VARCHAR(6), nullable=True)
    inn = Column(VARCHAR(16), nullable=True)
    ogrn = Column(VARCHAR(32), nullable=True)
    snils = Column(VARCHAR(32), nullable=True)
    email = Column(VARCHAR(32), nullable=True)
