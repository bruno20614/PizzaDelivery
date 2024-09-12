#
from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseSettings
from auth_routes import auth_router
from order_routes import order_router
from schemas import BaseModel

app = FastAPI(
    docs_url="/docs",  # URL para Swagger UI
    redoc_url="/redoc",  # URL para ReDoc
    openapi_url="/openapi.json"  # URL para OpenAPI JSON
)

class Settings(BaseSettings):
    authjwt_secret_key: str = "your_secret_key"

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)