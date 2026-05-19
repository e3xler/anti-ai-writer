# anti-ai-writer

Ein Claude-kompatibler Skill, der deutsche Texte, die nach KI klingen, so umschreibt, dass sie wie von einem Menschen geschrieben wirken.

Der Skill arbeitet in zwei Durchgängen:

1. **Watermark-Bereinigung** — ein deterministisches Python-Skript (`source/scripts/watermark_cleaner.py`) erkennt und entfernt versteckte Unicode-Zeichen, die häufig in kopiertem KI-Output stecken: Zero-Width-Spaces, Byte-Order-Marks, Soft Hyphens, Word Joiner, NBSPs, Bidi-Kontrollzeichen, Dash-Varianten. Drei Modi: `detect`, `clean_basic`, `clean_advanced`.
2. **Stilistische Prüfung und Rewrite** — der Skill scannt den Text auf Muster, die Leser sofort als „das ist von ChatGPT" einordnen: Negation-Affirmation, Dreierregel, Puffery, oberflächliche Analyse, Elegant Variation, KI-Vokabular-Cluster, symmetrische Kadenz. Ein mechanischer Linter (`source/scripts/kadenz_linter.py`) fängt die per Regex erkennbaren Muster ab; das LLM übernimmt die subtilen strukturellen und rhythmischen Muster.

Der Skill liefert einen strukturierten Findings-Report und auf Wunsch eine umgeschriebene Version des Textes. Offene Inhalte werden mit `[?]`-Platzhaltern markiert — der Skill erfindet keine Fakten.

## Was dieser Skill ist — und was nicht

**Er ist:** ein Sanitations- und Qualitätstool. Geeignet für Marketing-Copy, LinkedIn-Posts, Newsletter, Blog-Entwürfe, Pitches, interne Dokumente — überall dort, wo „klingt nach KI" das Problem ist.

**Er ist nicht:** ein Detector-Bypass-Tool. Der Skill verspricht nicht, dass der bereinigte Text einen KI-Detektor täuscht. Er kann auch keine statistischen Watermarks wie SynthID entfernen, weil diese nicht in sichtbaren Zeichen stecken. Wenn das Ziel ist, einen Plagiats- oder KI-Detektor für eine benotete Abgabe auszutricksen, ist dieses Tool nicht das richtige — und der Skill sagt das auch so.

## Installation

### Als Claude-Skill

Das `.skill`-Paket direkt verwenden:

```
anti-ki-review.skill
```

Über den Skill-Installer deines Claude-Clients (Claude Code, Cowork oder den passenden Plugin-Manager) installieren.

### Standalone-Nutzung der Skripte

Beide Skripte sind reines Python 3, ohne Abhängigkeiten:

```bash
# Versteckte Unicode-Zeichen in einer Datei erkennen
python3 source/scripts/watermark_cleaner.py myfile.md --mode detect

# Versteckte Unicode-Zeichen bereinigen, Ergebnis in neue Datei
python3 source/scripts/watermark_cleaner.py myfile.md --mode clean_basic --output cleaned.md

# Advanced: zusätzlich Spaces, Dashes, Leerzeilen normalisieren
python3 source/scripts/watermark_cleaner.py myfile.md --mode clean_advanced \
  --normalize-dashes --dash-style em_dash --output cleaned.md

# Stilistischen Linter ausführen
python3 source/scripts/kadenz_linter.py myfile.md
```

Beide Skripte geben strukturiertes JSON zurück.

## Repository-Struktur

```
anti-ai-writer/
├── README.md                              Projektübersicht (diese Datei)
├── INSTALL.md                             Schnellinstallation und Nutzung
├── LICENSE                                MIT-Lizenz
├── anti-ki-review.skill                   Installierbares Claude-Paket (ZIP)
└── source/
    ├── SKILL.md                           Haupt-Instruktionen des Skills
    ├── scripts/
    │   ├── watermark_cleaner.py           Schritt 0: Unicode-Detection / Cleanup
    │   └── kadenz_linter.py               Schritt 1: Mechanischer Pattern-Linter
    └── references/
        ├── ai-patterns.md                 G1–G6 Pattern-Katalog (Negation-Affirmation, Puffery, etc.)
        ├── rewrite-playbook.md            Before/After Rewrite-Strategien
        └── unicode-ruleset.md             Welche Code Points der Cleaner verarbeitet
```

Die `.skill`-Datei und der `source/`-Ordner enthalten denselben Inhalt — `.skill` ist das installierbare Bundle, `source/` ist da, damit du Code direkt lesen und anpassen kannst.

## ZIP-Download von GitHub

Wer das Repo per „Download ZIP" zieht, bekommt das komplette Paket — `anti-ki-review.skill`, `source/SKILL.md`, sämtliche Scripts und References sind enthalten.

## Sprache

Der Skill, die References und das Regelwerk des Linters sind auf **Deutsch** zugeschnitten. Die stilistischen Muster (Dreierregel, Negation-Affirmation, Puffery, oberflächliche Analyse) sind weitgehend sprachunabhängig, und der LLM-Teil funktioniert auch für Englisch und andere Sprachen — aber die Vokabular-Blockliste und die Regex-Muster greifen außerhalb des Deutschen nicht vollständig.

## Lizenz

MIT. Siehe `LICENSE`.

## Was der Watermark-Cleaner abdeckt

Der Cleaner zielt auf die in `source/references/unicode-ruleset.md` aufgeführten Unicode-Code-Points. Die Standard-Entfernungsliste umfasst:

- Zero-Width-Separatoren (U+200B, U+200C, U+200D)
- BOM (U+FEFF)
- Soft Hyphen (U+00AD)
- Word-Joiner-Familie (U+2060–U+2064)
- Bidi-Kontrollzeichen (U+200E, U+200F, U+202A–U+202E)
- Space-Varianten — werden im Modus `clean_advanced` normalisiert (U+00A0, U+2002–U+200A, U+202F, U+205F, U+3000)
- Dash-Varianten — optional auf einen gewählten Stil vereinheitlicht

Sonderfall: U+200D (Zero Width Joiner) wird standardmäßig entfernt, aber der Cleaner gibt eine Warnung aus. Grund: In Emoji-Sequenzen (👨‍👩‍👧) und mehreren indischen Schriften ist der Joiner semantisch erforderlich. Wenn dein Text solche Inhalte enthält, prüf das Ergebnis oder überspring die Bereinigung für die betroffenen Abschnitte.
