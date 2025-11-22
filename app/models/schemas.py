# app/models/schemas.py
from pydantic import BaseModel
from typing import Optional
from .enums import DocumentType


# ============================================================
# Pydantic Base Models for API Output
# ============================================================

class KYCBase(BaseModel):
    document_type: DocumentType

    # Common fields
    full_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    document_number: Optional[str] = None
    issue_date: Optional[str] = None
    expiry_date: Optional[str] = None

    # Passport fields
    issuing_country: Optional[str] = None
    place_of_birth: Optional[str] = None
    nationality: Optional[str] = None

    # DL fields
    issuing_state: Optional[str] = None
    address: Optional[str] = None

    # Shared fields
    gender: Optional[str] = None
    confidence_score: Optional[float] = None
    raw_ocr_text: Optional[str] = None


class KYCResult(KYCBase):
    """Final validated output after pipeline processing."""


class ClassificationResult(BaseModel):
    document_type: DocumentType
    confidence: float


class OCRResult(BaseModel):
    text: str


# ============================================================
# Fireworks JSON Schemas (STRICT + SEPARATE)
# ============================================================

# ---------- PASSPORT SCHEMA ----------
PASSPORT_JSON_SCHEMA = {
    "name": "passport_kyc_schema",
    "schema": {
        "type": "object",
        "properties": {
            "document_type": {"type": "string"},

            "full_name": {"type": ["string", "null"]},
            "date_of_birth": {"type": ["string", "null"]},

            "place_of_birth": {"type": ["string", "null"]},
            "nationality": {"type": ["string", "null"]},
            "issuing_country": {"type": ["string", "null"]},

            "document_number": {"type": ["string", "null"]},
            "issue_date": {"type": ["string", "null"]},
            "expiry_date": {"type": ["string", "null"]},

            "gender": {"type": ["string", "null"]},

            "confidence_score": {"type": ["number", "null"]},
            "raw_ocr_text": {"type": ["string", "null"]},
        },

        "required": [
            "document_type",
            "issuing_country",
            "full_name",
            "date_of_birth",
            "document_number",
        ],

        "additionalProperties": False,
    },
}


# ---------- DRIVERS LICENSE SCHEMA ----------
DL_JSON_SCHEMA = {
    "name": "drivers_license_kyc_schema",
    "schema": {
        "type": "object",
        "properties": {
            "document_type": {"type": "string"},

            "full_name": {"type": ["string", "null"]},
            "date_of_birth": {"type": ["string", "null"]},
            "gender": {"type": ["string", "null"]},

            "issuing_state": {"type": ["string", "null"]},
            "address": {"type": ["string", "null"]},

            "document_number": {"type": ["string", "null"]},
            "issue_date": {"type": ["string", "null"]},
            "expiry_date": {"type": ["string", "null"]},

            "confidence_score": {"type": ["number", "null"]},
            "raw_ocr_text": {"type": ["string", "null"]},
        },

        "required": [
            "document_type",
            "issuing_state",
            "full_name",
            "date_of_birth",
            "document_number",
        ],

        "additionalProperties": False,
    },
}
