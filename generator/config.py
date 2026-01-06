"""
Zentrale Konfiguration für Lead Pages Generator.

Alle Agent-Optionen, Tools und Einstellungen werden hier verwaltet.
"""

from pathlib import Path
from typing import Optional, Dict

from claude_code_sdk import ClaudeCodeOptions


# =============================================================================
# TOOL CONFIGURATION
# =============================================================================

# Base Tools - für alle Agents verfügbar
BASE_TOOLS = [
    "Read",
    "Write",
    "Edit",
    "Bash",
    "Grep",
    "Glob",
    "WebFetch",
    "WebSearch",
]

# MCP Tool Patterns - Wildcards für MCP Server
MCP_PATTERNS = [
    "mcp__playwright__*",
    "mcp__airtable__*",
]

# Alle Tools kombiniert
ALL_TOOLS = BASE_TOOLS + MCP_PATTERNS

# Agent-spezifische Tool-Sets
STYLE_GUIDE_TOOLS = ALL_TOOLS
HOMEPAGE_TOOLS = ALL_TOOLS
SUBPAGES_TOOLS = ALL_TOOLS
LEGAL_PAGES_TOOLS = BASE_TOOLS + ["mcp__playwright__*"]  # Kein Airtable
LOGO_TOOLS = ALL_TOOLS
TEAM_PHOTOS_TOOLS = ALL_TOOLS
REFERENCES_TOOLS = ALL_TOOLS
LINK_QA_TOOLS = BASE_TOOLS + ["mcp__playwright__*"]
DESIGN_REVIEW_TOOLS = ALL_TOOLS
FINALIZE_TOOLS = BASE_TOOLS + ["mcp__airtable__*"]  # Git + Airtable
INSTAGRAM_TOOLS = ALL_TOOLS  # Playwright für Instagram
IMAGE_VERIFICATION_TOOLS = BASE_TOOLS + ["mcp__playwright__*"]  # Bildprüfung
LAYOUT_PATTERNS_TOOLS = BASE_TOOLS  # Nur CSS-Analyse
HUMAN_VIEW_TOOLS = ALL_TOOLS  # Screenshots + Fixes
REFERENCES_RESEARCH_TOOLS = ALL_TOOLS  # WebSearch + Playwright
REFERENCES_PAGE_TOOLS = ALL_TOOLS  # Bild-Download + HTML


# =============================================================================
# MODEL CONFIGURATION
# =============================================================================

# Haupt-Model für die meisten Agents
AGENT_MODEL = "opus"

# Schnelleres Model für einfache Tasks
FINALIZE_MODEL = "sonnet"

# Model-Zuordnung pro Agent (falls abweichend von AGENT_MODEL)
AGENT_MODELS = {
    "style_guide": "opus",
    "homepage": "opus",
    "subpages": "opus",
    "legal_pages": "opus",
    "logo": "opus",
    "team_photos": "opus",
    "references": "opus",
    "references_research": "opus",
    "references_page": "opus",
    "instagram_photos": "opus",
    "image_verification": "opus",
    "layout_patterns": "sonnet",  # CSS-Check ist einfacher
    "human_view": "opus",
    "link_qa": "opus",
    "design_review": "opus",
    "finalize": "sonnet",  # Schneller für Git/Airtable
}


# =============================================================================
# FIX-LOOP CONFIGURATION
# =============================================================================

# Anzahl identischer Findings bevor Deadlock erkannt wird
IDENTICAL_FINDINGS_THRESHOLD = 3

# Variation-Strategien bei Deadlock
VARIATION_STRATEGIES = [
    "rephrase",           # Problem anders formulieren
    "add_context",        # Mehr Code-Kontext hinzufügen
    "break_down",         # In kleinere Sub-Findings aufteilen
    "different_approach", # Alternativen Lösungsweg vorschlagen
]


# =============================================================================
# OUTPUT CONFIGURATION
# =============================================================================

# Basis-Verzeichnis für generierte Websites
OUTPUT_BASE_DIR = "docs"

# Temporäres Verzeichnis für Playwright Screenshots
PLAYWRIGHT_TMP_DIR = ".playwright-tmp"


