# Lead Pages Generator

Generiert personalisierte Landingpages für Leads mit Claude Code und deployed sie auf Cloudflare Pages.
Lead-Daten werden in Airtable verwaltet.

## Setup (einmalig)

### 1. Airtable Personal Access Token erstellen
1. Gehe zu [Airtable Developer Hub](https://airtable.com/create/tokens)
2. "Create new token"
3. Scopes auswählen:
   - `data.records:read`
   - `data.records:write`
   - `schema.bases:read`
   - `schema.bases:write`
4. Access: Wähle "All current and future bases" oder spezifische Workspace
5. Token kopieren (beginnt mit `pat...`)

### 2. Airtable MCP in Claude Code einrichten
Füge zu deiner Claude Code MCP Config hinzu:

**macOS:** `~/.claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "airtable": {
      "command": "npx",
      "args": ["airtable-mcp-server"],
      "env": {
        "AIRTABLE_API_KEY": "patXXXXXXXXXXXXXX"
      }
    }
  }
}
```

### 3. Cloudflare Pages verbinden
1. [Cloudflare Dashboard](https://dash.cloudflare.com/) → Pages
2. "Create a project" → "Connect to Git"
3. Repository `lead-pages` wählen
4. Build output directory: `docs`
5. Save and Deploy

### 4. Custom Domain (optional)
Cloudflare Pages → Custom Domains → `leads.leyal.tech`

## Verwendung

### Seiten generieren
```bash
cd /Users/yusufesentuerk/lead-pages
claude -p "$(cat generate-prompt.md)"
```

Der Agent:
1. Liest Leads aus Airtable (nur wo "Seite erstellt" = false)
2. Generiert personalisierte Landingpages
3. Pushed zu GitHub → Cloudflare deployed automatisch
4. Schreibt die URLs zurück in Airtable
5. Setzt "Seite erstellt" auf ✓

## Airtable Struktur

**Base:** Lead Pages
**Table:** Leads

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| Firma | Single line text | Firmenname |
| Branche | Single select | IT, Healthcare, Finance, etc. |
| Website | URL | Firmenwebsite |
| Ansprechpartner | Single line text | Kontaktperson |
| Position | Single line text | Job-Titel |
| Pain Point | Long text | Hauptproblem im Recruiting |
| Seite erstellt | Checkbox | ✓ wenn Landingpage generiert |
| Landingpage URL | URL | Generierte Seiten-URL |
| Erstellt am | Created time | Auto |

## Projekt-Struktur
```
lead-pages/
├── docs/                  # Generierte Seiten (Cloudflare Build Output)
│   ├── firma-a/
│   │   └── index.html
│   └── firma-b/
│       └── index.html
├── template.html          # Basis-Template
├── generate-prompt.md     # Claude Code Prompt
└── README.md
```
