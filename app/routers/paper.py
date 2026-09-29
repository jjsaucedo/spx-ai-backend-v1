from fastapi import APIRouter, HTTPException

from app.models import PaperTradeRequest
from app.services.paper import paper_service


router = APIRouter(
    prefix="/api/paper-trades",
    tags=["paper-trading"],
)


@router.post("")
async def open_paper_trade(req: PaperTradeRequest):
    try:
        return await paper_service.open_trade(
            req.candidate_id,
            req.contracts,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@router.get("/open")
async def list_open_paper_trades():
    return await paper_service.list_open()


@router.post("/{trade_id}/close")
async def close_paper_trade(trade_id: str):
    try:
        return await paper_service.close_trade(trade_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )
