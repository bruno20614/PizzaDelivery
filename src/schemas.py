from pydantic import BaseModel
from typing import Optional 


class SingUpModel(BaseModel):
    id=Optional[int]
    username=str
    email=str
    password=str
    is_staff=Optional[bool]
    is_active=Optional[bool]


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