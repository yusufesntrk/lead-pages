"""
Lead Pages Generator - Orchestrator

Koordiniert alle spezialisierten Agents in der richtigen Reihenfolge
und verwaltet den Kontext zwischen den Agents.

ARCHITEKTUR-SWITCH:
- use_new_agents=False: Legacy-Modus (prompt-basierte Agents aus definitions.py)
- use_new_agents=True: Neue Agent-Klassen (SDLC-Pattern)
- use_parallel=True: Parallelisierte Ausführung mit QA-Loop
"""

import asyncio
import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional, List

from claude_code_sdk import query, ClaudeCodeOptions

from .agents.definitions import AGENTS
from .agents import (
    StyleGuideAgent,
    HomepageAgent,
    SubpagesAgent,
    LegalPagesAgent,
    LogoAgent,
    TeamPhotosAgent,
    ReferencesResearchAgent,
    ReferencesPageAgent,
    InstagramPhotosAgent,
    ImageVerificationAgent,
    LayoutPatternsAgent,
    HumanViewAgent,
    LinkQAAgent,
    DesignReviewAgent,
    FinalizeAgent,
)
from .results import (
    StyleGuideResult,
    HomepageResult,
    SubpagesResult,
    LegalPagesResult,
    LogoResult,
    TeamPhotosResult,
    ReferencesResult,
    InstagramPhotosResult,
    ImageVerificationResult,
    LayoutPatternsResult,
    HumanViewResult,
    LinkQAResult,
    DesignReviewResult,
    FinalizeResult,
    LeadTask,
    TaskStatus,
    QAPhaseResult,
    Finding,
)
from .config import (
    QA_MAX_ITERATIONS,
    CRITICAL_SEVERITIES,
    PARALLEL_AGENT_TIMEOUT,
)


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

    Args:
        lead: Lead-Daten aus Airtable
        base_output_dir: Basis-Verzeichnis für Output
        use_new_agents: True = neue Agent-Klassen (SDLC-Pattern), False = Legacy
                        Default: liest aus ENV "USE_NEW_AGENTS" oder False
    """

    def __init__(
        self,
        lead: Lead,
        base_output_dir: str = "docs",
        use_new_agents: Optional[bool] = None,
        use_parallel: Optional[bool] = None
    ):
        self.lead = lead
        self.output_dir = Path(base_output_dir) / self._slugify(lead.firma)
        self.context = GeneratorContext(
            lead=lead,
            output_dir=self.output_dir
        )

        # Architektur-Switch: ENV oder Parameter
        if use_new_agents is None:
            self.use_new_agents = os.environ.get("USE_NEW_AGENTS", "").lower() == "true"
        else:
            self.use_new_agents = use_new_agents

        # Parallelisierungs-Switch: ENV oder Parameter
        if use_parallel is None:
            self.use_parallel = os.environ.get("USE_PARALLEL", "").lower() == "true"
        else:
            self.use_parallel = use_parallel

        # Neue Agent-Instanzen (lazy initialization)
        self._agents_initialized = False
        self._style_guide_agent: Optional[StyleGuideAgent] = None
        self._homepage_agent: Optional[HomepageAgent] = None
        self._subpages_agent: Optional[SubpagesAgent] = None
        self._legal_pages_agent: Optional[LegalPagesAgent] = None
        self._logo_agent: Optional[LogoAgent] = None
        self._team_photos_agent: Optional[TeamPhotosAgent] = None
        self._references_research_agent: Optional[ReferencesResearchAgent] = None
        self._references_page_agent: Optional[ReferencesPageAgent] = None
        self._instagram_photos_agent: Optional[InstagramPhotosAgent] = None
        self._image_verification_agent: Optional[ImageVerificationAgent] = None
        self._layout_patterns_agent: Optional[LayoutPatternsAgent] = None
        self._human_view_agent: Optional[HumanViewAgent] = None
        self._link_qa_agent: Optional[LinkQAAgent] = None
        self._design_review_agent: Optional[DesignReviewAgent] = None
        self._finalize_agent: Optional[FinalizeAgent] = None

        # LeadTask für Tracking (neue Architektur)
        self._lead_task: Optional[LeadTask] = None

        if self.use_new_agents:
            if self.use_parallel:
                print("🔧 Modus: Parallelisiert (SDLC-Pattern + QA-Loop)")
            else:
                print("🔧 Modus: Neue Agent-Klassen (SDLC-Pattern)")
            self._init_agents()
        else:
            print("🔧 Modus: Legacy (prompt-basiert)")

    def _init_agents(self):
        """Initialisiert alle Agent-Instanzen."""
        if self._agents_initialized:
            return

        working_dir = str(self.context.output_dir.parent.parent)

        self._style_guide_agent = StyleGuideAgent(working_dir)
        self._homepage_agent = HomepageAgent(working_dir)
        self._subpages_agent = SubpagesAgent(working_dir)
        self._legal_pages_agent = LegalPagesAgent(working_dir)
        self._logo_agent = LogoAgent(working_dir)
        self._team_photos_agent = TeamPhotosAgent(working_dir)
        self._references_research_agent = ReferencesResearchAgent(working_dir)
        self._references_page_agent = ReferencesPageAgent(working_dir)
        self._instagram_photos_agent = InstagramPhotosAgent(working_dir)
        self._image_verification_agent = ImageVerificationAgent(working_dir)
        self._layout_patterns_agent = LayoutPatternsAgent(working_dir)
        self._human_view_agent = HumanViewAgent(working_dir)
        self._link_qa_agent = LinkQAAgent(working_dir)
        self._design_review_agent = DesignReviewAgent(working_dir)
        self._finalize_agent = FinalizeAgent(working_dir)

        # LeadTask initialisieren
        self._lead_task = LeadTask(
            id=self.lead.id,
            company=self.lead.firma,
            branche=self.lead.branche,
            output_dir=str(self.output_dir)
        )

        self._agents_initialized = True

    def _create_message_callback(self, agent_name: str):
        """Erstellt einen Message-Callback für Streaming-Output."""
        def on_message(msg):
            if hasattr(msg, 'content'):
                for block in msg.content:
                    if hasattr(block, 'text'):
                        print(block.text, end="", flush=True)
            if hasattr(msg, 'total_cost_usd'):
                print(f"\n✅ {agent_name} fertig (${msg.total_cost_usd:.6f})")
        return on_message

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

    # =========================================================================
    # PARALLEL EXECUTION METHODS
    # =========================================================================

    async def _run_parallel(self, *coroutines) -> list:
        """
        Führt mehrere Coroutines parallel aus.

        Args:
            *coroutines: Variable Anzahl von Coroutines

        Returns:
            Liste der Ergebnisse (Exceptions werden durchgereicht)
        """
        return await asyncio.gather(*coroutines, return_exceptions=True)

    async def run_qa_phase(self, iteration: int = 0) -> QAPhaseResult:
        """
        Führt alle 4 QA-Agents parallel aus.

        Args:
            iteration: Aktuelle QA-Loop Iteration

        Returns:
            QAPhaseResult mit aggregierten Findings
        """
        print(f"\n🔍 QA Phase (Iteration {iteration + 1}): Starte 4 Agents parallel...")

        # Alle 4 QA-Agents parallel ausführen
        results = await self._run_parallel(
            self._run_link_qa_new(),
            self._run_layout_patterns_new(),
            self._run_design_review_new(),
            self._run_human_view_new(),
        )

        # Ergebnisse verarbeiten
        link_qa_result = None
        layout_patterns_result = None
        design_review_result = None
        human_view_result = None
        all_findings: List[Finding] = []

        for r in results:
            if isinstance(r, Exception):
                print(f"⚠️ Agent-Fehler: {r}")
                continue

            # Ergebnis-Typ identifizieren
            if isinstance(r, LinkQAResult):
                link_qa_result = r
                all_findings.extend(r.findings)
            elif isinstance(r, LayoutPatternsResult):
                layout_patterns_result = r
                all_findings.extend(r.findings)
            elif isinstance(r, DesignReviewResult):
                design_review_result = r
                all_findings.extend(r.findings)
            elif isinstance(r, HumanViewResult):
                human_view_result = r
                all_findings.extend(r.all_findings)
            elif isinstance(r, str):
                # Legacy string results - ignorieren
                pass

        # Deduplizieren nach ID
        seen_ids = set()
        unique_findings = []
        for f in all_findings:
            if f.id not in seen_ids:
                seen_ids.add(f.id)
                unique_findings.append(f)

        # Severity-Counts
        critical_count = sum(1 for f in unique_findings if f.severity == "critical")
        major_count = sum(1 for f in unique_findings if f.severity == "major")
        minor_count = sum(1 for f in unique_findings if f.severity == "minor")

        return QAPhaseResult(
            success=True,
            all_findings=unique_findings,
            critical_count=critical_count,
            major_count=major_count,
            minor_count=minor_count,
            link_qa=link_qa_result,
            layout_patterns=layout_patterns_result,
            design_review=design_review_result,
            human_view=human_view_result,
            iteration=iteration,
            fix_required=critical_count > 0,
        )

    async def fix_findings(self, findings: List[Finding]) -> int:
        """
        Fixt eine Liste von Findings via Claude Agent.

        Args:
            findings: Liste der zu fixenden Findings

        Returns:
            Anzahl erfolgreich gefixte Findings
        """
        if not findings:
            return 0

        print(f"\n🔧 Fixe {len(findings)} Findings...")

        # Gruppiere nach Datei
        by_file: dict = {}
        for f in findings:
            file_path = f.location.split(":")[0]
            by_file.setdefault(file_path, []).append(f)

        fixed_count = 0

        for file_path, file_findings in by_file.items():
            print(f"   📄 {file_path}: {len(file_findings)} Findings")

            # Baue Fix-Prompt
            prompt = self._build_fix_prompt(file_path, file_findings)

            # Führe Fix aus
            try:
                result_text, error = await self._run_fix_agent(prompt)
                if error:
                    print(f"      ❌ Fehler: {error}")
                    continue

                # Zähle erfolgreiche Fixes
                fix_count = result_text.upper().count("FIXED:") + result_text.upper().count("GEFIXT:")
                fixed_count += fix_count
                print(f"      ✅ {fix_count} gefixt")

            except Exception as e:
                print(f"      ❌ Exception: {e}")

        return fixed_count

    def _build_fix_prompt(self, file_path: str, findings: List[Finding]) -> str:
        """Baut den Prompt für den Fix-Agent."""
        findings_text = "\n".join([
            f"- [{f.id}] {f.severity}: {f.problem}\n  Fix: {f.fix_instruction}"
            for f in findings
        ])

        return f"""
