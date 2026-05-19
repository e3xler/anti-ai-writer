# Anti-KI Review — test-text-1-marketing.md

## Verdict
🔴 Klingt deutlich nach KI

Der Text ist in fast jedem Satz ein Lehrbuch-Beispiel für KI-Schreibmuster: dichtes Business-Vokabular, symmetrische Dreierschläge, Negation-Affirmation, Superficial Analysis und ein generischer Schluss-Aphorismus. Substanz steckt nur in der 87/23-Statistik — der Rest ist Verpackung.

## Statistik
- Wörter / Sätze / Absätze: 123 / 16 / 4
- Ø Satzlänge: 7,7 Wörter
- Linter-Findings: 9 Errors, 4 Warnings
- LLM-Findings: 11 (verteilt auf G1–G6)

## Kritische Muster

[G0/C8] 🔴 Zeile 1 — Generisches Business-Vokabular: "transformation"
   Zitat:  "digitale Transformation"
   Fix:    Streichen oder konkretisieren (z. B. "Einführung von KI-Tools").

[G0/C8] 🔴 Zeile 1 + 3 — "ganzheitlich" (2 Treffer)
   Zitat:  "ganzheitlicher Lösungen" / "ganzheitlichen … Ansatz"
   Fix:    Streichen. Wenn etwas abgedeckt wird, dann benennen, was.

[G0/C8] 🔴 Zeile 3 — "innovativ" + "nachhaltig" + "game-changer" im selben Satz
   Zitat:  "einen innovativen, ganzheitlichen und nachhaltigen Ansatz … Sondern ein game-changer."
   Fix:    Alle vier Begriffe streichen. Stattdessen eine konkrete Fähigkeit der Plattform.

[G0/C1] 🔴 Zeile 3 — Symmetrischer Dreierschlag
   Zitat:  "Sie ist kein gewöhnliches Tool. Sie ist keine Standard-Software. Sondern ein game-changer."
   Fix:    In einen normalen Satz auflösen — und das "game-changer" gleich mit entfernen.

[G0/C14] 🔴 Zeile 5 — Telegraphische Dreierliste
   Zitat:  "Recherchiert. Getestet. Bewährt."
   Fix:    In Fließtext einbauen oder weglassen.

[G2] 🔴 Zeile 1 + 5 — Superficial Analysis (2x "unterstreicht")
   Zitat:  "unterstreicht die Notwendigkeit ganzheitlicher Lösungen" / "Diese Statistik unterstreicht die Dringlichkeit"
   Fix:    Die Zahlen selbst sprechen lassen. "87 % sehen den Bedarf, 23 % handeln." reicht.

[G3] 🔴 Zeile 1 — Puffery-Cluster: "entscheidender Bedeutung" + "zentrale Rolle"
   Zitat:  "von entscheidender Bedeutung für Unternehmen. Sie spielt eine zentrale Rolle …"
   Fix:    Beide Phrasen streichen. KI ist in Unternehmen relevant — das muss man nicht zweimal sagen.

[G5] 🔴 Zeile 7 — AI-Vokabel-Cluster (4 Treffer in einem Absatz)
   Zitat:  "verkörpert den Geist … vielschichtig, intrinsisch motivierend und prägt nachhaltig"
   Fix:    Kompletter Satz raus. Hier steht nichts, was über das vorher Gesagte hinausgeht.

## Mittlere Muster

[G0/B2] ⚠️ Zeile 3 + 5 — Zwei Absätze mit 5 Sätzen
   Fix:    An natürlicher Bruchstelle teilen — oder, besser, kürzen.

[G0/C22] ⚠️ Zeile 3 — "Sie ist" 3x als Satzanfang
   Zitat:  "Sie ist nicht nur … Sie ist kein … Sie ist keine …"
   Fix:    Auflösen über G1-Fix (Negation-Affirmation, siehe unten).

[G0/C16] ⚠️ Zeile 7 — Setup-Satz ohne Inhalt
   Zitat:  "Schauen wir uns das genauer an."
   Fix:    Streichen. Wenn der Folgesatz Substanz hat, leitet er sich selbst ein.

[G1] ⚠️ Zeile 3 — Nicht-nur-sondern-auch
   Zitat:  "Sie ist nicht nur effizient, sondern auch skalierbar."
   Fix:    Auftrennen oder direkt: "Effizient und skalierbar." (wobei "effizient" als Puffery selbst rausfliegen sollte).

