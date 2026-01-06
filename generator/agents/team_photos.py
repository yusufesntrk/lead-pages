"""
Team Photos Agent - Sucht und lädt Team-Fotos.

Quellen: Original-Website, LinkedIn, Google Images
"""

from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import TeamPhotosResult


class TeamPhotosAgent(BaseAgent):
    """
    Agent zum Finden und Herunterladen von Team-Fotos.

    Sucht auf:
    1. Original-Website (Team-Sektion, Über uns)
    2. LinkedIn Profile
    3. Google Images

    Speichert Fotos lokal in assets/
    """

    @property
    def agent_name(self) -> str:
        return "team_photos"

    async def find(
        self,
        team_members: list[dict],
        company_name: str,
        website_url: Optional[str],
        output_dir: str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> TeamPhotosResult:
        """
        Sucht Team-Fotos für alle Team-Mitglieder.

        Args:
            team_members: Liste von Team-Mitgliedern [{name, role}, ...]
            company_name: Firmenname für Suche
            website_url: URL der Original-Website (kann None sein)
            output_dir: Ausgabeverzeichnis für Fotos
            on_message: Callback für Streaming

        Returns:
            TeamPhotosResult mit gefundenen Fotos
        """
        if not team_members:
            return TeamPhotosResult(
                success=True,
                photos_found=0,
                photos_downloaded=[],
                sources=[]
            )

        members_text = "\n".join([
            f"- {m.get('name', 'Unbekannt')} ({m.get('role', 'Mitarbeiter')})"
            for m in team_members
        ])

        prompt = f"""
Suche Team-Fotos für {company_name}.

## TEAM-MITGLIEDER

{members_text}

## SUCHQUELLEN (in dieser Reihenfolge)

1. **Original-Website** ({website_url or 'Nicht vorhanden'})
   - Team-Sektion
   - Über uns Seite
   - Impressum (manchmal Geschäftsführer-Foto)

2. **LinkedIn**
   - Nach "[Name] [Firma]" suchen
   - Profil-Foto extrahieren

3. **Google Images**
   - "[Name] [Firma] [Stadt]"
   - Nur hochauflösende, professionelle Fotos

## OUTPUT-VERZEICHNIS

{output_dir}/assets/

## DATEINAMEN

team-[vorname]-[nachname].jpg

## WICHTIG

- Jedes Foto MUSS zur Person passen!
- NIEMALS Stock-Fotos oder generische Bilder!
- IMMER lokal speichern (nicht URL verlinken)
- Foto vor Download visuell prüfen (Read Tool)

## OUTPUT

Gib am Ende aus:

GEFUNDENE FOTOS:
- [Dateiname]: [Quelle]
- ...

NICHT GEFUNDEN:
- [Name]: [Grund]
"""

        result_text, error = await self._query_with_retry(prompt, on_message=on_message)

        if error:
            return TeamPhotosResult(success=False, error=error)

        return self._parse_result(result_text, team_members)

    def _parse_result(self, text: str, team_members: list) -> TeamPhotosResult:
        """Parst das Ergebnis und extrahiert gefundene Fotos."""
        photos_downloaded = []
        sources = set()

        # Suche nach "GEFUNDENE FOTOS:" Sektion
        if "GEFUNDENE FOTOS:" in text:
            lines = text.split("GEFUNDENE FOTOS:")[1].split("\n")
            for line in lines:
                if line.strip().startswith("-") and ":" in line:
                    parts = line.strip("- ").split(":")
                    if len(parts) >= 2:
                        filename = parts[0].strip()
                        source = parts[1].strip().lower()

                        if filename.endswith(('.jpg', '.png', '.webp')):
                            photos_downloaded.append(f"assets/{filename}")

                            if "linkedin" in source:
                                sources.add("linkedin")
                            elif "google" in source:
                                sources.add("google")
                            else:
                                sources.add("website")
                elif "NICHT GEFUNDEN:" in line:
                    break

        return TeamPhotosResult(
            success=True,
            photos_found=len(photos_downloaded),
            photos_downloaded=photos_downloaded,
            sources=list(sources)
        )
