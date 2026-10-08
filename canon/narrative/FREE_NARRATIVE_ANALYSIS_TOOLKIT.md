# Free Narrative Analysis Toolkit

Status: WORKING / free-only recommendation set
Updated: 2026-10-08

## Purpose

Use external tools as diagnostics, never as automatic judges of literary quality.

The project's own continuity/backpropagation analysis remains the primary method.

Only tools with a usable free offering are listed here. Paid-only writing platforms are deliberately excluded.

## 1. Voyant Tools

**Use for:** corpus-level analysis across multiple episodes/chapters.

Useful questions for this project:
- Which names/locations become unusually dominant?
- Are certain words or motifs suddenly overused?
- Does a character's vocabulary change over time?
- Are two episodes lexically too similar?
- Which scenes contain unusually dense technical vocabulary?

Voyant is a web-based text-reading and analysis environment and supports uploading multiple texts as a corpus.
It is an open-source scholarly project. citeturn526697search3turn526697search15

Best moment:
**after Episodes 1–2 have first drafts**, when comparison becomes meaningful.

## 2. AntConc

**Use for:** precise corpus investigation.

Useful questions:
- how often Nathan says/uses a recurring phrase;
- how frequently characters mention each other;
- repeated n-grams;
- collocations;
- dialogue vocabulary;
- distribution of particular terms across episodes.

AntConc is explicitly freeware and provides concordance/corpus-analysis tools for Windows, macOS and Linux.
The current official site lists Windows installer and portable releases. citeturn122344search0turn122344search62

Best moment:
**whenever we suspect repetition or want to compare character language across a batch of chapters.**

## 3. ProseEngine

**Use for:** scene/chapter-level mechanical prose diagnostics.

It currently provides free analysis of dialogue ratio, adverb density, filter words, sentence rhythm and
readability. Its analyzer runs locally in the browser and says text is not uploaded or stored. citeturn122344search6

Best moment:
**after the first prose pass**, especially for identifying mechanically repetitive sentence rhythm or
overuse of filter words.

## 4. Vale

**Use for:** repository-integrated prose linting.

Vale is an open-source MIT-licensed command-line prose linter that works offline and supports Markdown and
other markup. Custom rules can encode project-specific style constraints. citeturn122344search1

Potential future project rules:
- flag forbidden continuity terms;
- flag accidental "piano" references for Alex;
- detect outline placeholders left in prose;
- flag repeated exposition patterns;
- enforce manuscript-specific terminology.

Vale is particularly attractive because the story lives in Git.

## 5. LanguageTool

**Use for:** grammar, punctuation, spelling and basic style cleanup after narrative decisions are stable.

Its Windows application is available free and supports Portuguese rules, including spelling, punctuation and
style checks. citeturn526697search18

Best moment:
**late revision**, not during scene invention.

---

# Tool sequence for this project

### Before prose

No external tool is necessary.

Use:
- timeline;
- character grids;
- causal graph;
- backpropagation.

### After Episode 1 first draft

1. Our manual narrative/continuity review.
2. ProseEngine for mechanical prose signals.
3. LanguageTool for language errors.
4. Optional Voyant for vocabulary/focus distribution.

### After Episodes 1–2

Use Voyant + AntConc as a corpus.

This is when we can answer questions such as:
- Is Nathan's internal voice becoming repetitive?
- Is Alex receiving enough independent language/action?
- Are technical scenes clustered too heavily?
- Are the same verbs appearing around Nathan's anxiety?
- Are exposition patterns recurring?

### After several episodes

Add Vale to the repository and create project-specific lint rules.

At that point we can build a lightweight **story-specific linter** alongside the prose lint:
continuity dates, character ages, forbidden stale facts, object provenance markers and thread consistency.

## Interpretation rule

A tool finding is evidence to inspect, not a correction to apply automatically.

For this project, some apparent "problems" will be intentional:
- repeated motifs;
- deliberate silence;
- slow relationship pacing;
- technical vocabulary in technical scenes;
- long sentences at emotional or reflective moments.

The author decides whether a flagged pattern is actually a flaw.
