from fastapi import APIRouter,status
from models import User
from database import Session,engine
from schemas import SingUpModel
from fastapi.exceptions import HttpException
from werkzeug.security import generate_password_hash , check_password_hash
auth_router=APIRouter(
    prefix = '/auth',
    tags=['auth']
)

@auth_router.get('/')
async def hello():
    return {"Message" : "Hello World"}

@auth_router.post('/signup',response_model=SingUpModel,
                  status_code=status.HTTP_201_CREATED)
async def signup(user:SingUpModel):

    db_email=Session.query(User).filter(User.email==user.email).first()

    if db_email is not None:
            return HttpException(status_code=status.HTTP_400_BAD_REQUEST,      
                       detail="User with the eail already exists" 
                       )
    db_username=Session.query(User).filter(User.username== user.username).First()

    if db_email is not None:
         return HttpException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User with the username already exists"
                        )
    
    new_user=User(
         username=user.username,
         email=user.email,
         passwor=generate_password_hash(user.password),
         is_activate=user.is_active,
         is_staff=user.is_staff
    )

    Session.add(new_user)

    Session.commit()

    return new_user