from fastapi import Request, Response
from typing import Callable
from app.utils import *

# 허용된 IP 및 URL prefix 설정
ALLOWED_IPS = {"127.0.0.1", "localhost", "testclient"}
ALLOWED_PREFIXES = {"/items"}
ALLOWED_METHODS = {
    "/items" : {
        "POST"
    }    
}

async def ip_access(request: Request, call_next: Callable[[Request], Response]) -> Response:
    """IP 및 경로 접근 제어 미들웨어"""

    client_ip = request.client.host
    path = request.url.path

    if client_ip not in ALLOWED_IPS:
        return http_return(
            403, "C001", f"Access denied for IP: {client_ip}", action = "ip_block"
        )

    base_prefix = "/" + path.lstrip("/").split("/", 1)[0]
    allowed_methods = ALLOWED_METHODS.get(base_prefix)

    if not allowed_methods or request.method not in allowed_methods:
        return http_return(
            404, "C002", f"Invalid API path: {path}", action = "api_path_block"
        )

    return await call_next(request)