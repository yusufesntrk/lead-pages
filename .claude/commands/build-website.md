---
argument-hint: [firmenname] [website-url]
description: Vollständige Website-Erstellung mit allen Agents in Kette
---

# Website-Build Pipeline

Erstelle eine vollständige Website für **$1** basierend auf der Original-Website **$2**.

## Pipeline - Agents in Reihenfolge

Führe die folgenden Agents **nacheinander** aus. Warte bis jeder Agent fertig ist, bevor du den nächsten startest.

### Phase 1: Website erstellen

1. **website-builder**
   - Erstelle die komplette Website für $1
   - Original-Website: $2
   - Output: `docs/$1/`
   - Extrahiere Style Guide, Logo, Content
   - Erstelle index.html, styles.css, script.js

2. **subpages-builder**
   - Erstelle alle relevanten Unterseiten für `docs/$1/`
   - about.html, contact.html, services.html
   - impressum.html, datenschutz.html
   - Weitere Seiten je nach Branche

### Phase 2: Bilder & Medien

3. **team-photos-extractor**
   - Extrahiere echte Team-Fotos von $2
   - Suche auch auf Anwaltsportalen, LinkedIn, etc.
   - Binde gefundene Fotos in die Website ein

4. **placeholder-replacer**
   - Finde alle SVG-Platzhalter (Team, Gebäude, Produkte)
   - Ersetze durch echte Bilder von $2

5. **broken-images-fixer**
   - Finde nicht angezeigte Bilder
   - Behebe falsche Pfade, fehlende Dateien

### Phase 3: Content-Qualität

6. **testimonials-verifier**
   - Finde echte Testimonials von $2 oder Google Reviews
   - Integriere in die Website
   - Keine Fake-Testimonials!

7. **image-quality-checker**
   - Prüfe Bildauflösung (min. 72dpi)
   - Prüfe Dateigröße (max. 500KB)
   - Prüfe Retina-Support (@2x)

8. **image-authenticity-checker**
   - Prüfe ob Team-Fotos echt sind
   - Prüfe ob Testimonial-Fotos echt sind
   - Keine Stock-Fotos erlaubt!

### Phase 4: Technische Prüfung

9. **google-maps-verifier**
   - Prüfe Google Maps Embed URLs
   - Stelle sicher dass Business-Profil verlinkt ist
   - Nicht nur Adresse!

10. **links-checker**
    - Prüfe ALLE Links auf der Website
    - Interne Links (Navigation, CTAs)
    - Externe Links (Social Media, Maps)
    - Keine 404-Fehler!

11. **responsive-checker**
    - Prüfe Desktop-Ansicht (1280x800)
    - Prüfe Mobile-Ansicht (375x667)
    - Keine abgeschnittenen Elemente
    - Navigation funktioniert

## Nach Abschluss

Wenn alle Agents erfolgreich durchgelaufen sind:

1. **Git Commit:**
   ```
   git add docs/$1/
   git commit -m "Add landing page for $1"
   git push origin main
   ```

2. **Airtable Update:**
   - Setze "Seite erstellt" auf ✓
   - Trage Landingpage URL ein: `https://lead-pages.pages.dev/$1/`

3. **Zusammenfassung:**
   - Liste alle erstellten Seiten
   - Liste alle gefundenen/behobenen Probleme
   - Finale URL mitteilen

---

**WICHTIG:** Jeder Agent muss seine Aufgabe vollständig abschließen bevor der nächste startet. Bei Fehlern: Problem dokumentieren und mit nächstem Agent fortfahren.
