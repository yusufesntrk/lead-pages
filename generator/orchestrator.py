"""
Lead Pages Generator - Orchestrator

Koordiniert alle spezialisierten Agents in der richtigen Reihenfolge
und verwaltet den Kontext zwischen den Agents.
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from claude_code_sdk import query, ClaudeCodeOptions

from .agents.definitions import AGENTS


@dataclass
class Lead:
    """Daten eines Leads aus Airtable"""
    id: str
    firma: str
    branche: str
    website: Optional[str] = None
    strasse: Optional[str] = None
    plz: Optional[str] = None
    ort: Optional[str] = None
    telefon: Optional[str] = None
    email: Optional[str] = None
    google_rating: Optional[float] = None
    google_reviews: Optional[int] = None


@dataclass
class GeneratorContext:
    """Geteilter Kontext zwischen allen Agents"""
    lead: Lead
    output_dir: Path
    style_guide_path: Optional[Path] = None
    style_guide_content: str = ""
    created_files: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    review_feedback: list[str] = field(default_factory=list)
    iteration: int = 0
    max_iterations: int = 3


class LeadPagesOrchestrator:
    """
    Orchestrator für den Lead Pages Generator.

    Ruft spezialisierte Agents in der richtigen Reihenfolge auf
    und übergibt Kontext zwischen den Schritten.
    """

    def __init__(self, lead: Lead, base_output_dir: str = "docs"):
        self.lead = lead
        self.output_dir = Path(base_output_dir) / self._slugify(lead.firma)
        self.context = GeneratorContext(
            lead=lead,
            output_dir=self.output_dir
        )

    def _slugify(self, text: str) -> str:
        """Konvertiert Text zu URL-sicherem Slug"""
        # Umlaute ersetzen für Dateipfade
        replacements = {
            'ä': 'ae', 'ö': 'oe', 'ü': 'ue',
            'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
            'ß': 'ss'
        }
        slug = text.lower()
        for old, new in replacements.items():
            slug = slug.replace(old, new)
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        return slug.strip('-')

    async def _run_agent(
        self,
        agent_name: str,
        task_prompt: str,
        additional_context: str = ""
    ) -> str:
        """
        Führt einen einzelnen Agent aus.

        Args:
            agent_name: Name des Agents aus AGENTS dict
            task_prompt: Spezifische Aufgabe für diesen Aufruf
            additional_context: Zusätzlicher Kontext (z.B. vorherige Ergebnisse)

        Returns:
            Ergebnis-Text des Agents
        """
        agent_def = AGENTS.get(agent_name)
        if not agent_def:
            raise ValueError(f"Agent '{agent_name}' nicht gefunden")

        print(f"\n{'='*60}")
        print(f"🤖 AGENT: {agent_name}")
        print(f"📋 Task: {task_prompt[:100]}...")
        print(f"{'='*60}\n")

        # Baue vollständigen Prompt mit Kontext
        full_prompt = f"""
{agent_def.prompt}

---
AKTUELLER TASK:
{task_prompt}

---
KONTEXT:
- Firma: {self.context.lead.firma}
- Branche: {self.context.lead.branche}
- Website: {self.context.lead.website or 'Keine'}
- Output-Verzeichnis: {self.context.output_dir}

