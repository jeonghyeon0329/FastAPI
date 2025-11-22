from pydantic import ConfigDict, ValidationError
from pydantic_settings import BaseSettings
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

class _Settings(BaseSettings):
    model_config = ConfigDict(
        extra="forbid",
        env_file = ENV_PATH,
        env_file_encoding = "utf-8"
    )

    host: str
    port : str
    app_env : str
    debug : bool

try:
    settings = _Settings()
except ValidationError: raise