from fastapi import APIRouter,status,Depends
from models import User
from database import Session,engine
from schemas import SingUpModel,LoginModel
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash , check_password_hash
from fastapi_jwt_auth import AuthJWT
auth_router=APIRouter(
    prefix = '/auth',
    tags=['auth']
)


Session=Session(bind=engine)

@auth_router.get('/')
async def hello():
    return {"Message" : "Hello World"}

@auth_router.post('/signup',response_model=SingUpModel,status_code=status.HTTP_201_CREATED)
async def signup(user:SingUpModel):

    db_email=Session.query(User).filter(User.email==user.email).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail="User with the email already exists"
                             )
    db_username=Session.query(User).filter(User.username== user.username).first()

    if db_email is not None:
         return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User with the username already exists"
                        )

    new_user=User(
         username=user.username,
         email=user.email,
         password=generate_password_hash(user.password),
         is_activate=user.is_active,
         is_staff=user.is_staff
    )

    Session.add(new_user)

    Session.commit()

    return new_user

#Login route

@auth_router.post('/login')
async def login( user:LoginModel,Authorize:AuthJWT=Depends()):
    db_user=Session.query(User).filter(user.email==user.email).fisrt()

    if db_user and  check_password_hash(db_user.password,user.password):
        acces_token=Authorize.create_access_token(subject=db_user.username)