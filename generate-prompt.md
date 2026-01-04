Lies die Datei leads.csv in diesem Verzeichnis.

Für JEDE Zeile in der CSV (außer Header):

1. Erstelle einen Ordner in docs/ mit dem Firmennamen (lowercase, Leerzeichen durch Bindestriche ersetzen, Umlaute ersetzen: ä→ae, ö→oe, ü→ue, ß→ss)

2. Erstelle eine personalisierte index.html basierend auf template.html mit folgenden Anpassungen:
   - {{FIRMA}} → Firmenname aus CSV
   - {{BRANCHE}} → Branche aus CSV
   - {{ANSPRECHPARTNER}} → Ansprechpartner aus CSV
   - {{PAIN_POINT}} → Pain Point aus CSV, ausformuliert als 2-3 Sätze
   - {{SOLUTION_TEXT}} → Schreibe 2-3 Sätze wie ShortSelect/Leyal Tech diesen spezifischen Pain Point löst
   - {{BENEFITS_HTML}} → Generiere 3-4 branchenspezifische Benefits als HTML:
     <div class="benefit">
       <div class="benefit-icon">✓</div>
       <div>[Benefit Text]</div>
     </div>

3. Die Benefits sollen spezifisch für die Branche und den Pain Point sein, nicht generisch.

4. Speichere die Datei als docs/[firmenname]/index.html

Nachdem alle Seiten erstellt sind:
- git add .
- git commit -m "Neue Lead-Seiten generiert: [Liste der Firmennamen]"
- git push

Zeige mir am Ende eine Liste aller erstellten Seiten mit ihren zukünftigen URLs.