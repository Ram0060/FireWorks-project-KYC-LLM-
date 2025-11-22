# app/routers/extract.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.enums import DocumentType
from app.models.schemas import KYCResult
from app.models.responses import KYCResponse
from app.services.passport_extractor import extract_passport_fields
from app.services.dl_extractor import extract_dl_fields
from app.utils.errors import ExtractionError


class ExtractRequest(BaseModel):
    image_b64: str
    raw_ocr_text: str | None = None


router = APIRouter(prefix="/extract", tags=["extraction"])


@router.post("/{doc_type}", response_model=KYCResponse)
async def extract(doc_type: DocumentType, req: ExtractRequest):
    try:
        if doc_type == DocumentType.PASSPORT:
            result = extract_passport_fields(req.image_b64, req.raw_ocr_text)
        elif doc_type == DocumentType.DRIVERS_LICENSE:
            result = extract_dl_fields(req.image_b64, req.raw_ocr_text)
        else:
            raise HTTPException(status_code=400, detail="Unsupported document_type")
    except ExtractionError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return KYCResponse(success=True, data=result)
