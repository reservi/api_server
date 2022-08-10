
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from datetime import timedelta

from app.enum.user_enum import UserState
from app.handlers.user_handler import UserHandler
from app.handlers.token_handler import TokenHandler

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
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

    token = TokenHandler().get_token(uh)

    return {"access_token": token, "token_type": "Bearer"}

@router.get("/me")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Get current user data

    Params:
        token: jwt token of user

    Raises:
        HTTPException - when user data is empty

    Returns: Data of user
    """
    uh = TokenHandler(token).get_user_handler()
    if not uh.public_user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return uh.public_user_data

@router.get("/logout")
async def logout(token: str = Depends(oauth2_scheme)) -> None:
    """
    Logout user by adding his token to blacklist

    Raises:
        HTTPException - when user data is empty

    Params:
        token: jwt token of user
    """
    th = TokenHandler(token)
    if not th.get_user_handler().public_user_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    th.blackist_token()