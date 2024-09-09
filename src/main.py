from fastapi import FastAPI
from auth_routes import auth_router

app = FastAPI()

app = FastAPI(
    docs_url="/docs",  # URL para Swagger UI
    redoc_url="/redoc",  # URL para ReDoc
    openapi_url="/openapi.json"  # URL para OpenAPI JSON
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/{name}")
async def read_item(name: str):
    return {"Hello": name}