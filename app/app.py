from fastapi import FastAPI
from fast_bitrix24 import Bitrix
from app.routes.bitrix_crm_contact import router as crm_contact_router
from app.routes.bitrix_catalog_product import router as catalog_product_router
# from settings import settings
import json


app = FastAPI()

app.include_router(crm_contact_router)
app.include_router(catalog_product_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
