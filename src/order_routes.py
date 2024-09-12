from fastapi import APIRouter, Depends, status
from fastapi.params import Depends
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from models import User, Order
from schemas import OrderModel
from database import Session, engine

order_router = APIRouter(
    prefix="/orders",
    tags=['orders']
)


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


@order_router.post('/')
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
        pizza_size=Order.pizza_size,
    )
