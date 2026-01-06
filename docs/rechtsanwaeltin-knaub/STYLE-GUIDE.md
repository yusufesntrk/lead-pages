# Style Guide - Kanzlei Knaub

## Firmeninformationen

### Grunddaten
- **Kanzleiname:** Kanzlei Knaub
- **Inhaberin:** Rechtsanwältin Brigitte Knaub
- **Qualifikationen:**
  - Rechtsanwältin
  - Fachanwältin für Arbeitsrecht
  - Fachanwältin für Verkehrsrecht

### Kontaktdaten
- **Adresse:** Blumenstraße 15a, 77694 Kehl
- **Telefon:** +49 7851 4748
- **Fax:** +49 7851 4749
- **E-Mail:** knaub@kanzlei-knaub.de
- **Website:** www.kanzlei-knaub.de (derzeit geparkt/inaktiv)

### Öffnungszeiten
- **Montag:** 08:00 - 12:00 Uhr, 13:30 - 17:00 Uhr
- **Dienstag:** 08:00 - 12:00 Uhr
- **Mittwoch:** 08:00 - 12:00 Uhr, 13:30 - 17:00 Uhr
- **Donnerstag:** 08:00 - 12:00 Uhr, 13:30 - 17:00 Uhr
- **Freitag:** 08:00 - 12:00 Uhr
- **Termine außerhalb der Öffnungszeiten:** Nach Vereinbarung möglich

### Sprachen
- Deutsch
- Französisch (wichtig für Grenzregion zu Frankreich/Straßburg)

### Bewertungen
- **Google Rating:** 4.8 von 5 Sternen
- **Anzahl Bewertungen:** 35

### Besonderheiten
- Rollstuhlgerechter Parkplatz vorhanden
- Lage am Marktplatz in Kehl
- Grenznähe zu Frankreich (Straßburg nur wenige Kilometer entfernt)

---

## Rechtsgebiete

### Schwerpunkte (mit Fachanwaltstitel)

#### Arbeitsrecht
- Erstellung und Prüfung von Arbeitsverträgen
- Kündigungsschutzrecht
- Abfindungsverhandlungen
- Arbeitszeugnisse
- Aufhebungsverträge
- Betriebsratsfragen

#### Verkehrsrecht
- Unfallregulierung
- Schadensabwicklung mit Versicherungen
- Bußgeldverfahren
- Führerscheinentzug
- Verkehrsstrafrecht
- OWi-Verfahren (Ordnungswidrigkeiten)

### Weitere Rechtsgebiete

#### Familienrecht
- Scheidung
- Unterhalt
- Sorgerecht
- Vermögensauseinandersetzung

#### Erbrecht
- Testamentsgestaltung
- Erbauseinandersetzung
- Pflichtteilsansprüche
- Nachlassregelung

---

## Farbpalette

Da keine aktive Website vorhanden ist, wird das Design basierend auf der Branche "Rechtsanwalt" erstellt.

### Primärfarben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Dunkelblau | `#1a365d` | Primärfarbe, Navigation, Überschriften |
| Navy | `#0f2744` | Header, Footer, dunkle Akzente |

### Sekundärfarben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Gold/Messing | `#c9a962` | Akzente, Buttons, Icons |
| Warmgold | `#b8942e` | Hover-States, Links |

### Neutrale Farben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Weiß | `#ffffff` | Hintergrund, Karten |
| Hellgrau | `#f8f9fa` | Sektions-Hintergrund |
| Mittelgrau | `#6b7280` | Sekundärer Text |
| Dunkelgrau | `#374151` | Body-Text |
| Fast Schwarz | `#111827` | Überschriften |

### Statusfarben
| Farbe | Hex | Verwendung |
|-------|-----|------------|
| Erfolg | `#059669` | Bestätigungen |
| Warnung | `#d97706` | Hinweise |
| Fehler | `#dc2626` | Fehlermeldungen |

---

## Typografie

### Schriftarten
```css
/* Überschriften - Elegant, seriös */
font-family: 'Playfair Display', 'Georgia', serif;

/* Body - Gut lesbar, professionell */
font-family: 'Source Sans Pro', 'Helvetica Neue', sans-serif;
```

### Schriftgrößen
| Element | Desktop | Mobile | Gewicht |
|---------|---------|--------|---------|
| H1 | 48px | 32px | 700 |
| H2 | 36px | 28px | 600 |
| H3 | 24px | 20px | 600 |
| H4 | 20px | 18px | 500 |
| Body | 16px | 16px | 400 |
| Small | 14px | 14px | 400 |
| Caption | 12px | 12px | 400 |

### Zeilenhöhe
- Überschriften: 1.2
- Body: 1.6
- Navigation: 1.4

---

## Spacing-System

### Basis-Einheit: 8px

