"""Agent definitions for the Lead Pages Generator"""

from .definitions import AGENTS, get_agent

# Neue Agent-Klassen (SDLC-Pattern)
from .base import BaseAgent, BaseReviewAgent
from .style_guide import StyleGuideAgent
from .homepage import HomepageAgent
from .subpages import SubpagesAgent
from .legal_pages import LegalPagesAgent
from .logo import LogoAgent
from .link_qa import LinkQAAgent
from .design_review import DesignReviewAgent
from .finalize import FinalizeAgent

# Zusätzliche spezialisierte Agents
from .team_photos import TeamPhotosAgent
from .references_research import ReferencesResearchAgent
from .references_page import ReferencesPageAgent
from .instagram_photos import InstagramPhotosAgent
from .image_verification import ImageVerificationAgent
from .layout_patterns import LayoutPatternsAgent
from .human_view import HumanViewAgent

__all__ = [
    # Legacy (prompt-basiert)
    "AGENTS",
    "get_agent",
    # Basis-Klassen
    "BaseAgent",
    "BaseReviewAgent",
    # Content-Agents
    "StyleGuideAgent",
    "HomepageAgent",
    "SubpagesAgent",
    "LegalPagesAgent",
    "LogoAgent",
    # Asset-Agents
    "TeamPhotosAgent",
    "ReferencesResearchAgent",
    "ReferencesPageAgent",
    "InstagramPhotosAgent",
    # QA-Agents
    "LinkQAAgent",
    "DesignReviewAgent",
    "ImageVerificationAgent",
    "LayoutPatternsAgent",
    "HumanViewAgent",
    # Finalize
    "FinalizeAgent",
]
