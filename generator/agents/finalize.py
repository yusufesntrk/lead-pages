"""
Finalize Agent - Git und Airtable Deployment.

Committed die Website zu Git und aktualisiert
den Airtable-Record mit der Live-URL.
"""

import re
from pathlib import Path
from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import FinalizeResult
from ..config import AIRTABLE_BASE_ID, AIRTABLE_TABLE_ID


class FinalizeAgent(BaseAgent):
    """
    Finalisiert die Website-Erstellung.

    Der Finalize-Agent:
    - Committed und pusht zu Git
    - Aktualisiert Airtable-Record
    - Gibt Live-URL zurück
    """

    @property
    def agent_name(self) -> str:
        return "finalize"

    async def finalize(
        self,
        lead_id: str,
        company_name: str,
        output_dir: Path | str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> FinalizeResult:
        """
        Finalisiert die Website.

        Args:
            lead_id: Airtable Record ID
            company_name: Firmenname (für Commit-Message)
            output_dir: Verzeichnis mit fertiger Website
            on_message: Callback für Streaming-Messages

        Returns:
            FinalizeResult mit Git/Airtable Status und Live-URL
        """
        # String zu Path konvertieren
        if isinstance(output_dir, str):
            output_dir = Path(output_dir)

        # Erstelle URL-Slug
        slug = self._slugify(company_name)
        live_url = f"https://lead-pages.pages.dev/{slug}/"

        prompt = self._build_prompt(
            lead_id=lead_id,
            company_name=company_name,
            output_dir=output_dir,
            slug=slug,
            live_url=live_url
        )

        result_text, error = await self._query_with_retry(
            prompt=prompt,
            max_retries=2,
            on_message=on_message
        )

        if error:
            return FinalizeResult(success=False, error=error)

        return self._parse_result(result_text, live_url)

    def _slugify(self, text: str) -> str:
        """Konvertiert Text zu URL-sicherem Slug."""
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

    def _build_prompt(
        self,
        lead_id: str,
        company_name: str,
        output_dir: Path,
        slug: str,
        live_url: str
    ) -> str:
        """Baut den Task-Prompt für den Agent."""

        return f"""
## AUFGABE

Finalisiere die Website für: **{company_name}**

## DATEN

- **Output-Verzeichnis:** {output_dir}
- **URL-Slug:** {slug}
- **Airtable Record ID:** {lead_id}
- **Live URL:** {live_url}

## SCHRITT 1: GIT COMMIT & PUSH

```bash
# Status prüfen
git status

# Nur Website-Ordner stagen
git add {output_dir}/

# Commit
git commit -m "Add landing page for {company_name}

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

# Push
git push origin main
```

Bei Fehler: `git pull --rebase origin main` dann nochmal pushen.

## SCHRITT 2: AIRTABLE AKTUALISIEREN

```
mcp__airtable__update_records({{
    baseId: "{AIRTABLE_BASE_ID}",
    tableId: "{AIRTABLE_TABLE_ID}",
    records: [{{
        id: "{lead_id}",
        fields: {{
            "Seite erstellt": true,
            "Landingpage URL": "{live_url}"
        }}
    }}]
}})
```

## OUTPUT

```
═══════════════════════════════════════════════════════════════
  FINALIZE REPORT
═══════════════════════════════════════════════════════════════

📤 GIT:
  [✅/❌] Commit: "Add landing page for {company_name}"
  [✅/❌] Push: origin/main

📊 AIRTABLE:
  [✅/❌] Record: {lead_id}
  [✅/❌] Seite erstellt: true
  [✅/❌] Landingpage URL: {live_url}

🌐 LIVE URL: {live_url}

═══════════════════════════════════════════════════════════════
```
"""

    def _parse_result(self, result_text: str, live_url: str) -> FinalizeResult:
        """
        Parsed das Ergebnis und prüft Erfolg.
        """
        result = FinalizeResult(success=True, live_url=live_url)

        # Prüfe Git Status
        if "git" in result_text.lower():
            if "✅" in result_text and ("commit" in result_text.lower() or "push" in result_text.lower()):
                result.git_committed = True
                result.git_pushed = True
            elif "error" in result_text.lower() or "❌" in result_text:
                result.success = False
                result.error = "Git push failed"

        # Prüfe Airtable Status
        if "airtable" in result_text.lower():
            if "✅" in result_text and "seite erstellt" in result_text.lower():
                result.airtable_updated = True
            elif "error" in result_text.lower() or "❌" in result_text:
                # Git kann trotzdem erfolgreich sein
                result.airtable_updated = False

        # Gesamt-Erfolg
        result.success = result.git_pushed  # Mindestens Git muss klappen

        return result
