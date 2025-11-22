from fastapi import Request, Response
from typing import Callable
from app.utils import *

ALLOWED_IPS = {"127.0.0.1", "localhost", "testclient"}

async def ip_access(request: Request, call_next: Callable[[Request], Response]) -> Response:
    """IP 접근 제어 미들웨어"""

    client_ip = request.client.host

    if client_ip not in ALLOWED_IPS:
        return http_return(403, "C001", f"Access denied for IP: {client_ip}", action="ip_block")

    return await call_next(request)
