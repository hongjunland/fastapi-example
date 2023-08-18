from fastapi import FastAPI
from routers import hello_routes

app = FastAPI()

app.include_router(hello_routes.router)
