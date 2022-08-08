from enum import Enum

class UserState(Enum):
    NOT_FOUND = -1
    INVALID_PASSWORD = -2
    VALID_USER = 0