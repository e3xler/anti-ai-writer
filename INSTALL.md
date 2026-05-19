# Installation & Nutzung

## Schnellinstallation in Claude (Cowork / Claude Code)

Doppelklick auf `anti-ki-review.skill` — dein Claude-Client erkennt die Datei automatisch.

Falls das nicht klappt: Option „Install from file" im Client nutzen und auf `anti-ki-review.skill` zeigen.

## Standalone-Nutzung (ohne Claude)

Die beiden Python-Skripte in `source/scripts/` haben keine Abhängigkeiten und laufen eigenständig:

```bash
# Versteckte Unicode-Watermarks erkennen / entfernen
python3 source/scripts/watermark_cleaner.py myfile.md --mode clean_basic --output cleaned.md

# Stilistischen Linter ausführen (erkennt KI-typische deutsche Muster)
python3 source/scripts/kadenz_linter.py myfile.md
```

Beide geben strukturiertes JSON zurück.

## Was liegt wo

| Pfad | Was es ist |
|------|------------|
| `anti-ki-review.skill` | Installierbares Claude-Paket — enthält alles aus `source/`, sofort installierbar |
| `README.md` | Projektübersicht |
| `LICENSE` | MIT |
| `source/SKILL.md` | Haupt-Instruktionen des Skills (das, was Claude liest) |
| `source/scripts/watermark_cleaner.py` | Unicode-Watermark-Erkennung / Bereinigung |
| `source/scripts/kadenz_linter.py` | Linter für deutsche KI-Muster |
| `source/references/ai-patterns.md` | G1–G6 Pattern-Katalog |
| `source/references/rewrite-playbook.md` | Before/After Rewrite-Strategien |
| `source/references/unicode-ruleset.md` | Welche Code Points der Cleaner verarbeitet |

Die `.skill`-Datei und der `source/`-Ordner enthalten denselben Inhalt — `.skill` ist das installierbare Bundle, `source/` macht den Code direkt lesbar und änderbar.

## Updates

Aktuelle Version: https://github.com/e3xler/anti-ai-writer
