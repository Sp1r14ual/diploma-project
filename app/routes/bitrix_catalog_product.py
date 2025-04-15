from app.bitrix.get_catalog_product import get_catalog_product_by_id, get_catalog_product_list
from fastapi import APIRouter

router = APIRouter(
    prefix="/bitrix/catalog/product",
    tags=["Bitrix_Catalog_Product"]
)

# Сделать post с передачей параметров


@router.get("/get")
async def bitrix_get_catalog_product():
    return await get_catalog_product_by_id()


@router.get("/list")
async def bitrix_catalog_product_list():
    return await get_catalog_product_list()
