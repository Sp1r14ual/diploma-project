from fastapi import APIRouter, HTTPException, Depends
# from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from app.auth.admin_auth import authenticate
from app.schemas.auth_schema import LoginSchema
from app.settings import security_settings

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# security = HTTPBearer()


@router.post('/login')
def login(LoginSchema: LoginSchema, Authorize: AuthJWT = Depends()):
    if not authenticate(LoginSchema.login):
        raise HTTPException(status_code=401, detail="Неверный логин")

    access_token = Authorize.create_access_token(
        subject=LoginSchema.login, expires_time=security_settings.access_token_expire_time)
    refresh_token = Authorize.create_refresh_token(
        subject=LoginSchema.login, expires_time=security_settings.refresh_token_expire_time)

    Authorize.set_access_cookies(access_token)
    Authorize.set_refresh_cookies(refresh_token)

    return {"access_token": access_token, "refresh_token": refresh_token}


@router.put('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(
        subject=current_user, expires_time=security_settings.access_token_expire_time)

    Authorize.set_access_cookies(new_access_token)

    return {"access_token": new_access_token}


@router.delete('/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    Authorize.unset_jwt_cookies()
    return {"msg": "Successfully logout"}


@router.get('/test_auth')
def test_auth(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}
