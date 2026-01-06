"""
StyleGuide Agent - Extrahiert Design von Original-Website.

Analysiert bestehende Websites, Logos oder erstellt
branchenspezifisches Design wenn nichts vorhanden ist.
"""

import json
import re
from pathlib import Path
from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import StyleGuideResult


class StyleGuideAgent(BaseAgent):
    """
    Analysiert Website/Logo und erstellt Style Guide.

    Der StyleGuide-Agent ist der erste Agent in der Pipeline.
    Er extrahiert alle Design- und Content-Informationen die
    von den nachfolgenden Agents benötigt werden.
    """

    @property
    def agent_name(self) -> str:
        return "style_guide"

    async def extract(
        self,
        company_name: str,
        website_url: Optional[str],
        branche: str,
        company_data: dict,
        output_dir: Path | str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> StyleGuideResult:
        """
        Extrahiert Style Guide von Website oder erstellt Default.

        Args:
            company_name: Firmenname
            website_url: URL der Original-Website (kann None sein)
            branche: Branche für Default-Design
            company_data: Firmendaten (Adresse, Telefon, etc.)
            output_dir: Zielverzeichnis für STYLE-GUIDE.md
            on_message: Callback für Streaming-Messages

        Returns:
            StyleGuideResult mit Farben, Fonts, Team-Infos etc.
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        prompt = self._build_prompt(
            company_name=company_name,
            website_url=website_url,
            branche=branche,
            company_data=company_data,
            output_dir=output_dir
        )

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            return StyleGuideResult(success=False, error=error)

        # Parse das Ergebnis und extrahiere strukturierte Daten
        return self._parse_result(result_text, output_dir)

    def _build_prompt(
        self,
        company_name: str,
        website_url: Optional[str],
        branche: str,
        company_data: dict,
        output_dir: Path
    ) -> str:
        """Baut den Task-Prompt für den Agent."""

        company_info = self._format_company_data(company_data)

        return f"""
## AUFGABE

Analysiere und erstelle einen vollständigen Style Guide für: **{company_name}**

## KONTEXT

- **Branche:** {branche}
- **Website:** {website_url or 'Keine Website vorhanden - Design nach Branche erstellen'}
- **Output-Verzeichnis:** {output_dir}

## FIRMENDATEN

{company_info}

## SCHRITTE

1. **Falls Website vorhanden ({website_url}):**
   - Öffne die Website mit Playwright
   - Extrahiere alle Farben (Hex-Codes)
   - Identifiziere Schriftarten
   - Finde Team-Seite und extrahiere Team-Mitglieder mit Foto-URLs
   - Extrahiere Services/Leistungen
   - Finde Impressum und Datenschutz Texte
   - Lade Logo herunter

2. **Falls keine Website:**
   - Erstelle branchenspezifisches Design
   - Recherchiere Firma auf Google/Social Media für Bilder

3. **Erstelle STYLE-GUIDE.md in {output_dir}/ mit:**
   - Farbpalette (Hex-Codes mit Verwendungszweck)
   - Typografie (Schriftart, Größen)
   - Firmendaten (für Impressum)
   - Team-Mitglieder (Name, Rolle, Foto-URL)
   - Services/Leistungen
   - Kreative Design-Empfehlungen

## OUTPUT-FORMAT

Die STYLE-GUIDE.md MUSS diese Sektionen enthalten:

```markdown
# Style Guide - [Firmenname]

## Firmeninfos
| Feld | Wert |
|------|------|
| Name | ... |
| Adresse | ... |
| Telefon | ... |
| E-Mail | ... |

## Farbpalette
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Primärfarbe | #xxx | Buttons, Akzente |
| Sekundärfarbe | #xxx | CTAs, Highlights |
| ...

## Typografie
| Typ | Schrift | Verwendung |
|-----|---------|------------|
| Headlines | ... | H1, H2, H3 |
| Body | ... | Fließtext |

## Team
| Name | Position | Foto-URL |
|------|----------|----------|
| ... | ... | https://... |

## Services
- Service 1: Beschreibung
- Service 2: Beschreibung

## Kreative Design-Empfehlungen
1. Layout-Konzept: ...
2. Signature-Effekt: ...
3. Animations-Level: ...
```

**WICHTIG:** Erstelle die Datei WIRKLICH in {output_dir}/STYLE-GUIDE.md!
"""

    def _format_company_data(self, data: dict) -> str:
        """Formatiert Firmendaten für den Prompt."""
        lines = []
        for key, value in data.items():
            if value:
                lines.append(f"- **{key}:** {value}")
        return "\n".join(lines) if lines else "- Keine Firmendaten vorhanden"

    def _parse_result(self, text: str, output_dir: Path) -> StyleGuideResult:
        """
        Parsed das Agent-Ergebnis und extrahiert strukturierte Daten.

        Liest die erstellte STYLE-GUIDE.md und extrahiert:
        - Farben
        - Fonts
        - Team-Mitglieder
        - Services
        """
        style_guide_path = output_dir / "STYLE-GUIDE.md"

        # Prüfe ob Style Guide erstellt wurde
        if not style_guide_path.exists():
            return StyleGuideResult(
                success=False,
                error="STYLE-GUIDE.md wurde nicht erstellt"
            )

        content = style_guide_path.read_text(encoding="utf-8")

        # Extrahiere strukturierte Daten aus der Markdown-Datei
        result = StyleGuideResult(
            success=True,
            style_guide_path=str(style_guide_path)
        )

        # Farben extrahieren
        result.colors = self._extract_colors(content)

        # Fonts extrahieren
        result.fonts = self._extract_fonts(content)

        # Team extrahieren
        result.team_members = self._extract_team(content)

        # Services extrahieren
        result.services = self._extract_services(content)

        # Firmendaten extrahieren
        result.company_data = self._extract_company_data(content)

        # Logo-URL extrahieren
        result.logo_url = self._extract_logo_url(content)

        return result

    def _extract_colors(self, content: str) -> dict:
        """Extrahiert Farben aus dem Style Guide."""
        colors = {}

        # Suche nach Hex-Farben im Farbpalette-Bereich
        color_section = re.search(
            r'##\s*Farbpalette.*?(?=##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )

        if color_section:
            section_text = color_section.group()

            # Pattern für Tabellenzeilen: | Name | #xxx | Verwendung |
            rows = re.findall(
                r'\|\s*([^|]+)\s*\|\s*(#[0-9A-Fa-f]{3,6})\s*\|',
                section_text
            )

            for name, hex_color in rows:
                name = name.strip().lower()
                if 'primär' in name or 'primary' in name:
                    colors['primary'] = hex_color
                elif 'sekundär' in name or 'secondary' in name:
                    colors['secondary'] = hex_color
                elif 'text' in name:
                    colors['text'] = hex_color
                elif 'hintergrund' in name or 'background' in name:
                    colors['background'] = hex_color
                else:
                    colors[name] = hex_color

        return colors

    def _extract_fonts(self, content: str) -> dict:
        """Extrahiert Fonts aus dem Style Guide."""
        fonts = {}

        # Suche nach Typografie-Bereich
        font_section = re.search(
            r'##\s*Typografie.*?(?=##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )

        if font_section:
            section_text = font_section.group()

            # Pattern für Tabellenzeilen
            rows = re.findall(
                r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|',
                section_text
            )

            for typ, font in rows:
                typ = typ.strip().lower()
                font = font.strip()
                if 'headline' in typ or 'heading' in typ:
                    fonts['heading'] = font
                elif 'body' in typ or 'fließtext' in typ:
                    fonts['body'] = font

        return fonts

    def _extract_team(self, content: str) -> list:
        """Extrahiert Team-Mitglieder aus dem Style Guide."""
        team = []

        # Suche nach Team-Bereich
        team_section = re.search(
            r'##\s*Team.*?(?=##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )

        if team_section:
            section_text = team_section.group()

            # Pattern für Tabellenzeilen: | Name | Position | Foto-URL |
            rows = re.findall(
                r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*(https?://[^|\s]+)\s*\|',
                section_text
            )

            for name, position, photo_url in rows:
                name = name.strip()
                position = position.strip()
                photo_url = photo_url.strip()

                if name and name != 'Name' and name != '---':
                    team.append({
                        'name': name,
                        'position': position,
                        'photo_url': photo_url
                    })

        return team

    def _extract_services(self, content: str) -> list:
        """Extrahiert Services aus dem Style Guide."""
        services = []

        # Suche nach Services-Bereich
        services_section = re.search(
            r'##\s*Services.*?(?=##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )

        if services_section:
            section_text = services_section.group()

            # Pattern für Listeneinträge: - Service: Beschreibung
            items = re.findall(
                r'-\s*\*?\*?([^:*]+)\*?\*?:\s*(.+)',
                section_text
            )

            for title, description in items:
                services.append({
                    'title': title.strip(),
                    'description': description.strip()
                })

        return services

    def _extract_company_data(self, content: str) -> dict:
        """Extrahiert Firmendaten aus dem Style Guide."""
        company_data = {}

        # Suche nach Firmeninfos-Bereich
        company_section = re.search(
            r'##\s*Firmeninfos.*?(?=##|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )

        if company_section:
            section_text = company_section.group()

            # Pattern für Tabellenzeilen: | Feld | Wert |
            rows = re.findall(
                r'\|\s*\*?\*?([^|*]+)\*?\*?\s*\|\s*([^|]+)\s*\|',
                section_text
            )

            for field, value in rows:
                field = field.strip().lower()
                value = value.strip()

                if value and value != '---' and field != 'feld':
                    if 'name' in field:
                        company_data['name'] = value
                    elif 'adresse' in field:
                        company_data['address'] = value
                    elif 'telefon' in field:
                        company_data['phone'] = value
                    elif 'e-mail' in field or 'email' in field:
                        company_data['email'] = value

        return company_data

    def _extract_logo_url(self, content: str) -> Optional[str]:
        """Extrahiert Logo-URL aus dem Style Guide."""
        # Suche nach Logo-URL Pattern
        logo_match = re.search(
            r'Logo[^:]*:\s*(https?://[^\s\)]+)',
            content,
            re.IGNORECASE
        )

        if logo_match:
            return logo_match.group(1)

        return None
