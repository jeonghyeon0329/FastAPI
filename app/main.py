from fastapi import FastAPI

from app.core.middleware import ip_access
from app.routers import items

app = FastAPI()

app.middleware("http")(ip_access)

app.include_router(items.router, prefix="/items", tags = ["items"])