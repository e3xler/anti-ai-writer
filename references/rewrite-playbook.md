# Rewrite-Playbook — Vorher/Nachher

Konkrete Fix-Strategien für die häufigsten KI-Muster. Wenn du im Rewrite-Modus arbeitest, halte dich an diese Muster — sie funktionieren in 90% der Fälle.

---

## 1. Negation-Affirmation → Direkte Aussage

```
BAD: "Das ist kein Schicksal. Das ist ein Strukturproblem."
FIX: "Ein lösbares Strukturproblem."
```

```
BAD: "Es geht nicht um Tools. Es geht um Haltung."
FIX: "Die Tools sind sekundär. Die Haltung entscheidet."
```

**Warum es funktioniert:** Direkte Aussagen sind sicherer. Verneinung zwingt den Leser, das X erst aufzubauen, um es wieder fallen zu lassen — das wirkt rhetorisch konstruiert.

---

## 2. Puffery → Fakten oder streichen

```
BAD: "spielt eine entscheidende Rolle bei der Digitalisierung"
FIX: [streichen, oder:] "60 % der Unternehmen nutzen es bereits."
```

```
BAD: "ist ein revolutionärer Ansatz"
FIX: "Erste Tests zeigen 30 % weniger Aufwand."
```

**Faustregel:** Wenn das Adjektiv weg kann ohne Sinnverlust → weg damit.

---

## 3. Superficial Analysis → Aussage statt Metakommentar

```
BAD: "Diese Statistik unterstreicht die Dringlichkeit des Problems."
FIX: "2,3 Stunden produktive Arbeit pro Tag. Der Rest ist Verwaltung."
```

```
BAD: "Die Zahlen verdeutlichen den Wandel."
FIX: "Vor zwei Jahren: 12 %. Heute: 47 %."
```

**Pattern:** Statt zu kommentieren, was die Zahlen bedeuten — die Zahlen selbst sprechen lassen.

---

## 4. Rule of Three → Auf den Kern reduzieren

```
BAD: "Schnell, präzise und skalierbar."
FIX: "Schnell und präzise." (oder den einen Aspekt nennen, der wirklich zählt)
```

```
BAD: "effizient, transparent und nachhaltig"
FIX: "spart Zeit und ist nachvollziehbar"
```

**Test:** Frag dich pro Wort: hätte ich das geschrieben, wenn ich nicht in einer Dreierreihe wäre?

---

## 5. Symmetrische Dreierschläge → Asymmetrie

```
BAD: "Kein Glück. Keine Magie. Sondern System."
FIX: "Kein Glück — sondern ein System, das man lernen kann."
```

```
BAD: "Recherchiert. Getestet. Entschieden."
FIX: "Wir haben recherchiert, getestet und uns entschieden."
```

**Warum:** Drei kurze Parallelsätze sind ein starkes KI-Signal. Ein normaler Satz transportiert dieselbe Info ohne Rhetorik.

---

## 6. Elegant Variation → Wiederholung zulassen

```
BAD: "Die Anforderung muss erfasst werden. Das Requirement…"
FIX: "Die Anforderung muss erfasst werden. Die Anforderung…"
```

```
BAD: "Der Kunde erwartet X. Der Auftraggeber zahlt Y. Der Klient prüft Z."
FIX: "Der Kunde erwartet X. Er zahlt Y. Er prüft Z."
```

**Faustregel:** Pronomen statt Synonym. Wenn das Pronomen nicht reicht, wiederhol das Wort.

---

## 7. Setup-Sätze ohne Inhalt → Direkt einsteigen

```
BAD: "Schauen wir uns das nächste Beispiel an. Es geht um…"
FIX: "Im nächsten Beispiel geht es um…"
```

```
BAD: "Und jetzt wird es interessant. Denn…"
FIX: "Der spannende Teil: [Inhalt]"
```

**Test:** Streich den Setup-Satz raus. Liest sich der Folgesatz noch sinnvoll? Dann war der Setup überflüssig.

