from sqlalchemy import Column, Integer, VARCHAR
from app.models.base_model import Base


class HouseEquip(Base):
    __tablename__ = 'house_equip'
    __table_args__ = {'implicit_returning': False, 'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    id_abonent = Column(Integer, nullable=True)
    id_house = Column(Integer, nullable=True)
    id_type_house_equip = Column(Integer, nullable=True)
    year_produce = Column(Integer, nullable=True)
    remark = Column(VARCHAR(128), nullable=True)
