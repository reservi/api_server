from app.model.db.user import User
from app.session import Session

class UserHandler:
    """
    Class responsible for user handling
    """

    def __init__(self, user_data: dict) -> None:
        self.__user_data = user_data
        self.__session = Session()

    def validate_user(self) -> bool:
        """
        Validate whether user exists, and its valid

        Returns:
            True/False
        """

        xd = self.__session.query(User).filter_by(id=1).first()
        print(xd)