---

## 8. Generisches Business-Vokabular → Konkretisieren

| Phrase | Frag dich | Mögliche Fixes |
|--------|-----------|----------------|
| "ganzheitliche Lösung" | Was deckt sie ab? | "deckt Vertrieb, Service und Marketing ab" |
| "Mehrwert schaffen" | Welchen? | "spart 4 Stunden pro Woche" |
| "innovativer Ansatz" | Was ist neu? | "erstes Tool, das X mit Y kombiniert" |
| "nachhaltig" (im übertragenen Sinn) | Was meinst du wirklich? | "langfristig", "robust", "wiederholbar" |
| "synergien nutzen" | Welche? | "Vertriebsteam liefert Use Cases, Marketing macht draus Content" |

---

## 9. Lange Sätze → Aufteilen oder kürzen

```
BAD: "Die Methode, die ursprünglich von Toyota entwickelt wurde, um Verschwendung in der Produktion zu identifizieren, wird heute auch im Softwareentwicklungsbereich erfolgreich eingesetzt, was ihre breite Anwendbarkeit unterstreicht."
FIX: "Toyota hat die Methode für die Produktion entwickelt. Heute wird sie auch in der Softwareentwicklung genutzt."
```

**Faustregel:** Zwei klare Sätze schlagen einen verschachtelten. Aber: nicht jeder Satz auf 8 Wörter eindampfen — das wirkt gehackt.

---

## 10. Lange Absätze → Visuelle Pause

Wenn ein Absatz mehr als 4 Sätze hat: Schnitt an der natürlichsten Bruchstelle. Meist gibt es einen Themenwechsel oder eine Zäsur — da setzt der Absatzumbruch hin.

Nicht erlaubt: Jeden Satz zu seinem eigenen Absatz machen. Das ist kein Rhythmus, das ist Twitter.

---

## 11. Doppelpunkt-Setup-Punchline → Normalsatz

```
BAD: "Es gibt nur eine Antwort: Ja."
BAD: "Das Problem ist klar: Niemand will es lösen."
FIX: "Die einzige Antwort ist ja."
FIX: "Das Problem ist klar, niemand will es lösen."
```

Ein Doppelpunkt-Setup pro Absatz ist okay — zwei oder mehr werden zur Manier.

---

## 12. Gedankenstrich-Turn → Punkt + Normalsatz

```
BAD: "Wir haben es probiert — aber es funktionierte nicht."
FIX: "Wir haben es probiert. Es funktionierte nicht."
```

Gedankenstriche wirken theatralisch, wenn sie sich häufen. Einer pro Absatz ist die Grenze.

---

## Markierung offener Stellen

Wenn du beim Rewrite eine Stelle nicht ohne Domain-Wissen entscheiden kannst, lass sie als Kommentar drin — nicht raten:

```
[?] Hier stand „spielt eine entscheidende Rolle bei der Digitalisierung".
Welche Rolle genau? Eine Zahl oder ein konkreter Effekt würde das
Puffery-Problem lösen.
```

Lieber ein Fragezeichen als eine erfundene Zahl.

---

## Was du nicht tun sollst

- **Kein Casual-Push:** "Diese Statistik unterstreicht…" wird nicht zu "Boah, krass die Zahl." Sondern zu einer sachlichen Aussage mit Zahl.
- **Keine Du-Form erzwingen:** Wenn der Originaltext Sie-Form hat (Geschäftskorrespondenz, formelle Texte), bleibt es bei Sie. Ansprache übernimmst du.
- **Keine Inhalte streichen, nur weil sie phrasenhaft klingen:** Wenn da steht „spielt eine entscheidende Rolle bei der Digitalisierung der Logistikkette" und du weißt nichts über die Logistikkette — frag nach oder markier die Stelle.
- **Keine Über-Kürzung:** Wenn der Originaltext 500 Wörter hat, hat der Rewrite ungefähr 400–500 Wörter. Nicht 200.
