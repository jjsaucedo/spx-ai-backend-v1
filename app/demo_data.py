from datetime import datetime, timezone

from app.models import (
    MarketSnapshot,
    Indicators,
    MarketLevel,
    TradeCandidate,
    OptionLeg,
)


def now():
    return datetime.now(timezone.utc)


def demo_market_snapshot() -> MarketSnapshot:
    return MarketSnapshot(
        symbol="SPX",
        price=6850.25,
        change=24.10,
        change_percent=0.35,
        day_high=6861.40,
        day_low=6818.90,
        previous_close=6826.15,
        market_status="DEMO",
        source="demo",
        is_demo=True,
        timestamp=now(),
    )


def demo_indicators() -> Indicators:
    return Indicators(
        symbol="SPX",
        vwap=6838.40,
        rsi_5m=61.8,
        rsi_15m=58.3,
        ema_9=6846.7,
        ema_21=6839.2,
        ema_50=6828.6,
        atr_14=8.9,
        opening_range_high=6842.0,
        opening_range_low=6820.5,
        trend="BULLISH",
        volatility_regime="NORMAL",
        source="demo",
        is_demo=True,
        timestamp=now(),
    )


def demo_levels() -> list[MarketLevel]:
    return [
        MarketLevel(
            price=6838.40,
            type="vwap",
            strength="major",
            source="demo",
        ),
        MarketLevel(
            price=6825.00,
            type="support",
            strength="major",
            source="demo",
        ),
        MarketLevel(
            price=6815.00,
            type="support",
            strength="moderate",
            source="demo",
        ),
        MarketLevel(
            price=6860.00,
            type="resistance",
            strength="major",
            source="demo",
        ),
        MarketLevel(
            price=6875.00,
            type="resistance",
            strength="moderate",
            source="demo",
        ),
        MarketLevel(
            price=6842.00,
            type="opening_range_high",
            strength="moderate",
            source="demo",
        ),
        MarketLevel(
            price=6820.50,
            type="opening_range_low",
            strength="moderate",
            source="demo",
        ),
    ]


def demo_candidates() -> list[TradeCandidate]:
    expiration = datetime.now(timezone.utc).date().isoformat()

    return [
        TradeCandidate(
            id="demo-bull-put-1",
            strategy="BULL_PUT_SPREAD",
            dte=0,
            expiration=expiration,
            legs=[
                OptionLeg(
                    action="SELL",
                    option_type="PUT",
                    strike=6820,
                ),
                OptionLeg(
                    action="BUY",
                    option_type="PUT",
                    strike=6815,
                ),
            ],
            entry_price
