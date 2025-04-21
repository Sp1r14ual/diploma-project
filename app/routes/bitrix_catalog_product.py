from app.bitrix.catalog_product import get_catalog_product_by_id, get_catalog_product_list, get_infoblocks_list, add_catalog_product
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


@router.get("/infoblocks/list")
async def bitrix_get_infoblocks_list():
    return await get_infoblocks_list()


@router.get("/create")
async def bitrix_add_product():
    add_catalog_product()
    return "OK"
