from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class MarketSnapshot(BaseModel):
    symbol: str = "SPX"
    price: float
    change: float
    change_percent: float
    day_high: float
    day_low: float
    previous_close: float
    market_status: Literal[
        "OPEN",
        "CLOSED",
        "PREMARKET",
        "AFTER_HOURS",
        "DEMO",
    ]
    source: str
    is_demo: bool
    timestamp: datetime


class Indicators(BaseModel):
    symbol: str = "SPX"
    vwap: float
    rsi_5m: float
    rsi_15m: float
    ema_9: float
    ema_21: float
    ema_50: float
    atr_14: float
    opening_range_high: float
    opening_range_low: float
    trend: Literal[
        "STRONG_BULLISH",
        "BULLISH",
        "NEUTRAL",
        "BEARISH",
        "STRONG_BEARISH",
    ]
    volatility_regime: Literal[
        "LOW",
        "NORMAL",
        "ELEVATED",
        "HIGH",
    ]
    source: str
    is_demo: bool
    timestamp: datetime


class MarketLevel(BaseModel):
    price: float
    type: Literal[
        "support",
        "resistance",
        "vwap",
        "opening_range_high",
        "opening_range_low",
    ]
    strength: Literal[
        "minor",
        "moderate",
        "major",
    ]
    source: str


class OptionLeg(BaseModel):
    action: Literal["BUY", "SELL"]
    option_type: Literal["CALL", "PUT"]
    strike: float


class TradeCandidate(BaseModel):
    id: str
    strategy: Literal[
        "BULL_PUT_SPREAD",
        "BEAR_CALL_SPREAD",
        "CALL_DEBIT_SPREAD",
        "PUT_DEBIT_SPREAD",
        "IRON_CONDOR",
    ]
    dte: Literal[0, 1]
    expiration: str
    legs: list[OptionLeg]
    entry_price: float
    max_profit: float
    max_loss: float
    risk_reward: float
    liquidity_score: float = Field(ge=0, le=100)


class AISignal(BaseModel):
    decision: Literal[
        "TRADE",
        "WAIT",
        "NO_TRADE",
        "MONITOR",
    ]
    strategy: str | None = None
    candidate_id: str | None = None
    confidence: int = Field(ge=0, le=100)
    market_regime: str
    reasons: list[str]
    invalidation: str | None = None
    risk_notes: list[str] = []
    generated_by: str
    is_demo: bool
    timestamp: datetime


class PaperTradeRequest(BaseModel):
    candidate_id: str
    contracts: int = Field(
        default=1,
        ge=1,
        le=100,
    )


class PaperTrade(BaseModel):
    trade_id: str
    candidate_id: str
    status: Literal["OPEN", "CLOSED"]
    strategy: str
    contracts: int
    entry_price: float
    current_price: float
    max_profit: float
    max_loss: float
    pnl: float
    opened_at: datetime
    closed_at: datetime | None = None
    is_demo: bool = True
