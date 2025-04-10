from sqlalchemy import Column, Integer, VARCHAR
from app.models.base_model import Base


class Street(Base):
    __tablename__ = 'street'
    __table_args__ = {'implicit_returning': False, 'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    id_type_street = Column(Integer, nullable=False)
    name = Column(VARCHAR(512), nullable=True)
    # short_name = Column(VARCHAR(128), nullable=True)
    id_district = Column(Integer, nullable=True)
    id_town = Column(Integer, nullable=True)
