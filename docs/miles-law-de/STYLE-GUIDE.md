# Style Guide: MILES-LAW.DE

## Firmeninformationen

### Grunddaten
- **Kanzleiname:** MILES-LAW.DE
- **Inhaber:** Rechtsanwalt Faris Hussain
- **Slogan:** "Weil Ihr Recht unser Gesetz ist"
- **Branche:** Rechtsanwalt

### Kontaktdaten
- **Adresse:** Großherzog-Friedrich-Straße 2, 77694 Kehl
- **Telefon:** +49 7851 6430763
- **Fax:** +49 7851 6430764
- **E-Mail:** ihr-recht@miles-law.de
- **Website:** http://miles-law.de/
- **Tätigkeitsgebiet:** Bundesweit, insbesondere Kehl, Offenburg, Oberkirch, Achern, Freiburg, Karlsruhe

### Berufsdaten
- **Berufsbezeichnung:** Rechtsanwalt (verliehen in der Bundesrepublik Deutschland)
- **USt-IdNr:** DE356071727
- **Rechtsanwaltskammer:** Freiburg
- **Marke:** M I L E S - L A W.DE (eingetragene Marke)
- **Berufshaftpflicht:** NÜRNBERGER Allgemeine Versicherungs-AG

---

## Farbpalette

### Primärfarben (aus Logo extrahiert)
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Kanzlei-Grün (Primary) | `#009B77` | Logo-Text "MILES-LAW.DE", CTAs, Akzente |
| Kanzlei-Gold (Accent) | `#C9A227` | Slogan, Highlights, Hover-Effekte |

### Sekundärfarben (empfohlen)
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Dunkelgrün (Darker) | `#007A5E` | Buttons Hover, Footer |
| Helles Gold | `#D4B94E` | Akzent-Highlights |
| Anthrazit | `#2B2B2B` | Haupttext |
| Dunkelgrau | `#545454` | Sekundärtext |
| Hellgrau | `#F5F5F5` | Hintergründe, Sections |
| Weiß | `#FFFFFF` | Haupthintergrund |

### Semantische Farben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Erfolg | `#009B77` | Success States (= Primary) |
| Warnung | `#C9A227` | Hinweise (= Gold) |
| Fehler | `#D32F2F` | Error States |
| Info | `#1976D2` | Informationen |

---

## Typografie

### Schriftarten
- **Original-Website:** Century Schoolbook (Serifenschrift)
- **Empfehlung für Rebuild:**
  - **Headlines:** Playfair Display (Google Font) - elegant, seriös
  - **Body:** Source Sans Pro oder Inter - modern, lesbar
  - **Alternative Headlines:** Cormorant Garamond - klassisch-juristisch

### Schriftgrößen
| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 | 48px / 3rem | 36px / 2.25rem |
| H2 | 36px / 2.25rem | 28px / 1.75rem |
| H3 | 24px / 1.5rem | 20px / 1.25rem |
| Body | 18px / 1.125rem | 16px / 1rem |
| Small | 14px / 0.875rem | 14px / 0.875rem |

### Textformatierung
- **Zeilenabstand:** 1.6 - 1.8 für Fließtext
- **Textausrichtung:** Blocksatz (justify) für längere Texte - typisch für juristische Dokumente

---

## Spacing-System

### Basis: 8px Grid
| Variable | Wert |
|----------|------|
| --space-xs | 4px |
| --space-sm | 8px |
| --space-md | 16px |
| --space-lg | 24px |
| --space-xl | 32px |
| --space-2xl | 48px |
| --space-3xl | 64px |
| --space-4xl | 96px |

### Container
- **Max-Width:** 1200px
- **Padding:** 24px (mobile), 48px (desktop)

---

## Komponenten-Styles

### Buttons
```css
/* Primary Button */
.btn-primary {
  background: #009B77;
  color: #FFFFFF;
  padding: 12px 32px;
  border-radius: 4px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: #007A5E;
  box-shadow: 0 4px 12px rgba(0, 155, 119, 0.3);
}

/* Secondary Button (Gold) */
.btn-secondary {
  background: transparent;
  color: #C9A227;
  border: 2px solid #C9A227;
  padding: 12px 32px;
  border-radius: 4px;
}

.btn-secondary:hover {
  background: #C9A227;
  color: #FFFFFF;
}
```

### Cards
```css
.card {
  background: #FFFFFF;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 32px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}
```

---

## Team / Rechtsanwalt

### Faris Hussain
- **Name:** Rechtsanwalt Faris Hussain
- **Position:** Inhaber / Rechtsanwalt
- **Foto:** Kein Porträtfoto auf der Website verfügbar
- **Qualifikationen:**
  - Rechtsanwalt (zugelassen in Deutschland)
  - Mitglied der Rechtsanwaltskammer Freiburg
  - Mitglied Legal Tech Verband Deutschland e.V.
  - Mitglied Deutscher Arbeitsgerichtstag e.V.
