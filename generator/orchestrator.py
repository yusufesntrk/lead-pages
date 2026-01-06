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
        except Exception as e:
            print(f"\n❌ Agent-Fehler: {e}")
            self.context.errors.append(f"{agent_name}: {str(e)}")
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

        result = await self._run_agent("style-guide", task)

        # Speichere Style Guide Pfad im Kontext
        self.context.style_guide_path = self.context.output_dir / "STYLE-GUIDE.md"

        # Lese Style Guide für nächste Agents
        if self.context.style_guide_path.exists():
            self.context.style_guide_content = self.context.style_guide_path.read_text()

        return result

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

        return await self._run_agent("legal-pages", task, additional_context)

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
