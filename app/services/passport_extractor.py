# app/services/passport_extractor.py
from core.fireworks_client import client
from core.config import settings
from app.models.prompts import PASSPORT_EXTRACTION_SYSTEM_PROMPT
from app.models.schemas import PASSPORT_JSON_SCHEMA, KYCResult
from app.models.enums import DocumentType
from app.utils.errors import ExtractionError
from app.utils.image_utils import normalize_data_url


def extract_passport_fields(image_b64: str, raw_ocr_text: str | None = None) -> KYCResult:
    data_url = normalize_data_url(image_b64)

    content = [
        {"type": "text", "text": PASSPORT_EXTRACTION_SYSTEM_PROMPT},
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
            model=settings.PASSPORT_MODEL,
            messages=[
                {"role": "system", "content": PASSPORT_EXTRACTION_SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ],
            response_format={
                "type": "json_schema",
                "json_schema": PASSPORT_JSON_SCHEMA,
            },
        )
        parsed = resp.choices[0].message.parsed  # fireworks JSON-schema parsing
    except Exception as e:
        raise ExtractionError(str(e))

    parsed["document_type"] = DocumentType.PASSPORT
    return KYCResult(**parsed)
