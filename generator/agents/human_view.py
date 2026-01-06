"""
Human View Agent - Prüft Website aus Nutzersicht.

Macht Screenshots und prüft UX-Aspekte wie ein echter Nutzer.
"""

from typing import Optional, Callable, Any
from dataclasses import dataclass, field

from .base import BaseAgent
from ..results import BaseResult, Finding


@dataclass
class SectionCheck:
    """Prüfergebnis einer Sektion."""
    name: str
    desktop_ok: bool = True
    mobile_ok: bool = True
    issues: list[str] = field(default_factory=list)
    fixes_applied: list[str] = field(default_factory=list)


@dataclass
class HumanViewResult(BaseResult):
    """Ergebnis der Human View Prüfung."""
    sections_checked: int = 0
    desktop_score: int = 0  # 0-100
    mobile_score: int = 0   # 0-100
    overall_score: int = 0  # 0-100
    critical_fixes: int = 0
    warnings: int = 0
    section_checks: list[SectionCheck] = field(default_factory=list)


class HumanViewAgent(BaseAgent):
    """
    Agent zur UX-Prüfung aus Nutzersicht.

    Macht für jede Sektion:
    1. Desktop Screenshot (1280x800)
    2. Mobile Screenshot (375x812)
    3. Volle Sektions-Ansicht

    Prüft:
    - Lesbarkeit
    - Buttons & CTAs
    - Leerraum-Probleme
    - Mobile-Probleme
    - Visuelle Hierarchie
    """

    @property
    def agent_name(self) -> str:
        return "human_view"

    async def review(
        self,
        output_dir: str,
        company_slug: str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> HumanViewResult:
        """
        Prüft Website aus Nutzersicht.

        Args:
            output_dir: Verzeichnis mit Website
            company_slug: Firmen-Slug für Screenshots
            on_message: Callback für Streaming

        Returns:
            HumanViewResult
        """
        prompt = f"""
Prüfe die Website wie ein echter Nutzer sie sehen würde.

## ARBEITSVERZEICHNIS

{output_dir}/

## TEMP-ORDNER FÜR SCREENSHOTS

```bash
mkdir -p {output_dir}/.playwright-tmp
```

## FÜR JEDE SEKTION - 3 SCREENSHOTS

### 1. Desktop Viewport (1280x800)

```javascript
playwright_navigate({{
    url: "file://{output_dir}/index.html",
    width: 1280,
    height: 800
}})
playwright_screenshot({{
    name: "section-desktop",
    selector: ".hero",  // oder andere Sektion
    savePng: true,
    downloadsDir: "{output_dir}/.playwright-tmp"
}})
```

### 2. Mobile Viewport (375x812)

```javascript
playwright_resize({{ width: 375, height: 812 }})
playwright_screenshot({{
    name: "section-mobile",
    selector: ".hero",
    savePng: true,
    downloadsDir: "{output_dir}/.playwright-tmp"
}})
```

### 3. Nach jeder Sektion Screenshots löschen!

```bash
rm {output_dir}/.playwright-tmp/*.png
```

## PRÜFE JEDE SEKTION AUF

### Lesbarkeit
- Ist der Text gut lesbar?
- Stimmen die Kontraste?
- Ist die Schriftgröße angemessen?

### Buttons & CTAs
- Sind Buttons sichtbar und klickbar?
- Haben sie genug Abstand?
- Ist die Beschriftung klar?

### Leerraum-Probleme
- Gibt es ungewollte Lücken?
- Sind Abstände gleichmäßig?
- Ist die Sektion ausbalanciert?

### Mobile-Probleme
- Passt alles auf den Bildschirm?
- Sind Touch-Targets groß genug (min. 44x44px)?
- Funktioniert die Navigation?

### Visuelle Hierarchie
- Ist klar was wichtig ist?
- Führt das Auge durch die Seite?
- Sind Headlines prominent?

## KRITISCHE ISSUES SOFORT FIXEN

Bei schweren Problemen:
1. CSS direkt korrigieren
2. Erneut Screenshot machen
3. Verbesserung dokumentieren

## AUFRÄUMEN AM ENDE

```bash
rm -rf {output_dir}/.playwright-tmp
```

## OUTPUT

```
HUMAN VIEW REPORT
=================

📱 MOBILE CHECK
- Hero: ✅ OK
- Services: ⚠️ Cards zu eng - GEFIXT
- Footer: ❌ Links zu klein für Touch - GEFIXT

🖥️ DESKTOP CHECK
- Hero: ✅ OK
- Services: ✅ OK
- Team: ⚠️ Bilder pixelig - HINWEIS

GESAMT-SCORE: 85/100

KRITISCHE FIXES: 2
HINWEISE: 3
```
"""

        result_text, error = await self._query_with_retry(prompt, on_message=on_message)

        if error:
            return HumanViewResult(success=False, error=error)

        return self._parse_result(result_text)

    def _parse_result(self, text: str) -> HumanViewResult:
        """Parst das Ergebnis."""
        section_checks = []
        overall_score = 0
        critical_fixes = 0
        warnings = 0

        # Parse overall score
        if "GESAMT-SCORE:" in text:
            try:
                line = text.split("GESAMT-SCORE:")[1].split("\n")[0]
                score_str = line.strip().split("/")[0]
                overall_score = int(score_str)
            except (ValueError, IndexError):
                pass

        # Parse critical fixes count
        if "KRITISCHE FIXES:" in text:
            try:
                line = text.split("KRITISCHE FIXES:")[1].split("\n")[0]
                critical_fixes = int(line.strip())
            except (ValueError, IndexError):
                pass

        # Parse warnings count
        if "HINWEISE:" in text:
            try:
                line = text.split("HINWEISE:")[1].split("\n")[0]
                warnings = int(line.strip())
            except (ValueError, IndexError):
                pass

        # Parse section checks
        sections = ["Hero", "Services", "Team", "Footer", "About", "Contact", "Gallery"]
        for section in sections:
            if section in text:
                # Find lines containing this section
                for line in text.split("\n"):
                    if section in line and ("✅" in line or "⚠️" in line or "❌" in line):
                        desktop_ok = "❌" not in line
                        mobile_ok = desktop_ok  # Simplified

                        issues = []
                        fixes = []

                        if "GEFIXT" in line:
                            fixes.append(line.split("-")[-1].strip().replace("GEFIXT", "").strip())
                        elif "⚠️" in line or "❌" in line:
                            issues.append(line.split("-")[-1].strip())

                        section_checks.append(SectionCheck(
                            name=section,
                            desktop_ok=desktop_ok,
                            mobile_ok=mobile_ok,
                            issues=issues,
                            fixes_applied=fixes
                        ))
                        break

        # Calculate scores (simplified)
        desktop_issues = sum(1 for s in section_checks if not s.desktop_ok)
        mobile_issues = sum(1 for s in section_checks if not s.mobile_ok)
        total_sections = len(section_checks) or 1

        desktop_score = max(0, 100 - (desktop_issues * 15))
        mobile_score = max(0, 100 - (mobile_issues * 15))

        return HumanViewResult(
            success=True,
            sections_checked=len(section_checks),
            desktop_score=desktop_score,
            mobile_score=mobile_score,
            overall_score=overall_score or ((desktop_score + mobile_score) // 2),
            critical_fixes=critical_fixes,
            warnings=warnings,
            section_checks=section_checks
        )
