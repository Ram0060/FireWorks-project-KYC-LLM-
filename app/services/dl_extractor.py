# app/services/dl_extractor.py
from core.fireworks_client import client
from core.config import settings
from app.models.prompts import DL_EXTRACTION_SYSTEM_PROMPT
from app.models.schemas import DL_JSON_SCHEMA, KYCResult
from app.models.enums import DocumentType
from app.utils.errors import ExtractionError
from app.utils.image_utils import normalize_data_url


def extract_dl_fields(image_b64: str, raw_ocr_text: str | None = None) -> KYCResult:
    data_url = normalize_data_url(image_b64)

    content = [
        {"type": "text", "text": DL_EXTRACTION_SYSTEM_PROMPT},
        {"type": "image", "image_url": data_url},
    ]

    if raw_ocr_text:
        content.append(
            {
                "type": "text",
                "text": f"Here is OCR text to help you:\n\n{raw_ocr_text}",
            }
        )

    try:
        resp = client.chat.completions.create(
            model=settings.DL_MODEL,
            messages=[
                {"role": "system", "content": DL_EXTRACTION_SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ],
            response_format={
                "type": "json_schema",
                "json_schema": DL_JSON_SCHEMA,
            },
        )
        parsed = resp.choices[0].message.parsed
    except Exception as e:
        raise ExtractionError(str(e))

    parsed["document_type"] = DocumentType.DRIVERS_LICENSE
    return KYCResult(**parsed)
