# escrita — A Modern Family Parallel Fiction Project

An episodic literary fiction novel set in the *Modern Family* universe, engineered with period-accurate 2009 research, strict chronological continuity, and multi-threaded parallel causal architecture.

---

## 1. Project Overview & Premise

* **Protagonist:** **Nathan Callahan** (turns 13 on September 7, 2009 in Seattle; relocates to Cheviot Hills, Los Angeles).
  * **Nature:** Reincarnated with prior viewer memory of *Modern Family*, but strictly epistemically bounded: no telepathy, no omniscience, fragmented directional memory, and conscious awareness of the butterfly effect.
  * **Personality:** Highly disciplined in computer science (C++/OpenGL ES) and athletics (soccer and judo), but guarded, intensely shy, and burdened by a chronic fear of appearing arrogant or presumptuous.
* **The Callahan Family:** Clifford Callahan (father, Senior VP of Engineering Operations) and Heather Callahan (mother, corporate financial consultant). Pragmatic, loving, stable foundation.
* **Independent Core Tech Arc:** Independent development of a custom 2D mobile game in C++ featuring flow-field spatial AI for the newly launched iPhone 3GS (2009).
* **Alex Dunphy Dynamic:** Absolute slow burn. Begins with cautious observation and mutual intellectual respect in 8th grade; deepens into a resilient, unpretentious friendship throughout Season 1.
* **Prose Language:** **American English** (contemporary 2009 setting, authentic character dialogue, and technical precision; see `canon/DECISION_LOG.md` DEC-008).

---

## 2. Repository Structure

```
escrita/
├── .github/
│   └── workflows/
│       └── story-tests.yml        # CI test suite automation on push/PR
├── canon/                         # Single Source of Truth for canon, continuity, and naming
│   ├── characters/                # Character dossiers (Nathan, Alex, Callahans, Maxwell, etc.)
│   ├── narrative/
│   │   ├── EVENT_REGISTRY.md      # Master authoritative event ledger (EVT-xxx)
│   │   ├── SERIES_GLOBAL_ARCHITECTURE.md # Multi-season roadmaps (t=0.0 to t=1.0)
│   │   ├── SEASON_1_ARC_PLAN.md   # Season 1 episode-by-episode master plan (EP01 to EP12)
│   │   ├── PROP_AND_CLUE_REGISTRY.md # Backpropagated props and clues causal ledger
│   │   ├── MODERN_PROSE_AND_THEATRICAL_STYLE.md # Staging, pacing, and chameleonic POV rules
│   │   ├── TECHNICAL_AND_LEGAL_FOUNDATIONS.md  # 2009 Apple Dev terms & 3GS hardware reality
│   │   ├── DIALOGUE_NATURALNESS_STANDARD.md
│   │   └── NARRATIVE_AND_CAUSAL_METHOD.md
│   └── DECISION_LOG.md            # Authoritative decision ledger (DEC-001 through DEC-010)
├── docs/
│   └── memory/                    # ai-memory system documentation, ADRs, and procedures
├── episodes/
│   └── season-1/                  # Outlines and full prose drafts for Season 1
│       ├── EP01_BEFORE_AND_AFTER_OUTLINE.md
│       ├── EP01_DRAFT.md          # Full prose draft (Movements I, II, and III)
│       ├── EP02_FINISH_THE_GAME_OUTLINE.md
│       ├── EP02_DRAFT.md          # Full prose draft (Movements I, II, and III)
│       ├── EP03_VECTOR_TRAJECTORIES_OUTLINE.md
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
    ├── test_chronology.py         # Validates strict monotonic Gregorian progression
    ├── test_parallel_plots.py     # Validates multi-plot concurrency & anti-filler state changes
    └── test_prose_drafts.py       # Validates English dialogue format & absence of sitcom tropes
```

---

## 3. Automated Integrity Test Suite (`tests/`)

Every outline and prose draft is verified by an automated test suite executed via Python:

```bash
python tests/run_story_tests.py
```

The suite validates:
1. **Monotonic Gregorian Chronology:** Dates advance strictly forward and match the real 2009 calendar days of the week.
2. **Backpropagation & Prop Continuity:** Every prop or clue in `PROP_AND_CLUE_REGISTRY.md` has its genesis documented prior to its payoff episode and appears in the relevant files.
3. **Single Source of Truth Event Alignment:** Character introductions and key milestones match `canon/narrative/EVENT_REGISTRY.md`.
4. **Anti-Filler & Multi-Thread Concurrency:** Every episode maintains concurrent active threads with non-solo character interactions and permanent state changes.
5. **Prose Integrity:** Drafts are authored in English, formatted with standard dialogue, and free of artificial fourth-wall breaks or canned clichés.

---

## 4. Current State

* **Phase 1 — Season 1 Foundation & Active Drafting:**
  * **Episode 1 ("Before and After"):** Full prose draft completed in English ([EP01_DRAFT.md](episodes/season-1/EP01_DRAFT.md)).
  * **Episode 2 ("Finish the Game"):** Full prose draft completed in English ([EP02_DRAFT.md](episodes/season-1/EP02_DRAFT.md)).
  * **Episodes 3 to 6:** Detailed outlines completed with multi-plot concurrency graphs and editorial cutaways.
  * **Episodes 7 to 12:** Season 1 second semester arc mapped in `canon/narrative/SEASON_1_ARC_PLAN.md`.
