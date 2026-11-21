# Decision Log — Story, Naming and Causal Method

Status: AUTHORITATIVE PROVENANCE LOG
Updated: 2026-11-21

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
- **Reassessment (2026-11-21): RETAINED, NARROWED IN PRACTICE.** Randomization is useful for ordinary, low-stakes, underdetermined choices after plausibility and continuity filters. It is not a general story generator and must not decide emotionally or causally consequential choices. The author remains the final authority.
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
- **Reassessment (2026-11-21): RETAINED.** The method is stronger than choosing only top-down or only linearly: the directions solve different problems. Its recursive anchors are planning aids, not a mathematical schedule; forward construction and regression remain the test of whether a transition is earned.
- **Alternatives:** write the whole story only top-down (risks schematic scenes); write only linearly without an end architecture (risks drift); backpropagation without forward regression (risks pasted hints and new contradictions). The hybrid explicitly mitigates all three.
- **Dependencies:** story development workflow, scene/episode audits, timeline, decision/state ledger and all episode drafting.
- **Revisit trigger:** use actual drafts and post-episode/season continuity findings to improve the process.

## DEC-007 — Repository transparency and disclaimer

- **Date:** 2026-10-12.
- **Question:** is a private repository necessary for a fanfic planning repository?
- **Current result:** recommend making `Siuo-Player/escrita` public if the author is comfortable sharing all current and future outlines, research notes, branches, issues and Actions logs. A disclaimer is appropriate for clarity but does not grant rights or guarantee legal clearance.
- **Validation:** GitHub documents that a public repository is visible to everyone and can be forked, and that Actions history/logs become public. The U.S. Copyright Office describes preparing derivative works as an exclusive right subject to statutory limitations and says fair use is a case-specific analysis.
- **Sources:** [GitHub — setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility); [U.S. Copyright Office — derivative-work rights](https://www.copyright.gov/eco/help-limitation.html); [U.S. Copyright Office — Fair Use Index](https://copyright.gov/fair-use/).
- **Reassessment (2026-11-21): RECLASSIFIED AS ADMINISTRATIVE GUIDANCE, NOT STORY CANON.** The privacy/security and copyright caveats remain useful if repository visibility is reconsidered; this entry does not decide any fictional event, character or story premise.
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
- **Validation:** combines visual/physical blocking (movement, prop interaction, active pauses, comedic/dramatic timing) with viewpoint-sensitive narration. Focalisation changes what the viewpoint character notices, interprets, fears, values and chooses to say; no fixed caricature, catchphrase or stylistic gimmick is imposed on a character.
- **Reassessment (2026-11-21): RETAINED WITH A CLARIFICATION.** Theatrical staging and viewpoint-sensitive prose remain, but character voices must emerge from context, intention and current relationships rather than a rigid archetype. POV changes remain selective and must earn their place.
- **Dependencies:** `canon/narrative/MODERN_PROSE_AND_THEATRICAL_STYLE.md`, `episodes/season-1/EP*_DRAFT.md`, ai-memory (`decisions/theatrical-chameleonic-prose-style.md`).

## DEC-010 — Multi-plot concurrency and director's cutting table

- **Date:** 2026-11-19.
- **Question:** how are parallel plots organized and presented to the reader?
- **Current result:** **Time-bar concurrency mapping ($x \to y$) + Director's editorial cutting table**.
- **Status:** USER-LOCKED.
- **Method:** explicit user instruction («usar gráficos de tempo com barras de x a y para plotar os plots num gráfico e ver se eles ficam em paralelo... servimos como editores/diretores do que aparece, quando, do fluxo da cena»).
- **Validation:** maintains at least three meaningful concurrent threads per episode, visualizes their date ranges with timeline bars, and makes deliberate editorial decisions about scene duration, pacing, selective POV allocation and information disclosure. “Concurrent” means the threads continue to exist during overlapping story time; it does not mean every scene must show them all.
- **Reassessment (2026-11-21): RETAINED WITH A QUALITY GATE.** A thread counts only when it has an objective, obstacle, choice and consequence. Never invent a weak subplot or cutaway merely to reach a number; no equal page-time or per-scene quota applies.
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
- **Current result:** thirty agents require 435 unique **unordered** pair checks per frame (26,100 per second at 60 FPS), a reasonable initial demonstration rather than evidence that the 600 MHz CPU is saturated. The spatial grid is reused to support the broader architecture and the already established 200-agent stress case, which would require 19,900 unique unordered pairs per frame (1.194 million per second at 60 FPS). A directed per-agent neighbour loop that processes each relationship twice would perform 870 and 39,800 comparisons respectively. A uniform grid reduces typical candidate counts but does not eliminate quadratic worst-case clustering.
- **Status:** TECHNICAL/NARRATIVE CONSISTENCY RULE; arithmetic is deterministic.
- **Reason:** the previous outline overstated the cost of thirty agents and made the spatial grid appear necessary for an implausibly small demonstration.
- **Dependencies:** `EP06_WINTER_CONSTANTS_OUTLINE.md`, `NATHAN_FIRST_MOBILE_GAME.md`, `EP03_DRAFT.md`.
- **Reassessment (2026-11-21): RETAINED; COUNTING CONVENTION MADE EXPLICIT.** The arithmetic is for unique unordered pairs counted once; do not compare it with a directed loop's twice-counted neighbour visits as though the units were identical.
- **Revisit trigger:** a changed agent count, update rate, perception radius or measured device profile; update the arithmetic and test together.

## DEC-015 — Place final grade results after the 2009–10 instructional year

- **Date:** 2026-11-20.
- **Question:** when can Nathan and Alex receive final grade results and move to the next school year?
- **Current result:** the EP11 window ending 20 May is too early for final year-end results. The results and different grade transitions belong in EP12, after the last instructional day of the school calendar they attend. EP12's working window is extended to 25 June 2010 to cover the approved LAUSD single-track baseline.
- **Status:** ESTABLISHED CHRONOLOGY CORRECTION; the exact school calendar variant and ceremony date remain unresolved.
- **Reason:** the LAUSD board-approved 2009–10 single-track calendar lists 24 June as the last day of instruction and 25 June as a pupil-free day. A contemporaneous administrators' report dated 12 April 2010 describes subsequent revisions, with 18 June as the final day for traditional-calendar schools and 21 June for schools using 8 February as a pupil-free day. Neither source supports final results by 20 May.
- **Dependencies:** `SEASON_1_ARC_PLAN.md`, `SEASON_1_CONTINUITY.md`, `SEASON_1_DECISION_AND_STATUS_REGISTER.md`, EP11/EP12 outlines and any Season 2 opening.
- **Reassessment (2026-11-21): RETAINED AS A PLANNING WINDOW, NOT A CONFIRMED CEREMONY DATE.** The 25 June EP12 boundary allows the story to cover the end-of-year transition, but the exact school, calendar variant, last instructional day and ceremony remain unconfirmed. Do not stage a school event on a pupil-free day by inference.
- **Revisit trigger:** once Nathan and Alex's actual campus/calendar track is fixed; record the exact last instructional day before assigning the ceremony/results date.


## DEC-016 — Protect character agency and narrative quality across the series

- **Date:** 2026-11-20.
- **Question:** how should the project prevent the protagonist-centred wish-fulfilment patterns identified in comparative fanfiction review, while preserving the author's intended long-term story?
- **Current result:** The **NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md** is the project-wide review standard for character autonomy, narrative causality, romance, technology arcs and literary quality. Nathan must not be universally competent or universally admired; Alex and Haley retain independent goals and decisions; the Dunphy/Pritchett/Tucker ensemble and the Callahans keep relationships and conflicts that do not depend on Nathan; and every meaningful plot thread needs an objective, obstacle, choice and consequence. Technology is treated as lived work under constraints, not a résumé of achievements. The planned Nathan/Alex reconciliation and pregnancy epilogue remain authorial destinations, but cannot override character agency or erase the costs of the path.
- **Status:** PROJECT-WIDE NARRATIVE QUALITY STANDARD. This is a planning and review contract, not a new diegetic fact and not a guarantee of subjective literary quality.
- **Reason:** comparative examples highlighted recurring risks: an overpowered or universally praised OC, a canon character reduced to a romantic reward or therapist, author preference flattening canon characterization, decorative parallel plots, and technical milestones presented without human cost. The existing project scope already required independent lives and recognizable motives; this decision makes those requirements operational across planning and drafting.
- **Dependencies:** `canon/narrative/NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md`, `canon/narrative/SERIES_GLOBAL_ARCHITECTURE.md`, `canon/STORY_SCOPE_AND_PROTAGONIST_DESIGN.md`, `canon/narrative/STORY_DEVELOPMENT_WORKFLOW.md`, `canon/narrative/SEASON_1_ARC_PLAN.md`, `tests/test_narrative_quality_contracts.py`, and all future outlines/drafts materially affected by the standard.
- **Validation:** deterministic tests verify the presence of the standard, its cross-document links and selected planning contracts. **Human review remains mandatory** for voice, humour, characterization, emotional credibility, scene quality and whether the prose actually respects agency.
- **Reassessment (2026-11-21): RETAINED.** The standard protects the ensemble without cancelling the author's intended long-term destinations. A planned reconciliation or pregnancy ending is a direction to develop, not permission to force Alex's consent, growth, career, intimacy or decision.
- **Revisit trigger:** review after each season audit, or whenever the author deliberately changes the central relationship, a major character trajectory, the multi-plot rule or the narrative point of view.


## DEC-017 — Grounded slice of life; reincarnation is the only supernatural exception

- **Date:** 2026-11-21.
- **Question:** which elements from Modern Family reincarnation fanfics may inspire this project, and what is the genre boundary?
- **Current result:** This project is a grounded **slice-of-life** fanfic. **Reincarnation is the only supernatural exception.** Nathan retains continuity of identity and imperfect memories from his previous life; these are the premise's residue, not an extra ability. After rebirth, the world follows ordinary human causality. There are no gacha mechanics, systems, status screens, quests, levels, stat points, skill unlocks, magical gifts, divine interventions, gods, powers, supernatural abilities, precognition or other supernatural mechanisms. All skills and achievements must arise from plausible human aptitude, study, practice, experience, resources and opportunity.
- **Status:** USER-LOCKED GENRE AND WORLD RULE.
- **Inspiration boundaries:**
  - **Modern Family: Green Sun:** may be studied for its 2009 neighbour premise, slow-burn intention and music as an ordinary interest. Apollo, the divine system, godlike voice, mastery of every instrument, perfect musical recall and all supernatural gifts are explicitly excluded.
  - **Re:Life With Karmic Gacha (Modern Family):** may be studied for family bonding, everyday scenes and gradual relationship development. Karmic Gacha, system mechanics, rewards and shounen escalation are explicitly excluded.
  - **Reincarnated into Modern Family:** comparator for slow pacing, natural relationship-building and close protagonist viewpoint.
  - **Modern Family: Adrian Delgado:** comparator for limited show memories, slice-of-life framing and the no-cheats intention.
  - **Modern Family: The Singer:** comparator for a rebirth premise that explicitly excludes additional superpowers; its celebrity/music trajectory, accelerated romance and crossover are not project canon.
  - **Modern Family: New Life:** comparator for family integration and everyday interaction; its celebrity trajectory, adoption changes and planned crossovers are not project canon.
- **Reason:** the author explicitly clarified that these works are inspirations, not permission to import their systems or powers. The story should remain about the ordinary life Nathan builds after rebirth, including school, family, friendship, romance, work, money, health, interests, technology and consequences.
- **Dependencies:** `canon/narrative/NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md`, `canon/STORY_SCOPE_AND_PROTAGONIST_DESIGN.md`, `canon/narrative/SERIES_GLOBAL_ARCHITECTURE.md`, `canon/narrative/STORY_DEVELOPMENT_WORKFLOW.md`, `tests/test_narrative_quality_contracts.py`, and all future outlines/drafts.
- **Revisit trigger:** only an explicit author decision to change the genre or introduce another supernatural mechanism. Do not infer permission from an inspiration, tag, review or reader suggestion.


## Historical decision review — 2026-11-21

The older decisions were reviewed against the latest story premise, dated event records and the quality/agency standard.

| Decision | Review result |
|---|---|
| DEC-001–002 | **Keep.** Nathan Callahan remains author-locked; no reason to reopen either name. |
| DEC-003–004 | **Keep as WORKING only.** Maxwell, Clifford and Heather remain useful names, but the random method does not make them author-locked. |
| DEC-005 | **Keep, narrow.** Constrained randomness is for low-stakes options, not major plot or character decisions. |
| DEC-006 | **Keep.** Top-down architecture, forward causality and backward setup review complement each other; do not impose rigid mathematical spacing. |
| DEC-007 | **Reclassify.** Repository visibility/copyright notes are administrative guidance, not story canon. |
| DEC-008 | **Keep.** Draft prose and dialogue remain American English appropriate to the 2009 setting. |
| DEC-009 | **Keep, refine.** Theatrical staging and viewpoint-sensitive narration remain; fixed character caricatures do not. |
| DEC-010 | **Keep, refine.** At least three meaningful concurrent threads; no forced cutaways, equal allocation or per-scene quota. |
| DEC-011–013 | **Keep.** The grade separation, public-release ladder and allocation/navigation design correction remain the more coherent solutions. |
| DEC-014 | **Keep, clarify units.** Pair counts refer to unique unordered pairs, counted once. |
| DEC-015 | **Keep as a time envelope.** The actual school-calendar variant and ceremony date remain open. |
| DEC-016–017 | **Keep.** Character agency and grounded slice-of-life boundaries remain project-wide constraints. |
| DEC-018–020 | **New clarifications.** Organic introductions, fallible memory and document authority are now explicit. |

A decision's presence in this log records provenance and status; it does not turn a working proposal into immutable canon.

## DEC-018 — Organic family introductions; retire the pre-Pilot contact quota

- **Date:** 2026-11-21.
- **Question:** must at least four members of the Dunphy/Pritchett/Tucker family know Nathan by the 23 September 2009 Pilot-memory anchor?
- **Current result:** **No.** The former four-contact target is retired. Alex is Nathan's first meaningful school connection, with their first conversation on 18 September; Phil's first meeting is 28 September; Claire's is 10 October; Luke's is 22 October. Other introductions follow the event and season plans.
- **Status:** EDITORIAL CONTINUITY RESOLUTION; replaces an earlier WORKING GOAL, not an author-locked premise.
- **Reason:** the quota was not supported by the dated event registry and encouraged artificial introductions in the opening. The current slower sequence gives each encounter a distinct cause and lets relationships develop at a believable pace.
- **Dependencies:** canon/characters/NATHAN_CALLAHAN.md; canon/STORY_DECISIONS_TO_MAKE.md; canon/narrative/EVENT_REGISTRY.md; canon/narrative/SEASON_1_ARC_PLAN.md; EP01–EP03 outlines and drafts.
- **Revisit trigger:** only if a future scene earns an earlier meeting for a character-specific reason. There is no replacement numerical target.

## DEC-019 — Previous-life memories are human, selective and fallible

- **Date:** 2026-11-21.
- **Question:** does Nathan possess eidetic or effectively perfect memory of the programme and future events?
- **Current result:** **No.** Nathan has ordinary human recollections from his previous life. Repeated viewing and emotional significance can make some scenes familiar or vivid, but he can forget, conflate or misremember details, dates, order, wording and causes. He does not have eidetic storage, a searchable memory interface, guaranteed exact recall, or knowledge of private/off-screen events. Memory accuracy and the reliability of predicting the altered world are separate uncertainties.
- **Status:** USER-LOCKED PREMISE CLARIFICATION, consistent with DEC-017.
- **Reason:** an eidetic-memory premise would create a de facto additional power and contradict the grounded slice-of-life constraint. Fallible recollection also gives the butterfly effect a human, believable epistemic limit.
- **Dependencies:** canon/characters/NATHAN_CALLAHAN.md; canon/narrative/FOREKNOWLEDGE_INTERVENTION_POLICY.md; canon/STORY_DECISIONS_TO_MAKE.md; canon/STORY_SCOPE_AND_PROTAGONIST_DESIGN.md; canon/timeline/MULTI_SEASON_CHRONOLOGY_MAP.md; canon/narrative/OPENWRITE_CODEX_SEED.md; all outlines and drafts that use foreknowledge.
- **Revisit trigger:** only if the author explicitly changes the reincarnation/memory premise. Do not infer such a change from a fanfic inspiration.

## DEC-020 — Canonical document ownership and precedence

- **Date:** 2026-11-21.
- **Question:** how do we keep the repository's documents on the same story version without maintaining competing copies of every fact?
- **Current result:** the Story Bible is the concise, current snapshot and navigation map; specialist sources remain authoritative in their own domains. The Decision Log records provenance, status, alternatives and revisions. The World Difference Registry defines world-level differences; the Event Registry defines dated events and persistent changes; the Multi-Season Chronology Map defines ages, dates, school years and calendar dependencies; Series Global Architecture defines long-form dramatic arcs; character profiles define character-specific details; season/episode plans define scoped story structure; prose drafts remain WORKING until reviewed against those sources.
- **Status:** PROJECT-WIDE DOCUMENTATION RULE adopted during the 2026-11-21 audit.
- **Reason:** several files used the term “SSOT” for different kinds of truth, creating accidental precedence conflicts. Authority must be domain-specific and explicit; README and Story Bible summaries do not silently override specialist records.
- **Dependencies:** README.md; canon/STORY_BIBLE.md; canon/narrative/SEASON_1_DECISION_AND_STATUS_REGISTER.md; and all canon sources listed above.
- **Revisit trigger:** when the repository structure changes enough that an authority domain or owner needs reassignment.

## Change protocol

When a decision is changed:
1. add or amend its decision entry, preserving the previous result and reason;
2. update the source-of-truth registry/profile;
3. find all dependent paths and cross-references in Git and every open planning PR;
4. change the dependent documents together in a reviewed branch/PR;
5. record the validation and known remaining conflicts;
6. do not claim complete propagation until the updated tree has been searched and the key paths re-read.
