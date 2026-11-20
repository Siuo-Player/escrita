# Decision Log — Story, Naming and Causal Method

Status: AUTHORITATIVE PROVENANCE LOG
Updated: 2026-11-20

This file stores **what was decided, how the current answer was validated, and what remains revisable**. Consult it with the Character Name Registry, the story-decision file, the relevant character profile, timeline and any open PR before asking the author a question. Do not treat an assistant-generated suggestion as author approval.

## DEC-001 — Protagonist's given name

- **Date:** historical decision, reconfirmed by the naming registry on 2026-10-12.
- **Question:** what should the reincarnated protagonist be called?
- **Current result:** **Nathan**.
- **Status:** USER-LOCKED.
- **Alternatives/history:** Ethan Brooks was suggested earlier and rejected by the author as an overused fan-fiction-style choice.
- **Method:** explicit author choice, not frequency ranking or randomization.
- **Validation:** no further statistical test overrides the author's preference.
- **Revisit trigger:** only if the author explicitly asks to rename him.
- **Dependencies:** all character, episode, series and OpenWrite references.

## DEC-002 — Protagonist's family surname

- **Date:** 2026-10-12.
- **Question:** which surname should replace the assistant's provisional 'Pierce'?
- **Prior state:** Pierce appeared across the working documents but had not been explicitly chosen by the author. It was a placeholder, not a locked decision.
- **Candidate-generation method:** used U.S. Census surname frequency data to avoid defaulting to the most ubiquitous surnames. Seed `687708412` was reused for a reproducible shuffle of the frozen input pool `Whitaker (#610), Callahan (#682), Ellison (#829), Gentry (#821)`. The resulting order was `Gentry, Callahan, Ellison, Whitaker`; the first three were offered as the protagonist's shortlist and Whitaker was reserved for the football peer. The ordered shortlist was:
  1. Gentry — 2020 U.S. Census surname rank 821.
  2. Callahan — rank 682.
  3. Ellison — rank 829.
