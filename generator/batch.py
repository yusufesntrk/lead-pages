"""
Lead Pages Generator - Batch Mode

Verarbeitet mehrere Leads parallel mit Rate Limiting und Git-Konflikt-Vermeidung.

Verwendung:
    python -m generator.batch --all                    # Alle unerledigten Leads
    python -m generator.batch --leads rec1,rec2,rec3   # Spezifische Leads
    python -m generator.batch --parallel 3             # Max. 3 parallel
    python -m generator.batch --test                   # Test-Modus (kein Git/Airtable)
"""

import argparse
import asyncio
import os
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests
from dotenv import load_dotenv

from .main import (
    AIRTABLE_BASE_ID,
    AIRTABLE_TABLE_ID,
    fetch_lead_by_id,
    fetch_leads,
    get_airtable_headers,
    record_to_lead,
    update_lead,
)
from .orchestrator import Lead, LeadPagesOrchestrator

# Lade .env
load_dotenv()


@dataclass
class BatchResult:
    """Ergebnis eines einzelnen Lead-Durchlaufs"""
    lead_id: str
    firma: str
    success: bool
    output_path: Optional[Path] = None
    error: Optional[str] = None
    duration_seconds: float = 0.0
    live_url: Optional[str] = None


@dataclass
class BatchSummary:
    """Zusammenfassung des Batch-Durchlaufs"""
    total: int = 0
    successful: int = 0
    failed: int = 0
    results: list[BatchResult] = field(default_factory=list)
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    @property
    def duration(self) -> float:
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0


class BatchGenerator:
    """
    Batch-Generator für Lead Pages.

    Features:
    - Parallele Verarbeitung mit konfigurierbarem Limit
    - Rate Limiting für API-Calls
    - Sequentielles Git-Pushing zur Konfliktvermeidung
    - Detailliertes Logging und Zusammenfassung
    """

    def __init__(
        self,
        max_parallel: int = 3,
        test_mode: bool = False,
        verbose: bool = False,
        output_dir: str = "docs"
    ):
        self.max_parallel = max_parallel
        self.test_mode = test_mode
        self.verbose = verbose
        self.output_dir = output_dir
        self.summary = BatchSummary()
        self._git_lock = asyncio.Lock()
        self._semaphore: Optional[asyncio.Semaphore] = None

    async def generate_single(self, lead: Lead) -> BatchResult:
        """Generiert Website für einen einzelnen Lead"""
        start_time = datetime.now()
        result = BatchResult(
            lead_id=lead.id,
            firma=lead.firma,
            success=False
        )

        try:
            print(f"\n{'='*60}")
            print(f"🚀 STARTE: {lead.firma}")
            print(f"{'='*60}")

            # Website generieren
            orchestrator = LeadPagesOrchestrator(lead, self.output_dir)
            output_path = await orchestrator.generate()

            result.output_path = output_path
            result.success = True

            # Git & Airtable (sequentiell, mit Lock)
            if not self.test_mode:
                async with self._git_lock:
                    await self._finalize(lead, output_path)
                    result.live_url = f"https://lead-pages.pages.dev/{output_path.name}/"

            duration = (datetime.now() - start_time).total_seconds()
            result.duration_seconds = duration

            print(f"\n✅ FERTIG: {lead.firma} ({duration:.1f}s)")

        except Exception as e:
            result.error = str(e)
            result.duration_seconds = (datetime.now() - start_time).total_seconds()
            print(f"\n❌ FEHLER bei {lead.firma}: {e}")

        return result

    async def _finalize(self, lead: Lead, output_path: Path):
        """Git commit/push und Airtable Update (unter Lock)"""
        url = f"https://lead-pages.pages.dev/{output_path.name}/"

        # Git
        print(f"   📤 Git push für {lead.firma}...")
        try:
            subprocess.run(
                ["git", "add", str(output_path)],
                check=True,
                capture_output=True
            )
            subprocess.run(
                ["git", "commit", "-m", f"Add landing page for {lead.firma}"],
                check=True,
                capture_output=True
            )
            subprocess.run(
                ["git", "push", "origin", "main"],
                check=True,
                capture_output=True
            )
            print(f"   ✅ Gepusht: {output_path.name}/")
        except subprocess.CalledProcessError as e:
            stderr = e.stderr.decode() if e.stderr else str(e)
            # Ignoriere "nothing to commit"
            if "nothing to commit" not in stderr:
                print(f"   ⚠️ Git-Warnung: {stderr}")

        # Airtable
        print(f"   📊 Airtable Update für {lead.firma}...")
        try:
            update_lead(lead.id, {
                "Seite erstellt": True,
                "Landingpage URL": url
            })
            print(f"   ✅ Airtable aktualisiert")
        except Exception as e:
            print(f"   ⚠️ Airtable-Fehler: {e}")

    async def run(self, leads: list[Lead]) -> BatchSummary:
        """Führt Batch-Generierung für alle Leads durch"""
        self.summary = BatchSummary(
            total=len(leads),
            start_time=datetime.now()
        )
        self._semaphore = asyncio.Semaphore(self.max_parallel)

        print(f"\n{'#'*60}")
        print(f"# BATCH GENERATOR")
        print(f"# Leads: {len(leads)}")
        print(f"# Parallel: {self.max_parallel}")
        print(f"# Test-Modus: {'Ja' if self.test_mode else 'Nein'}")
        print(f"{'#'*60}\n")

        async def limited_generate(lead: Lead) -> BatchResult:
            async with self._semaphore:
                return await self.generate_single(lead)

        # Alle Leads parallel (mit Semaphore-Limit)
        tasks = [limited_generate(lead) for lead in leads]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Ergebnisse verarbeiten
        for r in results:
            if isinstance(r, Exception):
                self.summary.failed += 1
            elif isinstance(r, BatchResult):
                self.summary.results.append(r)
                if r.success:
                    self.summary.successful += 1
                else:
                    self.summary.failed += 1

        self.summary.end_time = datetime.now()
        self._print_summary()

        return self.summary

    def _print_summary(self):
        """Druckt Zusammenfassung"""
        print(f"\n{'='*60}")
        print(f"📊 BATCH ZUSAMMENFASSUNG")
        print(f"{'='*60}")
        print(f"   Gesamt:      {self.summary.total}")
        print(f"   Erfolgreich: {self.summary.successful} ✅")
        print(f"   Fehlerhaft:  {self.summary.failed} ❌")
        print(f"   Dauer:       {self.summary.duration:.1f}s")
        print(f"{'='*60}")

        if self.summary.results:
            print(f"\n📋 DETAILS:\n")
            for r in self.summary.results:
                status = "✅" if r.success else "❌"
                print(f"   {status} {r.firma}")
                if r.live_url:
                    print(f"      🌐 {r.live_url}")
                if r.error:
                    print(f"      ⚠️ {r.error[:80]}...")
                print(f"      ⏱️ {r.duration_seconds:.1f}s")

        print()


