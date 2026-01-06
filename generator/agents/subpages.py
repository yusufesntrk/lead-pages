"""
Subpages Agent - Erstellt alle Unterseiten der Website.

Generiert Kontakt, Über uns, Service-Seiten etc. basierend auf
dem Style Guide mit konsistentem Design zur Homepage.
"""

import re
from pathlib import Path
from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import SubpagesResult


class SubpagesAgent(BaseAgent):
    """
    Erstellt alle Unterseiten basierend auf Style Guide.

    Der Subpages-Agent bekommt:
    - Liste der zu erstellenden Seiten
    - Design-Vorgaben (Farben, Fonts) für Konsistenz
    - Services und Team-Daten

    Er verwendet das bestehende styles.css der Homepage.
    """

    @property
    def agent_name(self) -> str:
        return "subpages"

    async def create(
        self,
        company_name: str,
        branche: str,
        pages_to_create: list[str],
        services: list,
        team_members: list,
        company_data: dict,
        output_dir: Path | str,
        style_guide_content: str = "",
        on_message: Optional[Callable[[Any], None]] = None
    ) -> SubpagesResult:
        """
        Erstellt alle Unterseiten.

        Args:
            company_name: Firmenname
            branche: Branche
            pages_to_create: Liste der zu erstellenden Seiten ["kontakt", "ueber-uns", ...]
            services: Liste der Services
            team_members: Team-Mitglieder
            company_data: Firmendaten (Adresse, Telefon, etc.)
            output_dir: Zielverzeichnis
            style_guide_content: Optional - vollständiger Style Guide Text
            on_message: Callback für Streaming-Messages

        Returns:
            SubpagesResult mit erstellten Seiten
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        prompt = self._build_prompt(
            company_name=company_name,
            branche=branche,
            pages_to_create=pages_to_create,
            services=services,
            team_members=team_members,
            company_data=company_data,
            output_dir=output_dir,
            style_guide_content=style_guide_content
        )

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            return SubpagesResult(success=False, error=error)

        return self._parse_result(output_dir, pages_to_create)

    def _build_prompt(
        self,
        company_name: str,
        branche: str,
        pages_to_create: list[str],
        services: list,
        team_members: list,
        company_data: dict,
        output_dir: Path,
        style_guide_content: str
    ) -> str:
        """Baut den Task-Prompt für den Agent."""

        # Formatiere zu erstellende Seiten
        pages_text = self._format_pages(pages_to_create, branche)

        # Formatiere Services
        services_text = self._format_services(services)

        # Formatiere Team
        team_text = self._format_team(team_members)

        # Formatiere Firmendaten
        company_text = self._format_company_data(company_data)

        # Style Guide (gekürzt wenn zu lang)
        if style_guide_content and len(style_guide_content) > 2000:
            style_guide_section = f"""
## STYLE GUIDE (Zusammenfassung)

{style_guide_content[:2000]}...
"""
        elif style_guide_content:
            style_guide_section = f"""
## STYLE GUIDE

{style_guide_content}
"""
        else:
            style_guide_section = ""

        return f"""
## AUFGABE

Erstelle alle Unterseiten für: **{company_name}**

## KONTEXT

- **Branche:** {branche}
- **Output-Verzeichnis:** {output_dir}

## ZU ERSTELLENDE SEITEN

{pages_text}

## FIRMENDATEN

{company_text}

## SERVICES

{services_text}

## TEAM

{team_text}

{style_guide_section}

## WICHTIG

1. **Verwende bestehendes styles.css** - erweitere es nur bei Bedarf
2. **Konsistente Navigation** auf allen Seiten
3. **Logo verlinkt auf index.html** (NICHT "/")
4. **Mindestens ein CTA** pro Seite
5. **Footer identisch** auf allen Seiten
6. **Google Maps** - suche zuerst die echte Business-URL!
7. **Keine Platzhalter** - alle Texte final
8. **Deutsche Umlaute** verwenden (ä, ö, ü, ß)
"""

    def _format_pages(self, pages: list[str], branche: str) -> str:
        """Formatiert die zu erstellenden Seiten."""
        if not pages:
            # Default-Seiten basierend auf Branche
            default_pages = ["kontakt"]
            if branche in ["Restaurant", "Café", "Gastronomie"]:
                default_pages.extend(["speisekarte"])
            else:
                default_pages.extend(["ueber-uns"])
            pages = default_pages

        lines = []
        for page in pages:
            if page == "kontakt":
                lines.append(f"- **kontakt.html**: Kontaktformular, Adresse, Telefon, Öffnungszeiten, Google Maps")
            elif page == "ueber-uns" or page == "about":
                lines.append(f"- **ueber-uns.html**: Firmengeschichte, Werte, Team-Übersicht")
            elif page == "team":
                lines.append(f"- **team.html**: Detaillierte Team-Vorstellung mit Fotos und Biografie")
            elif page == "speisekarte":
                lines.append(f"- **speisekarte.html**: Menü mit Kategorien und Preisen")
            else:
                lines.append(f"- **{page}.html**: Detailseite für {page}")

        return "\n".join(lines)

    def _format_services(self, services: list) -> str:
        """Formatiert Services für den Prompt."""
        if not services:
            return "- Keine Services definiert"

        lines = []
        for i, service in enumerate(services, 1):
            title = service.get('title', f'Service {i}')
            description = service.get('description', '')
            lines.append(f"{i}. **{title}**: {description}")
        return "\n".join(lines)

    def _format_team(self, team_members: list) -> str:
        """Formatiert Team für den Prompt."""
        if not team_members:
            return "- Kein Team definiert"

        lines = []
        for member in team_members:
            name = member.get('name', 'Unbekannt')
            position = member.get('position', '')
            photo = member.get('photo_url', '')
            lines.append(f"- **{name}** ({position})")
            if photo:
                lines.append(f"  Foto: {photo}")
        return "\n".join(lines)

    def _format_company_data(self, data: dict) -> str:
        """Formatiert Firmendaten für den Prompt."""
        if not data:
            return "- Keine Firmendaten vorhanden"

        lines = []
        field_names = {
            'strasse': 'Straße',
            'plz': 'PLZ',
            'ort': 'Ort',
            'telefon': 'Telefon',
            'email': 'E-Mail',
            'name': 'Firmenname',
            'address': 'Adresse',
            'phone': 'Telefon',
        }

        for key, value in data.items():
            if value:
                display_name = field_names.get(key, key.title())
                lines.append(f"- **{display_name}:** {value}")

        return "\n".join(lines) if lines else "- Keine Firmendaten vorhanden"

    def _parse_result(self, output_dir: Path, expected_pages: list[str]) -> SubpagesResult:
        """
        Analysiert die erstellten Unterseiten.

        Prüft welche Seiten erstellt wurden und zählt die Sektionen.
        """
        result = SubpagesResult(success=True)

        # Prüfe welche Seiten erstellt wurden
        html_files = list(output_dir.glob("*.html"))

        for html_file in html_files:
            # Ignoriere index.html (Homepage)
            if html_file.name == "index.html":
                continue

            result.pages_created.append(html_file.name)

            # Zähle Sektionen
            content = html_file.read_text(encoding="utf-8")
            sections = re.findall(r'<section[^>]*>', content, re.IGNORECASE)
            result.total_sections += len(sections)

        # Warnung wenn keine Seiten erstellt wurden
        if not result.pages_created:
            result.success = False
            result.error = "Keine Unterseiten wurden erstellt"

        return result
