# app/routers/health.py
from fastapi import APIRouter
from app.models.responses import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/healthz", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="ok")
