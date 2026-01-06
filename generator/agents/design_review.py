"""
Design Review Agent - QA für visuelles Design.

Prüft Design auf Modernität, Symmetrie, Assets und
generiert strukturierte Findings für Fix-Loop.
"""

import re
from pathlib import Path
from typing import Optional, Callable, Any, List

from .base import BaseReviewAgent
from ..results import DesignReviewResult, Finding, ReviewStatus


class DesignReviewAgent(BaseReviewAgent):
    """
    Führt Design Review durch und generiert Findings.

    Der DesignReview-Agent:
    - Macht sektionsweise Screenshots
    - Prüft auf modernes Design
    - Validiert Assets und Bilder
    - Generiert strukturierte Findings
    """

    @property
    def agent_name(self) -> str:
        return "design_review"

    async def review(
        self,
        output_dir: Path | str,
        style_guide_content: str = "",
        iteration: int = 1,
        previous_findings: List[Finding] = None,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> DesignReviewResult:
        """
        Führt Design Review durch.

        Args:
            output_dir: Verzeichnis mit HTML/CSS/JS
            style_guide_content: Style Guide für Farbvergleich
            iteration: Aktuelle Iteration (für Kontext)
            previous_findings: Findings aus vorheriger Iteration
            on_message: Callback für Streaming-Messages

        Returns:
            DesignReviewResult mit Findings und Score
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        prompt = self._build_prompt(
            output_dir=output_dir,
            style_guide_content=style_guide_content,
            iteration=iteration,
            previous_findings=previous_findings
        )

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            return DesignReviewResult(success=False, error=error)

        return self._parse_result(result_text)

    def _build_prompt(
        self,
        output_dir: Path,
        style_guide_content: str,
        iteration: int,
        previous_findings: List[Finding]
    ) -> str:
        """Baut den Task-Prompt für den Agent."""

        # Previous findings section
        prev_section = ""
        if previous_findings:
            findings_text = "\n".join(
                f"- [{f.id}] {f.location}: {f.problem}"
                for f in previous_findings
            )
            prev_section = f"""
## VORHERIGE FINDINGS (sollten gefixt sein!)

{findings_text}

Prüfe ob diese Probleme behoben wurden.
"""

        # Style Guide section (gekürzt)
        style_section = ""
        if style_guide_content:
            style_section = f"""
## STYLE GUIDE (Referenz für Farben)

{style_guide_content[:1500]}...
"""

        return f"""
## AUFGABE

Design Review für: **{output_dir}**
Iteration: {iteration}

## SCREENSHOTS

Erstelle sektionsweise Screenshots:
1. Temp-Ordner: {output_dir}/.playwright-tmp/
2. Für jede Sektion einen Screenshot
3. Nach Analyse: Screenshots löschen!

## PRÜFUNGEN

1. **Assets**: Alle Bilder lokal? Keine externen URLs?
2. **Bild-Content-Match**: Bilder passen zum Text?
3. **Modernes Design**: Großzügig, modern, nicht veraltet?
4. **Symmetrie**: Grid-Layouts ausbalanciert?
5. **Logo**: Desktop + Mobile korrekt?
6. **Farben**: Konsistent mit Style Guide?

{style_section}

{prev_section}

## OUTPUT-FORMAT (WICHTIG!)

Erstelle strukturierte Findings:

```
## FINDINGS

### KRITISCH
- [F001] index.html:45 | Problem: ... | Fix: ...
- [F002] styles.css:123 | Problem: ... | Fix: ...

### MAJOR
- [F003] ...

### MINOR
- [F004] ...

## SCORE: XX/100

## FIX_REQUIRED: true/false
```

Jedes Finding MUSS haben:
- ID (F001, F002, ...)
- Location (datei:zeile)
- Problem (kurz)
- Fix (konkrete Anweisung)
"""

    def _parse_result(self, result_text: str) -> DesignReviewResult:
        """
        Parsed Findings aus dem Review-Text.
        """
        result = DesignReviewResult(success=True)

        # Parse Score
        score_match = re.search(r'SCORE:\s*(\d+)', result_text, re.IGNORECASE)
        if score_match:
            result.score = int(score_match.group(1))

        # Parse FIX_REQUIRED
        fix_match = re.search(r'FIX_REQUIRED:\s*(true|false)', result_text, re.IGNORECASE)
        if fix_match:
            result.fix_required = fix_match.group(1).lower() == "true"

        # Parse Findings
        # Pattern: [F001] location | Problem: ... | Fix: ...
        finding_pattern = r'\[F(\d+)\]\s*([^|]+)\s*\|\s*Problem:\s*([^|]+)\s*\|\s*Fix:\s*(.+?)(?=\n|$)'
        matches = re.findall(finding_pattern, result_text, re.IGNORECASE)

        for match in matches:
            finding_id, location, problem, fix = match
            result.findings.append(Finding(
                id=f"F{finding_id.zfill(3)}",
                severity=self._determine_severity(result_text, f"F{finding_id}"),
                location=location.strip(),
                problem=problem.strip(),
                fix_instruction=fix.strip(),
                fix_agent=self._determine_fix_agent(problem)
            ))

        # Alternative Pattern: - [F001] location: problem → fix
        alt_pattern = r'-\s*\[F(\d+)\]\s*([^:]+):\s*(.+?)\s*[→→-]\s*(.+?)(?=\n|$)'
        alt_matches = re.findall(alt_pattern, result_text)

        for match in alt_matches:
            finding_id, location, problem, fix = match
            fid = f"F{finding_id.zfill(3)}"
            # Nur hinzufügen wenn nicht schon vorhanden
            if not any(f.id == fid for f in result.findings):
                result.findings.append(Finding(
                    id=fid,
                    severity=self._determine_severity(result_text, fid),
                    location=location.strip(),
                    problem=problem.strip(),
                    fix_instruction=fix.strip(),
                    fix_agent=self._determine_fix_agent(problem)
                ))

        # Set fix_required based on findings if not explicitly set
        if result.findings and not result.fix_required:
            result.fix_required = any(
                f.severity == "critical" for f in result.findings
            )

        # Set review status
        if not result.findings:
            result.review_status = ReviewStatus.APPROVED
        elif result.fix_required:
            result.review_status = ReviewStatus.NEEDS_CHANGES
        else:
            result.review_status = ReviewStatus.APPROVED

        return result

    def _determine_severity(self, text: str, finding_id: str) -> str:
        """Bestimmt Severity basierend auf Kontext im Text."""
        # Suche Finding in Text und prüfe Sektion
        lines = text.split('\n')
        current_severity = "minor"

        for line in lines:
            if "KRITISCH" in line.upper() or "CRITICAL" in line.upper():
                current_severity = "critical"
            elif "MAJOR" in line.upper():
                current_severity = "major"
            elif "MINOR" in line.upper():
                current_severity = "minor"

            if finding_id in line:
                return current_severity

        return "minor"

    def _determine_fix_agent(self, problem: str) -> str:
        """Bestimmt welcher Agent das Problem fixen soll."""
        problem_lower = problem.lower()

        if any(kw in problem_lower for kw in ["css", "farbe", "style", "spacing", "font"]):
            return "homepage"
        elif any(kw in problem_lower for kw in ["link", "href", "navigation"]):
            return "link_qa"
        elif any(kw in problem_lower for kw in ["bild", "image", "foto", "asset"]):
            return "homepage"
        elif any(kw in problem_lower for kw in ["impressum", "datenschutz", "legal"]):
            return "legal_pages"
        else:
            return "homepage"

    async def validate_fix(
        self,
        findings: List[Finding],
        files: List[str],
        loop_count: int,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> DesignReviewResult:
        """
        Validiert ob Fixes erfolgreich waren.

        Args:
            findings: Die ursprünglichen Findings
            files: Die betroffenen Dateien
            loop_count: Aktuelle Loop-Iteration

        Returns:
            DesignReviewResult mit verbleibenden Findings
        """
        findings_text = "\n".join(
            f"- [{f.id}] {f.location}: {f.problem}"
            for f in findings
        )

        prompt = f"""
## AUFGABE

Validiere ob diese Fixes erfolgreich waren (Loop {loop_count}):

{findings_text}

## BETROFFENE DATEIEN

{chr(10).join(f'- {f}' for f in files)}

## PRÜFUNG

Für jedes Finding:
1. Prüfe ob das Problem behoben wurde
2. Falls nicht behoben: In neuen Findings aufnehmen
3. Falls behoben: Nicht mehr auflisten

## OUTPUT

```
## VERBLEIBENDE FINDINGS

[Nur noch offene Probleme auflisten im gleichen Format]

## FIX_REQUIRED: true/false
```
"""

        result_text, error = await self._query(prompt, on_message)

        if error:
            return DesignReviewResult(
                success=False,
                error=error,
                findings=findings  # Alle Findings bleiben offen
            )

        return self._parse_result(result_text)
