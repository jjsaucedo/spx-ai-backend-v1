import json
from datetime import datetime, timezone

from openai import AsyncOpenAI

from app.config import settings
from app.models import AISignal
from app.services.market import market_service
from app.services.risk import risk_service


SYSTEM_INSTRUCTIONS = """
You are the analysis layer of an SPX options paper-trading system.

Rules:
- Only analyze verified data included in the user input.
- Never invent prices, strikes, option quotes, Greeks,
  market news, support, resistance, or indicators.
- The quantitative/risk engine has absolute authority.
- Choose only from approved candidate_id values.
- If evidence is weak, contradictory, stale, or no candidate
  clearly fits, return NO_TRADE.
- The system supports only SPX 0DTE/1DTE defined-risk spreads
  and iron condors.
- Never recommend naked short options.
- This is paper-trading analysis, not guaranteed financial advice.

Return ONLY valid JSON with this exact shape:

{
  "decision": "TRADE" | "WAIT" | "NO_TRADE" | "MONITOR",
  "strategy": string | null,
  "candidate_id": string | null,
  "confidence": integer from 0 to 100,
  "market_regime": string,
  "reasons": [string],
  "invalidation": string | null,
  "risk_notes": [string]
}
"""


class SPXOpenAIAgent:
    async def analyze(self) -> AISignal:
        market = await market_service.snapshot()
        indicators = await market_service.indicators()
        levels = await market_service.levels()
        candidates = await market_service.candidates()

        approved, rejected = risk_service.filter_candidates(candidates)

        # Safe fallback if OpenAI is not configured.
        if not settings.openai_api_key:
            best = approved[0] if approved else None

            return AISignal(
                decision="MONITOR" if best else "NO_TRADE",
                strategy=best.strategy if best else None,
                candidate_id=best.id if best else None,
                confidence=55 if best else 0,
                market_regime=indicators.trend,
                reasons=[
                    "OpenAI API key is not configured.",
                    "Returning deterministic demo-mode fallback.",
                ],
                invalidation=(
                    "Configure OPENAI_API_KEY to enable AI analysis."
                    if best
                    else None
                ),
                risk_notes=[
                    "Paper trading only.",
                    "Demo data is not live market data.",
                ],
                generated_by="fallback",
                is_demo=True,
                timestamp=datetime.now(timezone.utc),
            )

        payload = {
            "market": market.model_dump(mode="json"),
            "indicators": indicators.model_dump(mode="json"),
            "levels": [
                level.model_dump(mode="json")
                for level in levels
            ],
            "approved_candidates": [
                candidate.model_dump(mode="json")
                for candidate in approved
            ],
            "rejected_candidates": rejected,
        }

        client = AsyncOpenAI(
           
