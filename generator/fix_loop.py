"""
Fix-Loop Pattern mit Deadlock-Detection.

Implementiert unbegrenztes Fixen mit:
- Deadlock-Erkennung (gleiche Findings N-mal hintereinander)
- Variation-Strategien bei Deadlock
- Tracking von Fix-Statistiken
"""

from dataclasses import dataclass
from typing import Callable, Awaitable, Optional, List, Set
import asyncio

from .results import Finding, FixLoopStats, DesignReviewResult
from .config import IDENTICAL_FINDINGS_THRESHOLD, VARIATION_STRATEGIES


@dataclass
class VariationResult:
    """Ergebnis einer Variation-Strategie."""
    strategy: str
    new_findings: List[Finding]
    success: bool = True


class FixLoop:
    """
    Fix-Loop Controller mit Deadlock-Detection.

    Läuft UNBEGRENZT bis alle Issues gefixt sind.
    Erkennt Deadlocks wenn gleiche Findings wiederholt auftreten.
    """

    def __init__(
        self,
        phase: str,
        on_message: Optional[Callable[[str, str, dict], None]] = None
    ):
        """
        Args:
            phase: Name der Phase (z.B. "design_review")
            on_message: Callback für Status-Updates
        """
        self.phase = phase
        self.on_message = on_message
        self._variation_index = 0
        self._previous_finding_ids: List[Set[str]] = []

    def _emit(self, event: str, data: dict):
        """Sendet Status-Update."""
        if self.on_message:
            self.on_message(self.phase, event, data)

    async def run(
        self,
        initial_findings: List[Finding],
        fix_func: Callable[[List[Finding]], Awaitable[bool]],
        validate_func: Callable[[], Awaitable[DesignReviewResult]],
        vary_func: Optional[Callable[[List[Finding], str], Awaitable[List[Finding]]]] = None
    ) -> tuple[bool, List[Finding], FixLoopStats]:
        """
        Führt Fix-Loop aus bis alle Issues behoben.

        Args:
            initial_findings: Initiale Liste von Findings
            fix_func: Async Funktion zum Fixen (findings) -> success
            validate_func: Async Funktion zur Re-Validierung () -> ReviewResult
            vary_func: Optional - Async Funktion zur Variation bei Deadlock

        Returns:
            Tuple von (success, remaining_findings, stats)
        """
        current_findings = initial_findings
        loop_count = 0
        total_fixed = 0

        self._emit("start", {
            "findings_count": len(initial_findings),
            "findings": [f.id for f in initial_findings]
        })

        while current_findings:
            loop_count += 1
            current_ids = {f.id for f in current_findings}

            # Deadlock-Detection
            if self._is_deadlock(current_ids):
                self._emit("deadlock_detected", {
                    "loop": loop_count,
                    "identical_count": IDENTICAL_FINDINGS_THRESHOLD
                })

                # Variation anwenden
                if vary_func and self._variation_index < len(VARIATION_STRATEGIES):
                    strategy = VARIATION_STRATEGIES[self._variation_index]
                    self._variation_index += 1

                    self._emit("applying_variation", {
                        "strategy": strategy,
                        "attempt": self._variation_index
                    })

                    try:
                        varied_findings = await vary_func(current_findings, strategy)
                        current_findings = varied_findings
                        self._previous_finding_ids.clear()  # Reset nach Variation
                        continue
                    except Exception as e:
                        self._emit("variation_failed", {"error": str(e)})
                else:
                    # Alle Strategien erschöpft
                    self._emit("exhausted", {
                        "message": f"Alle Variationen erschöpft nach {loop_count} Loops",
                        "remaining_findings": len(current_findings)
                    })

                    stats = FixLoopStats(
                        phase=self.phase,
                        loops_run=loop_count,
                        issues_fixed=total_fixed,
                        issues_remaining=len(current_findings),
                        variation_applied=VARIATION_STRATEGIES[self._variation_index - 1] if self._variation_index > 0 else None
                    )
                    return False, current_findings, stats

            self._previous_finding_ids.append(current_ids)

            # Fix durchführen
            self._emit("fixing", {
                "loop": loop_count,
                "findings_count": len(current_findings),
                "findings": [{"id": f.id, "problem": f.problem[:50]} for f in current_findings]
            })

            try:
                fix_success = await fix_func(current_findings)
                if not fix_success:
                    self._emit("fix_failed", {"loop": loop_count})
                    # Trotzdem weiter validieren
            except Exception as e:
                self._emit("fix_error", {"loop": loop_count, "error": str(e)})

            # Re-Validierung
            self._emit("validating", {"loop": loop_count})

            try:
                validate_result = await validate_func()
            except Exception as e:
                self._emit("validate_error", {"loop": loop_count, "error": str(e)})
                continue  # Nächste Iteration versuchen

            if not validate_result.fix_required or not validate_result.findings:
                # Alle gefixt!
                fixed_count = len(initial_findings)
                self._emit("completed", {
                    "loops_run": loop_count,
                    "issues_fixed": fixed_count
                })

                stats = FixLoopStats(
                    phase=self.phase,
                    loops_run=loop_count,
                    issues_fixed=fixed_count,
                    issues_remaining=0
                )
                return True, [], stats

            # Update für nächste Iteration
            fixed_this_round = len(current_findings) - len(validate_result.findings)
            total_fixed += max(0, fixed_this_round)
            current_findings = validate_result.findings

            self._emit("progress", {
                "loop": loop_count,
                "fixed_this_round": fixed_this_round,
                "remaining": len(current_findings)
            })

        # Keine Findings mehr (sollte oben gefangen werden)
        stats = FixLoopStats(
            phase=self.phase,
            loops_run=loop_count,
            issues_fixed=total_fixed,
            issues_remaining=0
        )
        return True, [], stats

    def _is_deadlock(self, current_ids: Set[str]) -> bool:
        """
        Prüft ob Deadlock vorliegt.

        Deadlock = gleiche Finding-IDs N-mal hintereinander
        """
        if len(self._previous_finding_ids) < IDENTICAL_FINDINGS_THRESHOLD:
            return False

        recent = self._previous_finding_ids[-IDENTICAL_FINDINGS_THRESHOLD:]
        return all(ids == current_ids for ids in recent)


async def run_fix_loop(
    phase: str,
    initial_findings: List[Finding],
    fix_func: Callable[[List[Finding]], Awaitable[bool]],
    validate_func: Callable[[], Awaitable[DesignReviewResult]],
    on_message: Optional[Callable[[str, str, dict], None]] = None,
    vary_func: Optional[Callable[[List[Finding], str], Awaitable[List[Finding]]]] = None
) -> tuple[bool, List[Finding], FixLoopStats]:
    """
    Convenience-Funktion für Fix-Loop.

    Args:
        phase: Name der Phase
        initial_findings: Initiale Findings
        fix_func: Funktion zum Fixen
        validate_func: Funktion zur Validierung
        on_message: Status-Callback
        vary_func: Optional Variation-Funktion

    Returns:
        Tuple von (success, remaining_findings, stats)
    """
    loop = FixLoop(phase=phase, on_message=on_message)
    return await loop.run(
        initial_findings=initial_findings,
        fix_func=fix_func,
        validate_func=validate_func,
        vary_func=vary_func
    )
