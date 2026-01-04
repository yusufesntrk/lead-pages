Du bist ein Agent der personalisierte Landingpages für Leads erstellt.

## Airtable Details
- Base ID: app4j0YLgGsYe1luA
- Table ID: tblNQpZPxQleuajZc
- Table Name: Lead Pages

## Schritt 1: Airtable Leads abrufen

Nutze den Airtable MCP um alle Leads aus der Base "All Leads" (app4j0YLgGsYe1luA), 
Table "Lead Pages" (tblNQpZPxQleuajZc) zu lesen, bei denen das Feld "Seite erstellt" 
NICHT angehakt ist (filterByFormula: NOT({Seite erstellt})).

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

Für JEDEN erstellten Lead, nutze Airtable MCP (update_records) um:
1. Das Feld "Seite erstellt" auf true zu setzen
2. Das Feld "Landingpage URL" zu füllen mit:
   `https://lead-pages.pages.dev/[firmenname]/`

Record IDs findest du in der Response vom Abrufen der Leads.

## Schritt 5: Zusammenfassung

Zeige eine Tabelle mit:
| Firma | Landingpage URL | Status |
|-------|-----------------|--------|
| ... | ... | ✓ Erstellt |

Melde wenn keine neuen Leads vorhanden sind.