from app.model.db.user import User
from app.session import Session

from . import HandlerBase

class UserHandler(HandlerBase):
    """
    Class responsible for user handling
    """

    def __init__(self, user_data: dict) -> None:
        self.__user_data = user_data
        self.__session = Session()

        super().__init__(User, self.__session)

    def validate_user(self) -> bool:
        """
        Validate whether user exists, and its valid

        Returns:
            True/False
        """

        xd = self.__session.query(User).filter_by(id=1).first()
        print(xd)