| Name | Wert | Verwendung |
|------|------|------------|
| xs | 4px | Minimale Abstände |
| sm | 8px | Kleine Abstände |
| md | 16px | Standard-Abstände |
| lg | 24px | Größere Abstände |
| xl | 32px | Sektions-Padding |
| 2xl | 48px | Große Sektions-Abstände |
| 3xl | 64px | Hero-Bereiche |
| 4xl | 96px | Desktop Sektions-Trennung |

---

## Komponenten

### Buttons

```css
/* Primärer Button */
.btn-primary {
  background: #c9a962;
  color: #0f2744;
  padding: 14px 32px;
  border-radius: 4px;
  font-weight: 600;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background: #b8942e;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(201, 169, 98, 0.3);
}

/* Sekundärer Button */
.btn-secondary {
  background: transparent;
  color: #1a365d;
  border: 2px solid #1a365d;
  padding: 12px 30px;
  border-radius: 4px;
}

.btn-secondary:hover {
  background: #1a365d;
  color: #ffffff;
}
```

### Karten

```css
.card {
  background: #ffffff;
  border-radius: 8px;
  padding: 32px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.card:hover {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  transform: translateY(-4px);
}
```

### Navigation

```css
.nav {
  background: #0f2744;
  padding: 0 48px;
  height: 80px;
}

.nav-link {
  color: #ffffff;
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 0.3px;
}

.nav-link:hover {
  color: #c9a962;
}
```

---

## Team

### Brigitte Knaub
- **Position:** Inhaberin, Rechtsanwältin
- **Qualifikationen:**
  - Rechtsanwältin
  - Fachanwältin für Arbeitsrecht
  - Fachanwältin für Verkehrsrecht
- **Sprachen:** Deutsch, Französisch
- **Foto:** Kein öffentliches Foto verfügbar
- **Beschreibung:** Als langjährig erfahrene Fachanwältin für Arbeits- und Verkehrsrecht vertritt Rechtsanwältin Brigitte Knaub ihre Mandanten kompetent in diesen und verschiedenen weiteren Rechtsbereichen. Sie verfügt über eine Vielzahl an erfolgreich geführten Prozessen und langjährige Erfahrung, von der ihre Klienten maßgeblich profitieren.

---

## Logo

**Status:** Kein Logo verfügbar

**Empfehlung:** Text-Logo erstellen mit:
- Schriftart: Playfair Display
- Primärfarbe: #1a365d
- Akzent (Waage-Symbol oder Paragraph-Zeichen): #c9a962

---

## Bilder & Medien

### Bildstil
- Professionelle, seriöse Aufnahmen
- Warme, aber gedämpfte Farbgebung
- Authentische Kanzlei-/Büroatmosphäre
- Keine generischen Stock-Fotos

### Bildthemen
- Beratungssituationen
- Gerichtssaal-Symbolik (dezent)
- Kehl/Ortenau Lokalität
- Rechtssymbole (Waage, Paragraphen)

---

## Kreative Design-Empfehlungen

### 1. Empfohlenes Layout-Konzept

**"Trust & Expertise" Layout:**
- Hero mit großem Statement und Vertrauens-Indikatoren (35 Bewertungen, 4.8 Sterne)
- Asymmetrisches Grid für Rechtsgebiete
- Timeline für Mandatsablauf
- Testimonial-Bereich mit Google Reviews

### 2. Signature-Effekt

**Dezente Eleganz:**
- Subtile Linien-Ornamente (goldene Akzentlinien)
- Sanfte Schatten für Tiefe
- Goldene Unterstriche bei Überschriften
- Paragraph-Symbol (§) als wiederkehrendes Designelement

### 3. Animations-Level

**Dezent (passend für Rechtsanwaltskanzlei):**
- Fade-in beim Scrollen
- Subtle Hover-Effekte auf Karten
- Sanfte Übergänge bei Navigation
- Keine ablenkenden Animationen

### 4. Besondere Sektionen

1. **"Ihre Rechtsgebiete" - Interaktives Accordion**
   - Jedes Rechtsgebiet aufklappbar
   - Detaillierte Informationen zu Leistungen

2. **"Ihr Weg zum Recht" - Prozess-Timeline**
   - Erstberatung → Analyse → Strategie → Vertretung → Lösung
   - Visualisiert den Mandatsablauf

3. **"Grenzüberschreitend kompetent"**
   - Hervorhebung der Französisch-Kenntnisse
   - Relevanz für Grenzregion Kehl-Straßburg

4. **"Das sagen unsere Mandanten"**
   - Google Reviews Integration
   - 4.8 Sterne prominent anzeigen

5. **"Schnelle Hilfe" - Kontakt-Sektion**
   - Öffnungszeiten übersichtlich
   - Direkter Anruf-Button
   - Terminanfrage-Formular

### 5. Lokaler Bezug

- Kehl am Rhein als Standort hervorheben
- Nähe zu Straßburg/Frankreich betonen
- Ortenaukreis als Einzugsgebiet

---

## Impressum-Daten