# =============================================================================
# AIRTABLE CONFIGURATION
# =============================================================================

AIRTABLE_BASE_ID = "app4j0YLgGsYe1luA"
AIRTABLE_TABLE_ID = "tblNQpZPxQleuajZc"


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def load_mcp_config(cwd: str) -> Optional[str]:
    """
    Lädt .mcp.json Pfad aus dem Arbeitsverzeichnis.

    Returns:
        Pfad zu .mcp.json als String, oder None wenn nicht gefunden
    """
    mcp_path = Path(cwd) / ".mcp.json"
    if mcp_path.exists():
        return str(mcp_path)
    return None


def load_env_file(cwd: str) -> Dict[str, str]:
    """
    Lädt .env Datei aus dem Arbeitsverzeichnis.

    Returns:
        Dictionary mit Environment-Variablen
    """
    env_vars = {}
    env_path = Path(cwd) / ".env"
    if env_path.exists():
        try:
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if '=' in line:
                        key, _, value = line.partition('=')
                        key = key.strip()
                        value = value.strip()
                        # Quotes entfernen
                        if (value.startswith('"') and value.endswith('"')) or \
                           (value.startswith("'") and value.endswith("'")):
                            value = value[1:-1]
                        env_vars[key] = value
        except IOError:
            pass
    return env_vars


def create_agent_options(
    working_dir: str,
    system_prompt: str,
    allowed_tools: Optional[list] = None,
    model: Optional[str] = None
) -> ClaudeCodeOptions:
    """
    Factory für konsistente Agent-Optionen.

    Stellt sicher, dass alle Agents korrekt konfiguriert sind:
    - permission_mode="bypassPermissions" (KRITISCH!)
    - MCP Server geladen
    - Environment-Variablen geladen

    Args:
        working_dir: Arbeitsverzeichnis des Agents
        system_prompt: System Prompt für den Agent
        allowed_tools: Liste erlaubter Tools (default: ALL_TOOLS)
        model: Model zu verwenden (default: AGENT_MODEL)

    Returns:
        Konfiguriertes ClaudeCodeOptions Objekt
    """
    mcp_path = load_mcp_config(working_dir)
    env_vars = load_env_file(working_dir)

    return ClaudeCodeOptions(
        model=model or AGENT_MODEL,
        system_prompt=system_prompt,
        allowed_tools=allowed_tools or ALL_TOOLS,
        cwd=working_dir,
        mcp_servers=mcp_path,
        permission_mode="bypassPermissions",  # KRITISCH: Verhindert Permission-Prompts
        env=env_vars if env_vars else None,
    )


def get_agent_tools(agent_name: str) -> list:
    """
    Gibt die erlaubten Tools für einen Agent zurück.

    Args:
        agent_name: Name des Agents (z.B. "style_guide", "homepage")

    Returns:
        Liste der erlaubten Tools
    """
    tool_mapping = {
        "style_guide": STYLE_GUIDE_TOOLS,
        "homepage": HOMEPAGE_TOOLS,
        "subpages": SUBPAGES_TOOLS,
        "legal_pages": LEGAL_PAGES_TOOLS,
        "logo": LOGO_TOOLS,
        "team_photos": TEAM_PHOTOS_TOOLS,
        "references": REFERENCES_TOOLS,
        "references_research": REFERENCES_RESEARCH_TOOLS,
        "references_page": REFERENCES_PAGE_TOOLS,
        "instagram_photos": INSTAGRAM_TOOLS,
        "image_verification": IMAGE_VERIFICATION_TOOLS,
        "layout_patterns": LAYOUT_PATTERNS_TOOLS,
        "human_view": HUMAN_VIEW_TOOLS,
        "link_qa": LINK_QA_TOOLS,
        "design_review": DESIGN_REVIEW_TOOLS,
        "finalize": FINALIZE_TOOLS,
    }
    return tool_mapping.get(agent_name, ALL_TOOLS)


def get_agent_model(agent_name: str) -> str:
    """
    Gibt das Model für einen Agent zurück.

    Args:
        agent_name: Name des Agents

    Returns:
        Model-Name (z.B. "opus", "sonnet")
    """
    return AGENT_MODELS.get(agent_name, AGENT_MODEL)
