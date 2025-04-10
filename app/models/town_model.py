from sqlalchemy import Column, Integer, VARCHAR
from app.models.base_model import Base


class Town(Base):
    __tablename__ = 'town'
    __table_args__ = {'implicit_returning': False, 'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(512), nullable=False)
    # id_type_town = Column(VARCHAR(512), nullable=True)
