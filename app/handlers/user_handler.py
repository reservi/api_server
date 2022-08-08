from app.model.db.user import User
from app.session import Session
from app.enum.user_enum import UserState

from passlib.context import CryptContext

from . import HandlerBase

class UserHandler(HandlerBase):
    """
    Class responsible for user handling
    """

    def __init__(self, user_data: dict) -> None:
        self.__user_data = user_data
        self.__session = Session()
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        super().__init__(User, self.__session)

    def validate_user(self) -> bool:
        """
        Validate whether user exists, and its valid

        Returns:
            True/False
        """
        user_data = self.__session.query(User).filter_by(
            username=self.__user_data['username']
        ).first()
        if not user_data:
            return UserState.NOT_FOUND

        is_valid_password = self.__pwd_context.verify(
            self.__user_data['password'], user_data.password
        )

        if not is_valid_password:
            return UserState.INVALID_PASSWORD

        return UserState.VALID_USER