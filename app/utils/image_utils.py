# app/utils/image_utils.py
import base64
from pathlib import Path
from typing import Union


def encode_image_to_base64(path: Union[str, Path]) -> str:
    path = Path(path)
    with path.open("rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def normalize_data_url(image_b64: str, mime_type: str = "image/jpeg") -> str:
    """
    Ensure the base64 is wrapped as data URL for Fireworks vision models.
    """
    if image_b64.startswith("data:"):
        return image_b64

    return f"data:{mime_type};base64,{image_b64}"
