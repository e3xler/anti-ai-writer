# Anti-KI Pattern-Katalog (G0–G6)

Single Source of Truth für KI-typische Schreibmuster im Deutschen. Wird vom Skill `anti-ki-review` beim Pattern-Scan (G1–G6) gelesen. Die G0-Kategorie ist bereits in `scripts/kadenz_linter.py` automatisiert.

Verwende diesen Katalog wie eine Checkliste: pro Kategorie einmal durchscannen, Treffer im Findings-Report sammeln.

---

## G0 — Mechanisch prüfbar (Linter)

Diese Patterns findet der Linter deterministisch. Du musst sie nicht nochmal manuell prüfen — übernimm die Linter-Findings direkt.

| Regel | Was es findet |
|-------|---------------|
| B1 | Satz > 20 Wörter |
| B2 | Absatz > 4 Sätze |
| C1 | Symmetrischer Dreierschlag |
| C7 | weder-noch / Doppel-Verneinung |
| C8 | Generisches Business-Vokabular (transformation, mehrwert, ganzheitlich, innovativ, synergien, agil, disruptiv, paradigmenwechsel, game-changer, best practice, cutting-edge, zukunftsfähig, wegweisend, vorreiter …) |
| C13 | „X — nicht Y"-Reversals (ab dem 3.) |
| C14 | Telegraphische Dreierlisten |
| C16 | Setup-Sätze ohne Inhalt |
| C18 | >1 Doppelpunkt-Setup pro Absatz |
| C19 | >1 Gedankenstrich-Turn pro Absatz |
| C20 | Invertierter Opener |
| C21 | Vergleichskadenz |
| C22 | Wiederholte Satzanfänge |
| C23 | „statt" mehrfach pro Absatz |

---

## G1 — Strukturelle Patterns (LLM-Check für subtile Varianten)

| Pattern | BAD | FIX |
|---------|-----|-----|
| **Negation-Affirmation** | „Das ist kein X. Das ist Y." | Direkt sagen, was es ist |
| **Nicht-nur-sondern-auch** | „spart nicht nur Zeit, sondern auch Geld" | Auftrennen: „Spart Zeit. Und Geld." |
| **Rule of Three** | „effizient, klar und skalierbar" | Auf den Kern reduzieren |
| **Von-X-bis-Y** | „Von der Analyse bis zur Umsetzung" | Konkret werden |
| **False Range** | „von Startups bis Konzernen" | Wenn kein echtes Spektrum: streichen |
| **Challenges-and-Future** | „Trotz X… bleibt Y optimistisch" | Streichen oder konkretisieren |
| **Section Summary** | „Zusammenfassend lässt sich sagen…" | Streichen |
| **Didactic Disclaimer** | „Es ist wichtig zu beachten, dass…" | Einfach sagen |
| **Punkte-statt-Kommas** | „6 Monate. 47 Seiten. Sechsstellig." | Kommas verwenden |

**Überschneidung mit Linter:** Rule of Three (C1), Punkte-statt-Kommas (C14), Negation-Affirmation (C13) sind mechanisch erkennbar. Der LLM-Check deckt die subtileren Varianten ab, die der Linter wegen fehlender Symmetrie verpasst.

---

## G2 — Superficial Analysis

Unbelebte Subjekte, die Dinge „unterstreichen", „verdeutlichen", „hervorheben". Fakten sind Fakten — sie „unterstreichen" nichts.

```
BAD: "Diese Entwicklung unterstreicht die Bedeutung…"
BAD: "Das Ergebnis verdeutlicht den Wandel…"
BAD: "Die Zahlen heben hervor, dass…"
```

**Fix:** Sag was Sache ist. Keine abstrakte Metaebene.

```
FIX: "Die Entwicklung zeigt: [konkrete Aussage]."
FIX: "Die Zahlen: 40% im letzten Quartal. Deutlich mehr als erwartet."
```

**Grep-Pattern:** `unterstreicht|verdeutlicht|hebt hervor|beleuchtet|betont`

---

## G3 — Puffery & Importance-Inflation

Bedeutungs-Aufblähung ohne Substanz.

