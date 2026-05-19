#!/usr/bin/env python3
"""
Text Watermark Cleaner.

Erkennt und entfernt versteckte Unicode-Zeichen und Formatierungs-Artefakte, die
in KI-generiertem oder copy-pasted Text als Wasserzeichen oder Rest-Muell auftreten
koennen (Zero-Width-Spaces, BOM, Word Joiner, Soft Hyphen, Non-Breaking Space,
exotische Dash-Varianten, irregulaere Leerraum-Muster).

Wichtig — was dieses Tool NICHT macht:
- Es entfernt KEINE statistischen Wasserzeichen (z. B. SynthID), die auf
  Token-Auswahl-Bias basieren. Solche Wasserzeichen sind nicht im sichtbaren
  Text codiert und durch Unicode-Cleanup nicht zu beseitigen.
- Es verspricht NICHT, dass der gereinigte Text einen KI-Detektor oder einen
  proprietaeren Wasserzeichen-Scanner umgeht. Es ist ein Saubermach-Tool fuer
  Interoperabilitaet und Textqualitaet, kein Detektions-Bypass.

Keine externen Dependencies — laeuft mit jedem Python 3.

Usage:
    python3 watermark_cleaner.py <datei.txt> [--mode MODE] [--option ...]
    python3 watermark_cleaner.py --text "Eingabe-Text" [--mode MODE]

Modes:
    detect          Nur erkennen, nichts veraendern (Default)
    clean_basic     Versteckte Zeichen entfernen, sichtbarer Text unveraendert
    clean_advanced  Zusaetzlich Leerraeume/Dashes normalisieren

Optionen (nur in clean_advanced relevant):
    --normalize-spaces           NBSP / Thin Space etc. -> normaler Space
    --normalize-dashes           Em/En-Dash-Varianten vereinheitlichen
    --dash-style STYLE           em_dash | en_dash_spaced | hyphen_spaced
    --preserve-soft-hyphen       U+00AD nicht entfernen
    --preserve-code-blocks       Inhalt von ```...``` und `...` unangetastet lassen
    --preserve-blank-lines       Mehrfache Leerzeilen nicht zusammenfassen

Output: strukturiertes JSON mit summary, detected_characters, actions_taken,
cleaned_text (ausser im detect-Mode), warnings.
"""

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path


# --- Rule-Set ---------------------------------------------------------------

# Default-Aktion: 'remove', 'normalize', 'ignore'
HIDDEN_RULESET = {
    # Zero-Width-Separators
    "​": {"name": "Zero Width Space", "category": "Hidden separator", "action": "remove"},
    "‌": {"name": "Zero Width Non-Joiner", "category": "Hidden join control", "action": "remove"},
    "‍": {"name": "Zero Width Joiner", "category": "Hidden join control", "action": "remove_with_caution"},
    # BOM / No-Break Mark
    "﻿": {"name": "Zero Width No-Break Space (BOM)", "category": "Hidden mark", "action": "remove"},
    # Soft Hyphen
    "­": {"name": "Soft Hyphen", "category": "Hyphenation control", "action": "remove"},
    # Word Joiner und Konsorten
    "⁠": {"name": "Word Joiner", "category": "Hidden join control", "action": "remove"},
    "⁡": {"name": "Function Application", "category": "Hidden join control", "action": "remove"},
    "⁢": {"name": "Invisible Times", "category": "Hidden join control", "action": "remove"},
    "⁣": {"name": "Invisible Separator", "category": "Hidden join control", "action": "remove"},
    "⁤": {"name": "Invisible Plus", "category": "Hidden join control", "action": "remove"},
    # Bidi-Marken (Tags und Steuerzeichen, die meist nicht beabsichtigt sind)
    "‎": {"name": "Left-To-Right Mark", "category": "Bidi control", "action": "remove"},
    "‏": {"name": "Right-To-Left Mark", "category": "Bidi control", "action": "remove"},
    "‪": {"name": "Left-To-Right Embedding", "category": "Bidi control", "action": "remove"},
    "‫": {"name": "Right-To-Left Embedding", "category": "Bidi control", "action": "remove"},
    "‬": {"name": "Pop Directional Formatting", "category": "Bidi control", "action": "remove"},
    "‭": {"name": "Left-To-Right Override", "category": "Bidi control", "action": "remove"},
    "‮": {"name": "Right-To-Left Override", "category": "Bidi control", "action": "remove"},
}

