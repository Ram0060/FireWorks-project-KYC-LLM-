# app/routers/pipeline.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.pipeline import run_kyc_pipeline
from app.models.responses import KYCResponse
from app.utils.errors import KYCError


class PipelineRequest(BaseModel):
    image_b64: str
    include_debug: bool = False


router = APIRouter(prefix="/kyc", tags=["pipeline"])


@router.post("", response_model=KYCResponse)
async def kyc_pipeline(req: PipelineRequest):
    try:
        result, debug = run_kyc_pipeline(req.image_b64)
    except KYCError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return KYCResponse(
        success=True,
        data=result,
        debug=debug if req.include_debug else None,
    )