{additional_context}
"""

        options = ClaudeCodeOptions(
            allowed_tools=agent_def.tools or [],
            model=agent_def.model,
            cwd=str(self.context.output_dir.parent.parent),  # Projekt-Root
            permission_mode="bypassPermissions",
        )

        result_text = ""
        max_retries = 2
        retry_count = 0

        while retry_count <= max_retries:
            try:
                async for msg in query(prompt=full_prompt, options=options):
                    # Text-Blöcke verarbeiten
                    if hasattr(msg, 'content'):
                        for block in msg.content:
                            if hasattr(block, 'text'):
                                result_text += block.text
                                print(block.text, end="", flush=True)

                    # Result Message für Stats
                    if hasattr(msg, 'total_cost_usd'):
                        print(f"\n✅ Agent fertig (${msg.total_cost_usd:.6f})")

                # Erfolg - aus der Schleife brechen
                break

            except Exception as e:
                error_str = str(e)
                retry_count += 1

                # Bestimmte Fehler sind nicht retry-fähig
                non_retryable = [
                    "content filtering policy",
                    "rate_limit",
                    "authentication",
                ]

                is_retryable = not any(err in error_str.lower() for err in non_retryable)

                if is_retryable and retry_count <= max_retries:
                    print(f"\n⚠️ Agent-Fehler (Retry {retry_count}/{max_retries}): {e}")
                    # Bei Bild-Fehlern: Prompt anpassen
                    if "Could not process image" in error_str or "buffer size" in error_str:
                        full_prompt += "\n\n⚠️ WICHTIG: Das vorherige Bild/PDF hat nicht funktioniert! Suche ALTERNATIVE Bilder: andere Formate, andere Seiten der Website, Google Images, oder Social Media. Versuche es NICHT nochmal mit dem gleichen Bild!"
                    continue
                else:
                    print(f"\n❌ Agent-Fehler: {e}")
                    self.context.errors.append(f"{agent_name}: {error_str}")
                    raise

        print()  # Neue Zeile am Ende
        return result_text

    async def run_style_guide_agent(self) -> str:
        """Agent 1: Style Guide erstellen"""
        task = f"""
Erstelle einen Style Guide für {self.context.lead.firma}.

SCHRITTE:
1. Falls Website vorhanden ({self.context.lead.website}): Analysiere das Design
2. Extrahiere alle Farben, Schriften, Inhalte
3. Erstelle STYLE-GUIDE.md in {self.context.output_dir}/

FIRMENDATEN (für Impressum):
- Firma: {self.context.lead.firma}
- Straße: {self.context.lead.strasse or 'Nicht bekannt'}
- PLZ/Ort: {self.context.lead.plz or ''} {self.context.lead.ort or ''}
- Telefon: {self.context.lead.telefon or 'Nicht bekannt'}
- Email: {self.context.lead.email or 'Nicht bekannt'}
- Google Rating: {self.context.lead.google_rating or 'Nicht bekannt'} ({self.context.lead.google_reviews or 0} Bewertungen)
"""

        try:
            result = await self._run_agent("style-guide", task)
        except Exception as e:
            print(f"\n⚠️ Style-Guide Agent fehlgeschlagen, erstelle Fallback...")
            result = await self._create_fallback_style_guide()

        # Speichere Style Guide Pfad im Kontext
        self.context.style_guide_path = self.context.output_dir / "STYLE-GUIDE.md"

        # Lese Style Guide für nächste Agents
        if self.context.style_guide_path.exists():
            self.context.style_guide_content = self.context.style_guide_path.read_text()
        else:
            # Fallback wenn Datei nicht existiert
            print("⚠️ Style Guide nicht erstellt, erstelle Fallback...")
            result = await self._create_fallback_style_guide()
            if self.context.style_guide_path.exists():
                self.context.style_guide_content = self.context.style_guide_path.read_text()

        return result

    async def _create_fallback_style_guide(self) -> str:
        """Erstellt einen minimalen Fallback Style Guide basierend auf Branche"""
        branche = self.context.lead.branche or "Unbekannt"

        # Branchenspezifische Farben
        branche_colors = {
            "Restaurant": {"primary": "#C8943D", "secondary": "#E94F1D", "text": "#333333"},
            "Rechtsanwalt": {"primary": "#1E3A5F", "secondary": "#C8943D", "text": "#2C3E50"},
            "Steuerberater": {"primary": "#2C5282", "secondary": "#38A169", "text": "#2D3748"},
            "Handwerk": {"primary": "#DD6B20", "secondary": "#38A169", "text": "#2D3748"},
            "Arzt": {"primary": "#3182CE", "secondary": "#48BB78", "text": "#2D3748"},
        }

        colors = branche_colors.get(branche, {"primary": "#3182CE", "secondary": "#E53E3E", "text": "#2D3748"})

        fallback_content = f"""# Style Guide - {self.context.lead.firma}