# Whitespace-Varianten (in clean_advanced + --normalize-spaces zu normalem Space)
SPACE_NORMALIZE = {
    " ": "No-Break Space",
    " ": "En Space",
    " ": "Em Space",
    " ": "Three-Per-Em Space",
    " ": "Four-Per-Em Space",
    " ": "Six-Per-Em Space",
    " ": "Figure Space",
    " ": "Punctuation Space",
    " ": "Thin Space",
    " ": "Hair Space",
    " ": "Narrow No-Break Space",
    " ": "Medium Mathematical Space",
    "　": "Ideographic Space",
}

# Dash-Varianten
DASH_CHARS = {
    "‐": "Hyphen",
    "‑": "Non-Breaking Hyphen",
    "‒": "Figure Dash",
    "–": "En Dash",
    "—": "Em Dash",
    "―": "Horizontal Bar",
    "−": "Minus Sign",
}

DASH_STYLE_MAP = {
    "em_dash": "—",        # — (DE-typisch, ohne Spaces)
    "en_dash_spaced": " – ",  # space – space (oft in EN-Schreibweise)
    "hyphen_spaced": " - ",     # einfacher Bindestrich, plain ASCII
}


WARNINGS_ALWAYS = [
    "Cleaning hidden Unicode characters does not guarantee bypass of AI detectors or proprietary watermarking systems.",
    "Statistical watermarks (e.g. SynthID-style token-bias methods) do not rely on hidden characters and are unaffected by this tool.",
]


# --- Helpers ----------------------------------------------------------------

def _code_point(ch: str) -> str:
    return "U+%04X" % ord(ch)


def _detect(text: str) -> Counter:
    """Zaehlt alle in unseren Rulesets erfassten Zeichen."""
    counts = Counter()
    for ch in text:
        if ch in HIDDEN_RULESET or ch in SPACE_NORMALIZE or ch in DASH_CHARS:
            counts[ch] += 1
    return counts


def _extract_code_segments(text: str):
    """Findet Markdown-Code-Bloecke (``` ... ```) und Inline-Code (`...`).

    Liefert Liste von (start, end, content)-Tupeln, geordnet. Wird benutzt, um
    bei --preserve-code-blocks diese Bereiche aus dem Cleanup auszunehmen.
    """
    segments = []
    # Fenced code blocks (```...```)
    for m in re.finditer(r"```.*?```", text, re.DOTALL):
        segments.append((m.start(), m.end()))
    # Inline code (`...`) -- nur wenn keine Newline drin ist
    for m in re.finditer(r"`[^`\n]+`", text):
        segments.append((m.start(), m.end()))
    segments.sort()
    # Overlap-Filter (wenn Inline-Code in Fenced-Block faellt)
    merged = []
    for seg in segments:
        if merged and seg[0] < merged[-1][1]:
            continue
        merged.append(seg)
    return merged


def _apply_outside_segments(text: str, segments, transform_fn):
    """Wendet eine Transformations-Funktion nur ausserhalb der Segmente an."""
    if not segments:
        return transform_fn(text)
    parts = []
    last = 0
    for start, end in segments:
        parts.append(transform_fn(text[last:start]))
        parts.append(text[start:end])  # unchanged
        last = end
    parts.append(transform_fn(text[last:]))
    return "".join(parts)


# --- Main Cleaning Pipeline -------------------------------------------------