def get_pending_leads() -> list[dict]:
    """Holt alle Leads wo 'Seite erstellt' = False"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_ID}"
    params = {
        "filterByFormula": "NOT({Seite erstellt})",
        "maxRecords": 100
    }

    response = requests.get(url, headers=get_airtable_headers(), params=params)
    response.raise_for_status()

    return response.json().get("records", [])


async def main():
    """Hauptfunktion für Batch-Modus"""
    parser = argparse.ArgumentParser(description="Lead Pages Batch Generator")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Alle unerledigten Leads verarbeiten"
    )
    parser.add_argument(
        "--leads",
        type=str,
        help="Komma-separierte Lead-IDs (z.B. rec1,rec2,rec3)"
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=3,
        help="Max. parallele Generierungen (default: 3)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Test-Modus (kein Git/Airtable)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Detailliertes Logging"
    )
    parser.add_argument(
        "--output",
        default="docs",
        help="Output-Verzeichnis (default: docs)"
    )
    parser.add_argument(
        "--yes", "-y",
        action="store_true",
        help="Bestätigung überspringen"
    )

    args = parser.parse_args()

    # Leads sammeln
    leads: list[Lead] = []

    if args.all:
        print("📥 Lade alle unerledigten Leads...")
        try:
            records = get_pending_leads()
            leads = [record_to_lead(r) for r in records]
            print(f"   Gefunden: {len(leads)} Leads")
        except Exception as e:
            print(f"❌ Airtable-Fehler: {e}")
            sys.exit(1)

    elif args.leads:
        print("📥 Lade spezifische Leads...")
        lead_ids = [lid.strip() for lid in args.leads.split(",")]
        for lid in lead_ids:
            try:
                record = fetch_lead_by_id(lid)
                if record:
                    leads.append(record_to_lead(record))
                else:
                    print(f"   ⚠️ Lead nicht gefunden: {lid}")
            except Exception as e:
                print(f"   ⚠️ Fehler bei {lid}: {e}")

    else:
        print("❌ Bitte --all oder --leads angeben")
        print("\nBeispiele:")
        print("  python -m generator.batch --all")
        print("  python -m generator.batch --leads rec123,rec456")
        print("  python -m generator.batch --all --parallel 5 --test")
        sys.exit(1)

    if not leads:
        print("ℹ️ Keine Leads zu verarbeiten")
        sys.exit(0)

    # Bestätigung
    print(f"\n📌 ZU VERARBEITEN ({len(leads)} Leads):")
    for lead in leads[:10]:  # Max 10 anzeigen
        print(f"   • {lead.firma} ({lead.branche})")
    if len(leads) > 10:
        print(f"   ... und {len(leads) - 10} weitere")

    if not args.test and not args.yes:
        confirm = input(f"\n▶️ {len(leads)} Websites generieren? (j/n): ").strip().lower()
        if confirm != "j":
            print("👋 Abgebrochen")
            sys.exit(0)

    # Batch starten
    generator = BatchGenerator(
        max_parallel=args.parallel,
        test_mode=args.test,
        verbose=args.verbose,
        output_dir=args.output
    )

    summary = await generator.run(leads)

    # Exit Code
    sys.exit(0 if summary.failed == 0 else 1)


def main_sync():
    """Synchroner Entry Point"""
    asyncio.run(main())


if __name__ == "__main__":
    main_sync()
