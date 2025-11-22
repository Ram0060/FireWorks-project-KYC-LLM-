# app/services/ocr.py
from core.fireworks_client import client
from core.config import settings
from app.models.prompts import OCR_PROMPT
from app.models.schemas import OCRResult
from app.utils.errors import OCRCallError
from app.utils.image_utils import normalize_data_url


def run_ocr(image_b64: str) -> OCRResult:
    data_url = normalize_data_url(image_b64)

    try:
        response = client.responses.create(
            model=settings.OCR_MODEL,
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": OCR_PROMPT},
                        {"type": "image", "image_url": data_url},
                    ],
                }
            ],
            max_output_tokens=2048,
        )
        text = response.output_text
    except Exception as e:
        raise OCRCallError(str(e))

    return OCRResult(text=text)
