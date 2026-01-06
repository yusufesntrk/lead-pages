"""
Homepage Agent - Erstellt die Hauptseite der Website.

Generiert index.html, styles.css und script.js basierend auf
dem Style Guide mit modernem, einzigartigem Design.
"""

import re
from pathlib import Path
from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import HomepageResult


class HomepageAgent(BaseAgent):
    """
    Erstellt die Homepage basierend auf Style Guide.

    Der Homepage-Agent bekommt NUR die relevanten Daten:
    - Farben und Fonts aus dem Style Guide
    - Firmenname und Branche
    - Hero-Content und Services

    NICHT: Gesamten Style Guide Text (zu viel Kontext!)
    """

    @property
    def agent_name(self) -> str:
        return "homepage"

    async def create(
        self,
        company_name: str,
        branche: str,
        colors: dict,
        fonts: dict,
        hero_content: dict,
        services: list,
        team_members: list,
        output_dir: Path | str,
        style_guide_content: str = "",
        on_message: Optional[Callable[[Any], None]] = None
    ) -> HomepageResult:
        """
        Erstellt die Homepage.

        Args:
            company_name: Firmenname
            branche: Branche (für Design-Entscheidungen)
            colors: Farbpalette {"primary": "#xxx", "secondary": "#xxx", ...}
            fonts: Schriftarten {"heading": "Inter", "body": "Inter"}
            hero_content: Hero-Texte {"headline": "...", "subtext": "...", "cta": "..."}
            services: Liste der Services [{"title": "...", "description": "..."}]
            team_members: Team-Mitglieder [{"name": "...", "position": "...", "photo_url": "..."}]
            output_dir: Zielverzeichnis für HTML/CSS/JS
            style_guide_content: Optional - vollständiger Style Guide Text
            on_message: Callback für Streaming-Messages

        Returns:
            HomepageResult mit erstellten Dateien und Sektionen
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        prompt = self._build_prompt(
            company_name=company_name,
            branche=branche,
            colors=colors,
            fonts=fonts,
            hero_content=hero_content,
            services=services,
            team_members=team_members,
            output_dir=output_dir,
            style_guide_content=style_guide_content
        )

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            return HomepageResult(success=False, error=error)

        return self._parse_result(output_dir)

    def _build_prompt(
        self,
        company_name: str,
        branche: str,
        colors: dict,
        fonts: dict,
        hero_content: dict,
        services: list,
        team_members: list,
        output_dir: Path,
        style_guide_content: str
    ) -> str:
        """Baut den Task-Prompt für den Agent."""

        # Formatiere Farben
        colors_text = self._format_colors(colors)

        # Formatiere Fonts
        fonts_text = self._format_fonts(fonts)

        # Formatiere Services
        services_text = self._format_services(services)

        # Formatiere Team
        team_text = self._format_team(team_members)

        # Hero Content
        hero_text = self._format_hero(hero_content)

        # Style Guide (gekürzt wenn zu lang)
        if style_guide_content and len(style_guide_content) > 3000:
            style_guide_section = f"""
## STYLE GUIDE (Zusammenfassung)

{style_guide_content[:3000]}...

[Gekürzt - vollständiger Style Guide in {output_dir}/STYLE-GUIDE.md]
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

Erstelle die Homepage für: **{company_name}**

## KONTEXT

- **Branche:** {branche}
- **Output-Verzeichnis:** {output_dir}

## DESIGN-VORGABEN

### Farbpalette
{colors_text}

### Typografie
{fonts_text}

## INHALTE

### Hero-Sektion
{hero_text}

### Services
{services_text}

### Team
{team_text}

{style_guide_section}

## OUTPUT

Erstelle diese Dateien in {output_dir}/:

1. **index.html** - Vollständige Homepage mit:
   - Hero-Sektion
   - Vertrauenssignale
   - Services-Übersicht
   - Über uns Teaser
   - Team Preview (falls Team vorhanden)
   - CTA-Sektion
   - Footer

2. **styles.css** - Modernes CSS mit:
   - CSS Custom Properties für Farben
   - Responsive Design (Mobile First)
   - Hover-Animationen

3. **script.js** - JavaScript für:
   - Mobile Navigation
   - Smooth Scroll
   - Scroll-Reveal Animationen

## WICHTIG

