"""
References Research Agent - Recherchiert echte Testimonials.

Sucht auf Original-Website, Google Reviews, und recherchiert
Personen/Firmen für echte Referenzen.
"""

from typing import Optional, Callable, Any
from dataclasses import dataclass, field

from .base import BaseAgent
from ..results import ReferencesResult


@dataclass
class Testimonial:
    """Ein gefundenes Testimonial."""
    quote: str
    person_name: str
    person_role: Optional[str] = None
    company_name: Optional[str] = None
    photo_url: Optional[str] = None
    company_logo_url: Optional[str] = None
    source: str = "website"  # "website", "google", "linkedin"


@dataclass
class ReferencesResearchResult:
    """Ergebnis der Recherche."""
    success: bool = True
    error: Optional[str] = None
    testimonials: list[Testimonial] = field(default_factory=list)
    google_rating: Optional[float] = None
    google_reviews_count: int = 0


class ReferencesResearchAgent(BaseAgent):
    """
    Agent zum Recherchieren von echten Testimonials.

    Workflow:
    1. Original-Website nach Testimonials scannen
    2. Google Reviews prüfen
    3. Für jede Person/Firma: LinkedIn recherchieren
    4. Profilbilder und Logos finden
    """

    @property
    def agent_name(self) -> str:
        return "references_research"

    async def research(
        self,
        company_name: str,
        website_url: Optional[str],
        google_rating: Optional[float],
        google_reviews_count: int,
        output_dir: str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> ReferencesResearchResult:
        """
        Recherchiert Testimonials für eine Firma.

        Args:
            company_name: Firmenname
            website_url: URL der Original-Website
            google_rating: Google Rating (falls bekannt)
            google_reviews_count: Anzahl Google Reviews
            output_dir: Ausgabeverzeichnis

        Returns:
            ReferencesResearchResult mit gefundenen Testimonials
        """
        prompt = f"""
Recherchiere echte Testimonials für: {company_name}

## QUELLEN

1. **Original-Website** ({website_url or 'Nicht vorhanden'})
   - Referenzen-Seite
   - Kundenstimmen-Sektion
   - Case Studies

2. **Google Reviews**
   - Rating: {google_rating or 'Unbekannt'}
   - Anzahl: {google_reviews_count or 0}

3. **LinkedIn** (für jede gefundene Person/Firma)
   - Profilbild der Person
   - Firmenlogo
   - Verifizierung der Position

## WORKFLOW PRO TESTIMONIAL

1. Zitat und Name extrahieren
2. Person auf LinkedIn suchen: "[Name] [Firma]"
3. Profilbild-URL notieren
4. Firmenlogo suchen

## ASSET-DOWNLOAD

Speichere in {output_dir}/assets/:
- testimonial-[vorname].jpg (Personenfoto, NICHT SVG!)
- testimonial-[firma]-logo.svg (Firmenlogo, als SVG!)

## WICHTIG

- KEINE Fake-Testimonials erfinden!
- NIEMALS externe URLs im HTML verwenden!
- Alle Assets LOKAL speichern!
- Personenfotos: JPG/PNG (KEIN SVG!)
- Firmenlogos: SVG konvertieren!

## OUTPUT FORMAT

Für jedes gefundene Testimonial:

```
TESTIMONIAL #1
Zitat: "..."
Name: Max Mustermann
Position: Geschäftsführer
Firma: Mustermann GmbH
Foto: testimonial-max.jpg
Logo: testimonial-mustermann-logo.svg
Quelle: website
```

Am Ende:

GOOGLE RATING: X.X (Y Reviews)
TESTIMONIALS GEFUNDEN: N
"""

        result_text, error = await self._query_with_retry(prompt, on_message=on_message)

        if error:
            return ReferencesResearchResult(success=False, error=error)

        return self._parse_result(result_text, google_rating, google_reviews_count)

    def _parse_result(
        self,
        text: str,
        google_rating: Optional[float],
        google_reviews_count: int
    ) -> ReferencesResearchResult:
        """Parst das Ergebnis und extrahiert Testimonials."""
        testimonials = []

        # Parse TESTIMONIAL blocks
        if "TESTIMONIAL #" in text:
            blocks = text.split("TESTIMONIAL #")[1:]
            for block in blocks:
                testimonial = self._parse_testimonial_block(block)
                if testimonial:
                    testimonials.append(testimonial)

        return ReferencesResearchResult(
            success=True,
            testimonials=testimonials,
            google_rating=google_rating,
            google_reviews_count=google_reviews_count
        )

    def _parse_testimonial_block(self, block: str) -> Optional[Testimonial]:
        """Parst einen einzelnen Testimonial-Block."""
        lines = block.strip().split("\n")

        quote = None
        name = None
        role = None
        company = None
        photo = None
        logo = None
        source = "website"

        for line in lines:
            line = line.strip()
            if line.startswith("Zitat:"):
                quote = line.replace("Zitat:", "").strip().strip('"')
            elif line.startswith("Name:"):
                name = line.replace("Name:", "").strip()
            elif line.startswith("Position:"):
                role = line.replace("Position:", "").strip()
            elif line.startswith("Firma:"):
                company = line.replace("Firma:", "").strip()
            elif line.startswith("Foto:"):
                photo = line.replace("Foto:", "").strip()
            elif line.startswith("Logo:"):
                logo = line.replace("Logo:", "").strip()
            elif line.startswith("Quelle:"):
                source = line.replace("Quelle:", "").strip()

        if quote and name:
            return Testimonial(
                quote=quote,
                person_name=name,
                person_role=role,
                company_name=company,
                photo_url=f"assets/{photo}" if photo else None,
                company_logo_url=f"assets/{logo}" if logo else None,
                source=source
            )

        return None