## Firmeninfos

| Feld | Wert |
|------|------|
| **Name** | {self.context.lead.firma} |
| **Branche** | {branche} |
| **Adresse** | {self.context.lead.strasse or ''}, {self.context.lead.plz or ''} {self.context.lead.ort or ''} |
| **Telefon** | {self.context.lead.telefon or 'Nicht bekannt'} |
| **E-Mail** | {self.context.lead.email or 'info@example.de'} |
| **Google Rating** | {self.context.lead.google_rating or 'N/A'} ({self.context.lead.google_reviews or 0} Bewertungen) |

---

## Farbpalette

| Farbe | Hex | Verwendung |
|-------|-----|------------|
| **Primärfarbe** | `{colors['primary']}` | Buttons, Akzente, Links |
| **Sekundärfarbe** | `{colors['secondary']}` | CTAs, Highlights |
| **Textfarbe** | `{colors['text']}` | Fließtext |
| **Hintergrund** | `#FFFFFF` | Seitenhintergrund |
| **Hintergrund Alt** | `#F7FAFC` | Sektionen |

---

## Typografie

| Typ | Schrift | Verwendung |
|-----|---------|------------|
| **Headlines** | Inter | H1, H2, H3 |
| **Body** | Inter | Fließtext |

---

## Hinweis

Dieser Style Guide wurde automatisch erstellt, da die Original-Website nicht analysiert werden konnte.
Bitte passe Farben und Schriften nach Bedarf an.

---

## Kreative Design-Empfehlungen

1. **Layout-Konzept**: Modernes Card-Grid für Services
2. **Signature-Effekt**: Subtile Schatten und Hover-Animationen
3. **Animations-Level**: Moderat - sanfte Übergänge
4. **Besondere Sektionen**: Hero mit CTA, Services-Grid, Kontakt-Sektion
"""

        # Erstelle Output-Verzeichnis falls nicht vorhanden
        self.context.output_dir.mkdir(parents=True, exist_ok=True)

        # Schreibe Fallback Style Guide
        style_guide_path = self.context.output_dir / "STYLE-GUIDE.md"
        style_guide_path.write_text(fallback_content)

        print(f"✅ Fallback Style Guide erstellt: {style_guide_path}")
        return fallback_content

    async def run_logo_agent(self) -> str:
        """Agent 7: Logo verarbeiten"""
        task = f"""
Verarbeite das Logo für {self.context.lead.firma}.

OUTPUT-VERZEICHNIS: {self.context.output_dir}/assets/

SCHRITTE:
1. Prüfe ob Logo in {self.context.output_dir}/assets/ vorhanden
2. Falls PNG/JPG: Konvertiere zu SVG
3. Falls nur Text-Logo: Erstelle CSS-basiertes Logo
4. Prüfe Qualität des Ergebnisses
"""

        additional_context = f"""
STYLE GUIDE:
{self.context.style_guide_content[:2000]}
"""

        return await self._run_agent("logo", task, additional_context)

    async def run_homepage_agent(self) -> str:
        """Agent 2: Homepage erstellen"""
        task = f"""
Erstelle die Homepage für {self.context.lead.firma}.

OUTPUT:
- {self.context.output_dir}/index.html
- {self.context.output_dir}/styles.css
- {self.context.output_dir}/script.js

Verwende den Style Guide für alle Design-Entscheidungen.
"""

        additional_context = f"""
STYLE GUIDE:
{self.context.style_guide_content}
"""

        result = await self._run_agent("homepage", task, additional_context)
        self.context.created_files.extend(["index.html", "styles.css", "script.js"])
        return result

    async def run_subpages_agent(self) -> str:
        """Agent 3: Unterseiten erstellen"""
        task = f"""
Erstelle alle Unterseiten für {self.context.lead.firma}.

OUTPUT-VERZEICHNIS: {self.context.output_dir}/

VERWENDE das bestehende styles.css (erweitere es bei Bedarf).