## AUFGABE

Fixe die folgenden Probleme in der Datei: **{self.context.output_dir}/{file_path}**

## FINDINGS

{findings_text}

## ANWEISUNGEN

1. Lies die Datei
2. Führe ALLE Fixes durch
3. Schreibe die aktualisierte Datei
4. Bestätige jeden Fix mit "FIXED: [ID]"

## OUTPUT

```
FIXED: L001
FIXED: L002
...
```
"""

    async def _run_fix_agent(self, prompt: str) -> tuple:
        """Führt den Fix-Agent aus."""
        from .config import create_agent_options, ALL_TOOLS

        options = create_agent_options(
            working_dir=str(self.context.output_dir.parent.parent),
            system_prompt="Du bist ein Code-Fix Agent. Fixe die angegebenen Probleme.",
            allowed_tools=ALL_TOOLS,
            model="sonnet"  # Schneller für Fixes
        )

        result_text = ""
        error = None

        try:
            async for msg in query(prompt=prompt, options=options):
                if hasattr(msg, 'content'):
                    for block in msg.content:
                        if hasattr(block, 'text'):
                            result_text += block.text
        except Exception as e:
            error = str(e)

        return result_text, error

    async def _generate_parallel(self) -> Path:
        """
        Parallelisierte Website-Generierung.

        Nutzt asyncio.gather für parallele Agent-Ausführung
        und implementiert den QA-Loop.
        """
        print(f"\n{'#'*60}")
        print(f"# LEAD PAGES GENERATOR (PARALLEL)")
        print(f"# Firma: {self.context.lead.firma}")
        print(f"# Branche: {self.context.lead.branche}")
        print(f"# Output: {self.context.output_dir}")
        print(f"{'#'*60}\n")

        start_time = datetime.now()

        # Erstelle Output-Verzeichnis
        self.context.output_dir.mkdir(parents=True, exist_ok=True)
        (self.context.output_dir / "assets").mkdir(exist_ok=True)

        try:
            # ===== PHASE 1: Research =====
            print("\n📚 PHASE 1: Research")

            # StyleGuide muss zuerst laufen (andere brauchen den Output)
            await self.run_style_guide_agent()

            # Logo + ReferencesResearch parallel
            await self._run_parallel(
                self.run_logo_agent(),
                self.run_references_research_agent(),
            )

            # ===== PHASE 2: Content =====
            print("\n✍️ PHASE 2: Content")

            # Homepage + Subpages + LegalPages parallel
            await self._run_parallel(
                self.run_homepage_agent(),
                self.run_subpages_agent(),
                self.run_legal_pages_agent(),
            )

            # ReferencesPage braucht recherchierte Daten
            await self.run_references_page_agent()

            # TeamPhotos + InstagramPhotos parallel
            await self._run_parallel(
                self.run_team_photos_agent(),
                self.run_instagram_photos_agent(),
            )

            # ===== PHASE 3: QA Loop =====
            print(f"\n🔍 PHASE 3: QA Loop (max {QA_MAX_ITERATIONS}x)")

            for iteration in range(QA_MAX_ITERATIONS):
                print(f"\n--- Iteration {iteration + 1}/{QA_MAX_ITERATIONS} ---")

                # Alle QA-Agents parallel
                qa_result = await self.run_qa_phase(iteration)

                print(f"\n📊 QA Ergebnis:")
                print(f"   Critical: {qa_result.critical_count}")
                print(f"   Major: {qa_result.major_count}")
                print(f"   Minor: {qa_result.minor_count}")

                if not qa_result.fix_required:
                    print(f"\n✅ QA bestanden! Keine kritischen Findings.")
                    break

                # Nur kritische Findings fixen
                critical_findings = [
                    f for f in qa_result.all_findings
                    if f.severity in CRITICAL_SEVERITIES
                ]

                print(f"\n⚠️ {len(critical_findings)} kritische Findings gefunden")

                if critical_findings:
                    fixed = await self.fix_findings(critical_findings)
                    print(f"✅ {fixed} Findings gefixt")

                if iteration == QA_MAX_ITERATIONS - 1:
                    print(f"\n⚠️ Max. Iterationen erreicht ({QA_MAX_ITERATIONS})")

            # ===== PHASE 4: Finalize =====
            if self.context.lead.id and not self.context.lead.id.startswith("test"):
                print("\n🚀 PHASE 4: Finalize (Git Push & Airtable)")
                await self.run_finalize_agent()
            else:
                print("\n⏭️ PHASE 4: Übersprungen (Test-Modus)")

            # Zusammenfassung
            duration = datetime.now() - start_time
            print(f"\n{'='*60}")
            print(f"✅ WEBSITE ERFOLGREICH GENERIERT (PARALLEL)!")
            print(f"📁 Output: {self.context.output_dir}")
            print(f"⏱️ Dauer: {duration.total_seconds():.1f}s")
            print(f"{'='*60}\n")

            return self.context.output_dir

        except Exception as e:
            self.context.errors.append(str(e))
            print(f"\n❌ FEHLER: {e}")
            raise

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
        """
        Agent 1: Style Guide erstellen

        Verwendet entweder:
        - Legacy: _run_agent("style-guide", ...) mit prompt aus definitions.py
        - Neu: StyleGuideAgent.extract() mit typisiertem Result
        """
        # Speichere Style Guide Pfad im Kontext (für beide Modi)
        self.context.style_guide_path = self.context.output_dir / "STYLE-GUIDE.md"

        if self.use_new_agents:
            # === NEUE ARCHITEKTUR (SDLC-Pattern) ===
            return await self._run_style_guide_new()
        else:
            # === LEGACY ARCHITEKTUR (prompt-basiert) ===
            return await self._run_style_guide_legacy()

    async def _run_style_guide_new(self) -> str:
        """
        Neue Architektur: StyleGuideAgent mit typisiertem Result.

        Vorteile:
        - Kleinerer Kontext (nur relevante Daten)
        - Typisiertes Result (StyleGuideResult)
        - Bessere Fehlerbehandlung
        """
        print("\n🆕 StyleGuideAgent (SDLC-Pattern)")

        # Lazy initialization
        if self._style_guide_agent is None:
            self._style_guide_agent = StyleGuideAgent(
                working_dir=str(self.context.output_dir.parent.parent)  # Projekt-Root
            )

        # Company data für Agent
        company_data = {
            "strasse": self.context.lead.strasse,
            "plz": self.context.lead.plz,
            "ort": self.context.lead.ort,
            "telefon": self.context.lead.telefon,
            "email": self.context.lead.email,
            "google_rating": self.context.lead.google_rating,
            "google_reviews": self.context.lead.google_reviews,
        }

        # Message callback für Streaming-Output
        def on_message(msg):
            if hasattr(msg, 'content'):
                for block in msg.content:
                    if hasattr(block, 'text'):
                        print(block.text, end="", flush=True)
            if hasattr(msg, 'total_cost_usd'):
                print(f"\n✅ Agent fertig (${msg.total_cost_usd:.6f})")

        # Agent ausführen
        result: StyleGuideResult = await self._style_guide_agent.extract(
            company_name=self.context.lead.firma,
            website_url=self.context.lead.website,
            branche=self.context.lead.branche,
            company_data=company_data,
            output_dir=self.context.output_dir,
            on_message=on_message
        )

        if not result.success:
            print(f"\n⚠️ StyleGuideAgent fehlgeschlagen: {result.error}")
            print("Erstelle Fallback...")
            return await self._create_fallback_style_guide()

        # Lese erstellten Style Guide
        if self.context.style_guide_path.exists():
            self.context.style_guide_content = self.context.style_guide_path.read_text()

        # Log extrahierte Daten
        if result.colors:
            print(f"\n📊 Extrahierte Farben: {result.colors}")
        if result.fonts:
            print(f"📝 Extrahierte Fonts: {result.fonts}")
        if result.team_members:
            print(f"👥 Team-Mitglieder: {len(result.team_members)}")
        if result.services:
            print(f"🔧 Services: {len(result.services)}")

        return self.context.style_guide_content

    async def _run_style_guide_legacy(self) -> str:
        """
        Legacy Architektur: prompt-basierte Agents aus definitions.py
        """
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
        if self.use_new_agents:
            return await self._run_logo_new()
        else:
            return await self._run_logo_legacy()

    async def _run_logo_new(self) -> str:
        """Neue Architektur: LogoAgent"""
        print("\n🆕 LogoAgent (SDLC-Pattern)")

        # Extrahiere logo_url und primary_color aus Style Guide
        logo_url = None
        primary_color = "#333333"  # Fallback

        if self.context.style_guide_content:
            # Suche nach logo_url
            import re
            logo_match = re.search(r'Logo.*?URL.*?[`"\']?(https?://[^\s`"\']+)', self.context.style_guide_content, re.IGNORECASE)
            if logo_match:
                logo_url = logo_match.group(1)

            # Suche nach primary color
            color_match = re.search(r'(?:Prim[äa]rfarbe|Primary).*?[`"\']?(#[0-9A-Fa-f]{3,6})', self.context.style_guide_content, re.IGNORECASE)
            if color_match:
                primary_color = color_match.group(1)

        result: LogoResult = await self._logo_agent.process(
            company_name=self.context.lead.firma,
            website_url=self.context.lead.website,
            logo_url=logo_url,
            primary_color=primary_color,
            output_dir=self.context.output_dir,
            on_message=self._create_message_callback("LogoAgent")
        )

        if not result.success:
            print(f"⚠️ LogoAgent Warnung: {result.error}")

        if self._lead_task:
            self._lead_task.logo = result
            self._lead_task.status = TaskStatus.LOGO

        if result.svg_path:
            print(f"\n📊 Logo: {result.svg_path}")
            if result.converted_to_svg:
                print(f"   Konvertiert von: {result.original_format}")
            if result.used_text_logo:
                print("   (Text-Logo verwendet)")

        return f"Logo verarbeitet: {result.svg_path or 'Text-Logo'}"

    async def _run_logo_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_homepage_new()
        else:
            return await self._run_homepage_legacy()

    async def _run_homepage_new(self) -> str:
        """Neue Architektur: HomepageAgent"""
        print("\n🆕 HomepageAgent (SDLC-Pattern)")

        # Extrahiere Daten aus Style Guide Result oder Content
        colors = {}
        fonts = {}
        hero_content = {}
        services = []
        team_members = []

        if self._lead_task and self._lead_task.style_guide:
            sg = self._lead_task.style_guide
            colors = sg.colors
            fonts = sg.fonts
            hero_content = sg.hero_content
            services = sg.services
            team_members = sg.team_members

        result: HomepageResult = await self._homepage_agent.create(
            company_name=self.context.lead.firma,
            branche=self.context.lead.branche,
            colors=colors,
            fonts=fonts,
            hero_content=hero_content,
            services=services,
            team_members=team_members,
            output_dir=self.context.output_dir,
            style_guide_content=self.context.style_guide_content,
            on_message=self._create_message_callback("HomepageAgent")
        )

        if not result.success:
            raise Exception(f"HomepageAgent fehlgeschlagen: {result.error}")

        self.context.created_files.extend(result.files_created)

        if self._lead_task:
            self._lead_task.homepage = result
            self._lead_task.status = TaskStatus.HOMEPAGE

        print(f"\n📊 Erstellte Dateien: {result.files_created}")
        print(f"📊 Sektionen: {result.sections_created}")
        print(f"📊 CTAs: {result.cta_count}")

        return f"Homepage erstellt: {result.files_created}"

    async def _run_homepage_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_subpages_new()
        else:
            return await self._run_subpages_legacy()

    async def _run_subpages_new(self) -> str:
        """Neue Architektur: SubpagesAgent"""
        print("\n🆕 SubpagesAgent (SDLC-Pattern)")

        # Extrahiere Daten aus Style Guide Result
        services = []
        team_members = []
        if self._lead_task and self._lead_task.style_guide:
            sg = self._lead_task.style_guide
            services = sg.services
            team_members = sg.team_members

        # Standard-Seiten basierend auf Branche
        pages_to_create = ["kontakt", "ueber-uns"]
        if services:
            pages_to_create.append("leistungen")

        company_data = {
            "firma": self.context.lead.firma,
            "strasse": self.context.lead.strasse,
            "plz": self.context.lead.plz,
            "ort": self.context.lead.ort,
            "telefon": self.context.lead.telefon,
            "email": self.context.lead.email,
        }

        result: SubpagesResult = await self._subpages_agent.create(
            company_name=self.context.lead.firma,
            branche=self.context.lead.branche,
            pages_to_create=pages_to_create,
            services=services,
            team_members=team_members,
            company_data=company_data,
            output_dir=self.context.output_dir,
            style_guide_content=self.context.style_guide_content,
            on_message=self._create_message_callback("SubpagesAgent")
        )

        if not result.success:
            print(f"⚠️ SubpagesAgent Warnung: {result.error}")

        self.context.created_files.extend(result.pages_created)

        if self._lead_task:
            self._lead_task.subpages = result
            self._lead_task.status = TaskStatus.SUBPAGES

        print(f"\n📊 Erstellte Seiten: {result.pages_created}")
        return f"Unterseiten erstellt: {result.pages_created}"

    async def _run_subpages_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_legal_pages_new()
        else:
            return await self._run_legal_pages_legacy()

    async def _run_legal_pages_new(self) -> str:
        """Neue Architektur: LegalPagesAgent"""
        print("\n🆕 LegalPagesAgent (SDLC-Pattern)")

        company_data = {
            "firma": self.context.lead.firma,
            "strasse": self.context.lead.strasse,
            "plz": self.context.lead.plz,
            "ort": self.context.lead.ort,
            "telefon": self.context.lead.telefon,
            "email": self.context.lead.email,
        }

        # Hole Original-Texte aus Style Guide Result falls vorhanden
        impressum_text = None
        datenschutz_text = None
        if self._lead_task and self._lead_task.style_guide:
            impressum_text = self._lead_task.style_guide.impressum_text
            datenschutz_text = self._lead_task.style_guide.datenschutz_text

        result: LegalPagesResult = await self._legal_pages_agent.create(
            company_name=self.context.lead.firma,
            company_data=company_data,
            branche=self.context.lead.branche,
            output_dir=self.context.output_dir,
            impressum_text=impressum_text,
            datenschutz_text=datenschutz_text,
            on_message=self._create_message_callback("LegalPagesAgent")
        )

        if not result.success:
            print(f"⚠️ LegalPagesAgent Fehler: {result.error}")
            print("Erstelle Fallback...")
            return await self._create_legal_pages_fallback()

        self.context.created_files.extend(result.pages_created)

        if self._lead_task:
            self._lead_task.legal_pages = result
            self._lead_task.status = TaskStatus.LEGAL_PAGES

        if result.placeholders_found > 0:
            print(f"⚠️ {result.placeholders_found} Platzhalter gefunden!")

        print(f"\n📊 Erstellte Seiten: {result.pages_created}")
        return f"Legal Pages erstellt: {result.pages_created}"

    async def _run_legal_pages_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_references_research_new()
        else:
            return await self._run_references_research_legacy()

    async def _run_references_research_new(self) -> str:
        """Neue Architektur: ReferencesResearchAgent"""
        print("\n🆕 ReferencesResearchAgent (SDLC-Pattern)")

        result = await self._references_research_agent.research(
            company_name=self.context.lead.firma,
            website_url=self.context.lead.website,
            google_rating=self.context.lead.google_rating,
            google_reviews_count=self.context.lead.google_reviews or 0,
            output_dir=str(self.context.output_dir),
            on_message=self._create_message_callback("ReferencesResearchAgent")
        )

        if result.testimonials:
            print(f"\n📊 Gefundene Testimonials: {len(result.testimonials)}")
        if result.google_rating:
            print(f"📊 Google Rating: {result.google_rating}")

        return f"Referenzen recherchiert: {len(result.testimonials)} Testimonials"

    async def _run_references_research_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_references_page_new()
        else:
            return await self._run_references_page_legacy()

    async def _run_references_page_new(self) -> str:
        """Neue Architektur: ReferencesPageAgent"""
        print("\n🆕 ReferencesPageAgent (SDLC-Pattern)")

        result: ReferencesResult = await self._references_page_agent.create(
            testimonials=[],  # Wird vom Agent aus Style Guide gelesen
            google_rating=self.context.lead.google_rating,
            google_reviews_count=self.context.lead.google_reviews or 0,
            company_name=self.context.lead.firma,
            output_dir=str(self.context.output_dir),
            style_guide_path=str(self.context.style_guide_path),
            on_message=self._create_message_callback("ReferencesPageAgent")
        )

        if self._lead_task:
            self._lead_task.references = result
            self._lead_task.status = TaskStatus.REFERENCES

        print(f"\n📊 Referenzen-Seite erstellt: {result.references_page_created}")
        return f"Referenzen-Seite: {'erstellt' if result.references_page_created else 'übersprungen'}"

    async def _run_references_page_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_team_photos_new()
        else:
            return await self._run_team_photos_legacy()

    async def _run_team_photos_new(self) -> str:
        """Neue Architektur: TeamPhotosAgent"""
        print("\n🆕 TeamPhotosAgent (SDLC-Pattern)")

        # Team-Mitglieder aus Style Guide extrahieren (vereinfacht)
        team_members = []  # Wird vom Agent aus Style Guide gelesen

        result: TeamPhotosResult = await self._team_photos_agent.find(
            team_members=team_members,
            company_name=self.context.lead.firma,
            website_url=self.context.lead.website,
            output_dir=str(self.context.output_dir),
            on_message=self._create_message_callback("TeamPhotosAgent")
        )

        if self._lead_task:
            self._lead_task.team_photos = result
            self._lead_task.status = TaskStatus.TEAM_PHOTOS

        print(f"\n📊 Team-Fotos gefunden: {result.photos_found}")
        print(f"📊 Quellen: {result.sources}")
        return f"Team-Fotos: {result.photos_found} gefunden"

    async def _run_team_photos_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_instagram_photos_new()
        else:
            return await self._run_instagram_photos_legacy()

    async def _run_instagram_photos_new(self) -> str:
        """Neue Architektur: InstagramPhotosAgent"""
        print("\n🆕 InstagramPhotosAgent (SDLC-Pattern)")

        result: InstagramPhotosResult = await self._instagram_photos_agent.extract(
            company_name=self.context.lead.firma,
            city=self.context.lead.ort or "",
            branche=self.context.lead.branche,
            instagram_handle=None,  # Wird vom Agent gesucht
            output_dir=str(self.context.output_dir),
            on_message=self._create_message_callback("InstagramPhotosAgent")
        )

        if self._lead_task:
            self._lead_task.instagram_photos = result

        print(f"\n📊 Instagram-Fotos: {result.photos_found}")
        if result.instagram_handle:
            print(f"📊 Handle: @{result.instagram_handle}")
        return f"Instagram: {result.photos_found} Fotos"

    async def _run_instagram_photos_legacy(self) -> str:
        """Legacy Architektur"""
        task = f"""
