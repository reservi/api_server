from __future__ import annotations
from datetime import datetime, timedelta
from typing import AnyStr
from jose import JWTError, jwt
from app import session
from fastapi import HTTPException, status

from . import HandlerBase
from app.session import Session
from app.handlers.user_handler import UserHandler
from app.model.db.token import ForbiddenTokenModel


class TokenHandler(HandlerBase):

    def __init__(self, token: str = None):
        self.__token = token
        self.__session = Session()
        self.__secret_key = "c4f9b2055dd505e54e2b6696bb7e62d2b92bd02234f326e1ab1f611100ff43a9"
        self.__alghoritm = "HS256"
        super().__init__(ForbiddenTokenModel, self.__session)

    def __decode_token(self) -> dict:
        """
        Decode token

        Returns:
            Decoded token data as dict

        Raises:
            JWTError - if token is expired return Unauthorized message
        """
        login_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            token_data = jwt.decode(
                self.__token,
                self.__secret_key,
                algorithms=[self.__alghoritm]
            )
        except JWTError:
            raise login_exception

        if self.is_blacklisted:
            raise login_exception

        return token_data

    def get_user_handler(self) -> UserHandler:
        """
        Get User handler out of token
        """
        token_data = self.__decode_token()

        user_data = {
            "username": token_data['sub']
        }

        return UserHandler(user_data)

    def get_token(self, uh: UserHandler) -> AnyStr:
        """
        Get jwt token or generate new

        Returns:
            JWT token
        """
        to_encode = {
            "sub": uh.public_user_data.username,
            "exp": datetime.utcnow() + timedelta(seconds=60)
        }

        return jwt.encode(to_encode, self.__secret_key, self.__alghoritm)

    @property
    def is_blacklisted(self) -> bool:
        """
        Check whether token is blacklisted

        Returns
            True/False
        """
        db_result = self.__session.query(
            ForbiddenTokenModel
        ).filter_by(token=self.__token).first()

        if db_result:
            return True
        return False

    def blackist_token(self) -> None:
        """
        Decode token
        """
        self.__clear_expired_tokens()
        # Check if token if it's not expired already
        self.__decode_token()

        if self.is_blacklisted:
            return

        new_blacklist = ForbiddenTokenModel(
            token = self.__token,
        )

        self.__session.add(new_blacklist)
        self.__session.commit()

    def __clear_expired_tokens(self) -> None:
        """
        Delete all tokens that was expired
        """
        db_result = self.__session.query(
            ForbiddenTokenModel
        ).all()

        for record in db_result:
            try:
                jwt.decode(
                    record.token,
                    self.__secret_key,
                    algorithms=[self.__alghoritm]
                )
            except JWTError:
                self.__session.delete(record)

        self.__session.commit()