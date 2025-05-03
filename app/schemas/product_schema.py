from pydantic import BaseModel


class AddProductSchema(BaseModel):
    # id_house: int
    name: str
    year_produce: int
    remark: str


class EditProductSchema(AddProductSchema):
    id: int


class DeleteProductSchema(BaseModel):
    id: int


class ListProductSchema(AddProductSchema):
    pass


class GetProductSchema(DeleteProductSchema):
    pass
