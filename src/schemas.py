from pydantic import BaseModel
from typing import Optional
from secrets import token_hex

class SingUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


class Config:
    orm__mode=True
    schema_extra={
        'example':{
            "id": 1,
                "username": "Bruno Costa",
                "email": "brunocdl9@ga.com",
                "password": "securepassword",
                "is_staff": False,
                "is_active": True
        }
    }

    class Settings(BaseModel):
        auth_jwt_secret_key: str ='c60091945a923f21bf881fbb6132872cf9b949415775bdc92f99d18739b3924d'

class LoginModel(BaseModel):
    username:str
    password:str


