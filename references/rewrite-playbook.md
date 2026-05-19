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

## 13. Burstiness erhöhen → kurz und lang gezielt mischen

Menschliche Prosa schwankt stark in der Satzlänge — LLM-Output bleibt auffällig gleichmäßig bei 12–20 Wörtern pro Satz. Der Trick ist nicht „kürzer schreiben", sondern die Varianz hochziehen: einen 3-Wort-Satz neben einen 28-Wort-Satz stellen.

```
BAD (uniforme Kadenz, alle Sätze 12–16 Wörter):
"Wir haben das System im Februar eingeführt. Die ersten Wochen waren
holprig und brachten viele Rückfragen. Im März stabilisierte sich der
Prozess deutlich. Heute läuft alles routiniert und ohne Probleme."

FIX (gemischt — kurz, lang, mittel, sehr kurz):
"Wir haben das System im Februar eingeführt. Holprig. Die ersten
Wochen brachten so viele Rückfragen, dass wir zwischendrin überlegt
haben, ob wir das Ganze zurückrollen — was rückblickend übertrieben
war, denn schon im März stabilisierte sich der Prozess. Heute? Läuft."
```

**Faustregel:** In einem 100-Wort-Absatz sollten mindestens ein Satz unter 5 Wörter haben und einer über 25. Wenn alle Sätze in einem 10-Wort-Korridor liegen, ist das ein KI-Marker.

**Anti-Pattern:** Kurz/Lang/Kurz/Lang als striktes Schema durchziehen — das ist nur ein neues Muster. Asymmetrie kommt von echter Gedankenführung, nicht von Mechanik. Schau dir an, wo der Inhalt ein Punch-Statement verträgt, und wo er Raum zum Atmen braucht.

**Wo Punch-Sätze hingehören:** nach einer langen Erklärung, vor einem Themenwechsel, als Bewertung. Nicht als Setup.

---

## 14. Statistisch ungewöhnliche Wortwahl → seltenes Vokabular und unerwartete Kollokationen

LLMs greifen zur statistisch wahrscheinlichsten Wortwahl — was im Mittel korrekt klingt, aber genau deshalb austauschbar wird. Der Fix: Verben und Substantive durch präzisere, weniger erwartbare Alternativen ersetzen — sofern sie sachlich passen.

```
BAD: "Das Problem beeinflusst die Performance des Systems."
FIX: "Das Problem zieht die Performance nach unten."
FIX: "Der Engpass biegt die Latenz schief."
```

```
BAD: "Wir haben den Prozess verbessert."
FIX: "Wir haben den Prozess geschliffen."
FIX: "Wir haben den Prozess zugespitzt."
```

**Substitutions-Beispiele (Verben):**

| Erwartbar | Weniger erwartbar |
|-----------|-------------------|
| verbessern | schleifen, schärfen, zuspitzen, glattziehen |
| beeinflussen | verschieben, biegen, umlenken, kippen |
| analysieren | zerlegen, auseinanderpflücken, abklopfen |
| nutzen | anzapfen, ausschöpfen, abgreifen |
| reduzieren | abschmelzen, abräumen, eindampfen |
| optimieren | nachjustieren, glattziehen, feintunen |

**Substitutions-Beispiele (Substantive):**

| Erwartbar | Weniger erwartbar |
|-----------|-------------------|
| Problem | Knoten, Bruchstelle, Reibung, Sollbruchstelle |
| Lösung | Hebel, Ausweg, Klotz, Pfropfen |
| Veränderung | Ruck, Schwenk, Drift, Abkippen |
| Vorteil | Hebel, Vorsprung, Vorderhand |

**Ungewöhnliche Kollokationen:** Statt der erwartbaren Verb-Substantiv-Paarung eine, die in der Sprache existiert, aber selten ist.

```
BAD: "ein Problem lösen"
FIX: "einen Knoten lösen", "eine Reibung wegnehmen", "eine Bruchstelle kitten"
```

**Caveat:** Nur einsetzen, wenn die Alternative semantisch passt. „Wir haben den Prozess zerlegt" ist nicht gleich „verbessert" — das wäre Bedeutungsverschiebung. Wer hier ungenau wird, baut Fehler ein. Im Zweifel das gewöhnliche Wort behalten.

**Register-Check:** Ein Geschäftsbericht verträgt „zugespitzt" nicht. Eine LinkedIn-Story schon. Das Vokabular muss zum Ton passen, sonst klingt der Text gestelzt — was wieder nach KI riecht, nur eben nach einer anderen KI.

**Dichte:** 2–4 ungewöhnliche Wortwahlen pro 200 Wörter reichen. Mehr wirkt überspannt.

---

## 15. Idiosynkrasien einbauen → Halbsätze, persönliche Einschübe, Selbstkorrektur

Echte Menschen schreiben nicht nur Vollsätze. Sie unterbrechen sich. Korrigieren sich. Schieben einen Gedanken nach. LLMs tun das fast nie — und wenn doch, dann nach Schema. Das, was hier helfen soll, ist die echte Idiosynkrasie: kleine Brüche, die nicht performt wirken.

**Halbsätze als eigenständige Aussage:**

```
BAD: "Das Konzept überzeugt nicht, weil es zu abstrakt ist."
FIX: "Das Konzept überzeugt nicht. Zu abstrakt."
```

```
BAD: "Die Antwort lautet Nein."
FIX: "Die Antwort? Nein."
```

**Selbstkorrektur im laufenden Satz:**

```
BAD: "Der Ansatz funktioniert für 80 % der Fälle."
FIX: "Der Ansatz funktioniert für 80 % der Fälle — gut, eher 70, ehrlich gerechnet."
```

