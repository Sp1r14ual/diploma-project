from sqlalchemy import Column, Integer, VARCHAR
from app.models.base_model import Base


class District(Base):
    __tablename__ = 'district'
    __table_args__ = {'implicit_returning': False, 'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    id_town = Column(Integer, nullable=True)
    name = Column(VARCHAR(512), nullable=False)
    id_region = Column(Integer, nullable=True)
    r_case = Column(VARCHAR(32), nullable=True)
