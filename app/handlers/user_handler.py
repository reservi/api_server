from typing import Union
from passlib.context import CryptContext

from app.model.db.user import User
from app.model.api.user import UserPublicModel
from app.session import Session
from app.enum.user_enum import UserState

from . import HandlerBase

class UserHandler(HandlerBase):
    """
    Class responsible for user handling
    """

    def __init__(self, user_data: Union[dict, None]) -> None:
        self.__user_data = user_data
        self.__session = Session()
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.___db_data = None

        super().__init__(User, self.__session)

    @property
    def public_user_data(self) -> UserPublicModel:
        """
        Return public user data
        """

        return UserPublicModel(
            **self.__db_data.as_dict()
        )

    @property
    def __db_data(self) -> User:
        """
        Get user data from db
        """
        if self.___db_data is None:
            self.___db_data = self.__session.query(User).filter_by(
                username=self.__user_data['username']
            ).first()
        return self.___db_data

    def validate_user(self) -> bool:
        """
        Validate whether user exists, and its valid

        Returns:
            True/False
        """
        if not self.__db_data:
            return UserState.NOT_FOUND

        is_valid_password = self.__pwd_context.verify(
            self.__user_data['password'], self.__db_data.password
        )

        if not is_valid_password:
            return UserState.INVALID_PASSWORD

        return UserState.VALID_USER
