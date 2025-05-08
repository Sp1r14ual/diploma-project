from app.models.admin_model import Admin as AdminMD
from sqlalchemy.orm import Session
from app.settings import settings

def authenticate(username: str) -> bool:
    with Session(autoflush=False, bind=settings.ENGINE) as db:

        admin = db.query(AdminMD).filter(AdminMD.login == username).first()

        return bool(admin)
