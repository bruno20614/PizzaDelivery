from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT
from gi.overrides.Gio import Settings
from pydantic.v1 import BaseSettings
from auth_routes import auth_router
from src.order_routes import order_router
from schemas import  BaseModel
app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()
app.include_router(auth_router)
app.include_router(order_router)
app = FastAPI(
    docs_url="/docs",  # URL para Swagger UI
    redoc_url="/redoc",  # URL para ReDoc
    openapi_url="/openapi.json"  # URL para OpenAPI JSON
)

#@app.get("/")
#async def read_root():
 #   return {"Hello": "World"}

#@app.get("/{name}")
#async def read_item(name: str):
 #   return {"Hello": name}