Erstelle passende Seiten basierend auf den Services im Style Guide.
"""

        additional_context = f"""
STYLE GUIDE:
{self.context.style_guide_content}

BEREITS ERSTELLT:
{', '.join(self.context.created_files)}
"""

        return await self._run_agent("subpages", task, additional_context)

    async def run_legal_pages_agent(self) -> str:
        """Agent 4: Rechtliche Seiten erstellen"""
        task = f"""
Erstelle die rechtlichen Seiten für {self.context.lead.firma}.

OUTPUT:
- {self.context.output_dir}/impressum.html
- {self.context.output_dir}/datenschutz.html
- {self.context.output_dir}/agb.html (falls relevant)

Verwende ALLE Firmendaten aus dem Style Guide.
KEINE PLATZHALTER erlaubt!
"""

        additional_context = f"""
STYLE GUIDE (enthält Firmendaten und ggf. Original-Texte):
{self.context.style_guide_content}
"""

        try:
            return await self._run_agent("legal-pages", task, additional_context)
        except Exception as e:
            error_str = str(e).lower()
            if "content filtering" in error_str or "blocked" in error_str:
                print("\n⚠️ Content-Filter bei Legal Pages - verwende Fallback-Templates...")
                return await self._create_legal_pages_fallback()
            raise

    async def _create_legal_pages_fallback(self) -> str:
        """
        Fallback: Erstellt Legal Pages mit Templates wenn Content-Filter triggert.
        """
        lead = self.context.lead

        # Extrahiere Header/Footer aus index.html wenn vorhanden
        index_path = self.context.output_dir / "index.html"
        header_html = ""
        footer_html = ""

        if index_path.exists():
            index_content = index_path.read_text()

            # Extrahiere Header
            import re
            header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
            if header_match:
                header_html = header_match.group(1)

            # Extrahiere Footer
            footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
            if footer_match:
                footer_html = footer_match.group(1)

        # Fallback Header wenn nicht gefunden
        if not header_html:
            header_html = f'''<header class="header" id="header">
        <div class="header__container">
            <a href="index.html" class="header__logo">{lead.firma}</a>
            <nav class="header__nav" id="nav">
                <ul class="header__nav-list">
                    <li><a href="index.html" class="header__nav-link">Startseite</a></li>
                    <li><a href="kontakt.html" class="header__nav-link">Kontakt</a></li>
                </ul>
            </nav>
        </div>
    </header>'''

        # Fallback Footer wenn nicht gefunden
        if not footer_html:
            footer_html = f'''<footer class="footer">
        <div class="container">
            <div class="footer__bottom">
                <p class="footer__copy">© {datetime.now().year} {lead.firma}. Alle Rechte vorbehalten.</p>
            </div>
        </div>
    </footer>'''

        # Adresse zusammenbauen
        adresse = ""
        if lead.strasse:
            adresse += f"{lead.strasse}<br>"
        if lead.plz or lead.ort:
            adresse += f"{lead.plz or ''} {lead.ort or ''}"

        # Impressum HTML
        impressum_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Impressum | {lead.firma}</title>
    <meta name="robots" content="noindex, follow">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    {header_html}

    <main class="legal-page">
        <div class="container">
            <div class="legal-page__content">
                <h1 class="legal-page__title">Impressum</h1>

                <section class="legal-section">
                    <h2>Angaben gemäß § 5 TMG</h2>
                    <p>
                        <strong>{lead.firma}</strong><br>
                        {adresse}
                    </p>
                </section>

                <section class="legal-section">
                    <h2>Kontakt</h2>
                    <p>
                        {f'Telefon: <a href="tel:{lead.telefon}">{lead.telefon}</a><br>' if lead.telefon else ''}
                        {f'E-Mail: <a href="mailto:{lead.email}">{lead.email}</a>' if lead.email else ''}
                    </p>
                </section>

                <section class="legal-section">
                    <h2>Streitschlichtung</h2>
                    <p>
                        Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit:
                        <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener">https://ec.europa.eu/consumers/odr/</a>
                    </p>
                    <p>
                        Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.
                    </p>
                </section>

                <section class="legal-section">
                    <h2>Haftung für Inhalte</h2>
                    <p>
                        Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen.
                    </p>
                </section>

                <section class="legal-section">
                    <h2>Haftung für Links</h2>
                    <p>
                        Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber verantwortlich.
                    </p>
                </section>

                <div class="legal-page__back">
                    <a href="index.html" class="btn btn--secondary">← Zurück zur Startseite</a>
                </div>
            </div>
        </div>
    </main>

    {footer_html}

    <script src="script.js"></script>
</body>
</html>'''

        # Datenschutz HTML
        datenschutz_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datenschutz | {lead.firma}</title>
    <meta name="robots" content="noindex, follow">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    {header_html}

    <main class="legal-page">
        <div class="container">
            <div class="legal-page__content">
                <h1 class="legal-page__title">Datenschutzerklärung</h1>

                <section class="legal-section">
                    <h2>1. Datenschutz auf einen Blick</h2>
                    <h3>Allgemeine Hinweise</h3>
                    <p>
                        Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen.
                    </p>
                </section>

                <section class="legal-section">
                    <h2>2. Verantwortliche Stelle</h2>
                    <p>
                        {lead.firma}<br>
                        {adresse}
                        {f'<br>Telefon: {lead.telefon}' if lead.telefon else ''}
                        {f'<br>E-Mail: {lead.email}' if lead.email else ''}
                    </p>
                </section>

                <section class="legal-section">
                    <h2>3. Datenerfassung auf dieser Website</h2>
                    <h3>Server-Log-Dateien</h3>
                    <p>
                        Der Provider der Seiten erhebt und speichert automatisch Informationen in Server-Log-Dateien, die Ihr Browser automatisch übermittelt: Browsertyp, Betriebssystem, Referrer URL, Hostname, Uhrzeit der Serveranfrage und IP-Adresse.
                    </p>
                </section>

                <section class="legal-section">
                    <h2>4. Externe Dienste</h2>
                    <h3>Google Maps</h3>
                    <p>
                        Diese Seite nutzt ggf. den Kartendienst Google Maps. Anbieter ist die Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland.
                    </p>
                </section>

                <section class="legal-section">
                    <h2>5. Ihre Rechte</h2>
                    <p>Sie haben jederzeit das Recht auf Auskunft über Ihre gespeicherten Daten, deren Berichtigung, Löschung oder Einschränkung der Verarbeitung.</p>
                </section>

                <div class="legal-page__back">
                    <a href="index.html" class="btn btn--secondary">← Zurück zur Startseite</a>
                </div>
            </div>
        </div>
    </main>

    {footer_html}

    <script src="script.js"></script>
</body>
</html>'''

        # Dateien schreiben
        (self.context.output_dir / "impressum.html").write_text(impressum_html)
        (self.context.output_dir / "datenschutz.html").write_text(datenschutz_html)

        # CSS für Legal Pages hinzufügen wenn nicht vorhanden
        styles_path = self.context.output_dir / "styles.css"
        if styles_path.exists():
            styles_content = styles_path.read_text()
            if ".legal-page" not in styles_content:
                legal_css = '''

/* ========================================
   Legal Pages (Impressum, Datenschutz)
   ======================================== */
.legal-page {
    padding-top: calc(var(--header-height, 80px) + 3rem);
    padding-bottom: 4rem;
    min-height: 100vh;
}

.legal-page__content {
    max-width: 800px;
    margin: 0 auto;
}

.legal-page__title {
    font-size: clamp(2rem, 4vw, 3rem);
    margin-bottom: 3rem;
}

.legal-page__title::after {
    content: '';
    display: block;
    width: 80px;
    height: 3px;
    background: var(--color-primary, #333);
    margin-top: 1rem;
}

.legal-section {
    margin-bottom: 3rem;
}

.legal-section h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.legal-section h3 {
    font-size: 1.1rem;
    margin: 1.5rem 0 0.75rem;
}

.legal-section p {
    line-height: 1.8;
    margin-bottom: 1rem;
}

.legal-section ul {
    list-style: disc;
    margin-left: 1.5rem;
    margin-bottom: 1rem;
}

.legal-section ul li {
    line-height: 1.8;
    margin-bottom: 0.5rem;
}

.legal-section a {
    color: var(--color-primary, #333);
    text-decoration: underline;
}

.legal-page__back {
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid #eee;
}
'''
                styles_path.write_text(styles_content + legal_css)

        print("✅ Legal Pages via Fallback-Templates erstellt:")
        print(f"   - {self.context.output_dir}/impressum.html")
        print(f"   - {self.context.output_dir}/datenschutz.html")

        return "Legal Pages via Fallback erstellt"

    async def run_references_research_agent(self) -> str:
        """Agent 9: Referenzen recherchieren"""
        task = f"""
