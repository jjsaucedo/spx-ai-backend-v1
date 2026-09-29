from fastapi import APIRouter

from app.services.market import market_service


router = APIRouter(
    prefix="/api/options",
    tags=["options"],
)


@router.get("/candidates")
async def get_candidates():
    return await market_service.candidates()


@router.get("/chain")
async def get_demo_chain():
    """
    V1 placeholder.

    Returns strategy candidates instead of a full live SPX option chain.

    Replace this endpoint with real option-chain data when
    an authorized market-data provider is connected.
    """
    return {
        "mode": "demo",
        "warning": "This is not a live SPX option chain.",
        "candidates": await market_service.candidates(),
    }
