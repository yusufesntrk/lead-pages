"""
Lead Pages Generator - Main Entry Point

Verwendung:
    python -m generator.main                    # Interaktiv Lead auswählen
    python -m generator.main --lead recXXXXX    # Spezifischer Lead
    python -m generator.main --test             # Test mit Beispiel-Lead
"""

import asyncio
import os
import sys
from pathlib import Path
from typing import Optional

import requests
from dotenv import load_dotenv

from .orchestrator import Lead, generate_website


# Lade .env
load_dotenv()

# Airtable Konfiguration
AIRTABLE_TOKEN = os.getenv("AIRTABLE_TOKEN")
AIRTABLE_BASE_ID = "app4j0YLgGsYe1luA"
AIRTABLE_TABLE_ID = "tblNQpZPxQleuajZc"


def get_airtable_headers() -> dict:
    """Returns Airtable API headers"""
    if not AIRTABLE_TOKEN:
        raise ValueError("AIRTABLE_TOKEN nicht gesetzt. Bitte in .env definieren.")
    return {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }


def fetch_leads(max_records: int = 100) -> list[dict]:
    """Holt alle Leads aus Airtable"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_ID}"
    params = {"maxRecords": max_records}

    response = requests.get(url, headers=get_airtable_headers(), params=params)
    response.raise_for_status()

    return response.json().get("records", [])


def fetch_lead_by_id(record_id: str) -> Optional[dict]:
    """Holt einen spezifischen Lead"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_ID}/{record_id}"

    response = requests.get(url, headers=get_airtable_headers())
    if response.status_code == 404:
        return None
    response.raise_for_status()

    return response.json()


def update_lead(record_id: str, fields: dict) -> dict:
    """Aktualisiert einen Lead in Airtable"""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_ID}/{record_id}"

    response = requests.patch(
        url,
        headers=get_airtable_headers(),
        json={"fields": fields}
    )
    response.raise_for_status()

    return response.json()


def record_to_lead(record: dict) -> Lead:
    """Konvertiert Airtable Record zu Lead Objekt"""
    fields = record.get("fields", {})

    return Lead(
        id=record["id"],
        firma=fields.get("Firma", "Unbekannt"),
        branche=fields.get("Branche", "Unbekannt"),
        website=fields.get("Website"),
        strasse=fields.get("Straße"),
        plz=fields.get("PLZ"),
        ort=fields.get("Ort"),
        telefon=fields.get("Telefon"),
        email=fields.get("Email"),
        google_rating=fields.get("Google Rating"),
        google_reviews=fields.get("Google Reviews"),
    )


def select_lead_interactive(leads: list[dict]) -> Optional[Lead]:
    """Interaktive Lead-Auswahl"""
    print("\n📋 VERFÜGBARE LEADS:\n")

    for i, record in enumerate(leads, 1):
        fields = record.get("fields", {})
        firma = fields.get("Firma", "Unbekannt")
        branche = fields.get("Branche", "Unbekannt")
        erstellt = "✅" if fields.get("Seite erstellt") else "❌"

        print(f"{i:3}. {erstellt} {firma} ({branche})")

    print("\n0. Abbrechen")

    while True:
        try:
            choice = input("\nWähle Lead (Nummer): ").strip()
            if choice == "0":
                return None

            index = int(choice) - 1
            if 0 <= index < len(leads):
                return record_to_lead(leads[index])

            print("❌ Ungültige Auswahl")
        except ValueError:
            print("❌ Bitte eine Nummer eingeben")


def create_test_lead() -> Lead:
    """Erstellt einen Test-Lead für Entwicklung"""
    return Lead(
        id="test_001",
        firma="Test GmbH",
        branche="Software",
        website=None,
        strasse="Teststraße 1",
        plz="12345",
        ort="Teststadt",
        telefon="+49 123 456789",
        email="info@test.de",
        google_rating=4.5,
        google_reviews=42,
    )


async def main():
    """Hauptfunktion"""
    import argparse

    parser = argparse.ArgumentParser(description="Lead Pages Generator")
    parser.add_argument("--lead", help="Airtable Record ID des Leads")
    parser.add_argument("--test", action="store_true", help="Test-Modus mit Beispiel-Lead")
    parser.add_argument("--output", default="docs", help="Output-Verzeichnis")
    parser.add_argument("--yes", "-y", action="store_true", help="Bestätigung überspringen")

    args = parser.parse_args()

    print("\n" + "="*60)
    print("🚀 LEAD PAGES GENERATOR")
    print("="*60 + "\n")

    # Lead auswählen
    if args.test:
        print("🧪 Test-Modus aktiviert")
        lead = create_test_lead()

    elif args.lead:
        print(f"📥 Lade Lead: {args.lead}")
        record = fetch_lead_by_id(args.lead)
        if not record:
            print(f"❌ Lead '{args.lead}' nicht gefunden")
            sys.exit(1)
        lead = record_to_lead(record)

    else:
        print("📥 Lade Leads aus Airtable...")
        try:
            records = fetch_leads()
            if not records:
                print("❌ Keine Leads gefunden")
                sys.exit(1)

            lead = select_lead_interactive(records)
            if not lead:
                print("👋 Abgebrochen")
                sys.exit(0)

        except requests.RequestException as e:
            print(f"❌ Airtable-Fehler: {e}")
            print("💡 Tipp: AIRTABLE_TOKEN in .env setzen")
            sys.exit(1)

    # Bestätigung
    print(f"\n📌 AUSGEWÄHLTER LEAD:")
    print(f"   Firma:    {lead.firma}")
    print(f"   Branche:  {lead.branche}")
    print(f"   Website:  {lead.website or 'Keine'}")
    print(f"   Ort:      {lead.ort or 'Unbekannt'}")

    if not args.yes:
        confirm = input("\n▶️ Website generieren? (j/n): ").strip().lower()
        if confirm != "j":
            print("👋 Abgebrochen")
            sys.exit(0)

    # Website generieren
    try:
        output_path = await generate_website(lead, args.output)

        # Finalisierung (wenn nicht Test-Modus)
        if not args.test and lead.id != "test_001":
            url = f"https://lead-pages.pages.dev/{output_path.name}/"

            # 1. Git commit & push
            print("\n📤 Git commit & push...")
            import subprocess
            try:
                subprocess.run(["git", "add", str(output_path)], check=True, capture_output=True)
                subprocess.run(
                    ["git", "commit", "-m", f"Add landing page for {lead.firma}"],
                    check=True,
                    capture_output=True
                )
                subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True)
                print(f"   ✅ Gepusht: {output_path.name}/")
            except subprocess.CalledProcessError as e:
                print(f"   ⚠️ Git-Fehler: {e.stderr.decode() if e.stderr else str(e)}")

            # 2. Airtable aktualisieren
            print("\n📊 Airtable aktualisieren...")
            update_lead(lead.id, {
                "Seite erstellt": True,
                "Landingpage URL": url
            })
            print(f"   ✅ Seite erstellt: True")
            print(f"   ✅ Landingpage URL: {url}")

        print(f"\n🎉 Fertig! Website unter: {output_path}")
        print(f"   Lokal öffnen: file://{output_path.absolute()}/index.html")
        if not args.test and lead.id != "test_001":
            print(f"   Live URL: https://lead-pages.pages.dev/{output_path.name}/")

    except Exception as e:
        print(f"\n❌ Fehler beim Generieren: {e}")
        raise


def main_sync():
    """Synchroner Entry Point für CLI"""
    asyncio.run(main())


if __name__ == "__main__":
    main_sync()
