# Decision Log — Story, Naming and Causal Method

Status: AUTHORITATIVE PROVENANCE LOG
Updated: 2026-10-12

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

## Change protocol

When a decision is changed:
1. add or amend its decision entry, preserving the previous result and reason;
2. update the source-of-truth registry/profile;
3. find all dependent paths and cross-references in Git and every open planning PR;
4. change the dependent documents together in a reviewed branch/PR;
5. record the validation and known remaining conflicts;
6. do not claim complete propagation until the updated tree has been searched and the key paths re-read.


## DEC-008 — First supporting-cast pass for football and lead-character circles

- **Date:** 2026-10-12.
- **Question:** how to stop scenes from inventing disposable teammates/friends and make brief later interactions causally coherent?
- **Current result:** create two distinct football rosters (Nathan's Seattle team and the Southern California team) and stable social circles for Alex, Haley and Claire. Give every named person an independent immediate goal, behavioral tendencies, relationship context and recent-past state.
- **Status:** USER-REQUESTED RULE; names and invented biographies remain WORKING.
- **Method:** define narrative function/position before selecting names; draw given names reproducibly from SSA decade tables; assign surnames from a frozen candidate pool. Full pools and selections are in [Cast Naming Draw Audit](characters/CAST_NAMING_DRAW_AUDIT.md).
- **Validation:** first-name cohorts and ranks are recorded. Surname Census ranks remain pending, so no new surname is author-locked and no ethnicity is inferred.
- **Dependencies:** Episodes 1–2 football scenes, social scenes around Alex/Haley/Claire, schedules, dialogue, attendance/minutes, relationships and scene-state headers.
- **Revisit trigger:** author dislikes a name/character, demographic verification contradicts suitability, or draft evidence shows a role is redundant.

## DEC-009 — Life-to-scene continuity is mandatory

- **Date:** 2026-10-12.
- **Question:** how to prevent characters forgetting established facts, motives, fears, skills, objects or recent exchanges?
- **Current result:** every speaking or causally active individual must have a state snapshot for the exact scene date; the previous days/weeks must be documented for all active characters. Background detail remains mostly invisible unless it naturally improves the prose.
- **Status:** USER-REQUESTED PROJECT RULE.
- **Method:** scene-state header + persistent character profile + recent-past timeline + forward state update + backpropagation and forward-regression pass. Unknowns are explicitly marked UNKNOWN, not treated as absence.
- **Validation:** this operationalizes the established causal narrative model for knowledge, capabilities, possessions, health, obligations, relationships and off-page schedules.
- **Limit:** a standard reduces omissions; it cannot guarantee that a scene is good by itself. Drafts must be audited and the process improved when failures recur.
- **Dependencies:** every episode scene and every significant character/prop/skill change.
- **Revisit trigger:** the standard proves too cumbersome; reduce fields only if its causal protections remain.

## DEC-010 — Protagonist knowledge and skill ledger

- **Date:** 2026-10-12.
- **Question:** how to make Nathan's established abilities usable without displaying artificial levels in the story?
- **Current result:** maintain a private, dated ledger distinguishing factual knowledge, practical skill, retrieval, confidence, willingness to act and possibly wrong beliefs. Use bounded internal levels only to guide consistency.
- **Status:** USER-REQUESTED PROJECT RULE; individual skill ratings are WORKING estimates.
- **Method:** start from the character profile, record a baseline and update only when learning, practice, injury, disuse, new evidence or a meaningful choice changes the state. Check whether a known capability would solve the problem before writing a less effective choice.
- **Validation:** reflects Nathan's domain-specific academic/technical strength, soccer and physical training, social hesitation, arts weaknesses and imperfect access to future-world memories. It does not make him omniscient.
- **Open issue:** source profile and Episode 1 currently conflict about whether 7 September is already Nathan's thirteenth birthday or whether he is still about two weeks away; see DEC-012.
- **Dependencies:** Nathan's actions, mobile-game project, football, school scenes, social decisions and later scenes relying on previous-life knowledge.
- **Revisit trigger:** a drafted scene contradicts a baseline rating or evidence establishes a more precise ability.

## DEC-011 — Episode passing can revise the top-down relationship plan

- **Date:** 2026-10-12.
- **Question:** how to keep long-range architecture from forcing an unnatural romance or emotional timetable?
- **Current result:** continue both modes in parallel: recursively plan the long series, while writing and evaluating opening episodes in chronological causal detail. The early drafts test pacing. There is no fixed decision that Nathan and Alex must begin dating in Year 2.
- **Status:** USER-REQUESTED PROJECT RULE.
- **Method:** keep the current first-season friendship proposal as a hypothesis; assess the density, quality and emotional consequence of interactions in Episodes 1–2 and a small sample of Episode 3. Backpropagate setup where later states have earned it, then read forward to check revisions remain natural.
- **Validation:** preserves top-down anchors without turning them into unchangeable appointments. Relationship timing follows accumulated experience and scene quality rather than elapsed calendar alone.
- **Dependencies:** Season 1 relationship pacing, series/season anchors, outlines and later relationship payoffs.
- **Revisit trigger:** prose shows a faster/slower pace would be more believable; update the plan and every affected setup/payoff.

## DEC-012 — Open continuity conflict: Nathan's age/birthday

- **Date discovered:** 2026-10-12.
- **Conflict:** the opening outlines and profile use 7 September 2009 as Nathan's birthday, while the reincarnation passage says he begins life at twelve roughly two weeks before turning thirteen. These cannot all be true at once.
- **Status:** OPEN / must resolve before prose locks the birthday scene.
- **Why not silently fix it:** the opening date and birthday have been central planning anchors, and the author previously indicated that 6 or 8 September could be considered if needed. Preserve the conflict until the surrounding chronology is reconciled intentionally.
- **Immediate guardrail:** use the calendar fact that 7 September 2009 is Labor Day; do not schedule normal school or football training that day. A birthday scene must not call Nathan thirteen if the age choice remains unresolved.
- **Resolution options:** (A) birthday on 7 September and amend the "two weeks before" passage; (B) keep the two-weeks-before premise and move the birthday while preserving the opening start; (C) choose another date after checking episode and school chronology.
- **Dependencies:** Nathan's age, birthday episode, school grade, physical comparison with peers, family dialogue, name-cohort assumptions and both opening outlines.
- **Revisit trigger:** before Episode 1 prose is drafted.
