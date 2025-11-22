# app/models/responses.py
from pydantic import BaseModel
from typing import Any
from .schemas import KYCResult, ClassificationResult, OCRResult


class HealthResponse(BaseModel):
    status: str


class KYCResponse(BaseModel):
    success: bool
    data: KYCResult
    debug: dict[str, Any] | None = None


class ClassificationAPIResponse(BaseModel):
    success: bool
    data: ClassificationResult


class OCRAPIResponse(BaseModel):
    success: bool
    data: OCRResult