- **Ausbildung:**
  - Studium: Rheinische Friedrich-Wilhelms-Universität Bonn
  - 1. Staatsexamen: OLG Köln
  - Referendariat: Aachen
  - 2. Staatsexamen: OLG Köln
- **Sprachkenntnisse:** Deutsch (Muttersprache), Englisch (fortgeschritten), Französisch (fortgeschritten)

---

## Rechtsgebiete / Services

### Hauptrechtsgebiete
1. **Zivilrecht**
   - Berateranwalt und Prozessanwalt
   - Kläger- und Beklagtenseite
   - Allgemeines Vertragsrecht

2. **Strafrecht**
   - Strafverteidigung bundesweit
   - Ermittlungsverfahren bis Rechtsmittelverfahren
   - Regelmäßige Beiordnung als Pflichtverteidiger

3. **Arbeitsrecht**
   - Kündigungsschutz
   - Außergerichtliche und gerichtliche Vertretung
   - Arbeitsgericht Freiburg - Kammern Offenburg

4. **Fahrerlaubnisrecht**
   - MPU-Beratung
   - Entziehung Fahrerlaubnis
   - Verwaltungsverfahren

5. **Ordnungswidrigkeitenrecht**
   - Verkehrsordnungswidrigkeiten
   - Geschwindigkeitsüberschreitung
   - Bußgeldverfahren

### Weitere Rechtsgebiete
- Mietrecht
- Schadenersatz- und Schmerzensgeldrecht
- Versicherungsrecht
- Reiserecht
- Arzthaftungsrecht
- Transport- und Speditionsrecht
- Wirtschafts- und Wettbewerbsrecht
- Markenrecht

---

## Grundsätze der Kanzlei

### Die 6 Grundsätze
1. **"Wir nehmen unsere Pflichten ernst."**
   - Bewusstsein für Achtung und Vertrauen der Anwaltsstellung

2. **"Wir hören Ihnen zu."**
   - Informationen schätzen, Anliegen ernst nehmen

3. **"Wir kennen den sichersten Weg."**
   - Sicherste Strategie zur Erreichung des Rechtsschutzziels

4. **"Wir reden offen mit Ihnen."**
   - Aufzeigen von Chancen, Risiken und Kompromissen

5. **"Wir erkennen, was zu tun ist."**
   - Beherrschung aktueller Gesetze, Kenntnis der Arbeitsweise von Behörden

6. **"Wir unternehmen etwas."**
   - Interessenvertretung mit Nachdruck und taktischem Vorgehen

---

## Inhalte der Seiten

### Kanzlei-Seite
> Die Räume der Kanzlei befinden sich in Kehl am Rhein im Erdgeschoss der Stadtvilla an der Ecke Großherzog-Friedrich-Straße/Kinzigallee. In unmittelbarer Nähe befindet sich die Haltestelle "Hochschule/Läger" der Tram-Linie D. Die Kanzlei verfügt im Innenhof über 2 Stellplätze für PKW. Mit dem PKW ist die Kanzlei über die Oberländerstraße zu erreichen.
>
> Die Kanzlei ist sowohl zivil-, als auch strafrechtlich ausgerichtet, wobei die Beratung von Privatpersonen zu allen Rechtsfragen des täglichen Lebens im Vordergrund steht. Wir verstehen uns aber als Ansprechpartner und Berater für jeden Rechtsuchenden auf allen Rechtsgebieten.

### Wichtige Hinweise für Mandanten

**Strafrecht - Vorladung:**
> Sollten Sie von der Polizei oder von der Staatsanwaltschaft eine schriftliche Vorladung zum Zwecke der Vernehmung als Beschuldigter erhalten haben, lautet der unbedingte dringende Rat, einer solchen Vorladung nicht Folge zu leisten.

**Arbeitsrecht - Rechtsschutzversicherung:**
> Wir raten Ihnen dringend, unverzüglich eine Rechtsschutzversicherung abzuschließen. Nach Abschluss müssen Sie eine Wartefrist von 3 Monaten einhalten.

**Arbeitsrecht - Kündigungsschutzklage:**
> Für die Erhebung einer Kündigungsschutzklage gilt eine gesetzliche Frist von 3 Wochen ab Zugang der schriftlichen Kündigung.

**Ordnungswidrigkeiten - Einspruch:**
> Bei Bußgeldbescheiden müssen Sie innerhalb von 2 Wochen ab Zustellung Einspruch einlegen.

---

## Assets