- **Source:** [U.S. Census Bureau — 2020 Census names data](https://www.census.gov/topics/population/genealogy/data/2020_names.html); rank cross-checks are linked from the Character Name Registry.
- **Current result:** **Nathan Callahan**.
- **Status:** USER-LOCKED as of 2026-10-12, explicitly selected by the author from the generated shortlist.
- **Validation:** Callahan came from the prefiltered plausible U.S. surname pool and is not duplicated by Maxwell Whitaker. The author's preference is the final selection criterion. The random draw generated options; it did not choose over the author.
- **What this does not establish:** no Irish ancestry, religion or other cultural biography is inferred solely from the surname. Such background must be justified separately if it ever matters.
- **Dependencies:** the family members share Callahan as their current family surname unless a separately documented family/legal naming exception is introduced; update character file paths, titles, README, outlines, master plan, timeline, OpenWrite seed and internal links together.
- **Previous alternative:** Pierce is now RETIRED as the protagonist's surname; preserve it only in this decision history or an explicit migration note.

## DEC-003 — Recurring football peer

- **Date:** 2026-10-12.
- **Question:** how to name the recurring teammate without defaulting to familiar model-generated names?
- **Current result:** **Maxwell Whitaker**.
- **Status:** WORKING; author may revise.
- **Prior alternative:** Jordan Reyes was a provisional assistant choice and is RETIRED.
- **Method:** seeded draw from a filtered SSA U.S. 1990s male name pool; seed `687708412`, pool size 95, zero-based index 58, selecting Maxwell. Surname pool was filtered and shuffled with the same random stream; Whitaker ranked 610 in 2020 Census-derived surname data and did not duplicate the protagonist's candidate.
- **Validation:** name frequency and plausibility checked; character function and independent goal are defined separately in `canon/characters/MAXWELL_WHITAKER.md`.
- **Limit:** this is a working name, not canon. Do not invent ethnicity or biography solely from it.
- **Source/pool:** `canon/characters/CHARACTER_NAME_REGISTRY.md`.

## DEC-004 — Parents' working given names

- **Date:** 2026-10-12.
- **Question:** how to avoid keeping assistant-generated 'David' and 'Melissa' merely because they had already propagated through files?
- **Current result:** **Clifford** (father) and **Heather** (mother).
- **Status:** WORKING / randomly selected; revisit if the author dislikes them or character design later points to a better fit.
- **Method:** seed `637376247`, frozen candidate pools of 97 male and 97 female names from the U.S. Social Security Administration's 1960s decade tables after duplicate/canon/rejection filters. Male zero-based index 56 selected Clifford (SSA 1960s male rank 159); female zero-based index 25 selected Heather (rank 127).
- **Sources and exact pools:** [SSA — Top names of the 1960s](https://www.ssa.gov/OACT/babynames/decades/names1960s.html); exact pools and method in the Character Name Registry.
- **Validation:** name selection is period-informed; existing parental roles, careers, personality and relocation cause remain unchanged. The random choice does not justify inventing extra family history.
- **Dependencies:** both share the Callahan family surname. A future change must be migrated through character records, timeline, scene outlines, schedules and Codex seed.

## DEC-005 — How ordinary creative decisions are made

- **Date:** 2026-10-12.
- **Question:** how to reduce predictable, high-probability default suggestions while preserving coherence?
- **Current result:** controlled randomization is preferred for ordinary, underdetermined choices among equally reasonable candidates.
- **Status:** USER-REQUESTED PROJECT RULE.
- **Validation method:** candidate pool must first be evidence-based or constrained by canon, chronology, character and culture; draw seed and exact candidate order are then recorded; final choice is tested against causal consequences. Author preference overrides the draw. Do not randomize facts, canon, or major causally loaded events.
- **Alternatives:** model-default selection alone is rejected as insufficiently diverse; unconstrained randomness is rejected because it can produce implausible or causally damaging answers.
- **Dependencies:** all future original naming, optional scene details and other underdetermined choices should follow `canon/narrative/NARRATIVE_AND_CAUSAL_METHOD.md`.
- **Revisit trigger:** if the process creates arbitrary, implausible or repetitive story outcomes, revise the candidate filters and validation—not hide the failure or reroll until a preferred answer appears.

## DEC-006 — Narrative planning and causal construction

- **Date:** 2026-10-12.
- **Question:** how to combine whole-series purpose with causal detail and prevent contradictions?
- **Current result:** dual-track process:
  - recursive top-down architecture: define beginning and end, then midpoint, quarters and finer nested anchors;
  - forward linear causal construction: develop actual scenes/state changes in chronological order, including independent subplots;
  - episode/season backpropagation: trace later states backwards to find missing setup and then re-read forward to catch regressions.
- **Status:** USER-REQUESTED PROJECT RULE; empirical effectiveness remains to be tested on drafts.
- **Validation:** internally consistent with existing continuity, persistent-state, parallel-plot and backpropagation principles. It avoids forcing every small detail into the top-down outline while preserving cause/effect at scene level.
- **Alternatives:** write the whole story only top-down (risks schematic scenes); write only linearly without an end architecture (risks drift); backpropagation without forward regression (risks pasted hints and new contradictions). The hybrid explicitly mitigates all three.
- **Dependencies:** story development workflow, scene/episode audits, timeline, decision/state ledger and all episode drafting.
- **Revisit trigger:** use actual drafts and post-episode/season continuity findings to improve the process.

## DEC-007 — Repository transparency and disclaimer

- **Date:** 2026-10-12.
- **Question:** is a private repository necessary for a fanfic planning repository?
- **Current result:** recommend making `Siuo-Player/escrita` public if the author is comfortable sharing all current and future outlines, research notes, branches, issues and Actions logs. A disclaimer is appropriate for clarity but does not grant rights or guarantee legal clearance.
- **Validation:** GitHub documents that a public repository is visible to everyone and can be forked, and that Actions history/logs become public. The U.S. Copyright Office describes preparing derivative works as an exclusive right subject to statutory limitations and says fair use is a case-specific analysis.
- **Sources:** [GitHub — setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility); [U.S. Copyright Office — derivative-work rights](https://www.copyright.gov/eco/help-limitation.html); [U.S. Copyright Office — Fair Use Index](https://copyright.gov/fair-use/).
- **Revisit trigger:** before making the repository public, check it for credentials, private information, material not intended to be shared, and Actions logs/artifacts. Do not describe the disclaimer as permission or legal immunity.

## DEC-008 — Prose drafting language: English (American standard)

- **Date:** 2026-11-19.
- **Question:** what language must be used for the novel drafts, prose chapters, and character dialogue?
- **Current result:** **English (American standard, 2009 period-accurate)**.
- **Status:** USER-LOCKED.
- **Method:** explicit user instruction («é tudo em inglês, não traduzas de qualquer jeito, põe tudo em consideração ao fazer a tradução, passado, futuro, cenas planejadas, back storie dos personagens e etc.»).
- **Validation:** setting is Los Angeles, California in 2009 within the canon Modern Family universe; character voices, colloquialisms, comedic rhythm, and technical vocabulary require native English prose.
- **Consequences:** all `EP*_DRAFT.md` files must be authored strictly in English. Existing drafts must be translated/adapted thoroughly with full attention to character psychology, planned arcs, and authentic American dialogue cadence.
- **Dependencies:** `episodes/season-1/EP*_DRAFT.md`, `tests/test_prose_drafts.py`, ai-memory (`decisions/story-language-english.md`).

## DEC-009 — Narrative style: modern theatrical prose and chameleonic POV

- **Date:** 2026-11-19.
- **Question:** what narrative register and perspective techniques govern the prose?
- **Current result:** **Modern contemporary serialized fiction with theatrical staging and chameleonic free indirect discourse**.
- **Status:** USER-LOCKED.
- **Method:** explicit user instruction («usa uma escrita á la fanfics e models modernas, acho um pouco mais baseado em teatro... podes variar um pouco a escrita quando temos povs de personagens»).
- **Validation:** combines visual/physical blocking (movement, prop interaction, active pauses, comedic/dramatic timing) with a narrative voice that adapts its lexical and emotional register to the viewpoint character (Nathan: analytical/understated; Alex: acerbic/intellectually defensive; Phil: bouncy/enthusiastic; Manny: romantic/operatic/baroque; Claire: rapid/pragmatic; Luke: whimsical/kinetic; Jay: gruff/practical).
- **Dependencies:** `canon/narrative/MODERN_PROSE_AND_THEATRICAL_STYLE.md`, `episodes/season-1/EP*_DRAFT.md`, ai-memory (`decisions/theatrical-chameleonic-prose-style.md`).

## DEC-010 — Multi-plot concurrency and director's cutting table

- **Date:** 2026-11-19.
- **Question:** how are parallel plots organized and presented to the reader?
- **Current result:** **Time-bar concurrency mapping ($x \to y$) + Director's editorial cutting table**.
- **Status:** USER-LOCKED.
- **Method:** explicit user instruction («usar gráficos de tempo com barras de x a y para plotar os plots num gráfico e ver se eles ficam em paralelo... servimos como editores/diretores do que aparece, quando, do fluxo da cena»).
- **Validation:** maintains $\ge 3$ simultaneous threads per episode, visualizes them via timeline bars, and makes deliberate directorial decisions on scene duration, pacing, POV allocation, and information disclosure (what is shown vs. what is left in the background).
- **Dependencies:** `canon/narrative/SEASON_1_ARC_PLAN.md`, `brain/.../director_concurrency_matrix_season_1.md`, ai-memory (`concepts/multi-plot-concurrency-and-directors-cut.md`).

## DEC-011 — Preserve the one-grade gap through the end of Season 1

- **Date:** 2026-11-20.
- **Question:** how should the June 2010 school transition respect Nathan's and Alex's established grade levels?
- **Current result:** Nathan remains one school year above Alex. In the 2009–10 year Nathan is in 8th grade and Alex is in 7th. At the end of that year Nathan completes 8th grade and prepares to enter High School; Alex completes 7th grade and advances to 8th grade.
- **Status:** ESTABLISHED CONTINUITY RULE, derived from the pre-existing one-grade separation; this does not authorize skipping or repeating a grade.
- **Reason:** the former EP11/EP12 summary placed both characters in the same 8th-grade honours cohort and described both as graduating middle school together. That contradicted the established grade separation.
- **Dependencies:** `SEASON_1_ARC_PLAN.md`, `STORY_DECISIONS_TO_MAKE.md`, later school calendars and any Season 2 opening material.
- **Revisit trigger:** only if a separately justified school placement or acceleration/repetition event is deliberately written and registered.

## DEC-012 — Separate the game's internal milestone from its public release

- **Date:** 2026-11-20.
- **Question:** how do the October playable milestone, November Apple submission and December launch fit together?
- **Current result:** **15 October 2009** is the internal, end-to-end playable vertical-slice milestone for the first feature set. It is not the public App Store release. The project continues through collision/physics work, memory profiling and release preparation. Clifford, as adult developer-account holder, submits v1.0 to Apple on **18 November 2009**; the app becomes publicly available on the App Store on **3 December 2009** after review.
- **Status:** ESTABLISHED CHRONOLOGY RECONCILIATION, derived from EVT-021 and EVT-025 and the existing Episode 4/5 plans.
- **Reason:** earlier continuity wording called 15 October a "release", which blurred a playable internal build with distribution to customers.
- **Dependencies:** `SEASON_1_CONTINUITY.md`, `NATHAN_FIRST_MOBILE_GAME.md`, `EP02_FINISH_THE_GAME_OUTLINE.md`, `EP04_MEMORY_PROFILES_OUTLINE.md`, `EP05_LAUNCH_TRAJECTORY_OUTLINE.md`, `EVENT_REGISTRY.md`.
- **Revisit trigger:** a deliberate change to any of the three dated milestones; update all dependent documents and event anchors together.

## DEC-013 — Pooling de entidades e buffers, não pesquisa global por frame

- **Date:** 2026-11-20.
- **Question:** what work should the EP04 memory profile attribute to dynamic allocation?
- **Current result:** the bounded object pool targets repeated entity creation/removal and temporary collision-contact records during test resets and level activity. The stable flow field is built once and regenerated only when the map or shared destination requires it; it is not a global path search for every enemy every frame.
- **Status:** TECHNICAL/NARRATIVE CONSISTENCY RULE, derived from the existing flow-field design and the EP03 collision architecture.
- **Reason:** the former EP04 wording claimed that path-search nodes were allocated and freed hundreds of times per frame. That contradicted shared navigation and precomputation.
- **Dependencies:** `EP04_MEMORY_PROFILES_OUTLINE.md`, `NATHAN_FIRST_MOBILE_GAME.md`, `TECHNICAL_AND_LEGAL_FOUNDATIONS.md`.
- **Revisit trigger:** a deliberate redesign of navigation/physics allocation; do not revert to per-frame global path searches without redesigning and profiling that architecture.

## DEC-014 — Keep the 30-agent boids demonstration distinct from the 200-agent scale test

- **Date:** 2026-11-20.
- **Question:** how should the EP06 flocking scene describe pairwise cost on the iPhone 3GS?
- **Current result:** thirty agents require 435 pair checks per frame (26,100 per second at 60 FPS), a reasonable initial demonstration rather than evidence that the 600 MHz CPU is saturated. The spatial grid is reused to support the broader architecture and the already established 200-agent stress case, which would require 19,900 naïve pairs per frame (1.194 million per second at 60 FPS). A uniform grid reduces typical candidate counts but does not eliminate quadratic worst-case clustering.
- **Status:** TECHNICAL/NARRATIVE CONSISTENCY RULE; arithmetic is deterministic.
- **Reason:** the previous outline overstated the cost of thirty agents and made the spatial grid appear necessary for an implausibly small demonstration.
- **Dependencies:** `EP06_WINTER_CONSTANTS_OUTLINE.md`, `NATHAN_FIRST_MOBILE_GAME.md`, `EP03_DRAFT.md`.
- **Revisit trigger:** a changed agent count, update rate, perception radius or measured device profile; update the arithmetic and test together.

## Change protocol

When a decision is changed:
1. add or amend its decision entry, preserving the previous result and reason;
2. update the source-of-truth registry/profile;
3. find all dependent paths and cross-references in Git and every open planning PR;
4. change the dependent documents together in a reviewed branch/PR;
5. record the validation and known remaining conflicts;
6. do not claim complete propagation until the updated tree has been searched and the key paths re-read.
