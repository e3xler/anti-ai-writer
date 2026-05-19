#!/usr/bin/env python3
"""
Anti-KI Kadenz-Linter fuer deutschsprachige Texte.

Prueft mechanisch zaehlbare Muster aus references/ai-patterns.md (Regeln B1, B2,
C1, C7, C8, C13, C14, C16, C18, C19, C20, C21, C22, C23). Gibt strukturierte
Findings als JSON zurueck.

Keine externen Dependencies — laeuft mit jedem Python 3.

Usage:
    python3 kadenz_linter.py <datei.md>
    python3 kadenz_linter.py --text "Zu pruefender Text"
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path


def extract_spoken_text(text: str) -> str:
    """Extrahiert reinen Sprechertext aus Videoskript-aehnlichen Markdown-Dateien.

    Wenn keine `**Sprechertext:**`-Marker im Text sind, wird der Text unveraendert
    zurueckgegeben (Fliesstext-Pfad). Sind Marker vorhanden, werden nur die
    gesprochenen Bloecke extrahiert — Visualisierungs-Anweisungen, Regie-Notizen
    etc. werden ignoriert.

    Szenen-Grenzen (---) werden als Leerzeilen beibehalten, damit der
    Paragraph-Splitter sie als Absatzgrenzen erkennt.
    """
    if "**Sprechertext:**" not in text:
        return text

    lines = []
    in_speech = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped == "---" or stripped.startswith("**Szene"):
            if lines and lines[-1] != "":
                lines.append("")
            in_speech = False
            continue
        if stripped == "**Sprechertext:**":
            in_speech = True
            continue
        if stripped.startswith("**") and (stripped.endswith(":**") or stripped.endswith("**")):
            in_speech = False
            continue
        if in_speech and (stripped.startswith('*"') or stripped.startswith('*„')):
            cleaned = stripped.strip("*").strip('"').strip('„').strip('“').strip("'")
            lines.append(cleaned)
        elif not in_speech and stripped and not stripped.startswith(("**", "#", "-", "|", "<", "```", "---")):
            lines.append(stripped)
    return "\n".join(lines)


def split_paragraphs(text: str) -> list:
    """Splittet Text in Absaetze mit Zeilennummern."""
    paragraphs = []
    current_lines = []
    start_line = 1

    for i, line in enumerate(text.split("\n"), 1):
        if line.strip() == "":
            if current_lines:
                paragraphs.append({
                    "text": "\n".join(current_lines),
                    "start_line": start_line,
                    "end_line": i - 1
                })
                current_lines = []
        else:
            if not current_lines:
                start_line = i
            current_lines.append(line)

    if current_lines:
        paragraphs.append({
            "text": "\n".join(current_lines),
            "start_line": start_line,
            "end_line": start_line + len(current_lines) - 1
        })

    return paragraphs


def split_sentences(text: str) -> list:
    """Splittet Text in Saetze (deutsch-tauglich)."""
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ„\'])', text)
    result = []
    for s in sentences:
        s = s.strip()
        if s:
            result.append(s)
    return result


def check_sentence_length(paragraphs: list) -> list:
    """B1: Saetze ueber 20 Woerter."""
    findings = []
    for para in paragraphs:
        for sentence in split_sentences(para["text"]):
            word_count = len(sentence.split())
            if word_count > 20:
                findings.append({
                    "rule": "B1",
                    "severity": "warning",
                    "line": para["start_line"],
                    "message": "Satz mit %d Woertern (Richtwert: max. 20)" % word_count,
                    "text": sentence[:80] + ("..." if len(sentence) > 80 else ""),
                    "fix_hint": "Satz aufteilen oder kuerzen."
                })
    return findings


def check_paragraph_length(paragraphs: list) -> list:
    """B2: Absaetze ueber 4 Saetze."""
    findings = []
    for para in paragraphs:
        sentence_count = len(split_sentences(para["text"]))
        if sentence_count > 4:
            findings.append({
                "rule": "B2",
                "severity": "warning",
                "line": para["start_line"],
                "message": "Absatz mit %d Saetzen (Richtwert: max. 4)" % sentence_count,
                "text": para["text"][:80] + "...",
                "fix_hint": "Absatz aufteilen."
            })
    return findings


def check_symmetrical_triples(text: str, paragraphs: list) -> list:
    """C1: Symmetrische Dreierschlaege ('Kein X. Kein Y. Sondern Z.')"""
    findings = []
    for para in paragraphs:
        sentences = split_sentences(para["text"])
        for i in range(len(sentences) - 2):
            triple = sentences[i:i+3]
            if all(len(s.split()) <= 6 for s in triple):
                first_words = [s.split()[0].lower() if s.split() else "" for s in triple]
                if first_words[0] == first_words[1] or first_words[1] == first_words[2]:
                    findings.append({
                        "rule": "C1",
                        "severity": "error",
                        "line": para["start_line"],
                        "message": "Symmetrischer Dreierschlag",
                        "text": " | ".join(triple),
                        "fix_hint": "Einen klaren Satz statt drei kurzer Parallelen schreiben."
                    })
    return findings


def check_telegraphic_lists(text: str, paragraphs: list) -> list:
    """C14: Telegraphische Dreierlisten ('Recherchiert. Getestet. Entschieden.')"""
    findings = []
    pattern = re.compile(r'(\b\w+[.!]\s+\b\w+[.!]\s+\b\w+[.!])')
    for para in paragraphs:
        for match in pattern.finditer(para["text"]):
            words = match.group().replace(".", " ").replace("!", " ").split()
            if all(len(w) <= 15 for w in words) and len(words) <= 6:
                findings.append({
                    "rule": "C14",
                    "severity": "error",
                    "line": para["start_line"],
                    "message": "Telegraphische Dreierliste",
                    "text": match.group(),
                    "fix_hint": "In einen normalen Satz einbauen oder Items unterschiedlich lang machen."
                })
    return findings


def check_x_nicht_y_reversals(text: str, paragraphs: list) -> list:
    """C13: 'X - nicht Y'-Reversals (Richtwert: max. 1-2 pro Text)."""
    findings = []
    patterns = [
        r'nicht\s+\w+,?\s+sondern',
        r'kein[e]?\s+\w+,?\s+sondern',
        r'–\s+nicht\s+',
        r'—\s+nicht\s+',
    ]
    count = 0
    for para in paragraphs:
        for pat in patterns:
            matches = re.findall(pat, para["text"], re.IGNORECASE)
            for _match in matches:
                count += 1
                if count > 2:
                    findings.append({
                        "rule": "C13",
                        "severity": "warning" if count <= 3 else "error",
                        "line": para["start_line"],
                        "message": "'X - nicht Y'-Reversal #%d (Richtwert: max. 2 pro Text)" % count,
                        "text": para["text"][:80] + "...",
                        "fix_hint": "Positiv formulieren statt ueber Verneinung."
                    })
    return findings


def check_statt_frequency(paragraphs: list) -> list:
    """C23: 'Statt'-Haeufung (max. 1 pro Absatz)."""
    findings = []
    for para in paragraphs:
        statt_count = len(re.findall(r'\bstatt\b', para["text"], re.IGNORECASE))
        if statt_count > 1:
            findings.append({
                "rule": "C23",
                "severity": "error",
                "line": para["start_line"],
                "message": "'statt' kommt %dx im selben Absatz vor (max. 1)" % statt_count,
                "text": para["text"][:80] + "...",
                "fix_hint": "Alternativen: 'und nicht', 'lieber', oder positiven Fall beschreiben."
            })
    return findings


def check_colon_setup_punchline(paragraphs: list) -> list:
    """C18: Doppelpunkt-Setup-Punchline (max. 1 pro Absatz)."""
    findings = []
    for para in paragraphs:
        colons = re.findall(r'[a-zäöüß]\s*:\s+[A-ZÄÖÜ]', para["text"])
        if len(colons) > 1:
            findings.append({
                "rule": "C18",
                "severity": "warning",
                "line": para["start_line"],
                "message": "%d Doppelpunkt-Setups im selben Absatz (max. 1)" % len(colons),
                "text": para["text"][:80] + "...",
                "fix_hint": "Setup-Satz umformulieren, sodass der Doppelpunkt wegfaellt."
            })
    return findings


def check_dash_turns(paragraphs: list) -> list:
    """C19: Gedankenstrich-Turn (max. 1 pro Absatz)."""
    findings = []
    for para in paragraphs:
        dash_turns = len(re.findall(
            r'\s[–—]\s+(aber|doch|nur|dennoch|trotzdem|jedoch)',
            para["text"], re.IGNORECASE
        ))
        if dash_turns > 1:
            findings.append({
                "rule": "C19",
                "severity": "warning",
                "line": para["start_line"],
                "message": "%d Gedankenstrich-Turns im selben Absatz (max. 1)" % dash_turns,
                "text": para["text"][:80] + "...",
                "fix_hint": "Gedankenstrich durch Punkt ersetzen, zweiten Satz normal beginnen."
            })
    return findings


def check_repeated_sentence_starts(paragraphs: list) -> list:
    """C22: Wiederholte Satzanfaenge als Parallelismus."""
    findings = []
    for para in paragraphs:
        sentences = split_sentences(para["text"])
        if len(sentences) < 2:
            continue
        starts = []
        for s in sentences:
            words = s.split()
            if len(words) >= 2:
                starts.append("%s %s" % (words[0].lower(), words[1].lower()))
            elif words:
                starts.append(words[0].lower())

        start_counts = Counter(starts)
        for start, count in start_counts.items():
            if count >= 2 and start not in ("und das", "das ist"):
                findings.append({
                    "rule": "C22",
                    "severity": "warning",
                    "line": para["start_line"],
                    "message": "Satzanfang '%s' kommt %dx vor" % (start, count),
                    "text": para["text"][:80] + "...",
                    "fix_hint": "Satzanfaenge variieren."
                })
    return findings


def check_comparison_cadence(paragraphs: list) -> list:
    """C21: Vergleichskadenz ('dasselbe wie X, nur dass Y')."""
    findings = []
    patterns = [
        r'dasselbe wie .+?,\s+(nur|aber)',
        r'genauso wie .+?,\s+(nur|aber)',
        r'wie .+?,\s+nur dass',
        r'im grunde .+?,\s+nur',
    ]
    for para in paragraphs:
        for pat in patterns:
            matches = re.findall(pat, para["text"], re.IGNORECASE)
            if matches:
                findings.append({
                    "rule": "C21",
                    "severity": "warning",
                    "line": para["start_line"],
                    "message": "Vergleichskadenz ('wie X, nur dass Y')",
                    "text": para["text"][:80] + "...",
                    "fix_hint": "Gemeinsamkeit und Unterschied in getrennten Saetzen benennen."
                })
    return findings


def check_inverted_opener(paragraphs: list) -> list:
    """C20: Invertierte/rhetorische Opener."""
    findings = []
    patterns = [
        r'^(Nicht\s+\w+\s+(ist|war|sind))',
        r'^(Am\s+\w+\s+liegt\s+es)',
        r'^(Es\s+ist\s+nicht\s+)',
        r'^(Kein[e]?\s+\w+\s+(ist|war|hat))',
    ]
    for para in paragraphs:
        sents = split_sentences(para["text"])
        first_sentence = sents[0] if sents else ""
        for pat in patterns:
            if re.match(pat, first_sentence, re.IGNORECASE):
                findings.append({
                    "rule": "C20",
                    "severity": "warning",
                    "line": para["start_line"],
                    "message": "Invertierter/rhetorischer Opener",
                    "text": first_sentence[:80] + ("..." if len(first_sentence) > 80 else ""),
                    "fix_hint": "Flach anfangen - direkt sagen, worum es geht."
                })
    return findings


def check_business_vocabulary(text: str, paragraphs: list) -> list:
    """C8: Generisches Business-Vokabular."""
    findings = []
    banned = [
        "transformation", "mehrwert", "ganzheitlich", "innovativ",
        "nachhaltig", "synergien", "agil", "disruptiv", "paradigmenwechsel",
        "game-changer", "best practice", "cutting-edge", "state-of-the-art",
        "zukunftsfaehig", "vorreiter", "wegweisend",
    ]
    for para in paragraphs:
        text_lower = para["text"].lower()
        for word in banned:
            if word in text_lower:
                findings.append({
                    "rule": "C8",
                    "severity": "error",
                    "line": para["start_line"],
                    "message": "Generisches Business-Vokabular: '%s'" % word,
                    "text": para["text"][:80] + "...",
                    "fix_hint": "Sagen, was konkret gemeint ist."
                })
    return findings


def check_setup_sentences(paragraphs: list) -> list:
    """C16: Setup-Saetze ohne Inhalt."""
    findings = []
    patterns = [
        r'(was jetzt kommt)',
        r'(und jetzt wird es)',
        r'(jetzt kommt der dreh)',
        r'(was da gerade passiert)',
        r'(das hat einen namen)',
        r'(dafuer gibt es einen begriff)',
        r'(schauen wir uns .+ an)',
        r'(lass uns .+ anschauen)',
    ]
    for para in paragraphs:
        for pat in patterns:
            if re.search(pat, para["text"], re.IGNORECASE):
                findings.append({
                    "rule": "C16",
                    "severity": "warning",
                    "line": para["start_line"],
                    "message": "Setup-Satz ohne Inhalt",
                    "text": para["text"][:80] + "...",
                    "fix_hint": "Direkt den Inhalt liefern statt ihn anzukuendigen."
                })
    return findings


def check_weder_noch(paragraphs: list) -> list:
    """C7/C13: Symmetrische weder-noch / beides-Konstruktionen."""
    findings = []
    patterns = [
        r'weder\s+.+?\s+noch\s+',
        r'nicht\s+.+?,?\s+aber\s+auch\s+nicht',
    ]
    for para in paragraphs:
        for pat in patterns:
            if re.search(pat, para["text"], re.IGNORECASE):
                findings.append({
                    "rule": "C7",
                    "severity": "warning",
                    "line": para["start_line"],
                    "message": "Symmetrische Konstruktion (weder/noch oder Doppel-Verneinung)",
                    "text": para["text"][:80] + "...",
                    "fix_hint": "Asymmetrie zulassen. Beide Aspekte in eigene Saetze aufbrechen."
                })
    return findings


def run_all_checks(text: str) -> dict:
    """Fuehrt alle mechanischen Checks durch."""
    content = extract_spoken_text(text)
    paragraphs = split_paragraphs(content)

    all_findings = []
    all_findings.extend(check_sentence_length(paragraphs))
    all_findings.extend(check_paragraph_length(paragraphs))
    all_findings.extend(check_symmetrical_triples(content, paragraphs))
    all_findings.extend(check_telegraphic_lists(content, paragraphs))
    all_findings.extend(check_x_nicht_y_reversals(content, paragraphs))
    all_findings.extend(check_statt_frequency(paragraphs))
    all_findings.extend(check_colon_setup_punchline(paragraphs))
    all_findings.extend(check_dash_turns(paragraphs))
    all_findings.extend(check_repeated_sentence_starts(paragraphs))
    all_findings.extend(check_comparison_cadence(paragraphs))
    all_findings.extend(check_inverted_opener(paragraphs))
    all_findings.extend(check_business_vocabulary(content, paragraphs))
    all_findings.extend(check_setup_sentences(paragraphs))
    all_findings.extend(check_weder_noch(paragraphs))

    all_findings.sort(key=lambda f: f["line"])

    error_count = sum(1 for f in all_findings if f["severity"] == "error")
    warning_count = sum(1 for f in all_findings if f["severity"] == "warning")

    total_sentences = sum(len(split_sentences(p["text"])) for p in paragraphs)
    total_words = sum(len(s.split()) for p in paragraphs for s in split_sentences(p["text"]))
    avg_len = round(total_words / max(1, total_sentences), 1)

    if error_count > 0:
        verdict = "\U0001f534 Klingt deutlich nach KI"
    elif warning_count > 2:
        verdict = "⚠️ Nacharbeit empfohlen"
    else:
        verdict = "✅ Klingt menschlich"

    return {
        "total_findings": len(all_findings),
        "errors": error_count,
        "warnings": warning_count,
        "verdict": verdict,
        "findings": all_findings,
        "stats": {
            "paragraphs": len(paragraphs),
            "sentences": total_sentences,
            "avg_sentence_length": avg_len,
            "total_words": total_words
        },
        "note": "Dies sind nur die mechanisch pruefbaren Muster. Subtile Muster (Gesamtrhythmus, fehlende 'tote' Saetze, rhetorische Turns im Kontext, Elegant Variation, Superficial Analysis) erfordern zusaetzlich eine LLM-basierte Pruefung."
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 kadenz_linter.py <datei.md>")
        print('       python3 kadenz_linter.py --text "Zu pruefender Text"')
        sys.exit(1)

    if sys.argv[1] == "--text":
        input_text = " ".join(sys.argv[2:])
    else:
        input_text = Path(sys.argv[1]).read_text(encoding="utf-8")

    result = run_all_checks(input_text)
    print(json.dumps(result, ensure_ascii=False, indent=2))
