"""
Base Agent Klasse für Lead Pages Generator.

Alle spezialisierten Agents erben von BaseAgent und
implementieren ihre eigene Logik.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Any, Callable

from claude_code_sdk import query

from ..config import create_agent_options, get_agent_tools, get_agent_model


class BaseAgent(ABC):
    """
    Basis-Klasse für alle Lead Pages Agents.

    Stellt gemeinsame Funktionalität bereit:
    - System Prompt laden
    - Agent-Optionen erstellen
    - Query ausführen mit Streaming
    - Error Handling
    """

    def __init__(self, working_dir: str = "."):
        """
        Initialisiert den Agent.

        Args:
            working_dir: Arbeitsverzeichnis (Projekt-Root)
        """
        self.working_dir = working_dir
        self.system_prompt = self._load_system_prompt()

    @property
    @abstractmethod
    def agent_name(self) -> str:
        """
        Name des Agents (für Config-Lookup).

        z.B. "style_guide", "homepage", "legal_pages"
        """
        pass

    @property
    def prompt_name(self) -> str:
        """
        Name der Prompt-Datei ohne .md

        Default: gleich wie agent_name
        Kann überschrieben werden falls anders benannt.
        """
        return self.agent_name

    def _load_system_prompt(self) -> str:
        """
        Lädt System Prompt aus prompts/ Ordner.

        Sucht nach: generator/prompts/{prompt_name}.md

        Returns:
            Inhalt der Prompt-Datei

        Raises:
            FileNotFoundError: Wenn Prompt-Datei nicht existiert
        """
        prompt_path = Path(__file__).parent.parent / "prompts" / f"{self.prompt_name}.md"

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt-Datei nicht gefunden: {prompt_path}\n"
                f"Erstelle die Datei oder überschreibe prompt_name Property."
            )

        return prompt_path.read_text(encoding="utf-8")

    def _get_options(
        self,
        tools: Optional[list] = None,
        model: Optional[str] = None
    ):
        """
        Erstellt Agent-Optionen.

        Args:
            tools: Überschreibt Standard-Tools für diesen Agent
            model: Überschreibt Standard-Model für diesen Agent

        Returns:
            ClaudeCodeOptions Objekt
        """
        return create_agent_options(
            working_dir=self.working_dir,
            system_prompt=self.system_prompt,
            allowed_tools=tools or get_agent_tools(self.agent_name),
            model=model or get_agent_model(self.agent_name),
        )

    async def _query(
        self,
        prompt: str,
        on_message: Optional[Callable[[Any], None]] = None,
        tools: Optional[list] = None,
        model: Optional[str] = None
    ) -> tuple[Optional[str], Optional[str]]:
        """
        Führt Query aus und sammelt Ergebnis.

        Args:
            prompt: Der Prompt für den Agent
            on_message: Optional Callback für Streaming-Messages
            tools: Überschreibt Standard-Tools
            model: Überschreibt Standard-Model

        Returns:
            Tuple von (result_text, error)
            - Bei Erfolg: (text, None)
            - Bei Fehler: (None, error_message)
        """
        result_text = ""
        options = self._get_options(tools, model)

        try:
            async for msg in query(prompt=prompt, options=options):
                # Callback für UI-Updates
                if on_message:
                    on_message(msg)

                # Text sammeln
                if hasattr(msg, 'content'):
                    for block in msg.content:
                        if hasattr(block, 'text'):
                            result_text += block.text

                # Kosten loggen (optional)
                if hasattr(msg, 'total_cost_usd'):
                    self._log_cost(msg.total_cost_usd)

            return result_text, None

        except Exception as e:
            error_msg = str(e)
            self._log_error(error_msg)
            return None, error_msg

    async def _query_with_retry(
        self,
        prompt: str,
        max_retries: int = 2,
        on_message: Optional[Callable[[Any], None]] = None,
        tools: Optional[list] = None,
        model: Optional[str] = None
    ) -> tuple[Optional[str], Optional[str]]:
        """
        Führt Query mit Retry-Logik aus.

        Retries nur bei transienten Fehlern.
        Nicht bei: content filtering, rate limit, authentication

        Args:
            prompt: Der Prompt
            max_retries: Maximale Anzahl Retries
            on_message: Callback für Messages
            tools: Tool-Override
            model: Model-Override

        Returns:
            Tuple von (result_text, error)
        """
        non_retryable = [
            "content filtering policy",
            "rate_limit",
            "authentication",
        ]

        last_error = None

        for attempt in range(max_retries + 1):
            result, error = await self._query(prompt, on_message, tools, model)

            if error is None:
                return result, None

            last_error = error

            # Prüfe ob retryable
            is_retryable = not any(
                err in error.lower()
                for err in non_retryable
            )

            if not is_retryable:
                return None, error

            if attempt < max_retries:
                self._log_retry(attempt + 1, error)
                # Bei Bild-Fehlern: Hint hinzufügen
                if "Could not process image" in error or "buffer size" in error:
                    prompt += "\n\n⚠️ WICHTIG: Überspringe problematische Bilder und mach ohne sie weiter!"

        return None, last_error

    def _log_cost(self, cost_usd: float) -> None:
        """Loggt Kosten (kann überschrieben werden)."""
        pass  # Default: nichts tun

    def _log_error(self, error: str) -> None:
        """Loggt Fehler (kann überschrieben werden)."""
        print(f"❌ [{self.agent_name}] Error: {error}")

    def _log_retry(self, attempt: int, error: str) -> None:
        """Loggt Retry (kann überschrieben werden)."""
        print(f"⚠️ [{self.agent_name}] Retry {attempt}: {error[:100]}...")


class BaseReviewAgent(BaseAgent):
    """
    Spezialisierte Basis-Klasse für Review-Agents.

    Erweitert BaseAgent um:
    - validate_fix() Methode
    - Finding-Parsing
    """

    async def validate_fix(
        self,
        findings: list,
        files: list[str],
        loop_count: int,
        on_message: Optional[Callable[[Any], None]] = None
    ):
        """
        Validiert ob Fixes erfolgreich waren.

        Args:
            findings: Die ursprünglichen Findings
            files: Die betroffenen Dateien
            loop_count: Aktuelle Loop-Iteration

        Returns:
            Review-Result mit verbleibenden Findings
        """
        # Muss von Subklassen implementiert werden
        raise NotImplementedError("Subklassen müssen validate_fix implementieren")
