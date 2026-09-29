from datetime import datetime, timezone
from uuid import uuid4

from app.models import PaperTrade
from app.services.market import market_service


class PaperTradingService:
    def __init__(self):
        self._trades: dict[str, PaperTrade] = {}

    async def open_trade(
        self,
        candidate_id: str,
        contracts: int,
    ) -> PaperTrade:

        candidates = await market_service.candidates()

        candidate = next(
            (
                c
                for c in candidates
                if c.id == candidate_id
            ),
            None,
        )

        if not candidate:
            raise ValueError("Candidate not found")

        trade = PaperTrade(
            trade_id=str(uuid4()),
            candidate_id=candidate.id,
            status="OPEN",
            strategy=candidate.strategy,
            contracts=contracts,
            entry_price=candidate.entry_price,
            current_price=candidate.entry_price,
            max_profit=candidate.max_profit * contracts,
            max_loss=candidate.max_loss * contracts,
            pnl=0.0,
            opened_at=datetime.now(timezone.utc),
            is_demo=True,
        )

        self._trades[trade.trade_id] = trade

        return trade

    async def list_open(self):
        return [
            trade
            for trade in self._trades.values()
            if trade.status == "OPEN"
        ]

    async def close_trade(
        self,
        trade_id: str,
    ) -> PaperTrade:

        trade = self._trades.get(trade_id)

        if not trade:
            raise ValueError("Trade not found")

        # V1 demo close:
        # closes at the current stored price.
        # Later this will use live option pricing.
        trade.status = "CLOSED"
        trade.closed_at = datetime.now(timezone.utc)

        self._trades[trade_id] = trade

        return trade


paper_service = PaperTradingService()