### Logo
- **Datei:** `assets/logo.png`
- **Original-URL:** https://fotos.verwaltungsportal.de/seitengenerator/d7b9884bbcd82ddedd628c9ac91c9f6c236639/gross/logo-miles-law_5.png
- **Format:** PNG mit transparentem Hintergrund
- **Maße:** ca. 320px breit
- **Elemente:**
  - "MILES-LAW.DE" in Kanzlei-Grün
  - "IHR RECHT IST UNSER GESETZ" in Kanzlei-Gold

### Favicon
- **Original-URL:** http://daten.verwaltungsportal.de/dateien/favicon/15290/1/5/2/9/0/Bild.png

### Bilder
- **Kanzlei-Gebäude:** `assets/kanzlei-gebaeude.jpg`
- **Original-URL:** http://daten.verwaltungsportal.de/dateien//mypage/1/7/4/9/2/1/4/38D899A8-F022-487D-891C-82DBBF0E27F5.jpeg

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Vertrauen durch Klarheit"**
- Clean, strukturiertes Layout mit viel Weißraum
- Klassisch-moderne Ästhetik passend zur juristischen Branche
- Hero-Section mit Statement-Text und subtiler Anwalts-Silhouette/Justiz-Symbolik
- Card-basierte Darstellung der Rechtsgebiete mit Icons

**Besondere Layouts:**
- **Hero:** Split-Screen mit großem Typo-Statement links, dezentes Bild rechts
- **Services:** Icon-Grid mit 2-3 Spalten, Hover zeigt Kurzbeschreibung
- **Grundsätze:** Nummerierte Timeline oder Accordion
- **CTA-Sections:** Full-width mit Gold-Akzent

### 2. Signature-Effekt

**Geometrische Gold-Akzente**
- Dezente goldene Linien als Trennelemente
- Gold-Gradient unter Headlines
- Subtiler Gold-Rand bei wichtigen Cards
- Waage-/Justiz-Symbol als wiederkehrendes Designelement

### 3. Animations-Level: DEZENT

Passend zur seriösen Rechtsanwalts-Branche:
- **Erlaubt:**
  - Sanftes Fade-in beim Scrollen (AOS mit ease, 400-600ms)
  - Subtile Hover-Transitions auf Buttons/Cards (0.3s)
  - Smooth Scroll
- **Vermeiden:**
  - Bouncing-Effekte
  - Schnelle/aggressive Animationen
  - Zu viele gleichzeitige Bewegungen

### 4. Besondere Sektionen

1. **"Erste Schritte" / "Was tun bei..."**
   - Interaktive Hinweise für typische Situationen
   - Z.B. "Was tun bei einer Vorladung?" → expandierbarer Text

2. **Rechtsgebiete-Navigator**
   - Übersichtliche Card-Grid mit den 5 Hauptrechtsgebieten
   - Click führt zu Detailseite

3. **Die 6 Grundsätze**
   - Elegante Timeline oder nummerierte Cards
   - Gold-Akzente bei den Nummern

4. **Standort-Sektion**
   - Eingebettete Karte
   - Anfahrtsinformationen (Tram, Parkplätze)
   - Kontaktformular

5. **Vertrauens-Indikatoren**
   - Mitgliedschaften (RAK Freiburg, Legal Tech Verband, etc.)
   - Berufshaftpflicht-Hinweis
   - "Bundesweite Tätigkeit"

### 5. Icon-Empfehlungen

Passende Icons für Rechtsgebiete:
- Zivilrecht: Handshake / Vertrag
- Strafrecht: Waage / Schild
- Arbeitsrecht: Aktentasche / Dokument
- Fahrerlaubnisrecht: Auto / Führerschein
- Ordnungswidrigkeiten: Verkehrsschild / Tacho

---

## Rechtliche Seiten

### Impressum
Vollständiges Impressum verfügbar mit:
- Herausgeberadresse
- Kontaktdaten (Tel, Fax, E-Mail)
- USt-IdNr
- Zuständige Aufsichtsbehörde (RAK Freiburg)
- Berufsbezeichnung und berufsrechtliche Regelungen
- Berufshaftpflichtversicherung
- Außergerichtliche Streitschlichtung
- Haftungshinweise
- Urheberrecht

### Datenschutzerklärung
Vollständige DSGVO-konforme Datenschutzerklärung mit:
- Verantwortlicher
- Zugriffsdaten / Log-Dateien
- Cookies
- Erfassung personenbezogener Daten
- Kontaktformular
- SSL-Verschlüsselung
- 2-Klick-Lösung für Iframes
- Google Recaptcha
- Google Maps
- Google Web Fonts (selbst gehostet)
- Rechte der Nutzer
- Widerspruchsrecht

---

## Technische Hinweise

