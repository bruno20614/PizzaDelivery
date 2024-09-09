from fastapi import FastAPI
from auth_routes import auth_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/{name}")
async def read_item(name: str):
    return {"Hello": name}