Extrahiere Fotos von Instagram für {self.context.lead.firma}.

WANN DIESER AGENT RELEVANT IST:
- Firma hat KEINE Website (nur Social Media)
- Firma hat Website OHNE Bilder
- Branche: Restaurant, Café, Bäckerei, etc. → Food-Fotos

SCHRITTE:
1. Instagram-Handle finden
2. Bild-URLs extrahieren
3. Bilder herunterladen nach {self.context.output_dir}/assets/images/
"""

        additional_context = f"""
STYLE GUIDE:
{self.context.style_guide_content}
"""

        return await self._run_agent("instagram-photos", task, additional_context)

    async def run_link_qa_agent(self) -> str:
        """Agent 5: Link QA"""
        if self.use_new_agents:
            return await self._run_link_qa_new()
        else:
            return await self._run_link_qa_legacy()

    async def _run_link_qa_new(self) -> str:
        """Neue Architektur: LinkQAAgent"""
        print("\n🆕 LinkQAAgent (SDLC-Pattern)")

        result: LinkQAResult = await self._link_qa_agent.check(
            output_dir=str(self.context.output_dir),
            on_message=self._create_message_callback("LinkQAAgent")
        )

        if self._lead_task:
            self._lead_task.link_qa = result
            self._lead_task.status = TaskStatus.LINK_QA

        print(f"\n📊 Links geprüft: {result.links_checked}")
        print(f"📊 Broken: {result.broken_links_found}")
        print(f"📊 Findings: {len(result.findings)}")
        return result  # Return result for QA aggregation

    async def _run_link_qa_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_layout_patterns_new()
        else:
            return await self._run_layout_patterns_legacy()

    async def _run_layout_patterns_new(self) -> str:
        """Neue Architektur: LayoutPatternsAgent"""
        print("\n🆕 LayoutPatternsAgent (SDLC-Pattern)")

        result: LayoutPatternsResult = await self._layout_patterns_agent.check(
            output_dir=str(self.context.output_dir),
            on_message=self._create_message_callback("LayoutPatternsAgent")
        )

        if self._lead_task:
            self._lead_task.layout_patterns = result

        print(f"\n📊 Checks: {result.checks_passed}/{result.checks_run}")
        print(f"📊 Findings: {len(result.findings)}")
        return result  # Return result for QA aggregation

    async def _run_layout_patterns_legacy(self) -> str:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            result = await self._run_design_review_new()
            # Extract tuple for sequential mode compatibility
            feedback_text = f"Score: {result.score}, Findings: {len(result.findings)}"
            return feedback_text, result.fix_required
        else:
            return await self._run_design_review_legacy()

    async def _run_design_review_new(self) -> DesignReviewResult:
        """Neue Architektur: DesignReviewAgent"""
        print("\n🆕 DesignReviewAgent (SDLC-Pattern)")

        # Extrahiere previous_findings aus LeadTask falls vorhanden
        previous_findings = None
        if self._lead_task and self._lead_task.findings:
            previous_findings = self._lead_task.findings

        result: DesignReviewResult = await self._design_review_agent.review(
            output_dir=self.context.output_dir,
            style_guide_content=self.context.style_guide_content,
            iteration=self.context.iteration,
            previous_findings=previous_findings,
            on_message=self._create_message_callback("DesignReviewAgent")
        )

        if self._lead_task:
            self._lead_task.design_review = result
            self._lead_task.status = TaskStatus.DESIGN_REVIEW
            self._lead_task.findings = result.findings

        # Speichere Feedback
        feedback_text = f"Score: {result.score}, Findings: {len(result.findings)}"
        self.context.review_feedback.append(f"Iteration {self.context.iteration + 1}:\n{feedback_text}")

        print(f"\n📊 Score: {result.score}/100")
        print(f"📊 Findings: {len(result.findings)}")

        return result  # Return result for QA aggregation

    async def _run_design_review_legacy(self) -> tuple[str, bool]:
        """Legacy Architektur"""
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
        if self.use_new_agents:
            return await self._run_human_view_new()
        else:
            return await self._run_human_view_legacy()

    async def _run_human_view_new(self) -> str:
        """Neue Architektur: HumanViewAgent"""
        print("\n🆕 HumanViewAgent (SDLC-Pattern)")

        slug = self.context.output_dir.name

        result: HumanViewResult = await self._human_view_agent.review(
            output_dir=str(self.context.output_dir),
            company_slug=slug,
            on_message=self._create_message_callback("HumanViewAgent")
        )

        if self._lead_task:
            self._lead_task.human_view = result

        print(f"\n📊 Overall Score: {result.overall_score}/100")
        print(f"📊 Desktop: {result.desktop_score}/100")
        print(f"📊 Mobile: {result.mobile_score}/100")
        print(f"📊 Critical Fixes: {result.critical_fixes}")
        return f"Human View: {result.overall_score}/100"

    async def _run_human_view_legacy(self) -> str:
        """Legacy Architektur"""
        task = f"""
