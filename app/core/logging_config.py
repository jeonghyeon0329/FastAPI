from logging.handlers import RotatingFileHandler
from logging import LoggerAdapter, LogRecord
import os, sys, logging


def setup_logging(use_console: bool = True) -> logging.Logger:

    
    """로그 레코드 필드 보정 함수"""
    def context_filter(record: LogRecord) -> bool:    
        for key in ("action", "code", "log_msg"):
            if not hasattr(record, key):
                setattr(record, key, "-")
        return True

    def formatter():
        fmt = (
            "[%(asctime)s] [%(levelname)s] [%(action)s] %(message)s"
        )
        return logging.Formatter(fmt, "%Y-%m-%d %H:%M:%S")

    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("fastapi_server")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        return logger

    fmt = formatter()

    fh = RotatingFileHandler("logs/server.log", maxBytes=5_000_000, backupCount=5, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    if use_console:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(fmt)
        logger.addHandler(ch)

    logger.addFilter(context_filter)
    return logger


def get_request_logger(action: str="-", code: str="-", log_msg: str="-") -> LoggerAdapter:
    base = logging.getLogger("fastapi_server")
    return LoggerAdapter(base, {
        "action": action,
        "code": code,
        "log_msg": log_msg
        
    })