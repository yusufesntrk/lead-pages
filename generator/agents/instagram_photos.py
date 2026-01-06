"""
Instagram Photos Agent - Extrahiert Fotos von Instagram.

Für Restaurants, Cafés und andere Firmen mit Instagram-Präsenz.
"""

from typing import Optional, Callable, Any
from dataclasses import dataclass, field

from .base import BaseAgent
from ..results import BaseResult


@dataclass
class InstagramPhotosResult(BaseResult):
    """Ergebnis der Instagram-Extraktion."""
    photos_found: int = 0
    photos_downloaded: list[str] = field(default_factory=list)
    instagram_handle: Optional[str] = None
    categories: dict = field(default_factory=dict)  # {"food": 3, "interior": 2}


class InstagramPhotosAgent(BaseAgent):
    """
    Agent zum Extrahieren von Fotos von Instagram.

    Workflow:
    1. Instagram-Handle finden (Style Guide oder WebSearch)
    2. Profil mit Playwright öffnen
    3. Bild-URLs extrahieren
    4. Bilder lokal speichern
    5. Kategorisieren (food, interior, team, etc.)
    """

    @property
    def agent_name(self) -> str:
        return "instagram_photos"

    async def extract(
        self,
        company_name: str,
        city: str,
        branche: str,
        instagram_handle: Optional[str],
        output_dir: str,
        max_photos: int = 10,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> InstagramPhotosResult:
        """
        Extrahiert Fotos von Instagram.

        Args:
            company_name: Firmenname
            city: Stadt für Suche
            branche: Branche (Restaurant, Café, etc.)
            instagram_handle: Instagram-Handle (falls bekannt)
            output_dir: Ausgabeverzeichnis
            max_photos: Maximale Anzahl Fotos
            on_message: Callback für Streaming

        Returns:
            InstagramPhotosResult
        """
        prompt = f"""
Extrahiere Fotos von Instagram für {company_name}.

## INSTAGRAM-HANDLE

{f"Bekannt: @{instagram_handle}" if instagram_handle else "Unbekannt - muss gesucht werden"}

## SCHRITT 1: Handle finden (falls nicht bekannt)

WebSearch: "{company_name} {city} Instagram"

## SCHRITT 2: Instagram öffnen

```javascript
playwright_navigate({{
    url: "https://www.instagram.com/{instagram_handle or '[HANDLE]'}/",
    headless: true
}})

// Warten bis Bilder geladen
playwright_evaluate({{ script: "await new Promise(r => setTimeout(r, 3000))" }})
```

## SCHRITT 3: Bild-URLs extrahieren

```javascript
playwright_evaluate({{
    script: `
        const images = Array.from(document.querySelectorAll('img'));
        const posts = images
            .filter(img => img.src.includes('cdninstagram.com'))
            .filter(img => img.naturalWidth > 200)
            .map(img => ({{ src: img.src, alt: img.alt }}))
            .slice(0, {max_photos});
        JSON.stringify(posts);
    `
}})
```

## SCHRITT 4: Bilder herunterladen

```bash
mkdir -p {output_dir}/assets/images
curl -L -o {output_dir}/assets/images/[kategorie]-[nummer].jpg "[URL]"
```

## SCHRITT 5: Bilder kategorisieren

Nach visueller Prüfung (Read Tool auf jedes Bild!):

| Kategorie | Dateiname | Beschreibung |
|-----------|-----------|--------------|
| food | food-1.jpg, food-2.jpg | Gerichte, Speisen |
| interior | interior-1.jpg | Innenraum |
| exterior | exterior-1.jpg | Außenbereich |
| team | team-1.jpg | Personen, Team |

## BRANCHE

{branche}

## WICHTIG

- ALLE Bilder LOKAL speichern!
- NIEMALS Instagram-URLs direkt verlinken!
- JEDES Bild visuell prüfen (Read Tool)!
- Browser am Ende schließen: playwright_close()
- Max. {max_photos} Fotos

## OUTPUT

INSTAGRAM: @[handle]
HERUNTERGELADEN:
- food-1.jpg: [Beschreibung]
- interior-1.jpg: [Beschreibung]
...

KATEGORIEN:
- food: X
- interior: Y
- team: Z
"""

        result_text, error = await self._query_with_retry(prompt, on_message=on_message)

        if error:
            return InstagramPhotosResult(success=False, error=error)

        return self._parse_result(result_text)

    def _parse_result(self, text: str) -> InstagramPhotosResult:
        """Parst das Ergebnis."""
        photos_downloaded = []
        categories = {}
        handle = None

        # Parse Instagram handle
        if "INSTAGRAM:" in text:
            line = text.split("INSTAGRAM:")[1].split("\n")[0]
            handle = line.strip().lstrip("@")

        # Parse downloaded photos
        if "HERUNTERGELADEN:" in text:
            section = text.split("HERUNTERGELADEN:")[1]
            if "KATEGORIEN:" in section:
                section = section.split("KATEGORIEN:")[0]

            for line in section.split("\n"):
                line = line.strip()
                if line.startswith("-") and ".jpg" in line:
                    filename = line.split(":")[0].strip("- ")
                    photos_downloaded.append(f"assets/images/{filename}")

        # Parse categories
        if "KATEGORIEN:" in text:
            section = text.split("KATEGORIEN:")[1]
            for line in section.split("\n"):
                line = line.strip()
                if line.startswith("-") and ":" in line:
                    parts = line.strip("- ").split(":")
                    if len(parts) >= 2:
                        cat = parts[0].strip()
                        try:
                            count = int(parts[1].strip())
                            categories[cat] = count
                        except ValueError:
                            pass

        return InstagramPhotosResult(
            success=True,
            photos_found=len(photos_downloaded),
            photos_downloaded=photos_downloaded,
            instagram_handle=handle,
            categories=categories
        )
