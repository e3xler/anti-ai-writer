# Anti-KI Review — test-text-2-linkedin.md

## Verdict
🔴 Klingt deutlich nach KI

Der Post besteht praktisch nur aus rhetorischen Symmetrien — Dreierschläge, Negation-Affirmation, Wiederholungs-Anaphern. Inhalt: drei Generika ("Feedback ist ein Geschenk", "Wer kommuniziert, gewinnt", "Es geht um Menschen"). Die LinkedIn-Hook-Form ist so durchgenudelt, dass sie heute eher gegen den Autor arbeitet.

## Statistik
- Wörter / Sätze / Absätze: 88 / 16 / 6
- Ø Satzlänge: 5,5 Wörter
- Linter-Findings: 2 Errors, 2 Warnings
- LLM-Findings: 7 (verteilt auf G1, G2, G3, G5, G6)

## Kritische Muster

[G0/C1] 🔴 Zeile 5 — Symmetrischer Dreierschlag
   Zitat:  "Es geht nicht um Tools. Es geht nicht um Prozesse. Es geht um Menschen."
   Fix:    "Tools und Prozesse sind sekundär. Es geht um die Leute."

[G0/C1] 🔴 Zeile 9 — Symmetrischer Dreierschlag
   Zitat:  "Das ist kein Geheimnis. Das ist Erfahrung. Und Erfahrung hinterlässt bleibenden Eindruck."
   Fix:    "Kein Geheimnis — sondern Erfahrung, die hängenbleibt."

[G1] 🔴 Zeile 3 — Rule of Three + Doppelpunkt-Anaphern (Erstens/Zweitens/Drittens)
   Zitat:  "Erstens: Feedback ist ein Geschenk. Zweitens: Feedback ist unbequem. Drittens: Feedback macht dich besser."
   Fix:    "Feedback ist ein Geschenk, das oft unbequem ist — und genau deshalb wirkt es."
   Warum:  Die "Erstens/Zweitens/Drittens"-Form ist eines der häufigsten LLM-Pattern auf LinkedIn. Schon der Opener "3 Dinge, die ich diese Woche gelernt habe" plus diese Aufzählung schreit "AI-generiert".

[G1] 🔴 Zeile 7 — Negation-Affirmation-Kaskade (zweite Welle)
   Zitat:  "Die meisten Teams scheitern nicht an Strategie — sie scheitern an Kommunikation. […] Wer kommuniziert, gewinnt. Wer schweigt, verliert."
   Fix:    "Die meisten Teams scheitern nicht an der Strategie, sondern daran, dass sie nicht miteinander reden."
   Warum:  Doppelte Symmetrie ("Wer X, gewinnt. Wer Y, verliert.") direkt nach einer Negation-Affirmation — das ist drei rhetorische Figuren in zwei Sätzen.

## Mittlere Muster

[G2] ⚠️ Zeile 9 — Superficial Analysis
   Zitat:  "Diese Erkenntnis verdeutlicht, wie entscheidend transparente Kommunikation für moderne Organisationen ist."
   Fix:    streichen oder mit konkretem Beispiel ersetzen
   Warum:  Klassischer Meta-Kommentar ("verdeutlicht, wie entscheidend"). Sagt nichts Neues, schiebt nur eine Bedeutungsebene über die Aussage davor.

[G3] ⚠️ Zeile 7 — Puffery / Challenges-and-Future
   Zitat:  "Trotz aller Herausforderungen bleibt eines klar"
   Fix:    streichen
   Warum:  Reines Übergangs-Filler-Geschwafel ohne Substanz.

[G3] ⚠️ Zeile 9 — Puffery
   Zitat:  "hinterlässt bleibenden Eindruck"
   Fix:    "bleibt hängen"

[G0/C18] ⚠️ Zeile 3 — 3 Doppelpunkt-Setups im selben Absatz (max. 1)
   (Bereits durch Linter erfasst — Fix siehe Rule of Three oben.)

[G0/C22] ⚠️ Zeile 5 — Satzanfang "Es geht" 3x
   (Bereits durch Linter erfasst — Fix siehe C1 oben.)

## Niedrige Muster / Empfehlungen

[G5] ℹ️ Vokabel-Cluster: "entscheidend", "verdeutlicht", "nachhaltig" (impliziert über "bleibenden Eindruck"), "moderne Organisationen". Vier AI-Standardbegriffe in zwei Sätzen — selbst harmlos je einzeln, in der Dichte ein Signal.

[G6] ℹ️ Rhythmus: Sechs sehr kurze Absätze (Ø 5,5 Wörter pro Satz), keine Variation, keine Länge. Wirkt wie Stakkato — die typische "LinkedIn-Spacing-Maschine". Ein längerer Mittelteil mit konkretem Beispiel würde das auflockern.

[G6] ℹ️ Konkretheit: Null Zahlen, null Namen, null Situation. "Diese Woche gelernt" ohne dass je gesagt wird, woher die Erkenntnis kommt. Ein konkretes Mini-Beispiel (welches Feedback, von wem, was hat es ausgelöst) würde den Post sofort menschlich machen.

## Was funktioniert

- Die Closing-Frage "Was denkst du? Kommentier unten." ist okay — direkte Ansprache, nicht prätentiös.
- Die Du-Form passt für LinkedIn.
- Die Grund-These (Kommunikation > Strategie) ist tragfähig, sie braucht nur weniger Rhetorik und mehr Konkretes.

---

# Rewrite

Diese Woche habe ich nochmal gemerkt, wie schwer Feedback ist.

Nicht das Geben — das Annehmen. Jemand hat mir gesagt, dass eine Sache, an der ich seit Monaten hänge, in die falsche Richtung läuft. [?] Hier wäre eine konkrete Sache hilfreich — welches Projekt, welches Feedback? Im Original steht das nicht, ohne Domain-Info kann ich es nicht ergänzen.

Erste Reaktion: verteidigen. Zweite Reaktion: zuhören. Die dritte hat einen Tag gedauert.

Und dabei wurde mir klar: Die meisten Teams scheitern nicht an der Strategie, sondern daran, dass niemand sagt, was er wirklich denkt. Strategie kann man korrigieren. Schweigen nicht.

Keine neue Erkenntnis. Aber eine, die immer wieder neu wehtut.

Was war dein letztes unbequemes Feedback? Schreib es in die Kommentare.

---

**Notizen zum Rewrite:**

- Die drei Dreierschläge habe ich aufgelöst — einer ist als asymmetrische Variation ("Erste Reaktion / Zweite / die dritte hat einen Tag gedauert") überlebt, weil er eine echte Pointe trägt (Zeit-Sprung statt Parallelismus).
- Den "Trotz aller Herausforderungen"-Filler und den "verdeutlicht, wie entscheidend"-Meta-Kommentar habe ich gestrichen.
- Die Anekdoten-Stelle ist mit `[?]` markiert — das ist der Punkt, wo der Post wirklich menschlich würde. Ohne diese konkrete Info bleibt der Rewrite näher am Original, aber er sollte noch mit einer realen Szene gefüttert werden.
- Wortzahl: ~115 Wörter (Original: 88). Bewusst etwas länger, weil der originale Stakkato-Rhythmus Teil des KI-Problems war.
- Closing-Frage bewusst spezifischer als "Was denkst du?" — gibt dem Leser einen klaren Aufhänger.
