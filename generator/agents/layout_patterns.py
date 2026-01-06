"""
Layout Patterns Agent - Prüft CSS/Layout Patterns.

Automatische Erkennung und Korrektur von Layout-Problemen.
"""

from typing import Optional, Callable, Any
from dataclasses import dataclass, field

from .base import BaseAgent
from ..results import BaseResult, Finding


@dataclass
class LayoutCheck:
    """Ein einzelner Layout-Check."""
    name: str
    passed: bool
    location: Optional[str] = None  # Datei:Zeile
    problem: Optional[str] = None
    fixed: bool = False


@dataclass
class LayoutPatternsResult(BaseResult):
    """Ergebnis der Layout-Prüfung."""
    checks_run: int = 0
    checks_passed: int = 0
    issues_found: int = 0
    issues_fixed: int = 0
    checks: list[LayoutCheck] = field(default_factory=list)


class LayoutPatternsAgent(BaseAgent):
    """
    Agent zur Prüfung von CSS/Layout Patterns.

    Prüft 9 kritische Patterns:
    1. Scroll Container - keine Pfeile
    2. Hover Scale Verbot
    3. Card Alignment mit flex-col
    4. Container Breakout Pattern
    5. Animation Overflow
    6. Scroll vs Grid Regel
    7. Animation Height Konsistenz
    8. Theme Token Enforcement
    9. Grid Alignment
    """

    @property
    def agent_name(self) -> str:
        return "layout_patterns"

    async def check(
        self,
        output_dir: str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> LayoutPatternsResult:
        """
        Prüft alle Layout Patterns.

        Args:
            output_dir: Verzeichnis mit CSS/HTML
            on_message: Callback für Streaming

        Returns:
            LayoutPatternsResult
        """
        prompt = f"""
Prüfe alle CSS/Layout Patterns in {output_dir}.

## FÜHRE ALLE 9 CHECKS DURCH

### 1. Scroll Container - keine Pfeile
Horizontale Scroll-Container sollten keine Pfeil-Buttons haben.
```css
/* ❌ FALSCH */
.scroll-button {{ display: block; }}

/* ✅ RICHTIG */
.scroll-container {{ overflow-x: auto; scroll-snap-type: x mandatory; }}
```

### 2. Hover Scale Verbot
`transform: scale()` auf Hover verursacht Layout-Shifts.
```css
/* ❌ FALSCH */
.card:hover {{ transform: scale(1.05); }}

/* ✅ RICHTIG */
.card:hover {{ box-shadow: 0 10px 30px rgba(0,0,0,0.1); }}
```

### 3. Card Alignment mit flex-col
Cards mit flex-direction: column brauchen `flex-grow` für Content.
```css
.card {{ display: flex; flex-direction: column; }}
.card__content {{ flex-grow: 1; }}
.card__footer {{ margin-top: auto; }}
```

### 4. Container Breakout Pattern
Full-width Sektionen in begrenztem Container.
```css
.breakout {{
  width: 100vw;
  margin-left: calc(-50vw + 50%);
}}
```

### 5. Animation Overflow
Animierte Elemente dürfen nicht über Container hinausragen.
```css
.section {{ overflow: hidden; }}
```

### 6. Scroll vs Grid Regel
≤4 Items = Grid, >4 Items = Scroll erlaubt
```css
/* 3 Items */
.grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); }}

/* 6+ Items */
.scroll-container {{ display: flex; overflow-x: auto; }}
```

### 7. Animation Height Konsistenz
Animierte Container brauchen feste Höhe.
```css
.animated-container {{
  height: 400px; /* Oder min-height */
}}
```

### 8. Theme Token Enforcement
Farben müssen CSS-Variablen nutzen.
```css
/* ❌ FALSCH */
color: #333333;

/* ✅ RICHTIG */
color: var(--color-text);
```

### 9. Grid Alignment
Grids mit unterschiedlich hohen Spalten brauchen `align-items: start`.
```css
.two-column-grid {{
  display: grid;
  align-items: start; /* Verhindert Stretch! */
}}
```

## PRÜFUNG

Für jeden Check:
1. Suche im CSS nach dem Pattern
2. Prüfe ob korrekt implementiert
3. Falls nicht: AUTOMATISCH FIXEN

## OUTPUT

```
LAYOUT PATTERNS REPORT
======================

✅ Check 1: Scroll Container - OK
❌ Check 2: Hover Scale gefunden in styles.css:45 - GEFIXT
✅ Check 3: Card Alignment - OK
✅ Check 4: Container Breakout - OK
❌ Check 5: Animation Overflow fehlt in styles.css:120 - GEFIXT
✅ Check 6: Scroll vs Grid - OK
✅ Check 7: Animation Height - OK
❌ Check 8: Hardcoded Color in styles.css:78 - GEFIXT
✅ Check 9: Grid Alignment - OK

Checks: 9/9
Gefunden: 3
Gefixt: 3
```
"""

        result_text, error = await self._query_with_retry(prompt, on_message=on_message)

        if error:
            return LayoutPatternsResult(success=False, error=error)

        return self._parse_result(result_text)

    def _parse_result(self, text: str) -> LayoutPatternsResult:
        """Parst das Ergebnis."""
        checks = []
        checks_run = 0
        checks_passed = 0
        issues_found = 0
        issues_fixed = 0

        # Parse individual checks
        for i in range(1, 10):
            check_prefix = f"Check {i}:"
            if check_prefix in text:
                line = text.split(check_prefix)[1].split("\n")[0]

                passed = "✅" in line or "OK" in line.upper()
                fixed = "GEFIXT" in line.upper() or "FIXED" in line.upper()
                location = None
                problem = None

                # Extract location if present (e.g., "styles.css:45")
                if ".css:" in line or ".html:" in line:
                    import re
                    match = re.search(r'(\w+\.(css|html):\d+)', line)
                    if match:
                        location = match.group(1)

                # Extract problem description
                if "-" in line:
                    parts = line.split("-")
                    if len(parts) > 1:
                        problem = parts[-1].strip()

                checks.append(LayoutCheck(
                    name=f"Check {i}",
                    passed=passed or fixed,
                    location=location,
                    problem=problem if not passed else None,
                    fixed=fixed
                ))

        # Parse summary counts
        if "Checks:" in text:
            try:
                line = text.split("Checks:")[1].split("\n")[0]
                checks_run = 9  # Always 9 checks
            except (ValueError, IndexError):
                checks_run = len(checks)

        if "Gefunden:" in text:
            try:
                line = text.split("Gefunden:")[1].split("\n")[0]
                issues_found = int(line.strip().split()[0])
            except (ValueError, IndexError):
                pass

        if "Gefixt:" in text:
            try:
                line = text.split("Gefixt:")[1].split("\n")[0]
                issues_fixed = int(line.strip().split()[0])
            except (ValueError, IndexError):
                pass

        checks_passed = sum(1 for c in checks if c.passed)

        return LayoutPatternsResult(
            success=True,
            checks_run=checks_run or len(checks),
            checks_passed=checks_passed,
            issues_found=issues_found,
            issues_fixed=issues_fixed,
            checks=checks
        )