Prüfe die Website aus Sicht eines echten Nutzers.

WEBSITE: {self.context.output_dir}/

FÜR JEDE SEKTION mache 3 Screenshots:
1. Desktop Viewport (1280x800)
2. Mobile Viewport (375x812)
3. Sektion komplett

PRÜFE jede Sektion auf:
- Lesbarkeit, Buttons, CTAs
- Leerraum-Probleme
- Mobile-Probleme
- Visuelle Hierarchie

Fixe kritische Issues sofort!
"""

        return await self._run_agent("human-view", task)

    async def run_finalize_agent(self) -> str:
        """Agent 15: Finalize - Git Push & Airtable Update"""
        if self.use_new_agents:
            return await self._run_finalize_new()
        else:
            return await self._run_finalize_legacy()

    async def _run_finalize_new(self) -> str:
        """Neue Architektur: FinalizeAgent"""
        print("\n🆕 FinalizeAgent (SDLC-Pattern)")

        result: FinalizeResult = await self._finalize_agent.finalize(
            lead_id=self.context.lead.id,
            company_name=self.context.lead.firma,
            output_dir=str(self.context.output_dir),
            on_message=self._create_message_callback("FinalizeAgent")
        )

        if self._lead_task:
            self._lead_task.finalize = result
            self._lead_task.status = TaskStatus.COMPLETE if result.success else TaskStatus.FAILED

        print(f"\n📊 Git Committed: {result.git_committed}")
        print(f"📊 Git Pushed: {result.git_pushed}")
        print(f"📊 Airtable Updated: {result.airtable_updated}")
        if result.live_url:
            print(f"🌐 Live URL: {result.live_url}")

        return f"Finalize: {'Erfolg' if result.success else 'Fehler'}"

    async def _run_finalize_legacy(self) -> str:
        """Legacy Architektur"""
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

        Modi:
        - use_parallel=True: Parallelisierte Ausführung mit QA-Loop
        - use_parallel=False: Sequentielle Ausführung (Standard)
        """
        # Parallelisierter Modus
        if self.use_parallel and self.use_new_agents:
            return await self._generate_parallel()

        # Sequentieller Modus (Legacy oder neue Agents)
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


async def generate_website(
    lead: Lead,
    base_output_dir: str = "docs",
    use_new_agents: Optional[bool] = None,
    use_parallel: Optional[bool] = None
) -> Path:
    """
    Convenience-Funktion zum Generieren einer Website.

    Args:
        lead: Lead-Daten aus Airtable
        base_output_dir: Basis-Verzeichnis für Output
        use_new_agents: True = neue Agent-Klassen, False = Legacy, None = ENV
        use_parallel: True = parallelisierte Ausführung, False = sequentiell, None = ENV

    Returns:
        Pfad zum generierten Website-Verzeichnis

    Usage:
        # Legacy-Modus (default)
        await generate_website(lead)

        # Neue Agent-Klassen (sequentiell)
        await generate_website(lead, use_new_agents=True)

        # Parallelisiert mit QA-Loop
        await generate_website(lead, use_new_agents=True, use_parallel=True)

        # Via Environment-Variable
        export USE_NEW_AGENTS=true USE_PARALLEL=true
        await generate_website(lead)
    """
    orchestrator = LeadPagesOrchestrator(lead, base_output_dir, use_new_agents, use_parallel)
    return await orchestrator.generate()
