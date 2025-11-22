# app/routers/classify.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.classifier import classify_document
from app.models.responses import ClassificationAPIResponse


class ClassifyRequest(BaseModel):
    image_b64: str


router = APIRouter(prefix="/classify", tags=["classification"])


@router.post("", response_model=ClassificationAPIResponse)
async def classify(req: ClassifyRequest):
    result = classify_document(req.image_b64)
    return ClassificationAPIResponse(success=True, data=result)
