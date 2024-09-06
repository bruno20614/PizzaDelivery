from pydantic import BaseModel
from typing import Optional 


class SingUpModel(BaseModel):
    id=[int]
    username=str
    email=str
    password=str
    is_staff=Optional[bool]
    is_active=Optional[bool]


 class Config:
    orm__mode=True
    schema_extra={
        'example':{
            "username":"Bruno Costa"
            "brunocdl9@ga"
        }
    }