```
BAD: "spielt eine zentrale/entscheidende/pivotale Rolle"
BAD: "von entscheidender Bedeutung"
BAD: "prägt nachhaltig", "hinterlässt bleibenden Eindruck"
BAD: "revolutionär", "bahnbrechend", "wegweisend"
```

**Fix:** Weglassen. Wenn etwas wichtig ist, zeigt es sich durch Fakten.

```
FIX: [streichen, oder:] "60% der Unternehmen nutzen es bereits."
```

**Grep-Pattern:** `entscheidende Rolle|zentrale Rolle|pivotale Rolle|von entscheidender Bedeutung|revolutionär|bahnbrechend|wegweisend`

**Überschneidung mit Linter:** Teil des Business-Vokabulars (C8) ist bereits mechanisch.

---

## G4 — Elegant Variation

Künstliches Synonym-Hopping, um Wiederholung zu vermeiden. Klarheit vor Variation — Wiederholung ist in Fach-Content okay.

```
BAD: "Die Anforderung… Das Requirement… Die Spezifikation…"
BAD: "Das System… Die Lösung… Das Tool…"
BAD: "Der Kunde… Der Klient… Der Auftraggeber…"
```

**Fix:** Beim selben Begriff bleiben.

```
FIX: "Die Anforderung… Die Anforderung… Die Anforderung…"
```

**Warum LLM-only:** Erkennung erfordert semantisches Verständnis der Synonym-Äquivalenz im jeweiligen Kontext.

---

## G5 — AI-Vokabular

Wörter, die LLMs überproportional häufig verwenden. Eine Einzelerwähnung ist harmlos, mehrere davon in einem Text sind ein starkes KI-Signal.

### Verben

`unterstreichen, hervorheben, verdeutlichen, aufzeigen, beleuchten, betonen, fördern, kultivieren, prägen, verkörpern`

### Adjektive

`entscheidend, zentral, pivotal, maßgeblich, nachhaltig (im übertragenen Sinn), vielschichtig, komplex, intrinsisch`

### Bedeutungs-Aufblähung

`„ist ein Testament für", „steht symbolisch für", „verkörpert den Geist von"`

### Transitions

`„Trotz dieser Herausforderungen", „Zusammenfassend", „Insgesamt", „Abschließend lässt sich sagen"`

### Hedging

`„Es ist wichtig zu beachten", „Man sollte nicht vergessen"`

**Grep-Pattern:** `kultivieren|verkörpern|vielschichtig|intrinsisch|nachhaltig prägt`

**Überschneidung mit Linter:** Business-Vokabular-Blacklist (C8) deckt die häufigsten Begriffe ab.

**Dichte-Check:** 1 Treffer = harmlos. 3+ Treffer im selben Absatz = starkes Signal.

---

## G6 — Rhythmus & Konkretheit

Gesamtrhythmus eines Texts — erkennt man nur durch Lautlesen, nicht durch Regex.

### Rhythmus-Check

- Mehr als 3 Sätze mit ähnlicher Länge hintereinander?
- Fehlen kurze Punch-Sätze (3–6 Wörter)?
- Klingt es monoton, wenn laut gelesen?
- Fehlt das Auf-und-Ab zwischen langen und kurzen Sätzen?

### Konkretheit-Check

- Abstrakte Aussagen ohne Zahlen/Beispiele?
- Kann „optimiert" durch eine konkrete Änderung ersetzt werden?
- Kann „verbessert" durch eine messbare Differenz ersetzt werden?
- Steht irgendwo „effektiv" oder „effizient" ohne Metrik?

**Warum LLM-only:** Rhythmus-Beurteilung erfordert Gesamtwahrnehmung eines Absatzes; Konkretheit erfordert Domain-Verständnis.

---

## Regel-Index (für Rückverweise)

| Kategorie | Handhabung |
|-----------|------------|
| G0 | Mechanisch via `kadenz_linter.py` — keine LLM-Prüfung nötig |
| G1 | LLM-Prüfung für nicht-mechanische Varianten |
| G2 | Grep + LLM-Kontext-Bewertung |
| G3 | Grep + LLM-Kontext-Bewertung |
| G4 | LLM-only (semantische Synonym-Erkennung) |
| G5 | Grep + LLM für Gesamtdichte |
| G6 | LLM-only (Gesamtrhythmus, Konkretheit) |
