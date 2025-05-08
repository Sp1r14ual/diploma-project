from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from fast_bitrix24 import Bitrix
from app.routes.bitrix_crm_contact import router as crm_contact_router
from app.routes.bitrix_crm_company import router as crm_company_router
from app.routes.bitrix_catalog_product import router as catalog_product_router
from app.routes.db_person import router as person_router
from app.routes.db_organization import router as organization_router
from app.routes.db_house import router as house_router
from app.routes.db_house_equip import router as house_equip_router
from app.routes.validate_data import router as validate_data_router
from app.routes.auth import router as auth_router


app = FastAPI()


app.include_router(crm_contact_router)
app.include_router(crm_company_router)
app.include_router(catalog_product_router)
app.include_router(person_router)
app.include_router(organization_router)
app.include_router(house_router)
app.include_router(house_equip_router)
app.include_router(validate_data_router)
app.include_router(auth_router)



@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Starting page</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <h3>Для информации о доступных функциях перейдите в раздел с <a href='/docs'>документацией</a></h3>
        </body>
    </html>
    """