Recherchiere Referenzen und Testimonials für {self.context.lead.firma}.

QUELLEN:
- Original-Website: {self.context.lead.website}
- Google Reviews
- LinkedIn
- Branchenportale

Speichere gefundene Referenzen im Style Guide unter "## Referenzen".
"""

        return await self._run_agent("references-research", task)

    async def run_references_page_agent(self) -> str:
        """Agent 8: Referenzen-Seite erstellen"""
        # Aktualisiere Style Guide Content
        if self.context.style_guide_path and self.context.style_guide_path.exists():
            self.context.style_guide_content = self.context.style_guide_path.read_text()

        task = f"""
Erstelle die Referenzen-Seite für {self.context.lead.firma}.

OUTPUT: {self.context.output_dir}/referenzen.html

Integriere auch Testimonials in die Homepage (falls noch nicht vorhanden).
"""

        additional_context = f"""
STYLE GUIDE (enthält recherchierte Referenzen):
{self.context.style_guide_content}
"""

        return await self._run_agent("references-page", task, additional_context)

    async def run_team_photos_agent(self) -> str:
        """Agent 6: Team-Fotos suchen"""
        task = f"""
Finde Team-Fotos für {self.context.lead.firma}.

QUELLEN:
- Original-Website: {self.context.lead.website}
- LinkedIn Profile
- Google

