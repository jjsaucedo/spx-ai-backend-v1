from fastapi import APIRouter

from app.config import settings


router = APIRouter(
    prefix="/api",
    tags=["health"],
)


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.environment,
        "demo_mode": settings.demo_mode,
        "openai_configured": bool(settings.openai_api_key),
    }
