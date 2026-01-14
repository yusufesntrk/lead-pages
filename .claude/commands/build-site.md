---
description: Erstellt komplette Website mit allen Unterseiten für ein Unternehmen
argument-hint: [firmenname]
---

# Website erstellen für $ARGUMENTS

Erstelle eine vollständige, professionelle Website für das Unternehmen "$ARGUMENTS".

## Workflow

### Schritt 1: Website-Builder Agent
Nutze den **website-builder** Agent um die Hauptseite zu erstellen:
- Analysiere die Original-Website (falls vorhanden)
- Extrahiere Style Guide, Farben, Logo
- Extrahiere alle Inhalte (Team, Services, Kontakt)
- Erstelle index.html, styles.css, script.js
- Erstelle Impressum und Datenschutz

### Schritt 2: Subpages-Builder Agent
Nutze den **subpages-builder** Agent um alle relevanten Unterseiten zu erstellen:
- Analysiere die Sitemap der Original-Website
- Erstelle alle gefundenen Unterseiten
- Halte das Design konsistent

### Schritt 3: Deployment
Nach Fertigstellung:
1. Kopiere den Ordner nach `~/lead-pages/docs/[firmenname]/`
2. Git commit & push
3. Aktualisiere Airtable (Seite erstellt = true, URL eintragen)

## Wichtige Regeln
- Deutsche Umlaute verwenden (ä, ö, ü, ß)
- KEINE Platzhalter im fertigen HTML
- Echte Daten von der Original-Website
- Responsive Design
- Dezente Animationen (passend zur Branche)

## Output
- Ordner: `docs/[firmenname]/`
- Live-URL: `https://lead-pages.pages.dev/[firmenname]/`