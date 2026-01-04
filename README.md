# Lead Pages Generator

Generiert personalisierte Landingpages für Leads mit Claude Code und deployed sie auf Cloudflare Pages.

## Setup (einmalig)

### 1. GitHub Repo erstellen
```bash
cd /Users/yusufesentuerk/lead-pages
git init
git add .
git commit -m "Initial setup"
gh repo create lead-pages --public --push
```

### 2. Cloudflare Pages verbinden
1. Gehe zu [Cloudflare Dashboard](https://dash.cloudflare.com/) → Pages
2. "Create a project" → "Connect to Git"
3. Wähle das `lead-pages` Repository
4. Build settings:
   - Build command: (leer lassen)
   - Build output directory: `docs`
5. Save and Deploy

### 3. Custom Domain (optional)
In Cloudflare Pages → Custom Domains → `leads.leyal.tech`

## Verwendung

### 1. Leads vorbereiten
Bearbeite `leads.csv` mit deinen Leads:
```csv
firma,branche,website,ansprechpartner,pain_point
TechCorp GmbH,IT,techcorp.de,Max Müller,Zu viele Bewerbungen
```

### 2. Seiten generieren
Terminal öffnen und ausführen:
```bash
cd /Users/yusufesentuerk/lead-pages
claude -p "$(cat generate-prompt.md)"
```

### 3. Fertig!
Nach dem Push sind die Seiten live unter:
- `https://lead-pages.pages.dev/techcorp-gmbh/`
- oder `https://leads.leyal.tech/techcorp-gmbh/`

## Struktur
```
lead-pages/
├── docs/                  # Generierte Seiten (Cloudflare Build Output)
│   ├── firma-a/
│   │   └── index.html
│   └── firma-b/
│       └── index.html
├── leads.csv              # Deine Lead-Liste
├── template.html          # Basis-Template
├── generate-prompt.md     # Claude Code Prompt
└── README.md
```