OUTPUT: {self.context.output_dir}/assets/
Aktualisiere HTML-Referenzen entsprechend.
"""

        additional_context = f"""
STYLE GUIDE (enthält Team-Informationen):
{self.context.style_guide_content}
"""

        return await self._run_agent("team-photos", task, additional_context)

    async def run_instagram_photos_agent(self) -> str:
        """Agent 10: Instagram-Fotos extrahieren"""
        task = f"""
Extrahiere Fotos von Instagram für {self.context.lead.firma}.

WANN DIESER AGENT RELEVANT IST:
- Firma hat KEINE Website (nur Social Media)
- Firma hat Website OHNE Bilder
- Branche: Restaurant, Café, Bäckerei, etc. → Food-Fotos
- Branche: Friseur, Kosmetik → Vorher/Nachher Bilder
- Allgemein: Ambiente, Interior, Produkt-Fotos

SCHRITTE:
1. Instagram-Handle finden (suche im Style Guide oder via WebSearch)
2. Instagram-Profil mit Playwright öffnen
3. Bild-URLs extrahieren (JavaScript)
4. Bilder herunterladen nach {self.context.output_dir}/assets/images/
5. HTML-Platzhalter durch echte Bilder ersetzen
6. CSS für Bild-Container in styles.css ergänzen

HINWEIS:
Prüfe zuerst ob es Platzhalter-SVGs in den HTML-Dateien gibt.
Wenn keine Platzhalter vorhanden → Agent kann übersprungen werden.
"""

        additional_context = f"""
STYLE GUIDE:
{self.context.style_guide_content}

BEREITS ERSTELLTE DATEIEN:
{', '.join(self.context.created_files)}
"""

        return await self._run_agent("instagram-photos", task, additional_context)

    async def run_link_qa_agent(self) -> str:
        """Agent 5: Link QA"""
        task = f"""
