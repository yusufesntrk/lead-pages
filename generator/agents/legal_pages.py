"""
Legal Pages Agent - Erstellt Impressum und Datenschutz.

Generiert rechtlich konforme Seiten basierend auf den
Firmendaten aus dem Style Guide.
"""

import re
from pathlib import Path
from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import LegalPagesResult


class LegalPagesAgent(BaseAgent):
    """
    Erstellt Impressum und Datenschutz Seiten.

    Der LegalPages-Agent bekommt NUR Firmendaten:
    - Name, Adresse, Kontakt
    - Geschäftsführer/Inhaber
    - Berufsrechtliche Angaben (falls relevant)

    NICHT: Design-Vorgaben (verwendet bestehendes CSS)
    """

    @property
    def agent_name(self) -> str:
        return "legal_pages"

    async def create(
        self,
        company_name: str,
        company_data: dict,
        branche: str,
        output_dir: Path | str,
        impressum_text: Optional[str] = None,
        datenschutz_text: Optional[str] = None,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> LegalPagesResult:
        """
        Erstellt Impressum und Datenschutz.

        Args:
            company_name: Firmenname
            company_data: Firmendaten (Adresse, Telefon, etc.)
            branche: Branche (für berufsrechtliche Angaben)
            output_dir: Zielverzeichnis
            impressum_text: Optional - Original-Impressum von alter Website
            datenschutz_text: Optional - Original-Datenschutz von alter Website
            on_message: Callback für Streaming-Messages

        Returns:
            LegalPagesResult mit erstellten Seiten
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        prompt = self._build_prompt(
            company_name=company_name,
            company_data=company_data,
            branche=branche,
            output_dir=output_dir,
            impressum_text=impressum_text,
            datenschutz_text=datenschutz_text
        )

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            # Bei Content-Filter: Fallback verwenden
            if "content filtering" in error.lower() or "blocked" in error.lower():
                return await self._create_fallback(company_name, company_data, output_dir)
            return LegalPagesResult(success=False, error=error)

        return self._parse_result(output_dir)

    def _build_prompt(
        self,
        company_name: str,
        company_data: dict,
        branche: str,
        output_dir: Path,
        impressum_text: Optional[str],
        datenschutz_text: Optional[str]
    ) -> str:
        """Baut den Task-Prompt für den Agent."""

        # Formatiere Firmendaten
        company_text = self._format_company_data(company_data)

        # Original-Texte Section
        original_section = ""
        if impressum_text:
            original_section += f"""
### Original-Impressum (von alter Website)

{impressum_text[:2000]}
"""
        if datenschutz_text:
            original_section += f"""
### Original-Datenschutz (von alter Website)

{datenschutz_text[:2000]}
"""

        # Branchenspezifische Hinweise
        branche_hints = self._get_branche_hints(branche)

        return f"""
## AUFGABE

Erstelle Impressum und Datenschutz für: **{company_name}**

## KONTEXT

- **Branche:** {branche}
- **Output-Verzeichnis:** {output_dir}

## FIRMENDATEN

{company_text}

{original_section}

## BRANCHENSPEZIFISCHE ANFORDERUNGEN

{branche_hints}

## OUTPUT

Erstelle diese Dateien in {output_dir}/:

1. **impressum.html**
   - Angaben gemäß § 5 TMG
   - Vollständige Kontaktdaten
   - Verantwortlicher für den Inhalt
   - Streitschlichtung
   - Haftung für Inhalte und Links

2. **datenschutz.html**
   - Verantwortlicher
   - Datenerfassung auf dieser Website
   - Server-Log-Dateien
   - Kontaktformular (falls vorhanden)
   - Externe Dienste (Google Maps, Fonts)
   - Rechte der Betroffenen

## WICHTIG

- Verwende bestehendes styles.css
- Konsistente Navigation wie andere Seiten
- KEINE Platzhalter - alle Texte final
- Deutsche Umlaute verwenden (ä, ö, ü, ß)
- HTML-Kommentar am Ende: <!-- Entwurf -->
"""

    def _format_company_data(self, data: dict) -> str:
        """Formatiert Firmendaten für den Prompt."""
        if not data:
            return "- Keine Firmendaten vorhanden"

        lines = []
        field_names = {
            'name': 'Firmenname',
            'strasse': 'Straße',
            'plz': 'PLZ',
            'ort': 'Ort',
            'telefon': 'Telefon',
            'email': 'E-Mail',
            'address': 'Adresse',
            'phone': 'Telefon',
            'inhaber': 'Inhaber',
            'geschaeftsfuehrer': 'Geschäftsführer',
            'ust_id': 'USt-IdNr.',
        }

        for key, value in data.items():
            if value:
                display_name = field_names.get(key, key.title())
                lines.append(f"- **{display_name}:** {value}")

        return "\n".join(lines) if lines else "- Keine Firmendaten vorhanden"

    def _get_branche_hints(self, branche: str) -> str:
        """Gibt branchenspezifische Hinweise für Legal Pages."""
        branche_lower = branche.lower() if branche else ""

        if "anwalt" in branche_lower or "rechtsanwalt" in branche_lower:
            return """
- Berufsbezeichnung und Kammer angeben
- Berufsrechtliche Regelungen verlinken (BRAO, BORA)
- Berufshaftpflichtversicherung erwähnen
"""
        elif "arzt" in branche_lower or "zahnarzt" in branche_lower:
            return """
- Approbation und zuständige Kammer angeben
- Berufsordnung verlinken
- Berufshaftpflicht erwähnen
"""
        elif "steuerberater" in branche_lower:
            return """
- Berufsbezeichnung und Kammer angeben
- Steuerberaterkammer verlinken
- Berufshaftpflicht erwähnen
"""
        else:
            return "- Standard-Impressum ohne besondere berufsrechtliche Angaben"

    def _parse_result(self, output_dir: Path) -> LegalPagesResult:
        """
        Analysiert die erstellten Legal Pages.

        Prüft auf Platzhalter und fehlende Seiten.
        """
        result = LegalPagesResult(success=True)

        # Prüfe welche Seiten erstellt wurden
        expected_pages = ["impressum.html", "datenschutz.html"]

        for page in expected_pages:
            page_path = output_dir / page
            if page_path.exists():
                result.pages_created.append(page)

                # Prüfe auf Platzhalter
                content = page_path.read_text(encoding="utf-8")
                placeholders = re.findall(
                    r'\{\{[^}]+\}\}|\[[A-Z_]+\]|\[HIER[^\]]*\]',
                    content
                )
                result.placeholders_found += len(placeholders)

        # Warnung wenn Seiten fehlen
        if len(result.pages_created) < len(expected_pages):
            missing = set(expected_pages) - set(result.pages_created)
            result.error = f"Fehlende Seiten: {', '.join(missing)}"

        # Warnung wenn Platzhalter gefunden
        if result.placeholders_found > 0:
            result.success = False
            result.error = f"{result.placeholders_found} Platzhalter gefunden!"

        return result

    async def _create_fallback(
        self,
        company_name: str,
        company_data: dict,
        output_dir: Path
    ) -> LegalPagesResult:
        """
        Erstellt Fallback Legal Pages bei Content-Filter.

        Verwendet minimale Templates die immer funktionieren.
        """
        result = LegalPagesResult(
            success=True,
            used_fallback=True
        )

        # Adresse zusammenbauen
        address_parts = []
        if company_data.get('strasse'):
            address_parts.append(company_data['strasse'])
        if company_data.get('plz') or company_data.get('ort'):
            address_parts.append(
                f"{company_data.get('plz', '')} {company_data.get('ort', '')}".strip()
            )
        address = "<br>".join(address_parts) if address_parts else "Adresse nicht angegeben"

        telefon = company_data.get('telefon', '')
        email = company_data.get('email', '')

        # Lese Header/Footer aus index.html wenn vorhanden
        index_path = output_dir / "index.html"
        header_html = f'<header><a href="index.html">{company_name}</a></header>'
        footer_html = f'<footer><p>© {company_name}</p></footer>'

        if index_path.exists():
            index_content = index_path.read_text(encoding="utf-8")
            header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
            if header_match:
                header_html = header_match.group(1)
            footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
            if footer_match:
                footer_html = footer_match.group(1)

        # Impressum
        impressum_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Impressum | {company_name}</title>
    <meta name="robots" content="noindex, follow">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    {header_html}
    <main class="legal-page">
        <div class="container">
            <h1>Impressum</h1>
            <h2>Angaben gemäß § 5 TMG</h2>
            <p><strong>{company_name}</strong><br>{address}</p>
            <h2>Kontakt</h2>
            <p>
                {f'Telefon: <a href="tel:{telefon}">{telefon}</a><br>' if telefon else ''}
                {f'E-Mail: <a href="mailto:{email}">{email}</a>' if email else ''}
            </p>
            <h2>Haftung für Inhalte</h2>
            <p>Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich.</p>
        </div>
    </main>
    {footer_html}
    <!-- Entwurf - Fallback-Template -->
</body>
</html>'''

        # Datenschutz
        datenschutz_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datenschutz | {company_name}</title>
    <meta name="robots" content="noindex, follow">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    {header_html}
    <main class="legal-page">
        <div class="container">
            <h1>Datenschutzerklärung</h1>
            <h2>1. Verantwortlicher</h2>
            <p><strong>{company_name}</strong><br>{address}</p>
            <h2>2. Datenerfassung</h2>
            <p>Beim Besuch dieser Website werden automatisch Informationen in Server-Log-Dateien gespeichert.</p>
            <h2>3. Ihre Rechte</h2>
            <p>Sie haben jederzeit das Recht auf Auskunft über Ihre gespeicherten Daten.</p>
        </div>
    </main>
    {footer_html}
    <!-- Entwurf - Fallback-Template -->
</body>
</html>'''

        # Dateien schreiben
        (output_dir / "impressum.html").write_text(impressum_html, encoding="utf-8")
        (output_dir / "datenschutz.html").write_text(datenschutz_html, encoding="utf-8")

        result.pages_created = ["impressum.html", "datenschutz.html"]

        return result