- Modernes, einzigartiges Design (KEIN Template-Look!)
- Jede Sektion visuell unterschiedlich
- Responsive für alle Geräte
- Deutsche Umlaute verwenden (ä, ö, ü, ß)
- Logo auf index.html verlinken (NICHT "/")
- Lokale Bild-Pfade (assets/...)
"""

    def _format_colors(self, colors: dict) -> str:
        """Formatiert Farben für den Prompt."""
        if not colors:
            return "- Keine Farben definiert (erstelle passend zur Branche)"

        lines = []
        for name, value in colors.items():
            lines.append(f"- **{name}:** {value}")
        return "\n".join(lines)

    def _format_fonts(self, fonts: dict) -> str:
        """Formatiert Fonts für den Prompt."""
        if not fonts:
            return "- Keine Fonts definiert (verwende Inter)"

        lines = []
        for name, value in fonts.items():
            lines.append(f"- **{name}:** {value}")
        return "\n".join(lines)

    def _format_services(self, services: list) -> str:
        """Formatiert Services für den Prompt."""
        if not services:
            return "- Keine Services definiert (erstelle passend zur Branche)"

        lines = []
        for i, service in enumerate(services, 1):
            title = service.get('title', f'Service {i}')
            description = service.get('description', '')
            lines.append(f"{i}. **{title}**: {description}")
        return "\n".join(lines)

    def _format_team(self, team_members: list) -> str:
        """Formatiert Team für den Prompt."""
        if not team_members:
            return "- Kein Team definiert (Team-Sektion weglassen)"

        lines = []
        for member in team_members:
            name = member.get('name', 'Unbekannt')
            position = member.get('position', '')
            photo = member.get('photo_url', '')
            lines.append(f"- **{name}** ({position})")
            if photo:
                lines.append(f"  Foto: {photo}")
        return "\n".join(lines)

    def _format_hero(self, hero_content: dict) -> str:
        """Formatiert Hero-Content für den Prompt."""
        if not hero_content:
            return "- Keine Hero-Texte definiert (erstelle passend zur Branche)"

        lines = []
        if hero_content.get('headline'):
            lines.append(f"- **Headline:** {hero_content['headline']}")
        if hero_content.get('subtext'):
            lines.append(f"- **Subtext:** {hero_content['subtext']}")
        if hero_content.get('cta'):
            lines.append(f"- **CTA:** {hero_content['cta']}")
        return "\n".join(lines) if lines else "- Keine Hero-Texte definiert"

    def _parse_result(self, output_dir: Path) -> HomepageResult:
        """
        Analysiert die erstellten Dateien.

        Prüft welche Dateien erstellt wurden und welche
        Sektionen in der Homepage vorhanden sind.
        """
        result = HomepageResult(success=True)

        # Prüfe welche Dateien erstellt wurden
        expected_files = ["index.html", "styles.css", "script.js"]
        for filename in expected_files:
            filepath = output_dir / filename
            if filepath.exists():
                result.files_created.append(filename)

        # Wenn index.html nicht existiert, ist es ein Fehler
        index_path = output_dir / "index.html"
        if not index_path.exists():
            return HomepageResult(
                success=False,
                error="index.html wurde nicht erstellt"
            )

        # Analysiere index.html
        content = index_path.read_text(encoding="utf-8")

        # Erkenne Sektionen
        section_patterns = {
            "hero": [r'<section[^>]*class="[^"]*hero', r'id="hero"', r'class="hero'],
            "services": [r'<section[^>]*class="[^"]*service', r'id="services"'],
            "team": [r'<section[^>]*class="[^"]*team', r'id="team"'],
            "about": [r'<section[^>]*class="[^"]*about', r'id="about"', r'über uns'],
            "testimonials": [r'testimonial', r'review', r'rating'],
            "cta": [r'<section[^>]*class="[^"]*cta', r'id="cta"'],
            "contact": [r'<section[^>]*class="[^"]*contact', r'id="contact"'],
        }

        for section_name, patterns in section_patterns.items():
            for pattern in patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    result.sections_created.append(section_name)
                    break

        # Zähle CTAs
        cta_patterns = [
            r'<a[^>]*class="[^"]*btn[^"]*"',
            r'<button[^>]*class="[^"]*btn',
            r'<a[^>]*class="[^"]*cta',
        ]
        for pattern in cta_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            result.cta_count += len(matches)

        # Prüfe auf Hero, Footer, Navigation
        result.has_hero = "hero" in result.sections_created
        result.has_footer = bool(re.search(r'<footer', content, re.IGNORECASE))
        result.has_navigation = bool(re.search(r'<nav|<header', content, re.IGNORECASE))

        return result
