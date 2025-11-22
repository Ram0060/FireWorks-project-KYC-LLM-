# core/config.py
from functools import lru_cache
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    # Fireworks
    FIREWORKS_API_KEY: str = os.getenv("FIREWORKS_API_KEY", "")
    FIREWORKS_BASE_URL: str = os.getenv(
        "FIREWORKS_BASE_URL",
        "https://api.fireworks.ai/inference/v1",
    )

    # Model names
    CLASSIFICATION_MODEL: str = os.getenv("CLASSIFICATION_MODEL", "internvl3-8b")
    OCR_MODEL: str = os.getenv("OCR_MODEL", "internvl3-8b")

    PASSPORT_MODEL: str = os.getenv(
        "PASSPORT_MODEL", "accounts/fireworks/models/qwen2-vl-7b-instruct"
    )
    DL_MODEL: str = os.getenv(
        "DL_MODEL", "accounts/fireworks/models/qwen2-vl-7b-instruct"
    )

    # Misc settings
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
