"""
Image Verification Agent - Prüft Bild-Content-Matching.

Stellt sicher, dass Bilder zum beschreibenden Text passen.
"""

from typing import Optional, Callable, Any
from dataclasses import dataclass, field

from .base import BaseAgent
from ..results import BaseResult, Finding


@dataclass
class ImageMismatch:
    """Ein gefundenes Bild-Text-Mismatch."""
    image_path: str
    expected_content: str  # Was der Alt-Text/Kontext sagt
    actual_content: str    # Was das Bild tatsächlich zeigt
    html_location: str     # Datei:Zeile
    severity: str = "critical"


@dataclass
class ImageVerificationResult(BaseResult):
    """Ergebnis der Bildprüfung."""
    images_checked: int = 0
    mismatches_found: int = 0
    mismatches_fixed: int = 0
    mismatches: list[ImageMismatch] = field(default_factory=list)


class ImageVerificationAgent(BaseAgent):
    """
    Agent zur Prüfung der Bild-Text-Übereinstimmung.

    KRITISCH: Verhindert Fehler wie:
    - "Türkisches Frühstück" zeigt Açaí-Bowl
    - "Kebab" zeigt Burger
    - "Crêpes" zeigt Steaks
    """

    @property
    def agent_name(self) -> str:
        return "image_verification"

    async def verify(
        self,
        output_dir: str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> ImageVerificationResult:
        """
        Prüft alle Bilder auf Content-Matching.

        Args:
            output_dir: Verzeichnis mit HTML und Assets
            on_message: Callback für Streaming

        Returns:
            ImageVerificationResult
        """
        prompt = f"""
Prüfe ALLE Bilder auf Content-Matching in {output_dir}.

## SCHRITT 1: ALLE BILDER SAMMELN

```bash
ls -la {output_dir}/assets/images/
ls -la {output_dir}/assets/*.jpg {output_dir}/assets/*.png 2>/dev/null
```

## SCHRITT 2: JEDES BILD VISUELL PRÜFEN

Öffne JEDES Bild mit dem Read Tool:
```
Read(file_path="{output_dir}/assets/images/breakfast-1.jpg")
Read(file_path="{output_dir}/assets/images/kebab-1.jpg")
```

Beschreibe was du WIRKLICH siehst!

## SCHRITT 3: BILD-VERWENDUNG IM HTML PRÜFEN

```bash
grep -rn 'src="assets' {output_dir}/*.html
```

Für jede Bild-Referenz:
1. Finde das `<img>` Tag
2. Prüfe alt-Attribut und umgebenden Text
3. Vergleiche mit tatsächlichem Bildinhalt

## MISMATCH-BEISPIELE

❌ Alt-Text sagt "Türkisches Frühstück" aber Bild zeigt Bowl mit Früchten
❌ Alt-Text sagt "Kebab" aber Bild zeigt Burger
❌ Sektion heißt "Crêpes" aber Bild zeigt Steaks
❌ "Team-Foto" zeigt Stock-Photo

## FOOD-KATEGORIEN CHECKLISTE

| Beschreibung | Muss zeigen |
|--------------|-------------|
| Türkisches Frühstück | Platte mit Oliven, Käse, Eier, Brot |
| Kebab | Fleischspieße, Grill |
| Döner | Fleisch im Fladenbrot |
| Crêpes/Pancakes | Dünne Pfannkuchen |
| Burger | Brötchen mit Patty |
| Pizza | Runde Teigscheibe mit Belag |
| Salat | Grünes Blattgemüse |

## BEI MISMATCH

1. Besseres Bild suchen (Pexels, Unsplash):
   ```bash
   curl -L -o "{output_dir}/assets/images/[name]-correct.jpg" "[URL]"
   ```

2. HTML-Referenz aktualisieren

3. Falsches Bild löschen

## OUTPUT

```
BILD-VERIFICATION REPORT
========================

✅ food-1.jpg: "Burger" - KORREKT (zeigt Burger)
✅ interior-1.jpg: "Restaurant" - KORREKT (zeigt Innenraum)
❌ kebab-1.jpg: "Kebab" - FALSCH (zeigt Burger!)
   → Ersetzt durch neues Bild von Pexels

Geprüft: X Bilder
Korrekt: Y
Mismatches: Z
Ersetzt: N
```
"""

        result_text, error = await self._query_with_retry(prompt, on_message=on_message)

        if error:
            return ImageVerificationResult(success=False, error=error)

        return self._parse_result(result_text)

    def _parse_result(self, text: str) -> ImageVerificationResult:
        """Parst das Ergebnis."""
        images_checked = 0
        mismatches = []

        # Parse counts
        if "Geprüft:" in text:
            try:
                line = text.split("Geprüft:")[1].split("\n")[0]
                images_checked = int(line.strip().split()[0])
            except (ValueError, IndexError):
                pass

        mismatches_found = 0
        mismatches_fixed = 0

        if "Mismatches:" in text:
            try:
                line = text.split("Mismatches:")[1].split("\n")[0]
                mismatches_found = int(line.strip().split()[0])
            except (ValueError, IndexError):
                pass

        if "Ersetzt:" in text:
            try:
                line = text.split("Ersetzt:")[1].split("\n")[0]
                mismatches_fixed = int(line.strip().split()[0])
            except (ValueError, IndexError):
                pass

        # Parse individual mismatches (lines starting with ❌)
        for line in text.split("\n"):
            if line.strip().startswith("❌"):
                # Extract mismatch details
                mismatch = self._parse_mismatch_line(line)
                if mismatch:
                    mismatches.append(mismatch)

        return ImageVerificationResult(
            success=True,
            images_checked=images_checked,
            mismatches_found=mismatches_found,
            mismatches_fixed=mismatches_fixed,
            mismatches=mismatches
        )

    def _parse_mismatch_line(self, line: str) -> Optional[ImageMismatch]:
        """Parst eine Mismatch-Zeile."""
        # Format: ❌ kebab-1.jpg: "Kebab" - FALSCH (zeigt Burger!)
        try:
            parts = line.strip("❌ ").split(":")
            if len(parts) >= 2:
                image_path = parts[0].strip()
                rest = ":".join(parts[1:])

                expected = ""
                actual = ""

                if '"' in rest:
                    expected = rest.split('"')[1]
                if "zeigt" in rest.lower():
                    actual = rest.split("zeigt")[1].strip().rstrip("!)")

                return ImageMismatch(
                    image_path=f"assets/images/{image_path}",
                    expected_content=expected,
                    actual_content=actual,
                    html_location="",
                    severity="critical"
                )
        except (IndexError, ValueError):
            pass

        return None