Prüfe alle Links und Buttons in {self.context.output_dir}/.

TESTS:
1. Alle internen Links (HTML-Dateien existieren?)
2. Navigation auf allen Seiten konsistent?
3. Tel: und mailto: Links korrekt?
4. Externe Links mit target="_blank"?

Fixe alle gefundenen Probleme automatisch.
"""

        return await self._run_agent("link-qa", task)

    async def run_layout_patterns_agent(self) -> str:
        """Agent 13: Layout Patterns (CSS/Code QA)"""
        task = f"""
Prüfe alle CSS/Layout Patterns in {self.context.output_dir}/.

FÜHRE ALLE 9 CHECKS DURCH:
1. Scroll Container - keine Pfeile
2. Hover Scale Verbot
3. Card Alignment mit flex-col
4. Container Breakout Pattern
5. Animation Overflow
6. Scroll vs Grid Regel (≤4 Items = Grid!)
7. Animation Height Konsistenz
8. Theme Token Enforcement
9. Grid Alignment (align-items)

Fixe ALLE gefundenen Probleme automatisch!
"""

        return await self._run_agent("layout-patterns", task)

    async def run_design_review_agent(self) -> tuple[str, bool]:
        """
        Agent 10: Design Review mit Feedback Loop

        Returns:
            Tuple von (review_text, has_critical_issues)
        """
        task = f"""
Führe ein vollständiges Design Review durch für {self.context.output_dir}/.

Iteration: {self.context.iteration + 1}/{self.context.max_iterations}

PRÜFE:
1. Visuelles Design (Farben, Kontraste, Abstände)
2. Layout & Struktur (Sektionen unterschiedlich?)
3. UX & Usability (Navigation, CTAs)
4. Content (keine Platzhalter, Rechtschreibung, Umlaute)
5. Branding (Logo, Corporate Design)

KRITISCHE ISSUES SOFORT FIXEN!
"""

        if self.context.review_feedback:
            additional_context = f"""
VORHERIGES FEEDBACK:
{chr(10).join(self.context.review_feedback[-2:])}
"""
        else:
            additional_context = ""

        result = await self._run_agent("design-review", task, additional_context)

        # Speichere Feedback
        self.context.review_feedback.append(f"Iteration {self.context.iteration + 1}:\n{result}")

        # Prüfe ob kritische Issues vorhanden
        has_critical = any(
            keyword in result.lower()
            for keyword in ["kritisch", "critical", "muss gefixt", "fehler", "broken"]
        )

        return result, has_critical

    async def run_human_view_agent(self) -> str:
        """Agent 14: Human View - Visuelle Sektions-Prüfung"""
        task = f"""
Prüfe die Website aus Sicht eines echten Nutzers.

WEBSITE: {self.context.output_dir}/

FÜR JEDE SEKTION mache 3 Screenshots:
1. Desktop Viewport (1280x800) - Was sieht der User auf dem Laptop?
2. Mobile Viewport (375x812) - Was sieht der User auf dem Handy?
3. Sektion komplett - Wie sieht die gesamte Sektion aus?

PRÜFE jede Sektion auf:
- Lesbarkeit, Buttons, CTAs
- Leerraum-Probleme
- Mobile-Probleme
- Visuelle Hierarchie

Fixe kritische Issues sofort!
Erstelle am Ende einen Gesamtüberblick mit Score.
"""

        return await self._run_agent("human-view", task)

    async def run_finalize_agent(self) -> str:
        """Agent 15: Finalize - Git Push & Airtable Update"""

        # Slug für URL erstellen
        slug = self.context.output_dir.name

        task = f"""
Finalisiere die Website für {self.context.lead.firma}.

DATEN:
- Output-Verzeichnis: {self.context.output_dir}
- Firmenname: {self.context.lead.firma}
- URL-Slug: {slug}
- Airtable Record ID: {self.context.lead.id}

SCHRITTE:
1. Git: Committe und pushe {self.context.output_dir}/
2. Airtable: Aktualisiere Record {self.context.lead.id}
   - "Seite erstellt": true
   - "Landingpage URL": https://lead-pages.pages.dev/{slug}/

