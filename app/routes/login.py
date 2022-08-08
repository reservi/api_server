from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from datetime import timedelta

from app.enum.user_enum import UserState
from app.handlers.user_handler import UserHandler

router = APIRouter(
    prefix="/login",
    tags=["login"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

@router.post("/auth")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> None:
    """
    Login route
    """
    r = jsonable_encoder(form_data)
    uh = UserHandler(r)

    if uh.validate_user() != UserState.VALID_USER:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
