# Unicode-Ruleset für den Watermark-Cleaner

Dieser Katalog beschreibt, welche Code Points der `watermark_cleaner.py` standardmäßig erkennt, was er damit macht, und worauf bei sensiblen Texten zu achten ist.

Die maßgebliche Quelle der Ruleset-Logik ist `scripts/watermark_cleaner.py` — diese Datei ist die menschlich lesbare Erklärung.

---

## Versteckte Zeichen (Hidden Chars)

Diese Zeichen sind im Text unsichtbar, beeinflussen aber Wortgrenzen, Zeilenumbrüche oder bidirektionale Anzeige. Sie kommen besonders häufig in Copy-Paste-Material aus KI-Tools, Web-CMS, PDFs und Office-Dokumenten vor.

| Code Point | Name | Kategorie | Default-Aktion | Hinweis |
|------------|------|-----------|----------------|---------|
| U+200B | Zero Width Space | Hidden separator | Remove | Klassischer Watermark-Kandidat |
| U+200C | Zero Width Non-Joiner | Hidden join control | Remove | Stört in Arabisch/Persisch, sonst harmlos zu entfernen |
| U+200D | Zero Width Joiner | Hidden join control | Remove **mit Warnung** | Nötig für Emoji-Sequenzen (👨‍👩‍👧) und Indic-Schriften |
| U+FEFF | Zero Width No-Break Space (BOM) | Hidden mark | Remove | Häufig am Datei-Anfang als BOM |
| U+00AD | Soft Hyphen | Hyphenation control | Remove (override: `--preserve-soft-hyphen`) | In Layout-Texten manchmal gewollt |
| U+2060 | Word Joiner | Hidden join control | Remove | Hat keinen visuellen Effekt — sicher zu entfernen |
| U+2061 | Function Application | Hidden join control | Remove | Mathe-Notation, fast nie in Prosa |
| U+2062 | Invisible Times | Hidden join control | Remove | Mathe-Notation |
| U+2063 | Invisible Separator | Hidden join control | Remove | Mathe-Notation |
| U+2064 | Invisible Plus | Hidden join control | Remove | Mathe-Notation |
| U+200E | Left-To-Right Mark | Bidi control | Remove | Selten beabsichtigt in lateinischer Prosa |
| U+200F | Right-To-Left Mark | Bidi control | Remove | Selten beabsichtigt in lateinischer Prosa |
| U+202A–U+202E | Bidi Embedding/Override | Bidi control | Remove | Können für Spoofing genutzt werden; in normalen Texten sicher zu entfernen |

**Sensible Kontexte für U+200D:** Wenn der Text Emojis wie 👨‍👩‍👧 (Family-Sequenz) oder nicht-lateinische Schriften (Hindi, Tamil, Bengali, Telugu etc.) enthält, kann das Entfernen die Darstellung kaputt machen. In dem Fall: User fragen oder nur die anderen Hidden Chars entfernen.

---

## Space-Varianten (in clean_advanced normalisiert)

Diese Spaces sind sichtbar (oder fast sichtbar) und werden in `clean_advanced` zu normalem U+0020 normalisiert — außer der User schaltet das mit `--no-normalize-spaces` ab.

| Code Point | Name | Default-Aktion | Hinweis |
|------------|------|----------------|---------|
| U+00A0 | No-Break Space | → U+0020 | Häufig in HTML/Word, oft unbeabsichtigt |
| U+2002–U+200A | En/Em/Thin/Hair Spaces etc. | → U+0020 | Typografische Spaces, in Plain-Text selten gewollt |
| U+202F | Narrow No-Break Space | → U+0020 | Französische Typographie |
| U+205F | Medium Mathematical Space | → U+0020 | Mathe-Notation |
| U+3000 | Ideographic Space | → U+0020 | CJK-Text; ggf. bewusst beibehalten |

**Warnung:** Bei CJK-Texten (Chinesisch, Japanisch, Koreanisch) ist U+3000 oft semantisch gewünscht. Wenn der Text CJK enthält: vorher fragen oder mit `--preserve-code-blocks` arbeiten (greift hier zwar nicht direkt, aber zeigt das Prinzip).

---

## Dash-Varianten (in clean_advanced + --normalize-dashes)

Optional. Vereinheitlicht alle Dash-Varianten auf einen vom User gewählten Stil. Standard: `em_dash` (—).

| Code Point | Name |
|------------|------|
| U+2010 | Hyphen |
| U+2011 | Non-Breaking Hyphen |
| U+2012 | Figure Dash |
| U+2013 | En Dash |
| U+2014 | Em Dash |
| U+2015 | Horizontal Bar |
| U+2212 | Minus Sign |

**Wichtig:** Der ASCII-Bindestrich `-` (U+002D) wird *nicht* angefasst. Das ist Absicht — sonst zerschießen wir Komposita wie „well-known" oder Datums-Formate wie „2025-01-15".

Style-Optionen:

| Style | Ergebnis | Wann sinnvoll |
|-------|----------|---------------|
| `em_dash` | `—` | DE-typisch, ohne umschließende Spaces |
| `en_dash_spaced` | ` – ` | EN-typisch, mit Spaces drum |
| `hyphen_spaced` | ` - ` | Plain ASCII, max. Kompatibilität |

---

## Was *nicht* angefasst wird

- Sichtbare Buchstaben, Ziffern, Standard-Interpunktion
- Emojis (außer die ZWJ-Sequenzen im U+200D-Sonderfall)
- ASCII-Bindestrich `-`
- Inhalt innerhalb von Markdown-Code-Blöcken — sofern `--preserve-code-blocks` aktiv ist

---

## Was die Modes machen

| Mode | Was passiert |
|------|--------------|
| `detect` | Nur scannen, JSON-Report, keine Veränderung |
| `clean_basic` | Hidden Chars raus, sichtbarer Text bleibt 1:1 |
| `clean_advanced` | clean_basic + Space-Normalisierung (default an) + optional Dash-Normalisierung + Trailing-Whitespace-Trim + Blank-Line-Kollaps |

**Faustregel:** Bei reinem „mach den Text sauber, ich will nichts riskieren" → `clean_basic`. Bei „bring das in Form für Publikation" → `clean_advanced`.

---

## Sicherheits-Disclaimer

Der Cleaner gibt bei jedem Run zwei Standard-Warnungen mit:

1. „Cleaning hidden Unicode characters does not guarantee bypass of AI detectors or proprietary watermarking systems."
2. „Statistical watermarks (e.g. SynthID-style token-bias methods) do not rely on hidden characters and are unaffected by this tool."

Diese Disclaimer sind absichtlich nicht abschaltbar. Wer Unicode-Cleanup als Detektions-Bypass verkaufen will, missversteht, wofür das Tool da ist.
