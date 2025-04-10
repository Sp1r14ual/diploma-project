from sqlalchemy import Column, Integer, VARCHAR
from app.models.base_model import Base


class House(Base):
    __tablename__ = 'house'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)
    id_organization = Column(Integer, nullable=True)
    id_town = Column(Integer, nullable=True)
    id_district = Column(Integer, nullable=True)
    id_street = Column(Integer, nullable=True)
    house_number = Column(VARCHAR(32), nullable=True)
    corpus_number = Column(VARCHAR(32), nullable=True)
    flat_number = Column(VARCHAR(12), nullable=True)
    cadastr_number = Column(VARCHAR(32), nullable=True)
    postal_index = Column(VARCHAR(6), nullable=True)
    is_actual = Column(Integer, nullable=True)
