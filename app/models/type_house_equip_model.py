from sqlalchemy import Column, Integer, VARCHAR
from app.models.base_model import Base


class TypeHouseEquip(Base):
    __tablename__ = 'type_house_equip'
    __table_args__ = {'implicit_returning': False, 'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(128), nullable=False)
    descr = Column(VARCHAR(1024), nullable=True)
