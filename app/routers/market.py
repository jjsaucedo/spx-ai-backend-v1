from fastapi import APIRouter

from app.services.market import market_service


router = APIRouter(
    prefix="/api/market",
    tags=["market"],
)


@router.get("/spx")
async def get_spx():
    return await market_service.snapshot()


@router.get("/indicators")
async def get_indicators():
    return await market_service.indicators()


@router.get("/levels")
async def get_levels():
    return await market_service.levels()
