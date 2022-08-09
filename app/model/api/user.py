from pydantic import BaseModel

class UserPublicModel(BaseModel):
    name: str
    surename: str
    nickname: str
    username: str
    email: str

class UserPrivateModel(UserPublicModel):
    password: str