from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from src.routers import routers

app = FastAPI()


@app.get("/")
async def read_root(request: Request):
    return RedirectResponse("/docs")


for router in routers:
    app.include_router(router)
