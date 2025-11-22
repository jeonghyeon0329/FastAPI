from fastapi import APIRouter
from app.utils import *

router = APIRouter()

@router.post("/~test")
async def run_test():
    spinner = PrintUtils()

    with spinner.show_spinner("    spinner test..."):
        time.sleep(3)

    return http_return(200, "S001", "function run_test finish", data = {"status": "ok"}, action = "run_test")