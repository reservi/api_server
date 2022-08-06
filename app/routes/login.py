from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder

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
    uh = UserHandler(r).validate_user()

    
