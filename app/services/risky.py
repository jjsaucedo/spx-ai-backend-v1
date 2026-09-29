from app.models import TradeCandidate


class RiskService:
    """
    Hard risk rules.

    These rules override AI recommendations.
    """

    MAX_RISK_PER_TRADE = 500.0
    MIN_LIQUIDITY_SCORE = 70.0

    def candidate_allowed(
        self,
        candidate: TradeCandidate,
    ) -> tuple[bool, list[str]]:

        reasons = []

        if candidate.max_loss > self.MAX_RISK_PER_TRADE:
            reasons.append(
                f"max_loss {candidate.max_loss:.2f} "
                f"exceeds {self.MAX_RISK_PER_TRADE:.2f}"
            )

        if candidate.liquidity_score < self.MIN_LIQUIDITY_SCORE:
            reasons.append(
                f"liquidity_score {candidate.liquidity_score:.0f} "
                f"below {self.MIN_LIQUIDITY_SCORE:.0f}"
            )

        return len(reasons) == 0, reasons

    def filter_candidates(
        self,
        candidates: list[TradeCandidate],
    ):

        approved = []
        rejected = []

        for candidate in candidates:
            allowed, reasons = self.candidate_allowed(candidate)

            if allowed:
                approved.append(candidate)
            else:
                rejected.append(
                    {
                        "candidate_id": candidate.id,
                        "reasons": reasons,
                    }
                )

        return approved, rejected


risk_service = RiskService()