```
BAD: "Wir hatten das Problem im letzten Quartal gelöst."
FIX: "Wir hatten das Problem im letzten Quartal gelöst. Geglaubt. Bis es wiederkam."
```

**Persönlich gefärbte Einschübe in Klammern oder mit Gedankenstrich:**

```
BAD: "Die Migration war komplex und dauerte vier Wochen."
FIX: "Die Migration war komplex (komplexer, als der Plan vorsah) und dauerte vier Wochen."
```

```
BAD: "Die Statistik zeigt einen klaren Trend."
FIX: "Die Statistik zeigt einen klaren Trend — wobei „klar" hier großzügig ist."
```

**Konjunktional anfangen — was Schullehrer früher verboten haben:**

```
BAD: "Es gab natürlich Gegenstimmen."
FIX: "Aber es gab Gegenstimmen. Klar gab es die."
```

**Caveat — nicht inflationär:** Eine Idiosynkrasie pro Absatz, höchstens zwei. Wenn jeder dritte Satz einen Einschub hat, eine Selbstkorrektur enthält oder mit „Aber" anfängt, ist das ein neues Muster — kein menschliches mehr. Idiosynkrasie heißt: an der einen Stelle, wo es passt, nicht im Raster.

**Caveat — Tonwechsel beachten:** Selbstkorrektur passt in Essays, Briefen, Posts. In einem AGB-Text wirkt sie deplatziert. Wenn das Original durchgängig formal ist, halt dich an Halbsätze und Klammer-Einschübe und lass die Selbstkorrektur weg.

---

## 16. Heavy Paraphrasing → gezielte Token- und Phrasensubstitution

Statt Wort für Wort zu glätten: ganze Phrasen-Bausteine ersetzen, die LLMs überproportional verwenden. Das ändert die statistische Signatur des Texts deutlicher als jedes Einzelwort-Tuning.

**Hochfrequente LLM-Bausteine — pauschal verdächtig:**

| Erwartbar (LLM-typisch) | Substitution |
|-------------------------|--------------|
| „im Hinblick auf" | „bei", „für", konkret machen |
| „vor dem Hintergrund von" | „weil", „da" |
| „im Rahmen von" | „bei", „in", oder streichen |
| „spielt eine Rolle bei" | „ist beteiligt an", „wirkt auf", oder konkret |
| „in Bezug auf" | „zu", „bei" |
| „es lässt sich festhalten" | streichen, direkt sagen |
| „darüber hinaus" | „außerdem", „und" |
| „im Wesentlichen" | meist streichen — Füllwort |
| „nicht zuletzt" | streichen |
| „in der Tat" | streichen oder „tatsächlich" |
| „letztendlich" | „am Ende", oder streichen |
| „eine Vielzahl von" | „viele", oder Zahl nennen |
| „eine breite Palette an" | „mehrere", konkret machen |
| „im Einklang mit" | „passend zu", „nach" |
| „Aspekte" | konkret werden — meist meinst du „Punkte", „Stellen", „Teile" |

**Mehrwort-Strukturen ersetzen — nicht nur Wörter:**

```
BAD: "Im Hinblick auf die Anforderungen des Projekts lässt sich
      festhalten, dass eine Vielzahl von Aspekten zu berücksichtigen ist."
FIX: "Das Projekt hat viele bewegliche Teile. Welche, kommt gleich."
```

```
BAD: "Vor dem Hintergrund dieser Entwicklung spielt die neue Plattform
      eine zentrale Rolle bei der Transformation."
FIX: "Die neue Plattform trägt den Umbau."
FIX: "Ohne die neue Plattform stockt der Umbau."
```

**Pattern:** LLM-Phrasen sind oft nominal („spielt eine Rolle"), Mensch-Sprache ist oft verbal („trägt", „stockt", „treibt"). Ersetze Nominalstil durch Verbalstil, wo es geht.

```
BAD: "Die Durchführung der Migration nahm vier Wochen in Anspruch."
FIX: "Die Migration dauerte vier Wochen."
```

```
BAD: "Es kam zu einer deutlichen Reduktion der Latenz."
FIX: "Die Latenz fiel deutlich."
```

**Reihenfolge umstellen — nicht nur Wörter tauschen:**

LLMs bauen Sätze oft im Muster „Subjekt — Verb — Adverbial — Objekt". Wenn du das umkehrst (Adverbial vorne, Objekt vorne), brichst du das Muster, ohne den Sinn zu verlieren.

```
BAD: "Die Performance verbesserte sich nach der Umstellung deutlich."
FIX: "Nach der Umstellung: Performance deutlich besser."
FIX: "Deutlich bessere Performance — nach der Umstellung."
```

**Caveat — Bedeutung schützen:** Token-Substitution darf den Inhalt nicht beschädigen. „Im Rahmen von Phase 2" ist nicht das gleiche wie „bei Phase 2", wenn „Rahmen" hier wirklich Scope meint. Im Zweifel beim Original bleiben.

**Caveat — nicht jede Stelle paraphrasieren:** Fachbegriffe, Eigennamen, technische Formulierungen bleiben. Wenn der Originaltext „im Sinne von §3 GeschGehG" sagt, lass es so. Paraphrase greift dort, wo eine austauschbare, abstrakte Formulierung steht — nicht bei präziser Sprache.

**Hinweis zu Detektoren:** Diese Technik verschiebt die statistische Signatur stärker als alle vorherigen. Sie ist trotzdem keine Garantie für Detektor-Bypass — siehe SKILL.md, „Was dieser Skill kann — und was nicht". Wenn ein User explizit Detektor-Bypass für Prüfungs- oder Bewerbungskontexte will: ablehnen, nicht liefern.

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
