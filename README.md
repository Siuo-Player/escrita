# escrita — A Modern Family Parallel Fiction Project

<!-- WD-001 -->
<!-- WD-002 -->
<!-- WD-003 -->
<!-- WD-004 -->

An episodic, grounded *slice-of-life* fanfic set in the *Modern Family* parallel world. The Dunphy, Pritchett and Tucker families are real people with independent lives; Nathan remembers watching the television series in his previous life, but his memories are selective and fallible. **Reincarnation is the only supernatural exception**: there are no systems, gacha, magic, supernatural powers or precognition. The real-world 2009 baseline applies unless a documented difference says otherwise; see [the Story Bible](canon/STORY_BIBLE.md) for the current premise and document authority map, and [WORLD_DIFFERENCE_REGISTRY.md](canon/narrative/WORLD_DIFFERENCE_REGISTRY.md) for world rules.

---

## 1. Project Overview & Premise

* **Protagonist:** **Nathan Callahan** (turns 13 on September 7, 2009 in Seattle; relocates to Cheviot Hills, Los Angeles).
  * **Nature:** Reincarnated into his own childhood. The reincarnation is the only supernatural exception; his previous-life memories are fallible human recollections, not eidetic recall or a predictive power.
  * **Personality:** Highly disciplined in computer science (C++/OpenGL ES) and athletics (soccer and judo), but guarded, intensely shy, and burdened by a chronic fear of appearing arrogant or presumptuous.
* **The Callahan Family:** Clifford Callahan (father, Senior VP of Engineering Operations) and Heather Callahan (mother, corporate financial consultant). Pragmatic, loving, stable foundation.
* **Independent Core Tech Arc:** Independent development of a custom 2D mobile game in C++ featuring flow-field spatial AI for the newly launched iPhone 3GS (2009).
* **Alex Dunphy Dynamic:** Absolute slow burn. Begins with cautious observation and mutual intellectual respect across adjacent grade levels (Nathan in 8th grade, Alex in 7th); deepens into a resilient, unpretentious friendship throughout Season 1.
* **Prose Language:** **American English** (contemporary 2009 setting, authentic character dialogue, and technical precision; see `canon/DECISION_LOG.md` DEC-008).

### Parallel-world canon

The Dunphy, Pritchett and Tucker families are real people in the story world, not fictional characters being filmed. Nathan remembers the television series from his previous life. Episode titles are memory/reference labels only; they do not imply that the events are being broadcast in this world. The original timeline is a starting reference and may diverge cumulatively because Nathan exists and acts in it. Consult `canon/narrative/WORLD_DIFFERENCE_REGISTRY.md` before changing any assumption about the world. An unrecorded difference must not be invented; the sourced real-world 2009 baseline remains in force by default.

---

## 2. Repository Structure

```
escrita/
├── .github/
│   └── workflows/
│       └── story-tests.yml        # CI test suite automation on push/PR
├── canon/                         # Canonical story records and specialist sources of truth
│   ├── STORY_BIBLE.md              # Current story snapshot, document roles and canon hierarchy
│   ├── characters/                # Character dossiers (Nathan, Alex, Callahans, Maxwell, etc.)
│   ├── narrative/
│   │   ├── EVENT_REGISTRY.md      # Master authoritative event ledger (EVT-xxx)
│   │   ├── WORLD_DIFFERENCE_REGISTRY.md # Authoritative real-world vs parallel-world differences
│   │   ├── SERIES_GLOBAL_ARCHITECTURE.md # Multi-season roadmaps (t=0.0 to t=1.0)
│   │   ├── SEASON_1_ARC_PLAN.md   # Season 1 episode-by-episode master plan (EP01 to EP12)
│   │   ├── SEASON_1_DECISION_AND_STATUS_REGISTER.md # Consolidated decisions, status and open conflicts
│   │   ├── PROP_AND_CLUE_REGISTRY.md # Backpropagated props and clues causal ledger
│   │   ├── MODERN_PROSE_AND_THEATRICAL_STYLE.md # Staging, pacing, and chameleonic POV rules
│   │   ├── TECHNICAL_AND_LEGAL_FOUNDATIONS.md  # Source-qualified 2009 Apple terms & iPhone 3GS facts
│   │   ├── DIALOGUE_NATURALNESS_STANDARD.md
│   │   ├── NARRATIVE_AND_CAUSAL_METHOD.md
│   │   └── NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md # Agência, caracterização, estudos comparativos e revisão literária
│   └── DECISION_LOG.md            # Authoritative decision ledger (DEC-001 onwards)
├── docs/
│   └── memory/                    # ai-memory system documentation, ADRs, and procedures
├── episodes/
│   └── season-1/                  # Outlines and full prose drafts for Season 1
│       ├── EP01_BEFORE_AND_AFTER_OUTLINE.md
│       ├── EP01_DRAFT.md          # Working prose draft (~7.6k words; below target)
│       ├── EP02_FINISH_THE_GAME_OUTLINE.md
│       ├── EP02_DRAFT.md          # Working prose draft (~4.4k words; below target)
│       ├── EP03_VECTOR_TRAJECTORIES_OUTLINE.md
│       ├── EP03_DRAFT.md          # Structural full-prose draft; below the 10k–14k target
│       ├── EP04_MEMORY_PROFILES_OUTLINE.md
│       ├── EP05_LAUNCH_TRAJECTORY_OUTLINE.md
│       └── EP06_WINTER_CONSTANTS_OUTLINE.md
├── research/                      # Historical, demographic, and narrative studies
│   └── narrative/
└── tests/                         # Automated narrative integrity test suite
    ├── parser.py                  # Metadata, date, clue, and thread extractor
    ├── run_story_tests.py         # Test runner
    ├── test_backpropagation_clues.py # Validates prop genesis strictly precedes payoff
    ├── test_character_introductions.py # Validates gradual introduction order against EVENT_REGISTRY
    ├── test_chronology.py         # Validates date parsing, weekdays and nondecreasing order
    ├── test_event_registry_alignment.py # Aligns event IDs, dates, episode windows and document refs
    ├── test_ep03_technical_and_continuity.py # EP03 technical, source-memory and continuity regressions
    ├── test_season_1_decision_consistency.py # Cross-episode grade, release and status guardrails
    ├── test_parallel_plots.py     # Checks declared thread counts and persistence indicators
    ├── test_prop_clue_date_ordering.py # Validates dated genesis/payoff ordering
    ├── test_world_difference_registry.py # Validates AU differences, cross-references and draft wording
    ├── test_multi_season_chronology.py # Validates dates, ages, t-scale and SSOT domains
    ├── test_narrative_quality_contracts.py # Protects narrative agency standards and their documentation
    └── test_prose_drafts.py       # Checks draft structure, dialogue markers and banned phrases
```

