"""
Result-Dataclasses für alle Lead Pages Agents.

Jeder Agent gibt ein typisiertes Result-Objekt zurück,
das vom Orchestrator verarbeitet werden kann.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Any
from datetime import datetime


# =============================================================================
# ENUMS
# =============================================================================

class TaskStatus(Enum):
    """Status einer Lead-Generierung."""
    PENDING = "pending"
    STYLE_GUIDE = "style_guide"
    LOGO = "logo"
    HOMEPAGE = "homepage"
    SUBPAGES = "subpages"
    LEGAL_PAGES = "legal_pages"
    TEAM_PHOTOS = "team_photos"
    REFERENCES = "references"
    LINK_QA = "link_qa"
    DESIGN_REVIEW = "design_review"
    FIXING = "fixing"
    FINALIZING = "finalizing"
    COMPLETE = "complete"
    FAILED = "failed"
    PARTIAL = "partial"


class Severity(Enum):
    """Schweregrad eines Findings."""
    CRITICAL = "critical"  # Muss gefixt werden
    MAJOR = "major"        # Sollte gefixt werden
    MINOR = "minor"        # Nice to have


class ReviewStatus(Enum):
    """Status eines Reviews."""
    PENDING = "pending"
    APPROVED = "approved"
    NEEDS_CHANGES = "needs_changes"


# =============================================================================
# BASE RESULT
# =============================================================================

@dataclass
class BaseResult:
    """
    Basis für alle Agent-Results.

    Jedes Result hat mindestens success und error.
    """
    success: bool = True
    error: Optional[str] = None

    def to_dict(self) -> dict:
        """Konvertiert zu Dictionary für Serialisierung."""
        return {
            "success": self.success,
            "error": self.error,
        }


# =============================================================================
# FINDING (für Reviews)
# =============================================================================

@dataclass
class Finding:
    """
    Einzelnes Problem gefunden bei Review.

    Enthält alle Informationen die zum Fixen benötigt werden.
    """
    id: str                          # Eindeutige ID (z.B. "F001")
    severity: str                    # "critical", "major", "minor"
    location: str                    # Datei:Zeile (z.B. "index.html:45")
    problem: str                     # Beschreibung des Problems
    fix_instruction: str             # Wie es gefixt werden soll
    fix_code: str = ""               # Optional: Code-Snippet für Fix
    fix_agent: str = "homepage"      # Welcher Agent soll fixen

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "severity": self.severity,
            "location": self.location,
            "problem": self.problem,
            "fix_instruction": self.fix_instruction,
            "fix_code": self.fix_code,
            "fix_agent": self.fix_agent,
        }


# =============================================================================
# FIX-LOOP STATS
# =============================================================================

@dataclass
class FixLoopStats:
    """Statistiken eines Fix-Loops."""
    phase: str
    loops_run: int
    issues_fixed: int
    issues_remaining: int
    variation_applied: Optional[str] = None
    duration_seconds: float = 0.0

    def to_dict(self) -> dict:
        return {
            "phase": self.phase,
            "loops_run": self.loops_run,
            "issues_fixed": self.issues_fixed,
            "issues_remaining": self.issues_remaining,
            "variation_applied": self.variation_applied,
            "duration_seconds": self.duration_seconds,
        }


# =============================================================================
# AGENT-SPECIFIC RESULTS
# =============================================================================

@dataclass
class StyleGuideResult(BaseResult):
    """
    Ergebnis des StyleGuide-Agents.

    Enthält extrahierte Design-Informationen und Firmendaten.
    """
    # Design
    colors: dict = field(default_factory=dict)      # {"primary": "#xxx", "secondary": "#xxx", ...}
    fonts: dict = field(default_factory=dict)       # {"heading": "Inter", "body": "Inter"}
    spacing: dict = field(default_factory=dict)     # {"section": "4rem", "element": "1rem"}

    # Firmendaten
    company_data: dict = field(default_factory=dict)  # Name, Adresse, Telefon, etc.

    # Content
    team_members: list = field(default_factory=list)   # [{name, role, photo_url}, ...]
    services: list = field(default_factory=list)       # [{title, description}, ...]
    hero_content: dict = field(default_factory=dict)   # {headline, subtext, cta}

    # Original-Texte (für Legal Pages)
    impressum_text: Optional[str] = None
    datenschutz_text: Optional[str] = None

    # Datei
    style_guide_path: Optional[str] = None
    logo_url: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "colors": self.colors,
            "fonts": self.fonts,
            "spacing": self.spacing,
            "company_data": self.company_data,
            "team_members": self.team_members,
            "services": self.services,
            "hero_content": self.hero_content,
            "style_guide_path": self.style_guide_path,
            "logo_url": self.logo_url,
        })
        return base


@dataclass
class HomepageResult(BaseResult):
    """Ergebnis des Homepage-Agents."""
    files_created: list[str] = field(default_factory=list)  # ["index.html", "styles.css", "script.js"]
    sections_created: list[str] = field(default_factory=list)  # ["hero", "services", "team", ...]
    cta_count: int = 0
    has_hero: bool = False
    has_footer: bool = False
    has_navigation: bool = False

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "files_created": self.files_created,
            "sections_created": self.sections_created,
            "cta_count": self.cta_count,
            "has_hero": self.has_hero,
            "has_footer": self.has_footer,
            "has_navigation": self.has_navigation,
        })
        return base


@dataclass
class SubpagesResult(BaseResult):
    """Ergebnis des Subpages-Agents."""
    pages_created: list[str] = field(default_factory=list)  # ["kontakt.html", "ueber-uns.html", ...]
    total_sections: int = 0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "pages_created": self.pages_created,
            "total_sections": self.total_sections,
        })
        return base


@dataclass
class LegalPagesResult(BaseResult):
    """Ergebnis des LegalPages-Agents."""
    pages_created: list[str] = field(default_factory=list)  # ["impressum.html", "datenschutz.html"]
    placeholders_found: int = 0  # Sollte 0 sein!
    used_fallback: bool = False

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "pages_created": self.pages_created,
            "placeholders_found": self.placeholders_found,
            "used_fallback": self.used_fallback,
        })
        return base


@dataclass
class LogoResult(BaseResult):
    """Ergebnis des Logo-Agents."""
    svg_path: Optional[str] = None       # Pfad zur SVG-Datei
    original_format: Optional[str] = None  # "png", "jpg", "gif", "svg"
    converted_to_svg: bool = False
    used_text_logo: bool = False         # Falls kein Bild-Logo gefunden

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "svg_path": self.svg_path,
            "original_format": self.original_format,
            "converted_to_svg": self.converted_to_svg,
            "used_text_logo": self.used_text_logo,
        })
        return base


@dataclass
class TeamPhotosResult(BaseResult):
    """Ergebnis des TeamPhotos-Agents."""
    photos_found: int = 0
    photos_downloaded: list[str] = field(default_factory=list)  # ["assets/max-mustermann.jpg", ...]
    sources: list[str] = field(default_factory=list)  # ["website", "linkedin", "google"]

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "photos_found": self.photos_found,
            "photos_downloaded": self.photos_downloaded,
            "sources": self.sources,
        })
        return base


@dataclass
class ReferencesResult(BaseResult):
    """Ergebnis des References-Agents."""
    testimonials_found: int = 0
    google_rating: Optional[float] = None
    google_reviews_count: int = 0
    references_page_created: bool = False

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "testimonials_found": self.testimonials_found,
            "google_rating": self.google_rating,
            "google_reviews_count": self.google_reviews_count,
            "references_page_created": self.references_page_created,
        })
        return base


@dataclass
class LinkQAResult(BaseResult):
    """Ergebnis des LinkQA-Agents."""
    links_checked: int = 0
    broken_links_found: int = 0
    broken_links_fixed: int = 0
    external_links_count: int = 0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "links_checked": self.links_checked,
            "broken_links_found": self.broken_links_found,
            "broken_links_fixed": self.broken_links_fixed,
            "external_links_count": self.external_links_count,
        })
        return base


@dataclass
class DesignReviewResult(BaseResult):
    """Ergebnis des DesignReview-Agents."""
    findings: list[Finding] = field(default_factory=list)
    fix_required: bool = False
    score: int = 0  # 0-100
    review_status: ReviewStatus = ReviewStatus.PENDING
    screenshots_taken: int = 0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "findings": [f.to_dict() for f in self.findings],
            "fix_required": self.fix_required,
            "score": self.score,
            "review_status": self.review_status.value,
            "screenshots_taken": self.screenshots_taken,
        })
        return base


@dataclass
class FinalizeResult(BaseResult):
    """Ergebnis des Finalize-Agents."""
    git_committed: bool = False
    git_pushed: bool = False
    airtable_updated: bool = False
    live_url: Optional[str] = None

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "git_committed": self.git_committed,
            "git_pushed": self.git_pushed,
            "airtable_updated": self.airtable_updated,
            "live_url": self.live_url,
        })
        return base


@dataclass
class InstagramPhotosResult(BaseResult):
    """Ergebnis des Instagram-Photos-Agents."""
    photos_found: int = 0
    photos_downloaded: list[str] = field(default_factory=list)
    instagram_handle: Optional[str] = None
    categories: dict = field(default_factory=dict)  # {"food": 3, "interior": 2}

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "photos_found": self.photos_found,
            "photos_downloaded": self.photos_downloaded,
            "instagram_handle": self.instagram_handle,
            "categories": self.categories,
        })
        return base


@dataclass
class ImageVerificationResult(BaseResult):
    """Ergebnis der Bildprüfung."""
    images_checked: int = 0
    mismatches_found: int = 0
    mismatches_fixed: int = 0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "images_checked": self.images_checked,
            "mismatches_found": self.mismatches_found,
            "mismatches_fixed": self.mismatches_fixed,
        })
        return base


@dataclass
class LayoutPatternsResult(BaseResult):
    """Ergebnis der Layout-Prüfung."""
    checks_run: int = 0
    checks_passed: int = 0
    issues_found: int = 0
    issues_fixed: int = 0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "checks_run": self.checks_run,
            "checks_passed": self.checks_passed,
            "issues_found": self.issues_found,
            "issues_fixed": self.issues_fixed,
        })
        return base


@dataclass
class HumanViewResult(BaseResult):
    """Ergebnis der Human View Prüfung."""
    sections_checked: int = 0
    desktop_score: int = 0
    mobile_score: int = 0
    overall_score: int = 0
    critical_fixes: int = 0
    warnings: int = 0

    def to_dict(self) -> dict:
        base = super().to_dict()
        base.update({
            "sections_checked": self.sections_checked,
            "desktop_score": self.desktop_score,
            "mobile_score": self.mobile_score,
            "overall_score": self.overall_score,
            "critical_fixes": self.critical_fixes,
            "warnings": self.warnings,
        })
        return base


# =============================================================================
# LEAD TASK (Haupt-Status-Objekt)
# =============================================================================

@dataclass
class LeadTask:
    """
    Status einer kompletten Lead-Generierung.

    Enthält alle Agent-Results und Tracking-Informationen.
    """
    # Identifikation
    id: str                           # Airtable Record ID
    company: str                      # Firmenname
    branche: str                      # Branche

    # Status
    status: TaskStatus = TaskStatus.PENDING
    output_dir: Optional[str] = None  # z.B. "docs/max-mustermann-gmbh"

    # Agent Results
    style_guide: Optional[StyleGuideResult] = None
    logo: Optional[LogoResult] = None
    homepage: Optional[HomepageResult] = None
    subpages: Optional[SubpagesResult] = None
    legal_pages: Optional[LegalPagesResult] = None
    team_photos: Optional[TeamPhotosResult] = None
    references: Optional[ReferencesResult] = None
    instagram_photos: Optional[InstagramPhotosResult] = None
    image_verification: Optional[ImageVerificationResult] = None
    layout_patterns: Optional[LayoutPatternsResult] = None
    human_view: Optional[HumanViewResult] = None
    link_qa: Optional[LinkQAResult] = None
    design_review: Optional[DesignReviewResult] = None
    finalize: Optional[FinalizeResult] = None

    # Fix-Loop Tracking
    findings: list[Finding] = field(default_factory=list)
    fix_loop_stats: list[FixLoopStats] = field(default_factory=list)
    fix_iterations: int = 0

    # Error
    error: Optional[str] = None

    # Timestamps
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        """Konvertiert zu Dictionary für Serialisierung."""
        return {
            "id": self.id,
            "company": self.company,
            "branche": self.branche,
            "status": self.status.value,
            "output_dir": self.output_dir,
            "style_guide": self.style_guide.to_dict() if self.style_guide else None,
            "logo": self.logo.to_dict() if self.logo else None,
            "homepage": self.homepage.to_dict() if self.homepage else None,
            "subpages": self.subpages.to_dict() if self.subpages else None,
            "legal_pages": self.legal_pages.to_dict() if self.legal_pages else None,
            "team_photos": self.team_photos.to_dict() if self.team_photos else None,
            "references": self.references.to_dict() if self.references else None,
            "instagram_photos": self.instagram_photos.to_dict() if self.instagram_photos else None,
            "image_verification": self.image_verification.to_dict() if self.image_verification else None,
            "layout_patterns": self.layout_patterns.to_dict() if self.layout_patterns else None,
            "human_view": self.human_view.to_dict() if self.human_view else None,
            "link_qa": self.link_qa.to_dict() if self.link_qa else None,
            "design_review": self.design_review.to_dict() if self.design_review else None,
            "finalize": self.finalize.to_dict() if self.finalize else None,
            "findings": [f.to_dict() for f in self.findings],
            "fix_loop_stats": [s.to_dict() for s in self.fix_loop_stats],
            "fix_iterations": self.fix_iterations,
            "error": self.error,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def to_airtable(self) -> dict:
        """Konvertiert zu Airtable-Update-Format."""
        result = {
            "Seite erstellt": self.status == TaskStatus.COMPLETE,
        }
        if self.finalize and self.finalize.live_url:
            result["Landingpage URL"] = self.finalize.live_url
        return result
