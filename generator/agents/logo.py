"""
Logo Agent - Verarbeitet und optimiert das Firmenlogo.

Lädt Logo von Original-Website, konvertiert zu SVG
oder erstellt ein Text-Logo als Fallback.
"""

from pathlib import Path
from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import LogoResult


class LogoAgent(BaseAgent):
    """
    Verarbeitet das Firmenlogo zu SVG.

    Der Logo-Agent:
    - Lädt Logo von Original-Website
    - Konvertiert PNG/JPG/GIF zu SVG
    - Erstellt Text-Logo als Fallback
    """

    @property
    def agent_name(self) -> str:
        return "logo"

    async def process(
        self,
        company_name: str,
        website_url: Optional[str],
        logo_url: Optional[str],
        primary_color: str,
        output_dir: Path | str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> LogoResult:
        """
        Verarbeitet das Logo.

        Args:
            company_name: Firmenname (für Text-Logo)
            website_url: Original-Website URL
            logo_url: Direkte Logo-URL (falls bekannt)
            primary_color: Primärfarbe für Text-Logo
            output_dir: Zielverzeichnis (assets/ wird automatisch ergänzt)
            on_message: Callback für Streaming-Messages

        Returns:
            LogoResult mit Pfad zum SVG
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        prompt = self._build_prompt(
            company_name=company_name,
            website_url=website_url,
            logo_url=logo_url,
            primary_color=primary_color,
            output_dir=output_dir
        )

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            # Bei Fehler: Text-Logo erstellen
            return await self._create_text_logo(company_name, primary_color, output_dir)

        return self._parse_result(output_dir)

    def _build_prompt(
        self,
        company_name: str,
        website_url: Optional[str],
        logo_url: Optional[str],
        primary_color: str,
        output_dir: Path
    ) -> str:
        """Baut den Task-Prompt für den Agent."""

        assets_dir = output_dir / "assets"

        if logo_url:
            logo_source = f"""
### Direkte Logo-URL

Logo-URL: {logo_url}

1. Lade das Logo herunter
2. Konvertiere zu SVG
"""
        elif website_url:
            logo_source = f"""
### Logo von Website extrahieren

Website: {website_url}

1. Öffne die Website mit Playwright
2. Suche nach Logo im Header
3. Lade das Logo herunter
4. Konvertiere zu SVG
"""
        else:
            logo_source = f"""
### Kein Logo vorhanden

Erstelle ein professionelles SVG-Text-Logo für: **{company_name}**
Primärfarbe: {primary_color}
"""

        return f"""
## AUFGABE

Verarbeite das Logo für: **{company_name}**

## KONTEXT

- **Output-Verzeichnis:** {assets_dir}
- **Primärfarbe:** {primary_color}

{logo_source}

## OUTPUT

Erstelle in {assets_dir}/:

1. **logo.svg** - Hauptlogo (SVG Format!)
2. **logo-white.svg** - Weiße Version (optional, für dunkle Hintergründe)

## KONVERTIERUNG

Falls PNG/JPG/GIF:
1. Nutze /png-to-svg-converter Skill
2. Falls Ergebnis schlecht: Text-Logo erstellen

Falls Text-Logo nötig:
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 60">
  <text x="0" y="40" font-family="Inter, sans-serif"
        font-size="32" font-weight="700" fill="{primary_color}">
    {company_name}
  </text>
</svg>
```

## VALIDIERUNG

1. Prüfe ob SVG valide ist
2. Prüfe ob Farben stimmen
3. Screenshot machen und prüfen
"""

    def _parse_result(self, output_dir: Path) -> LogoResult:
        """
        Analysiert das erstellte Logo.

        Prüft ob logo.svg existiert und welches Format.
        """
        result = LogoResult(success=True)
        assets_dir = output_dir / "assets"

        # Suche nach Logo-Dateien
        logo_svg = assets_dir / "logo.svg"
        logo_original = None

        # Suche nach Original-Logo
        for ext in [".png", ".jpg", ".jpeg", ".gif"]:
            original = assets_dir / f"logo-original{ext}"
            if original.exists():
                logo_original = original
                result.original_format = ext[1:]  # Ohne Punkt
                break

        if logo_svg.exists():
            result.svg_path = str(logo_svg)
            result.converted_to_svg = logo_original is not None
        elif logo_original:
            # Nur Original gefunden, kein SVG
            result.success = False
            result.error = "Logo wurde nicht zu SVG konvertiert"
        else:
            # Gar kein Logo gefunden
            result.success = False
            result.error = "Kein Logo erstellt"

        return result

    async def _create_text_logo(
        self,
        company_name: str,
        primary_color: str,
        output_dir: Path
    ) -> LogoResult:
        """
        Erstellt ein Text-Logo als Fallback.

        Wird verwendet wenn:
        - Kein Logo auf Website gefunden
        - SVG-Konvertierung fehlschlägt
        """
        assets_dir = output_dir / "assets"
        assets_dir.mkdir(parents=True, exist_ok=True)

        # Erstelle SVG Text-Logo
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 60" width="400" height="60">
  <text x="0" y="42" font-family="'Inter', 'Helvetica Neue', Arial, sans-serif"
        font-size="32" font-weight="700" fill="{primary_color}">
    {company_name}
  </text>
</svg>'''

        # Weiße Version für dunkle Hintergründe
        svg_white = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 60" width="400" height="60">
  <text x="0" y="42" font-family="'Inter', 'Helvetica Neue', Arial, sans-serif"
        font-size="32" font-weight="700" fill="#FFFFFF">
    {company_name}
  </text>
</svg>'''

        # Schreibe Dateien
        logo_path = assets_dir / "logo.svg"
        logo_white_path = assets_dir / "logo-white.svg"

        logo_path.write_text(svg_content, encoding="utf-8")
        logo_white_path.write_text(svg_white, encoding="utf-8")

        return LogoResult(
            success=True,
            svg_path=str(logo_path),
            used_text_logo=True
        )
