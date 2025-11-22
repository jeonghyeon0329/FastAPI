from app.core.logging_config import setup_logging, get_request_logger
from fastapi import responses, Response
from rich.console import Console
import itertools
import threading
import inspect
import time

logger = setup_logging()

# =========================================================
# 🎯 공통 헬퍼
# =========================================================
def http_return(status: int, code: str, message: str, data=None, action: str = "-"):
    req_logger = get_request_logger(
        action = action,
        code = code,
        log_msg = message
    )
    if 200 <= status < 300:
        req_logger.info(f"{code} '{message}'")
    else:
        req_logger.error(f"{code} '{message}'")

    return responses.JSONResponse(
        status_code = status,
        content = {
            "code": code,
            "message": message,
            "data": data if data is not None else {}
        }
    )

def auto_http_return(status_code: int, code: str, data= None):
    caller = inspect.stack()[1].function
    return http_return(
        status=status_code,
        code = code,
        message = f"function {caller} finish",
        data = data,
        action = caller
    )


# =========================================================
# 💬 PrintUtils
# =========================================================
class PrintUtils:
    """터미널 스피너 & 출력 도우미"""
    def __init__(self):
        self.console = Console()

    def show_spinner(self, message: str = "작업중", interval: float = 0.1):
        console = self.console

        class SpinnerCtx:
            def __enter__(self):
                self._spinner = itertools.cycle(["-", "\\", "|", "/"])
                self._running = True
                self._thread = threading.Thread(target=self._spin_loop, daemon=True)
                self._thread.start()
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                self._running = False
                self._thread.join()
                if exc_type is None:
                    console.log(f"{message} [bold green]완료 ✅[/]")
                else:
                    console.log(f"{message} [bold red]실패 ❌[/]")

            def _spin_loop(self):
                while self._running:
                    console.print(f"{message} {next(self._spinner)}", end="\r", style="cyan")
                    time.sleep(interval)

        return SpinnerCtx()