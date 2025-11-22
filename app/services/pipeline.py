# app/services/pipeline.py
from app.models.schemas import KYCResult
from app.models.enums import DocumentType
from app.services.classifier import classify_document
from app.services.ocr import run_ocr
from app.services.passport_extractor import extract_passport_fields
from app.services.dl_extractor import extract_dl_fields
from app.services.validator import validate_kyc
from app.utils.errors import UnsupportedDocumentError


def run_kyc_pipeline(image_b64: str) -> tuple[KYCResult, dict]:
    """
    Full pipeline:
    1. Classify document (passport vs driver’s license)
    2. OCR
    3. Field extraction using appropriate Fireworks LLM
    4. Validation
    Returns: (validated_result, debug_info)
    """
    debug: dict = {}

    classification = classify_document(image_b64)
    debug["classification"] = classification.model_dump()

    if classification.document_type == DocumentType.OTHER:
        raise UnsupportedDocumentError("Unsupported document type")

    ocr_result = run_ocr(image_b64)
    debug["ocr"] = {"text_preview": ocr_result.text[:300]}

    if classification.document_type == DocumentType.PASSPORT:
        extracted = extract_passport_fields(image_b64, raw_ocr_text=ocr_result.text)
    else:
        extracted = extract_dl_fields(image_b64, raw_ocr_text=ocr_result.text)

    debug["raw_extraction"] = extracted.model_dump()

    validated = validate_kyc(extracted)
    debug["validated"] = validated.model_dump()

    return validated, debug
