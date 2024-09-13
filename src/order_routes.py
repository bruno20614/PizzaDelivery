from fastapi import APIRouter, status,Depends
from fastapi.params import Depends
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import session
from fastapi.encoders import jsonable_encoder
#from sqlalchemy.sql.functions import current_user
from models import User, Order
from schemas import OrderModel
from database import Session, engine
from src.auth_routes import auth_router
order_router = APIRouter(
    prefix="/orders",
    tags=['orders']
)

Session=Session(bind=engine)


class Order_router:


    @order_router.get('/')
    async def hello(Authorize: AuthJWT = Depends()):
        try:
            Authorize.jwt_required()
        except Exception as e:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials", )
        return {"message": "Hello World"}


@order_router.post('/orders/',status_code=status.HTTP_201_CREATED)
async def place_an_order(order: OrderModel, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    current_user = Authorize.get_jwt_subject()

    user = Session.query(User).filter(User.username == current_user).fist()

    new_order = Order(
        pizza_size=order.pizza_size,
        quantity=order.quantity,
    )

    new_order.user=user

    session.add(new_order)

    session.commit()

    response = {
        "pizza_size":new_order.pizza_size,
        "quantity":new_order.quantity,
        "id":new_order.id,
        "order_status":new_order.order_status,

    }

    return jsonable_encoder(response)

@order_router.get('/orders/')
async def list_all_orders(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials",
                            )

    current_user=Authorize.get_jwt_subject()

    user=Session.query(User).filter(User.username == current_user).fist()

    if user.is_staff:
        orders=Session.query(Order).all()

        return jsonable_encoder(orders)

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="You are not a super user",
                            )

@auth_router.get('/orders/{id}')
async def get_order_by_id(id:int,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token"
            )

    user=Authorize.get_jwt_subject()

    current_user=Session.query(User).filter(User.username == user).first()

    if current_user.is_staff:
        order=Session.query(Order).filter(Order.id==id).first()

        return jsonable_encoder(order)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User not allowed to carry out requested order"
    )