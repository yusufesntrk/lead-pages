"""
Link QA Agent - Prüft alle Links und Buttons.

Validiert interne Links, Navigation, CTAs und Bilder.
Fixt gefundene Probleme automatisch.
"""

import re
from pathlib import Path
from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import LinkQAResult


class LinkQAAgent(BaseAgent):
    """
    Prüft alle Links und Buttons auf Funktionalität.

    Der LinkQA-Agent:
    - Prüft interne Links (Zielseiten existieren?)
    - Prüft Navigation auf allen Seiten
    - Validiert Tel/Mail/Externe Links
    - Prüft Bild-Referenzen
    """

    @property
    def agent_name(self) -> str:
        return "link_qa"

    async def check(
        self,
        output_dir: Path | str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> LinkQAResult:
        """
        Prüft alle Links in der Website.

        Args:
            output_dir: Verzeichnis mit HTML-Dateien
            on_message: Callback für Streaming-Messages

        Returns:
            LinkQAResult mit Anzahl geprüfter/defekter Links
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        prompt = self._build_prompt(output_dir)

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            return LinkQAResult(success=False, error=error)

        return self._parse_result(result_text, output_dir)

    def _build_prompt(self, output_dir: Path) -> str:
        """Baut den Task-Prompt für den Agent."""

        # Liste alle HTML-Dateien
        html_files = list(output_dir.glob("*.html"))
        html_list = "\n".join(f"- {f.name}" for f in html_files)

        return f"""
## AUFGABE

Prüfe alle Links und Buttons in: **{output_dir}**

## HTML-DATEIEN

{html_list}

## TESTS

1. **Interne Links**: Alle href zu anderen HTML-Seiten
   - Existiert die Zielseite?
   - Funktionieren Anker-Links (#section)?

2. **Navigation**: Header-Menu auf jeder Seite
   - Alle Links funktionieren?
   - Konsistente Navigation auf allen Seiten?

3. **CTAs und Buttons**:
   - Tel-Links: tel:+49... korrekt formatiert?
   - Mail-Links: mailto:... vorhanden?
   - Externe Links: target="_blank"?

4. **Bilder**:
   - Alle src="assets/..." existieren?
   - Keine externen Bild-URLs?

## AUTOMATISCHE FIXES

- Korrigiere falsche Pfade
- Ergänze fehlende target="_blank"
- Korrigiere Tel/Mail-Formate

## OUTPUT

Erstelle Report:
```
LINK QA REPORT
==============

Geprüft: X Links
Fehler: Y
Gefixt: Z

[Details zu jedem Problem]
```
"""

    def _parse_result(self, result_text: str, output_dir: Path) -> LinkQAResult:
        """
        Analysiert das Ergebnis und zählt Links.
        """
        result = LinkQAResult(success=True)

        # Zähle Links in allen HTML-Dateien
        for html_file in output_dir.glob("*.html"):
            content = html_file.read_text(encoding="utf-8")

            # Interne Links
            internal = re.findall(r'href="([^"#]+\.html)"', content)
            result.links_checked += len(internal)

            # Externe Links
            external = re.findall(r'href="https?://[^"]+', content)
            result.external_links_count += len(external)

        # Parse Ergebnis-Text für Fehler
        if "fehler" in result_text.lower() or "broken" in result_text.lower():
            # Zähle gefundene/gefixte Fehler aus Report
            broken_match = re.search(r'fehler:\s*(\d+)', result_text.lower())
            if broken_match:
                result.broken_links_found = int(broken_match.group(1))

            fixed_match = re.search(r'gefixt:\s*(\d+)', result_text.lower())
            if fixed_match:
                result.broken_links_fixed = int(fixed_match.group(1))

        return result

    async def fix(self, finding: 'Finding') -> bool:
        """
        Fixt ein einzelnes Link-Problem.

        Args:
            finding: Das zu fixende Finding

        Returns:
            True wenn gefixt, False sonst
        """
        prompt = f"""
## AUFGABE

Fixe dieses Link-Problem:

**Location:** {finding.location}
**Problem:** {finding.problem}
**Anweisung:** {finding.fix_instruction}

{f'**Code:** {finding.fix_code}' if finding.fix_code else ''}

Führe den Fix durch und bestätige mit "FIXED" oder erkläre warum nicht möglich.
"""

        result_text, error = await self._query(prompt)

        if error:
            return False

        return "FIXED" in result_text.upper() or "gefixt" in result_text.lower()