WICHTIG: Beide Schritte MÜSSEN erfolgreich sein!
"""

        return await self._run_agent("finalize", task)

    async def generate(self) -> Path:
        """
        Hauptmethode: Generiert die komplette Website.

        Führt alle Agents in der richtigen Reihenfolge aus
        und implementiert den Design Review Feedback Loop.
        """
        print(f"\n{'#'*60}")
        print(f"# LEAD PAGES GENERATOR")
        print(f"# Firma: {self.context.lead.firma}")
        print(f"# Branche: {self.context.lead.branche}")
        print(f"# Output: {self.context.output_dir}")
        print(f"{'#'*60}\n")

        start_time = datetime.now()

        # Erstelle Output-Verzeichnis
        self.context.output_dir.mkdir(parents=True, exist_ok=True)
        (self.context.output_dir / "assets").mkdir(exist_ok=True)

        try:
            # Phase 1: Research & Vorbereitung
            print("\n📚 PHASE 1: Research & Vorbereitung")
            await self.run_style_guide_agent()
            await self.run_logo_agent()
            await self.run_references_research_agent()

            # Phase 2: Content-Erstellung
            print("\n✍️ PHASE 2: Content-Erstellung")
            await self.run_homepage_agent()
            await self.run_subpages_agent()
            await self.run_legal_pages_agent()
            await self.run_references_page_agent()
            await self.run_team_photos_agent()
            await self.run_instagram_photos_agent()

            # Phase 3: QA
            print("\n🔍 PHASE 3: Quality Assurance")
            await self.run_link_qa_agent()
            await self.run_layout_patterns_agent()

            # Phase 4: Design Review Loop
            print("\n🎨 PHASE 4: Design Review (Feedback Loop)")
            while self.context.iteration < self.context.max_iterations:
                self.context.iteration += 1
                _review_result, has_critical = await self.run_design_review_agent()

                if not has_critical:
                    print(f"\n✅ Design Review bestanden nach {self.context.iteration} Iteration(en)!")
                    break

                if self.context.iteration >= self.context.max_iterations:
                    print(f"\n⚠️ Max. Iterationen erreicht ({self.context.max_iterations})")
                    break

                print(f"\n🔄 Kritische Issues gefunden. Starte Iteration {self.context.iteration + 1}...")

            # Phase 5: Human View (Finale visuelle Prüfung)
            print("\n👁️ PHASE 5: Human View (Finale visuelle Prüfung)")
            await self.run_human_view_agent()

            # Phase 6: Finalize (Git Push & Airtable Update)
            # Nur wenn KEIN Test-Modus und echte Record ID
            if self.context.lead.id and not self.context.lead.id.startswith("test"):
                print("\n🚀 PHASE 6: Finalize (Git Push & Airtable)")
                await self.run_finalize_agent()
            else:
                print("\n⏭️ PHASE 6: Übersprungen (Test-Modus)")

            # Zusammenfassung
            duration = datetime.now() - start_time
            print(f"\n{'='*60}")
            print(f"✅ WEBSITE ERFOLGREICH GENERIERT!")
            print(f"📁 Output: {self.context.output_dir}")
            print(f"⏱️ Dauer: {duration.total_seconds():.1f}s")
            print(f"🔄 Review-Iterationen: {self.context.iteration}")
            print(f"{'='*60}\n")

            return self.context.output_dir

        except Exception as e:
            self.context.errors.append(str(e))
            print(f"\n❌ FEHLER: {e}")
            raise


async def generate_website(lead: Lead, base_output_dir: str = "docs") -> Path:
    """
    Convenience-Funktion zum Generieren einer Website.

    Args:
        lead: Lead-Daten aus Airtable
        base_output_dir: Basis-Verzeichnis für Output

    Returns:
        Pfad zum generierten Website-Verzeichnis
    """
    orchestrator = LeadPagesOrchestrator(lead, base_output_dir)
    return await orchestrator.generate()