[G1] ⚠️ Zeile 3 — Negation-Affirmation
   Zitat:  "Sie ist kein gewöhnliches Tool. Sie ist keine Standard-Software. Sondern …"
   Fix:    Sagen, was es ist — nicht aufzählen, was es nicht ist.

[G1] ⚠️ Zeile 5 — Didactic Disclaimer
   Zitat:  "Es ist wichtig zu beachten, dass die Digitalisierung von Startups bis Konzernen alle betrifft."
   Fix:    Streichen. Der Satz hat null Informationsgewinn.

[G1] ⚠️ Zeile 5 — False Range "von Startups bis Konzernen"
   Fix:    Streichen — gehört zum gleichen Satz wie der Didactic Disclaimer.

[G1] ⚠️ Zeile 7 — Section Summary "Zusammenfassend lässt sich sagen"
   Zitat:  "Zusammenfassend lässt sich sagen: Wer heute nicht handelt, verliert morgen den Anschluss."
   Fix:    Den Aphorismus streichen oder durch eine konkrete Handlungsaufforderung ersetzen (Demo, Trial, Kontakt).

## Niedrige Muster / Empfehlungen

[G5] ℹ️ Vokabel-Treffer einzeln: "verkörpert", "vielschichtig", "intrinsisch", "prägt nachhaltig" — siehe Cluster oben.

[G6] ℹ️ Rhythmus: Der Text hat im 2. und 4. Absatz mehrere kurze, gleichförmige Parallelsätze ("Sie ist … Sie ist … Sie ist …") direkt gefolgt vom telegraphischen "Recherchiert. Getestet. Bewährt." — das wirkt wie ein Pitch-Generator. Variation fehlt komplett.

[G6] ℹ️ Konkretheit: Außer den zwei Prozentzahlen (87/23) keine einzige spezifische Aussage. Was kann die Plattform? Für wen? Was kostet sie? — kein Wort.

## Was funktioniert

- Die Statistik **"87 % der Unternehmen erkennen den Bedarf, doch nur 23 % handeln"** ist die einzige Stelle mit echter Substanz. Sie ist konkret, kontrastiv, und der Spannungsbogen 87→23 trägt.
- Die Aussage, dass es um eine Plattform geht, kommt klar rüber — das Produkt ist erkennbar.

---

# Rewrite

87 % der Unternehmen sagen, sie brauchen KI. Nur 23 % setzen sie wirklich ein. Diese Lücke ist das eigentliche Problem.

Unsere Plattform schließt sie.

[?] Hier fehlt im Original der konkrete Mehrwert der Plattform: Was tut sie, für welche Teams, mit welchem messbaren Effekt? Ohne diese Info bleibt der Text zwangsläufig generisch. Liefere mir 1–2 Sätze zum tatsächlichen Funktionsumfang (z. B. "verbindet bestehende Datenquellen mit Sprachmodellen, ohne dass IT eine Zeile Code schreibt") — dann ersetzt das den nächsten Block.

Bisher haben wir sie mit [?: Anzahl] Unternehmen getestet. Das Ergebnis: [?: konkrete Metrik, z. B. "im Schnitt vier Stunden weniger Reporting pro Woche"].

Wenn du zu den 23 % gehören willst: [?: CTA — Demo buchen / Pilot starten / Kontakt].

---

## Hinweise zum Rewrite

- **Wortzahl:** Original 123 Wörter, Rewrite ca. 65 Wörter aktiver Text + drei Marker. Ich habe bewusst stark gekürzt, weil der Original-Text fast nur aus Phrasen besteht — bleibe ich näher am Original, transportiere ich die KI-Muster mit. **Bestätige diese Kürzung oder gib mir Substanz für die Marker — dann baue ich den Text auf vergleichbare Länge aus.**
- **Beibehalten:** Die 87/23-Statistik und der Plattform-Claim (es geht um eine Plattform, die diese Lücke adressiert).
- **Entfernt:** Alle Puffery-Adjektive, beide "unterstreicht"-Konstruktionen, die Nicht-nur-sondern-auch / Negation-Affirmation, die telegraphische Dreierliste, der Didactic Disclaimer, der "Zusammenfassend"-Aphorismus.
- **Ansprache:** Du-Form behalten (Original ist Du-nah über "Wer heute nicht handelt …").
