# anti-ai-writer

A Claude-compatible skill that turns AI-sounding German text into text that sounds like a human wrote it.

It works in two passes:

1. **Watermark cleanup** — a deterministic Python script (`scripts/watermark_cleaner.py`) detects and removes hidden Unicode characters often found in copy-pasted AI output: zero-width spaces, byte-order marks, soft hyphens, word joiners, NBSPs, bidi controls, dash variants. Three modes: `detect`, `clean_basic`, `clean_advanced`.
2. **Stylistic review and rewrite** — the skill scans the text for the patterns that make readers go "this was written by ChatGPT": negation-affirmation, rule-of-three, puffery, superficial analysis, elegant variation, AI-vocabulary clusters, symmetric cadence. A mechanical linter (`scripts/kadenz_linter.py`) catches the regex-detectable ones; the LLM handles the subtle structural and rhythmic patterns.

The skill produces a structured findings report and, on request, a rewritten version of the text. It marks open content with `[?]` placeholders rather than inventing facts.

## What this skill is — and is not

**It is:** a sanitation and quality tool. Good for marketing copy, LinkedIn posts, newsletters, blog drafts, pitches, internal docs — anything where "this sounds AI-generated" is the complaint.

**It is not:** a detector-bypass tool. It does not promise that the cleaned text will pass an AI-content detector. It cannot remove statistical watermarks like SynthID, because those don't live in visible characters. If your goal is to slip something past a plagiarism or AI-detection system for a graded submission, this tool is not the right fit and the skill will say so.

## Installation

### As a Claude skill

Use the `.skill` package directly:

```
anti-ki-review.skill
```

Install it through your Claude client's skill installer (Claude Code, Cowork, or the appropriate plugin manager).

### Standalone use of the scripts

Both scripts are pure Python 3, no dependencies:

```bash
# Detect hidden Unicode in a file
python3 scripts/watermark_cleaner.py myfile.md --mode detect

# Clean hidden Unicode, write result to a new file
python3 scripts/watermark_cleaner.py myfile.md --mode clean_basic --output cleaned.md

# Advanced: also normalize spaces, dashes, blank lines
python3 scripts/watermark_cleaner.py myfile.md --mode clean_advanced \
  --normalize-dashes --dash-style em_dash --output cleaned.md

# Run the stylistic linter
python3 scripts/kadenz_linter.py myfile.md
```

Both scripts return structured JSON.

## Repository layout

```
anti-ki-review/
├── SKILL.md                          The skill's main instructions
├── scripts/
│   ├── watermark_cleaner.py          Step 0: hidden Unicode detection / cleanup
│   └── kadenz_linter.py              Step 1: mechanical pattern linter
├── references/
│   ├── ai-patterns.md                G1–G6 pattern catalog (Negation-Affirmation, Puffery, etc.)
│   ├── rewrite-playbook.md           Before/after rewrite strategies
│   └── unicode-ruleset.md            Documentation of which code points the cleaner handles
└── evals/
    ├── test-text-*.md                Test inputs (KI-marketing, LinkedIn, human control, watermarked)
    ├── result-test-*.md              Test outputs from skill runs
    ├── eval-viewer.html              Browser-readable comparison of all test runs
    └── workspace/                    Eval-runner workspace (iteration-1, iteration-2)
```

## Language

The skill, the references, and the linter's rule set are tuned for **German**. The stylistic patterns (rule-of-three, negation-affirmation, puffery, superficial analysis) are largely language-independent and the LLM portion works for English and other languages too — but the vocabulary blocklist and the regex patterns won't catch everything outside German.

## License

MIT. See `LICENSE`.

## Notes on what the watermark cleaner covers

The cleaner targets the Unicode code points listed in `references/unicode-ruleset.md`. The default removal list includes:

- Zero-width separators (U+200B, U+200C, U+200D)
- BOM (U+FEFF)
- Soft Hyphen (U+00AD)
- Word Joiner family (U+2060–U+2064)
- Bidi controls (U+200E, U+200F, U+202A–U+202E)
- Space variants normalized in `clean_advanced` (U+00A0, U+2002–U+200A, U+202F, U+205F, U+3000)
- Dash variants optionally unified to a chosen style

Special care: U+200D (Zero Width Joiner) is removed by default but the cleaner emits a warning, because in emoji sequences (👨‍👩‍👧) and several Indic scripts the joiner is semantically required. If your text contains those, review the result or skip cleanup for the affected sections.