```
Rechtsanwältin Brigitte Knaub
Fachanwältin für Arbeitsrecht
Fachanwältin für Verkehrsrecht

Blumenstraße 15a
77694 Kehl

Telefon: +49 7851 4748
Telefax: +49 7851 4749
E-Mail: knaub@kanzlei-knaub.de

Zuständige Rechtsanwaltskammer: Rechtsanwaltskammer Freiburg
Berufsbezeichnung: Rechtsanwältin (verliehen in der Bundesrepublik Deutschland)

Berufsrechtliche Regelungen:
- Bundesrechtsanwaltsordnung (BRAO)
- Berufsordnung für Rechtsanwälte (BORA)
- Fachanwaltsordnung (FAO)
- Rechtsanwaltsvergütungsgesetz (RVG)

Die berufsrechtlichen Regelungen können über die Bundesrechtsanwaltskammer
(www.brak.de) eingesehen werden.

USt-IdNr.: [Wird bei Erstellung des Impressums ergänzt]
```

---

## Datenschutz-Hinweise

Für die Datenschutzerklärung relevant:
- Kontaktformular
- E-Mail-Kommunikation
- Mandatsdaten (besonders schützenswert)
- Keine Cookies für Tracking (empfohlen)
- Google Maps Einbindung (falls verwendet)

---

## Referenzen

### Bewertungsübersicht

| Plattform | Bewertung | Anzahl |
|-----------|-----------|--------|
| **Google** | ⭐ 4.8/5 | 35 Bewertungen |
| **Das Örtliche** | ⭐ 5.0/5 | 1 Bewertung |
| **Deutsches Branchenbuch** | ⭐ 5.0/5 | 2 Bewertungen |

### Ausgewählte Mandanten-Stimmen

#### Referenz 1
- **Name:** felixnobi71
- **Quelle:** Das Örtliche
- **Datum:** 01.09.2021
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
- **Zitat:**
  > „Habe immer sehr gute Erfahrungen gemacht. Für mich die beste Anwältin die ich kenne – korrekt, sehr geradeaus, hilft wenn sie kann. Im Ganzen so stellt man sich eine Anwältin vor."

#### Referenz 2
- **Name:** Andreas Eckfelder
- **Quelle:** Deutsches Branchenbuch
- **Datum:** 27.01.2018
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
- **Zitat:**
  > „Super Anwältin!!!!"

#### Referenz 3
- **Name:** Tweety
- **Quelle:** Deutsches Branchenbuch
- **Datum:** 15.06.2018
- **Bewertung:** ⭐⭐⭐⭐⭐ (5/5)
- **Zitat:**
  > „Top Anwältin!"

### Hinweise zur Verwendung

- **Keine Personenfotos verfügbar:** Die Bewertungen stammen von pseudonymen Online-Nutzern. Fotos können nicht recherchiert werden.
- **Empfehlung für Website:** Google Reviews als aggregierte Bewertung anzeigen (4.8 Sterne, 35 Bewertungen) mit Link zu Google Maps.
- **Alternative:** Die ausführliche Bewertung von felixnobi71 kann als Testimonial-Zitat verwendet werden.

### Testimonial-Sektion Empfehlung

Da keine echten, identifizierbaren Mandanten mit Fotos verfügbar sind, wird empfohlen:

1. **Google Reviews Widget** mit Gesamtbewertung (4.8★ bei 35 Bewertungen)
2. **Ausgewähltes Zitat** aus der felixnobi71-Bewertung (mit Hinweis "Mandanten-Bewertung")
3. **Vertrauensindikatoren** statt klassischer Testimonials:
   - 35+ zufriedene Mandanten
   - 4.8/5 Sterne Durchschnittsbewertung
   - Langjährige Erfahrung
   - Doppelte Fachanwaltsqualifikation

---

## Quellen

- [Deutsche Anwaltauskunft - Brigitte Knaub](https://anwaltauskunft.de/anwaltssuche/brigitte-knaub-kbe6y)
- [Verband Deutscher Anwälte](https://www.verband-deutscher-anwaelte.de/anwalt/brigitte-knaub-rechtsanwaeltin-fachanwaeltin-fuer-arbeitsrecht-fachanwaeltin-fuer-verkehrsrecht-kanzlei-knaub-kehl/)
- [Anwaltsportal 24](https://www.anwaltsportal24.eu/45978/Rechtsanw%C3%A4lte/77694-Kehl)
- [11880 Branchenbuch](https://www.11880.com/branchenbuch/kehl-rhein/081314253B25951325/brigitte-knaub-anwaltskanzlei.html)
- [Das Örtliche - Knaub Brigitte Anwaltskanzlei](https://www.dasoertliche.de/Themen/Knaub-Brigitte-Anwaltskanzlei-Kehl-Blumenstr)
- [Deutsches Branchenbuch - Knaub Rechtsanwältin](https://kehl.deutschbranchenbuch.com/lawyer/knaub-rechtsanwaltin/)