### SEO-Keywords
- Rechtsanwalt Kehl
- Anwalt Kehl
- Strafverteidiger Kehl
- Arbeitsrecht Offenburg
- Rechtsanwalt Ortenau
- Verkehrsrecht Kehl
- MPU Beratung Kehl

### Strukturierte Daten
- Schema.org: LegalService / Attorney
- LocalBusiness für lokale Suche
- FAQPage für häufige Fragen

### Performance
- Logo als SVG konvertieren
- Bilder in WebP optimieren
- Kritisches CSS inline
- Lazy Loading für Bilder

---

## Referenzen & Bewertungen

### Bewertungs-Übersicht

| Plattform | Bewertung | Anzahl | Link |
|-----------|-----------|--------|------|
| Google Maps | ⭐ 4,9 / 5 | - | [Google Maps](https://www.google.com/maps/search/MILES-LAW+Rechtsanwalt+Kehl) |
| anwalt.de | Sehr gut | 61 Bewertungen | [anwalt.de](https://www.anwalt.de/faris-hussain/bewertungen.php) |

### Ausgewählte Kundenstimmen (anwalt.de)

**Bewertung 1 - Arbeitsrecht**
> "Herr Hussain hat uns in einem Arbeitsrechtsfall sehr kompetent und zuverlässig beraten. Vielen Dank für Ihre Zeit, Extrameile und fachliche Unterstützung!"
- **Rechtsgebiet:** Arbeitsrecht
- **Quelle:** anwalt.de

**Bewertung 2 - Beratungsqualität**
> "Sehr kompetente Beratung, sehr freundlich, hält sich genau an Terminabsprachen, einfach empfehlenswert."
- **Rechtsgebiet:** Allgemein
- **Quelle:** anwalt.de

**Bewertung 3 - Telefonische Beratung**
> "Das Telefonat mit Herrn RA Hussain war sehr angenehm. Er ist sehr geduldig, nahm sich viel Zeit und hörte sich meinen Fall genau an. Anschließend erörterte er mir die Rechtslage und gab mir einige Ratschläge zur weiteren Vorgehensweise. Ich bedanke mich bei Herrn Hussain und gebe eine klare Weiterempfehlung."
- **Rechtsgebiet:** Allgemein
- **Quelle:** anwalt.de

**Bewertung 4 - Mehrfache Zusammenarbeit**
> "Zum zweiten Mal kann ich Herrn Hussain als Top Auskunftsgeber bewerten. Auskunft sowie nachgelagerte zusätzliche schriftliche Informationen zu meinem Anliegen waren sehr gut."
- **Rechtsgebiet:** Allgemein
- **Quelle:** anwalt.de

**Bewertung 5 - Nachbetreuung**
> "Super Beratung und Hilfsbereitschaft. Selbst nach Abschluss des Gesprächs hat er weiter recherchiert und bei neuen Erkenntnissen sofort zurückgerufen. Die Zusammenarbeit ist lobenswert und definitiv weiter zu empfehlen."
- **Rechtsgebiet:** Allgemein
- **Quelle:** anwalt.de

**Bewertung 6 - Freundliches Gespräch**
> "Das Beratungsgespräch mit Herrn Hussain war sehr angenehm. Er hat mir sehr hilfreiche Informationen gegeben. Ich danke ihm nochmals für das nette Telefonat."
- **Rechtsgebiet:** Allgemein
- **Quelle:** anwalt.de

### Hinweise für die Testimonials-Sektion

**Empfehlung für das Website-Design:**
Da keine individuellen Personenfotos oder Firmennamen der Rezensenten verfügbar sind (anonyme Bewertungen), empfehlen wir folgende Darstellung:

1. **Rating-Summary-Banner:**
   - Google Maps: 4,9 Sterne
   - anwalt.de: 61+ Bewertungen
   - Links zu den Bewertungsportalen

2. **Anonymisierte Zitate:**
   - Die Testimonials mit generischem Avatar oder Initialen darstellen
   - Rechtsgebiet als Kontext angeben

3. **Vertrauens-Elemente:**
   - "61+ zufriedene Mandanten auf anwalt.de"
   - "4,9 Sterne bei Google Maps"
   - Links zu den Original-Bewertungen für Transparenz

### Assets für Testimonials

**Keine individuellen Assets verfügbar:**
- Bewertungen auf anwalt.de sind anonym (keine Klarnamen/Fotos)
- Google Maps Bewertungen ebenfalls anonym
- Keine LinkedIn-Empfehlungen gefunden

**Alternative Assets:**
- anwalt.de Logo für Quellenangabe (extern verlinken)
- Google-Bewertungs-Sterne-Widget
- Generische Avatar-Icons für anonyme Testimonials
