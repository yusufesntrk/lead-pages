Du bist ein Agent der personalisierte Landingpages für Leads erstellt.

## Schritt 1: Airtable Leads abrufen

Nutze den Airtable MCP um alle Leads aus der Base "Lead Pages", Table "Leads" zu lesen, 
bei denen das Feld "Seite erstellt" NICHT angehakt ist (false/leer).

## Schritt 2: Für jeden Lead eine Seite erstellen

Für JEDEN Lead ohne erstellte Seite:

1. Erstelle einen Ordner in docs/ mit dem Firmennamen:
   - lowercase
   - Leerzeichen → Bindestriche
   - Umlaute ersetzen: ä→ae, ö→oe, ü→ue, ß→ss
   - Sonderzeichen entfernen

2. Erstelle eine personalisierte index.html basierend auf template.html:
   - {{FIRMA}} → Firmenname
   - {{BRANCHE}} → Branche
   - {{ANSPRECHPARTNER}} → Ansprechpartner
   - {{PAIN_POINT}} → Pain Point als 2-3 ausformulierte Sätze
   - {{SOLUTION_TEXT}} → 2-3 Sätze wie ShortSelect/Leyal Tech diesen Pain Point löst
   - {{BENEFITS_HTML}} → 3-4 branchenspezifische Benefits als HTML:
     ```html
     <div class="benefit">
       <div class="benefit-icon">✓</div>
       <div>[Benefit passend zur Branche und Pain Point]</div>
     </div>
     ```

3. Speichere als docs/[firmenname]/index.html

## Schritt 3: Git Push

Nachdem ALLE Seiten erstellt sind:
```bash
git add .
git commit -m "Neue Lead-Seiten: [Liste der Firmennamen]"
git push
```

## Schritt 4: Airtable aktualisieren

Für JEDEN erstellten Lead, nutze Airtable MCP um:
1. Das Feld "Seite erstellt" auf true/checked zu setzen
2. Das Feld "Landingpage URL" zu füllen mit:
   `https://lead-pages.pages.dev/[firmenname]/`

## Schritt 5: Zusammenfassung

Zeige eine Tabelle mit:
| Firma | Landingpage URL | Status |
|-------|-----------------|--------|
| ... | ... | ✓ Erstellt |

Melde wenn keine neuen Leads vorhanden sind.