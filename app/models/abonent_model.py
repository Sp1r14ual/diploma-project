from sqlalchemy import Column, Integer, VARCHAR
from app.models.base_model import Base


class Abonent(Base):
    __tablename__ = 'abonent'
    __table_args__ = {'implicit_returning': False, 'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    id_type_abonent = Column(Integer, nullable=False)
    id_person = Column(Integer, nullable=False)
    id_organization = Column(Integer, nullable=False)
    id_house = Column(Integer, nullable=False)
