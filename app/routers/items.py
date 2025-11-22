from fastapi import APIRouter
from app.utils import *

router = APIRouter()

@router.post("/~test")
async def test_api():
    spinner = PrintUtils()

    with spinner.show_spinner("    spinner test..."):
        time.sleep(3)

    return auto_http_return(200, "S001", data = {"status": "ok"})