def clean_text(text: str, opts: dict) -> dict:
    """Hauptfunktion. opts: dict mit allen Flags."""
    mode = opts.get("mode", "detect")
    detected = _detect(text)
    actions = []
    warnings = list(WARNINGS_ALWAYS)

    # Soft-Hyphen-Override
    soft_hyphen_remove = not opts.get("preserve_soft_hyphen", False)

    # Code-Block-Preservation
    if opts.get("preserve_code_blocks", False):
        protected_segments = _extract_code_segments(text)
    else:
        protected_segments = []

    if mode == "detect":
        # Reine Erkennung
        return _build_result(text, None, detected, actions, warnings, mode)

    # --- Baseline: hidden chars entfernen ---
    def remove_hidden(s: str) -> str:
        out_chars = []
        for ch in s:
            if ch in HIDDEN_RULESET:
                rule = HIDDEN_RULESET[ch]
                if ch == "­" and not soft_hyphen_remove:
                    out_chars.append(ch)
                    continue
                if rule["action"] == "ignore":
                    out_chars.append(ch)
                    continue
                # remove (auch remove_with_caution -> remove + Warnung)
                continue
            out_chars.append(ch)
        return "".join(out_chars)

    cleaned = _apply_outside_segments(text, protected_segments, remove_hidden)

    # Action-Log fuer Hidden Chars — tatsaechliche Removals zaehlen
    # (wichtig wenn --preserve-code-blocks aktiv ist und manche Chars geschuetzt sind)
    actual_removed = Counter()
    cleaned_counts = _detect(cleaned)
    for ch, original_count in detected.items():
        removed = original_count - cleaned_counts.get(ch, 0)
        if removed > 0:
            actual_removed[ch] = removed

    for ch, count in actual_removed.items():
        if ch not in HIDDEN_RULESET:
            continue
        rule = HIDDEN_RULESET[ch]
        if ch == "­" and not soft_hyphen_remove:
            continue
        suffix = ""
        if protected_segments and detected[ch] > count:
            suffix = " (%d more left untouched inside code blocks)" % (detected[ch] - count)
        actions.append("Removed %d %s (%s)%s" % (count, rule["name"], _code_point(ch), suffix))
        if rule["action"] == "remove_with_caution":
            warnings.append(
                "%s (%s) was removed; in script-sensitive contexts (e.g. emoji ZWJ sequences, Indic scripts) this can change rendering. Review the output if your text contains such content."
                % (rule["name"], _code_point(ch))
            )

    if mode == "clean_basic":
        return _build_result(text, cleaned, detected, actions, warnings, mode)

    # --- clean_advanced: optional Normalisierungen ---

    # 1) Space-Normalisierung
    if opts.get("normalize_spaces", True):
        def normalize_spaces(s: str) -> str:
            for variant in SPACE_NORMALIZE:
                if variant in s:
                    s = s.replace(variant, " ")
            return s
        cleaned = _apply_outside_segments(cleaned, _extract_code_segments(cleaned) if opts.get("preserve_code_blocks") else [], normalize_spaces)
        for variant, name in SPACE_NORMALIZE.items():
            c = detected.get(variant, 0)
            if c:
                actions.append("Normalized %d %s (%s) to standard space" % (c, name, _code_point(variant)))

    # 2) Dash-Normalisierung
    if opts.get("normalize_dashes", False):
        style = opts.get("dash_style", "em_dash")
        target = DASH_STYLE_MAP.get(style, "—")

        def normalize_dashes(s: str) -> str:
            # Nur die "echten" Dash-Varianten ersetzen, nicht den ASCII-Bindestrich
            # (sonst zerschiessen wir compound words wie "well-known")
            for variant in DASH_CHARS:
                if variant in s:
                    s = s.replace(variant, target)
            # Wenn Style hyphen_spaced/en_dash_spaced gewollt ist, vereinheitliche
            # Mehrfach-Spaces drum herum auf einen
            if " " in target:
                s = re.sub(r" {2,}", " ", s)
            return s

        cleaned = _apply_outside_segments(cleaned, _extract_code_segments(cleaned) if opts.get("preserve_code_blocks") else [], normalize_dashes)
        total_dashes = sum(detected.get(v, 0) for v in DASH_CHARS)
        if total_dashes:
            actions.append("Normalized %d dash character(s) to style '%s'" % (total_dashes, style))

    # 3) Mehrfache Leerzeilen
    if not opts.get("preserve_blank_lines", False):
        # 3+ Leerzeilen -> 2 (also max. eine echte Leerzeile zwischen Absaetzen)
        before = cleaned
        cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
        if cleaned != before:
            actions.append("Collapsed runs of 3+ blank lines to single blank line separators")

    # 4) Trailing whitespace pro Zeile
    before = cleaned
    cleaned = re.sub(r"[ \t]+(\n|$)", r"\1", cleaned)
    if cleaned != before:
        actions.append("Stripped trailing whitespace from lines")

    return _build_result(text, cleaned, detected, actions, warnings, mode)


