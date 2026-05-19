# Anti-KI Review — test-text-4-watermarked.md

## Verdict
🔴 Klingt deutlich nach KI — plus drei versteckte Zero-Width-Spaces im Original.

Der Text trägt sowohl Unicode-Wasserzeichen (3× U+200B) als auch ein dichtes Set an KI-typischen Stilmustern. Beide Probleme wurden adressiert: hidden chars raus via `watermark_cleaner` (clean_basic), stilistische Muster im Rewrite unten gefixt.

---

## Schritt 0 — Watermark-Cleanup

**Funde:**
- `U+200B` (Zero Width Space) — **3 Treffer**

**Aktion:** `clean_basic` ausgeführt → 3× Zero Width Space entfernt. Datei gespeichert als `evals/test-text-4-cleaned.md`.

**Wichtiger Befund beim Cleanup:** die Zero-Width-Spaces saßen zwischen sichtbaren Wörtern (`von` + `entscheidender`, `zentrale` + `Rolle`, `unterstreicht` + `die`). Nach dem Entfernen kleben die Wörter ohne Leerzeichen aneinander (`vonentscheidender`, `zentraleRolle`, `unterstreichtdie`). Das ist erwartbares Verhalten für `clean_basic` — der Cleaner ersetzt nicht durch Spaces, weil er nicht raten kann, ob der ZWSP semantisch ein Leerzeichen oder eine Glyph-Verbindung war. Im Rewrite unten ist das korrigiert.

**Disclaimer (aus Tool-Output):** Unicode-Cleanup hebelt keine statistischen Wasserzeichen (z. B. SynthID) aus und bietet keine Detector-Bypass-Garantie.

---

## Schritt 1 — Linter-Findings (auf gesäuberter Fassung)

| Stat | Wert |
|------|------|
| Wörter | 41 |
| Sätze | 9 |
| Absätze | 3 |
| Ø Satzlänge | 4,6 Wörter |
| Errors | 5 |
| Warnings | 1 |

**Verdict des Linters:** 🔴 Klingt deutlich nach KI

---

## Kritische Muster

**[C1] 🔴 Zeile 3 — Symmetrischer Dreierschlag**
   Zitat:  "Sie ist kein gewöhnliches Tool. Sie ist keine Standard-Software. Sondern ein game-changer."
   Fix:    Ein klarer Aussage-Satz statt drei rhetorisch gestapelter Mini-Sätze.

**[C14] 🔴 Zeile 5 — Telegraphische Dreierliste**
   Zitat:  "Recherchiert. Getestet. Bewährt."
   Fix:    In einen Satz einbauen oder Längen variieren.

**[C8] 🔴 Zeile 1 — Generisches Business-Vokabular: "transformation"**
   Zitat:  "...digitale Transformation und unterstreicht die Notwendigkeit ganzheitlicher Lösungen."
   Fix:    Sagen, was konkret passiert — was wird transformiert, woran?

**[C8] 🔴 Zeile 1 — Generisches Business-Vokabular: "ganzheitlich"**
   Zitat:  "...Notwendigkeit ganzheitlicher Lösungen."
   Fix:    "Ganzheitlich" ist Füll-Adjektiv. Welche Lösungen, für welches Problem?

**[C8] 🔴 Zeile 3 — Generisches Business-Vokabular: "game-changer"**
   Zitat:  "Sondern ein game-changer."
   Fix:    Konkret machen — was verändert sich für wen?

## Mittlere Muster

**[C22] ⚠️ Zeile 3 — Satzanfang "Sie ist" 2× hintereinander**
   Zitat:  "Sie ist kein gewöhnliches Tool. Sie ist keine Standard-Software."
   Fix:    Satzanfänge variieren oder Sätze zusammenziehen.

## Niedrige Muster / Empfehlungen (LLM-Scan, G1–G6)

- **G1 — Negation-Affirmation / Nicht-nur-sondern-auch:** "Unsere Plattform ist nicht nur effizient, sondern auch skalierbar." Klassisches KI-Korsett.
- **G1 — Punkte-statt-Kommas:** der "Sondern ein game-changer."-Satz hängt grammatikalisch am Vorgänger und ist nur durch einen Punkt abgetrennt — typisches Effekthascher-Pattern.
- **G2 — Superficial Analysis:** "unterstreicht die Notwendigkeit" — unbelebtes Subjekt, das "unterstreicht".
- **G3 — Puffery:** "von entscheidender Bedeutung", "zentrale Rolle" — beide im ersten Satz, beide inhaltsleer.
- **G5 — AI-Vokabel-Cluster:** "entscheidende Bedeutung" + "zentrale Rolle" + "ganzheitlich" + "Transformation" — vier Klassiker in einem Absatz.

## Was funktioniert
Der Text ist kurz und hat keine Setup-Sätze, die ohne Inhalt um sich werfen. Die kurze Form macht das Problem aber stärker sichtbar — fast jeder Satz trägt mindestens ein KI-Muster.

---

## Schritt 4 — Rewrite

Ich kenne den Produkt-Kontext nicht — die folgende Fassung räumt nur die Form auf und markiert offene Stellen, wo ohne Domain-Wissen geraten werden müsste. Du als Autor entscheidest, was konkret an die Stelle der Puffery soll.

```
KI verändert, wie wir arbeiten. [?] Hier stand "von entscheidender Bedeutung … zentrale Rolle bei der digitalen Transformation" — was genau verändert sich, in welchem Bereich? Eine Zahl oder ein konkreter Use Case macht den Satz tragfähig.

Unsere Plattform ist effizient und skaliert mit. [?] "game-changer" rausgenommen — was unterscheidet sie konkret von Standard-Software? (Z. B. "läuft on-premise", "kein Setup-Aufwand", "x-mal schneller als Y".)

Recherchiert, getestet, bewährt im Einsatz bei [?Kundenname / Branche].
```

**Diff-Logik:**
- Satz 1: Puffery-Cluster ("entscheidende Bedeutung", "zentrale Rolle", "ganzheitlich") raus, Platzhalter für konkrete Aussage. "Unterstreicht" (Superficial Analysis) gestrichen.
- Satz 2: "Nicht nur … sondern auch" aufgelöst zu einem geraden Satz. Dreierschlag mit "Sie ist kein … Sie ist keine … Sondern …" eliminiert. "game-changer" markiert als zu konkretisierende Stelle.
- Satz 3: Telegraphische Dreierliste in einen Satz integriert, der den Bezug klarmacht ("bewährt im Einsatz bei …" statt im luftleeren Raum).

---

## Selbst-Check

Linter-Re-Scan auf den Rewrite (mental): keine C1, keine C14, "game-changer" und "transformation" sind als `[?]`-Stellen markiert statt drinzubleiben — C8 ist damit auch entschärft. Satzanfänge variieren. Keine Symmetrien mehr.

Die offenen `[?]`-Marker sind bewusst drin — sie zeigen, wo Domain-Wissen rein muss, das ich nicht raten darf, ohne Inhalt zu erfinden.
