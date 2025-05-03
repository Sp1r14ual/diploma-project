from app.bitrix.catalog_product import get_catalog_product_by_id, get_catalog_product_list, get_infoblocks_list, add_catalog_product, update_catalog_product, delete_catalog_product
from app.schemas.product_schema import AddProductSchema, EditProductSchema, DeleteProductSchema, ListProductSchema, GetProductSchema
from fastapi import APIRouter
from app.settings import settings

router = APIRouter(
    prefix="/bitrix/catalog/product",
    tags=["Bitrix_Catalog_Product"]
)


@router.post("/create")
async def bitrix_add_product(AddProductSchema: AddProductSchema):
    params = {
        "iblockId": settings.iblockID,
        "name": AddProductSchema.name,
        "dateCreate": AddProductSchema.year_produce,
        "previewText": AddProductSchema.remark

    }

    add_catalog_product(params=params)
    return "OK"


@router.put("/update")
async def bitrix_update_product(EditProductSchema: EditProductSchema):
    params = {
        "name": EditProductSchema.name,
        "dateCreate": EditProductSchema.year_produce,
        "previewText": EditProductSchema.remark

    }

    update_catalog_product(id=EditProductSchema.id, params=params)
    return "OK"


@router.delete("/delete")
async def bitrix_delete_product(DeleteProductSchema: DeleteProductSchema):
    delete_catalog_product(id=DeleteProductSchema.id)
    return "OK"


@router.post("/get")
async def bitrix_get_catalog_product(GetProductSchema: GetProductSchema):
    return await get_catalog_product_by_id(id=GetProductSchema.id)


@router.post("/list")
async def bitrix_catalog_product_list(ListProductSchema: ListProductSchema):
    params = {
        "iblockId": settings.iblockID,
        "name": ListProductSchema.name,
        # "dateCreate": ListProductSchema.year_produce,
        "previewText": ListProductSchema.remark
    }

    return await get_catalog_product_list(filter_params=params)


@router.get("/infoblocks/list")
async def bitrix_get_infoblocks_list():
    return await get_infoblocks_list()