---

## 3. Automated Integrity Test Suite (`tests/`)

Deterministic consistency checks for the outlines, drafts and registries run through Python:

```bash
python tests/run_story_tests.py
```

The suite currently provides **regression guardrails**, not automated literary judgement:

1. **Chronology:** Parses registry dates and outline windows, checks Gregorian weekdays, and rejects backwards ordering. Ordering is nondecreasing, not necessarily strictly increasing.
2. **Event registry alignment:** Checks unique/contiguous event IDs, valid date intervals, event-to-episode window containment, exact hidden event anchors in the primary outline (including both dates), and that every declared dependent filename resolves to exactly one file. Malformed event rows and invalid Gregorian dates are reported rather than silently skipped.
3. **Props and clues:** Checks episode-level genesis/payoff ordering, explicit date ordering (including within one episode), textual ID presence, and non-empty background notes. Abbreviated `DD/MM` dates currently inherit 2009.
4. **Character introductions:** Derives first-contact episodes from registry participants, excluding events marked `parallel`. Premature-contact detection uses text patterns; relationship continuity currently checks name presence, not the quality of interactions.
5. **Parallel plots:** Checks declared thread counts, keyword-based participation heuristics, and persistence indicators. It does not understand whether a subplot has meaningful agency or consequences.
6. **Prose drafts:** Checks for a matching outline, dialogue markers, and a fixed list of prohibited phrases. It does not verify American English, voice, POV, naturalness, pacing, or literary quality.
7. **Parallel-world canon:** Checks the foundational WD entries, metadata, dependent-document markers, episode-source references and selected forbidden broadcast wording. It does not semantically understand every scene or prove complete narrative consistency.

---

## 4. Current State

* **Phase 1 — Season 1 Foundation & Active Drafting:**
  * **Episode 1 ("Before and After"):** Working prose draft in English, approximately 7,600 words; below the 10,000–14,000+ target ([EP01_DRAFT.md](episodes/season-1/EP01_DRAFT.md)).
  * **Episode 2 ("Finish the Game"):** Working prose draft in English, approximately 4,400 words; below the 10,000–14,000+ target ([EP02_DRAFT.md](episodes/season-1/EP02_DRAFT.md)).
  * **Episode 3 ("Vector Trajectories and Street Physics"):** Structural prose draft ([EP03_DRAFT.md](episodes/season-1/EP03_DRAFT.md)); approximately 8,400 words, below the outline's 10,000–14,000+ target. It has had targeted technical/source-continuity corrections but is not final prose.
  * **Episodes 4 to 6:** Detailed outlines completed with multi-plot concurrency graphs and editorial cutaways.
  * **Episodes 7 to 12:** Present only as season-arc summaries; individual outlines, event-registry coverage and drafts remain to be written.
  * **Season-wide decisions and open issues:** See [SEASON_1_DECISION_AND_STATUS_REGISTER.md](canon/narrative/SEASON_1_DECISION_AND_STATUS_REGISTER.md).
