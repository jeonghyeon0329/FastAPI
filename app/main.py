from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.middleware import ip_access
from app.routers import items
from app.utils import *


app = FastAPI()

app.middleware("http")(ip_access)

app.include_router(items.router, prefix="/items", tags = ["items"])

@app.exception_handler(StarletteHTTPException)
async def custom_starlette_http_exception_handler(request: Request, exc: StarletteHTTPException):
    return http_return(exc.status_code, "C002", exc.detail, action="starlette_exception")

@app.exception_handler(Exception)
async def custom_all_exception_handler(request: Request, exc: Exception):
    return http_return(500, "C003", "Internal Server Error", action="internal_error")



