from app.config import settings
from app.demo_data import (
    demo_market_snapshot,
    demo_indicators,
    demo_levels,
    demo_candidates,
)


class MarketService:
    """
    Provider abstraction for V1.

    In DEMO_MODE this returns example SPX/options data.

    Later, replace or extend these methods with a real
    authorized market-data provider.
    """

    async def snapshot(self):
        if settings.demo_mode:
            return demo_market_snapshot()

        raise NotImplementedError(
            "Real market provider not configured."
        )

    async def indicators(self):
        if settings.demo_mode:
            return demo_indicators()

        raise NotImplementedError(
            "Real market provider not configured."
        )

    async def levels(self):
        if settings.demo_mode:
            return demo_levels()

        raise NotImplementedError(
            "Real market provider not configured."
        )

    async def candidates(self):
        if settings.demo_mode:
            return demo_candidates()

        raise NotImplementedError(
            "Real options provider not configured."
        )


market_service = MarketService()
