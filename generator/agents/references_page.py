"""
References Page Agent - Erstellt Referenzen-Seite und Testimonials-Sektion.

Nutzt die recherchierten Testimonials vom ReferencesResearchAgent.
"""

from typing import Optional, Callable, Any

from .base import BaseAgent
from ..results import ReferencesResult


class ReferencesPageAgent(BaseAgent):
    """
    Agent zum Erstellen der Referenzen-Seite.

    Erstellt:
    1. referenzen.html - Vollständige Referenzen-Seite
    2. Testimonials-Sektion für Homepage
    """

    @property
    def agent_name(self) -> str:
        return "references_page"

    async def create(
        self,
        testimonials: list,
        google_rating: Optional[float],
        google_reviews_count: int,
        company_name: str,
        output_dir: str,
        style_guide_path: str,
        on_message: Optional[Callable[[Any], None]] = None
    ) -> ReferencesResult:
        """
        Erstellt Referenzen-Seite und Homepage-Integration.

        Args:
            testimonials: Liste von Testimonial-Objekten
            google_rating: Google Rating
            google_reviews_count: Anzahl Google Reviews
            company_name: Firmenname
            output_dir: Ausgabeverzeichnis
            style_guide_path: Pfad zum Style Guide

        Returns:
            ReferencesResult
        """
        if not testimonials and not google_rating:
            return ReferencesResult(
                success=True,
                testimonials_found=0,
                google_rating=None,
                google_reviews_count=0,
                references_page_created=False
            )

        testimonials_text = self._format_testimonials(testimonials)

        prompt = f"""
Erstelle Referenzen-Seite für {company_name}.

## STYLE GUIDE

Lies den Style Guide: {style_guide_path}

## TESTIMONIALS

{testimonials_text if testimonials_text else "Keine Testimonials gefunden."}

## GOOGLE RATING

Rating: {google_rating or 'Nicht vorhanden'}
Reviews: {google_reviews_count or 0}

## OUTPUT-VERZEICHNIS

{output_dir}/

## AUFGABEN

### 1. referenzen.html erstellen

- Header mit Navigation (wie index.html)
- Hero-Bereich: "Unsere Referenzen" o.ä.
- Testimonial-Cards:
  - Zitat
  - Personenfoto: `<img src="assets/testimonial-[name].jpg">` (LOKAL!)
  - Name und Position
  - Firmenlogo: `<img src="assets/testimonial-[firma]-logo.svg">` (LOKAL!)
- Google Rating Widget (falls vorhanden)
- Footer (wie index.html)

### 2. Homepage-Testimonials-Sektion

Falls index.html existiert, füge Testimonials-Sektion hinzu:
- 2-3 ausgewählte Testimonials
- "Mehr Referenzen" Button → referenzen.html

## ASSET-REGELN

- Personenfotos: `<img src="assets/testimonial-[vorname].jpg">` (JPG/PNG!)
- Firmenlogos: `<img src="assets/testimonial-[firma]-logo.svg">` (SVG!)
- NIEMALS externe URLs verwenden!
- NIEMALS Platzhalter im fertigen HTML!

## FALLBACK (keine Testimonials)

Nur Google Rating anzeigen:
- Sterne-Visualisierung
- "X.X von 5 Sternen (Y Bewertungen)"
- Link zu Google

## DEUTSCHE SPRACHE

- Echte Umlaute: ä, ö, ü, ß
- NICHT ae, oe, ue, ss

## OUTPUT

Gib am Ende aus:

ERSTELLT:
- referenzen.html
- Homepage-Sektion aktualisiert: ja/nein

TESTIMONIALS: X
GOOGLE RATING: X.X (Y Reviews)
"""

        result_text, error = await self._query_with_retry(prompt, on_message=on_message)

        if error:
            return ReferencesResult(success=False, error=error)

        return ReferencesResult(
            success=True,
            testimonials_found=len(testimonials) if testimonials else 0,
            google_rating=google_rating,
            google_reviews_count=google_reviews_count,
            references_page_created="referenzen.html" in result_text.lower()
        )

    def _format_testimonials(self, testimonials: list) -> str:
        """Formatiert Testimonials für den Prompt."""
        if not testimonials:
            return ""

        lines = []
        for i, t in enumerate(testimonials, 1):
            lines.append(f"""
### Testimonial #{i}
- Zitat: "{t.quote if hasattr(t, 'quote') else t.get('quote', '')}"
- Name: {t.person_name if hasattr(t, 'person_name') else t.get('person_name', '')}
- Position: {t.person_role if hasattr(t, 'person_role') else t.get('person_role', '')}
- Firma: {t.company_name if hasattr(t, 'company_name') else t.get('company_name', '')}
- Foto: {t.photo_url if hasattr(t, 'photo_url') else t.get('photo_url', '')}
- Logo: {t.company_logo_url if hasattr(t, 'company_logo_url') else t.get('company_logo_url', '')}
""")
        return "\n".join(lines)