def _build_result(original: str, cleaned, detected: Counter, actions, warnings, mode: str) -> dict:
    # detected_characters: dict mit Code-Point -> {name, count, category}
    detected_obj = {}
    for ch, count in sorted(detected.items()):
        cp = _code_point(ch)
        if ch in HIDDEN_RULESET:
            info = HIDDEN_RULESET[ch]
            detected_obj[cp] = {
                "name": info["name"],
                "category": info["category"],
                "count": count,
                "unicode_category": unicodedata.category(ch),
            }
        elif ch in SPACE_NORMALIZE:
            detected_obj[cp] = {
                "name": SPACE_NORMALIZE[ch],
                "category": "Space variant",
                "count": count,
                "unicode_category": unicodedata.category(ch),
            }
        elif ch in DASH_CHARS:
            detected_obj[cp] = {
                "name": DASH_CHARS[ch],
                "category": "Dash variant",
                "count": count,
                "unicode_category": unicodedata.category(ch),
            }

    if not detected_obj:
        summary = "No hidden Unicode characters or formatting artifacts detected. Text appears clean."
    elif mode == "detect":
        summary = "Found %d suspicious character(s) across %d distinct code point(s). No changes made — detect mode." % (
            sum(d["count"] for d in detected_obj.values()), len(detected_obj),
        )
    else:
        summary = "Hidden Unicode characters and formatting artifacts were found and cleaned."

    result = {
        "summary": summary,
        "mode": mode,
        "detected_characters": detected_obj,
        "actions_taken": actions,
        "warnings": warnings,
        "stats": {
            "original_length": len(original),
            "cleaned_length": len(cleaned) if cleaned is not None else len(original),
            "distinct_hidden_code_points": len(detected_obj),
        },
    }
    if cleaned is not None:
        result["cleaned_text"] = cleaned
    return result


# --- CLI --------------------------------------------------------------------

def _parse_args(argv):
    p = argparse.ArgumentParser(
        description="Detect and clean hidden Unicode characters and formatting artifacts."
    )
    p.add_argument("input", nargs="?", help="Path to a UTF-8 text file. Use --text for inline input.")
    p.add_argument("--text", help="Inline text to process (instead of a file).")
    p.add_argument("--mode", choices=["detect", "clean_basic", "clean_advanced"], default="detect")
    p.add_argument("--normalize-spaces", action="store_true",
                   help="In clean_advanced: replace NBSP/Thin/Em spaces with standard space (default: on in advanced).")
    p.add_argument("--no-normalize-spaces", dest="normalize_spaces", action="store_false")
    p.set_defaults(normalize_spaces=True)
    p.add_argument("--normalize-dashes", action="store_true",
                   help="In clean_advanced: unify dash variants to the configured style.")
    p.add_argument("--dash-style", choices=["em_dash", "en_dash_spaced", "hyphen_spaced"], default="em_dash")
    p.add_argument("--preserve-soft-hyphen", action="store_true",
                   help="Keep U+00AD (soft hyphen) instead of removing it.")
    p.add_argument("--preserve-code-blocks", action="store_true",
                   help="Do not touch content inside ```...``` fenced blocks or `inline` code spans.")
    p.add_argument("--preserve-blank-lines", action="store_true",
                   help="Do not collapse runs of multiple blank lines.")
    p.add_argument("--output", help="Write cleaned text to this file (in addition to JSON to stdout).")
    p.add_argument("--quiet", action="store_true", help="Suppress JSON; only write cleaned text (requires --output).")
    return p.parse_args(argv)


def _read_input(args) -> str:
    if args.text is not None:
        return args.text
    if args.input is None:
        sys.stderr.write("Error: provide either a file path or --text\n")
        sys.exit(2)
    return Path(args.input).read_text(encoding="utf-8")


def main(argv=None):
    args = _parse_args(argv if argv is not None else sys.argv[1:])
    text = _read_input(args)
    opts = {
        "mode": args.mode,
        "normalize_spaces": args.normalize_spaces,
        "normalize_dashes": args.normalize_dashes,
        "dash_style": args.dash_style,
        "preserve_soft_hyphen": args.preserve_soft_hyphen,
        "preserve_code_blocks": args.preserve_code_blocks,
        "preserve_blank_lines": args.preserve_blank_lines,
    }
    result = clean_text(text, opts)

    if args.output and "cleaned_text" in result:
        Path(args.output).write_text(result["cleaned_text"], encoding="utf-8")

    if not args.quiet:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
