from sqlalchemy import Column, NVARCHAR, DateTime
from app.models.base_model import Base


class Admin(Base):
    __tablename__ = 'admin_logins'
    __table_args__ = {'implicit_returning': False}

    login = Column(NVARCHAR(64), primary_key=True, nullable=False)
    added = Column(DateTime, nullable=False)
