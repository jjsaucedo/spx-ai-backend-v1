from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers.health import router as health_router
from app.routers.market import router as market_router
from app.routers.options import router as options_router
from app.routers.ai import router as ai_router
from app.routers.paper import router as paper_router
from app.routers.analytics import router as analytics_router


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description=(
        "SPX AI paper-trading backend. "
        "V1 ships with demo market data."
    ),
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=False
    if settings.cors_origin_list == ["*"]
    else True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_router)
app.include_router(market_router)
app.include_router(options_router)
app.include_router(ai_router)
app.include_router(paper_router)
app.include_router(analytics_router)


@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "status": "online",
        "demo_mode": settings.demo_mode,
        "docs": "/docs",
        "health": "/api/health",
    }
