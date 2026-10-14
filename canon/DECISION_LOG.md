# Decision Log — Story, Naming and Causal Method

Status: AUTHORITATIVE PROVENANCE LOG
Updated: 2026-10-14

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
- **Continuity check (2026-10-13):** Nathan turns thirteen on 7 September 2009; the prior-life transition occurs roughly two weeks earlier, while he is still twelve. These are separate dates, not a contradiction. See DEC-012 for the audit trail.
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

## DEC-012 — Resolved: apparent age/birthday conflict was a false positive

- **Date flagged:** 2026-10-12.
- **Review date:** 2026-10-13.
- **Initial concern:** one passage places the prior-life transition about two weeks before Nathan's thirteenth birthday, while the opening is on that birthday.
- **Validation:** these are different dates/events. Nathan's birthday is 7 September 1996; the story opens on his thirteenth birthday, Monday 7 September 2009. The prior-life transition happens in his twelve-year-old life roughly two weeks before that birthday. Neither passage claims the story opens on the transition date, so the chronology is consistent.
- **Status:** RESOLVED — FALSE POSITIVE; no birthday, opening-date or reincarnation retcon is required.
- **Decision:** retain the established 7 September 2009 opening/birthday. Do not move it merely because it is Labor Day. The calendar affects how the day is staged, not Nathan's age/date.
- **Scene guardrail:** 7 September 2009 is Labor Day. No ordinary school day or scheduled team practice; Nathan may celebrate his birthday, code, do solo conditioning or join an informal pickup/kickabout. The Seattle team's practice/match rhythm resumes on its normal non-holiday dates.
- **Options considered:** moving the birthday to 6/8 September or rewriting the transition timing is unnecessary; those options are rejected for this review because they solve a conflict that does not exist.
- **Dependencies checked:** profile, story-decision file, Nathan's knowledge/skill ledger, Episode 1 opening and football roster guardrails. Their statements now explicitly distinguish the transition date from the opening birthday.
- **Revisit trigger:** only if the author intentionally changes the established birthday/opening date or the reincarnation premise; do not reopen through date-only confusion.


## DEC-013 — Working mobile-game platform/toolchain and test-device path

- **Date:** 2026-10-13.
- **Question:** how can Nathan credibly build and test a C++-logic mobile game targeting 2009 iPhone/iPod touch hardware over the 43-day project cycle, with the first 39 days visible from the story opening?
- **Current working result:** use an Intel Mac running Mac OS X 10.5 Leopard with period-appropriate Xcode 3.1.x / iPhone OS SDK 3.x tooling; use an Objective-C framework layer such as the period-appropriate cocos2d for iPhone, with game/pathfinding/prediction logic in C++ connected through a small Objective-C++ bridge.
- **Working prop:** Nathan already has a second-generation iPod touch from the family before the story opens, plausibly bought/gifted in 2008. It supplies a real, conservative target for on-device tests. Do not introduce it for the first time on the day a test is needed; retain its provenance and OS/build version in the prop/test ledger.
- **Working administrative route:** Clifford, as the adult, handles any required developer-account, signing and provisioning administration with Nathan. Nathan remains the author of the code. This supports private device testing; a public launch is a separate milestone and must come only after technical/playability testing and App Store review.
- **Status:** WORKING / provisional creative-technical decision. The author has not separately locked the exact computer model, point-release SDK or device gift date.
- **Validation method:** compare the requirement against Apple's archived Xcode 3.1 release notes (iPhoneOS SDK cross-development requires an Intel Macintosh), Apple's 2008 announcement of the second-generation iPod touch, and Apple's support page listing its iPhone OS 3.1 documentation. See the technical design file for source links.
- **Alternatives considered:** (A) unspecified Windows-only development is rejected for an actual 2009 iOS build because it lacks the native Apple toolchain; (B) Mac simulator only is insufficient to substantiate real-device performance; (C) modern cross-platform/automated mobile pipelines are anachronistic; (D) immediate public release before private technical and playability testing is rejected; the public-launch sequence is recorded in DEC-014.
- **Causal consequences:** the opening computer setup is a Mac-compatible iOS development environment; device tests require a named target/build and plausible signing route; game logic remains C++ while framework integration may use Objective-C/Objective-C++; a successful simulator test does not automatically count as a successful hardware test.
- **Dependencies checked:** NATHAN_CALLAHAN profile; NATHAN_FIRST_MOBILE_GAME technical design; Episode 1 incoming inventory; Episode 2 old-device test and private playtest. Update them together if the author later selects a different target platform.
- **Revisit trigger:** if later canon establishes a non-Apple platform, a different household computer, a specific device gift/history, or a constraint that makes a real-device build implausible.

## DEC-014 — Public game launch follows technical and peer playability testing

- **Date:** 2026-10-13.
- **Author-confirmed rule:** Nathan does launch the game publicly, but not as soon as it first runs. He tests it technically himself and lets friends/classmates try the gameplay before the public release.
- **Testing sequence:** technical/profile/device checks occur throughout development; Maxwell and one teammate try the playable Mac/simulator build in a short session on 10 October; Wesley performs a final private playtest on Nathan's second-generation iPod touch on 15 October. Nathan incorporates actionable feedback and runs a final regression check before Clifford handles the adult account/submission administration.
- **Submission and release:** submit the candidate for App Store review by **15 October**. A public launch on **23 October 2009** is the current WORKING target, leaving an eight-day review interval. This exact date is a planning choice, not an author-locked date or a guarantee about historical review speed; contemporary reporting in August 2009 quoted Apple's response that 95% of submitted apps were approved within 14 days ([contemporary report](https://techcrunch.com/2009/08/21/apples-response-to-the-fcc-we-didnt-reject-the-google-voice-app-were-still-looking-at-it/)). If later continuity or research warrants a different date, preserve the required order—technical tests, peer playability tests, submission/review, public launch—and propagate the date change.
- **Outcome boundary:** public availability is established; download counts, revenue, reviews, virality, fame and industry recognition remain UNKNOWN until causally shown.
- **Dependencies:** Episode 2 outline and ledger; Season 1 continuity and plot bank; first-game technical design; OpenWrite Codex seed.

## DEC-015 — Author instructions for the chronological continuity repair

- **Date:** 2026-10-13.
- **Scope:** these instructions govern the current chronology/causality repair and any directly dependent follow-up edits.
- **Alex and Nathan's apology/hedging pattern:** preserve the line "You know you don't have to apologize every time you're right" as a potential later line. Do **not** use it when Alex has only just met Nathan. Reserve it for substantially later, after Nathan, the reader and Alex have all witnessed the habit repeatedly and the relationship has earned that level of familiarity. Early scenes should establish the behavior gradually, with no premature diagnosis of his personality.
- **CA-MATH-01:** replace the internal teacher ID with a proper human name, a distinct but plausible personality, a reasonable professional/personal background, and a dated knowledge history. Do this in the profile/registry and dependent episode/timeline documents together. The teacher must know Nathan's programming only after there is an explicit causal route for learning it.
- **Scene chronology and Cece:** use specific clock times (hours and minutes where possible) for relevant school, family and neighborhood events. In particular, establish whether Nathan's encounter with Cece happens before or after the relevant school scene on 14 October. If it happens before, Cece may already be affected by that encounter; if it happens after, she cannot react to it earlier. If neither has happened yet, any visible mood change needs a different, established cause. Never let an emotional consequence precede its trigger.
- **Move/background detail:** deepen the off-page causal background, not just the on-page summary: relocation provider and housing selection, moving cargo versus luggage, school transfer/records/transport, access to the computer and devices, and Heather's employment consequence. Background can remain invisible in prose but must be definite enough to support the scene.
- **Game quality:** the public release should launch without known blocking problems. If technical or peer playability tests find an issue, Nathan fixes it and tests the fix before submission. Do not leave a known critical bug unresolved merely to make the release imperfect; non-blocking polish work may remain only if explicitly distinguished and compatible with the actual build being shipped.
- **Peer testers:** Maxwell and any other test players need fuller, consistent character histories (temperament, household/family context, habits, goals, football role, and what they understand about this particular game). Their feedback must arise from what that person would actually notice and care about, rather than generic placeholder criticism.
- **Programming workload:** do not flag the established rhythm as intrinsically implausible. Nathan's normal days have about **2 focused programming hours**; open/free days can provide up to **8 hours**. When justified by the late-stage workload, Nathan may keep working until **04:00–05:00** during the 12–15 October crunch window; this is permission for an exceptional late night, not a mandatory schedule. If used, update the next day's sleep, fatigue and school/training state rather than letting the late finish have no consequences. The 60–85-hour project budget across roughly six weeks is feasible with this availability. Adjust availability only when specific schoolwork, training, matches, family events, fatigue or personal pressure creates a real conflict; explain the causal trade-off instead of treating long sessions as inherently excessive.
- **Remaining continuity issues:** resolve practical school/club registration, coach/parent permission, transport for social plans, object/access state, and other small causal gaps at the point they become relevant. Do not reopen author-confirmed premises without a direct contradiction.
- **Work method:** make changes in small batches of one or two files. After every batch, re-read the affected documents and run a targeted forward/backward consistency check before starting the next batch. Do not merge PR #11 unless the author explicitly asks.
- **Implementation note:** these are author-confirmed instructions; specific teacher identity/background, exact clock times, the precise public-launch date, and newly devised side-character facts remain WORKING proposals until propagated and checked.

## DEC-016 — Working App Store submission packet for Current

- **Date:** 2026-10-14.
- **Author-confirmed constraint:** Nathan's game is released publicly only after his technical checks, peer playability tests, defect fixes and App Store review. The exact launch date remains a working target of 23 October 2009.
- **Historical reference:** Apple's WWDC 2009 session [Publishing on the App Store](https://nonstrict.eu/wwdcindex/wwdc2009/702/) describes the period's iTunes Connect requirements: app/developer name, description, category, copyright/version, application/support URLs, support email, SKU, age rating, a 57×57 PNG app icon, a 512×512 store icon and at least one screenshot. It identifies the 4+, 9+, 12+ and 17+ rating bands. This is the period-appropriate submission model for the story.
- **Working app identity:** public name **Current**; version **1.0**, final tested build **19**; bundle/App ID **com.cliffordcallahan.current**; internal SKU **CALLAHAN-CURRENT-001**. Treat the bundle ID and SKU as immutable after submission. These values are practical working identifiers, not user-locked branding.
- **Working business choices:** free download; Games category / Puzzle subcategory; English metadata; initial distribution in the U.S. storefront; no advertising, in-app purchases, online service or user accounts. The simple chase/stealth content is provisionally rated **9+** under the 2009 rating bands, subject to the actual content questionnaire.
- **Account and attribution:** Clifford uses an already-active adult developer membership and handles signing, provisioning, iTunes Connect and submission. The developer/seller display name is **Clifford Callahan**. The in-game credit and description clearly state that the game was designed and programmed by **Nathan Callahan**, with Clifford providing account/submission administration. Clifford's existing web presence supplies a minimal support page and a monitored support email; the exact contact strings need not appear in dialogue.
- **Assets and rights:** title screen, game tiles, guards, objective/exit indicators and icons are made for this project from simple original shapes. Sound is generated/simple original tones; no borrowed music, third-party sprite pack or unlicensed font/art is included. Prepare a 57×57 PNG device icon and matching 512×512 store artwork, a simple 320×480 launch image, three genuine screenshots from the final build (title/start, mid-level with guards, objective completed/exit open), a short description, copyright/version, support contacts, age rating and the final signed binary. No screenshots or performance claims may depict a build that was not tested.
- **Store description — working copy:** “A compact single-player stealth puzzle. Read the guards' patrols, find a route through the room, and reach the exit. Built around simple controls and adaptive guard behavior.”
- **Submission gate:** use the final validated version 1.0 build 19 only after BUG-01 through BUG-06 have passing recorded regression evidence on the current build and Wesley's device/playability check has not reopened any blocker. Submit by about 21:30 on 15 October. The working public availability date is 23 October after review. If the review rejects the submission or final testing changes the binary, the publication date moves; do not claim it went public on schedule until approval is an established state.
- **Not implied by launch:** downloads, reviews, sales, virality, press, fame and commercial success remain UNKNOWN until the story gives them causes and observable evidence.
- **Status:** submission requirements above are working continuity decisions for closing the documented gap. Product name, seller name, price, storefront, app identifiers, rating and the exact release date may be revised before prose/publication if the author later chooses differently, but the testing-before-release order remains fixed.
- **Dependencies:** first-game technical design, Episode 2 outline and ledger, Clifford's account-administration role, asset provenance and Season 1 continuity.


## Open continuity audit — Cece chronology (2026-10-14)

The author specified that Cece's state at the relevant school scene must reflect whether the encounter with her occurs before that scene. Before adding the guardrails below, a targeted search across the working Episode 1–2 outlines and scene-state ledgers, season timeline/plot bank, core-character baseline and secondary-social-circles file in the current PR #11 branch, plus the Episode 1–4 outlines and master-plan/plot-bank files in PR #2, found no actual scene or character profile for **Cece/Cecilia**. The only mentions now present are this audit note and the guardrail in Episode 2 Scene 40; they do not establish her identity, the encounter, or its timestamp. Do not silently assume that Cece is DeDe or merge the characters.

In the current Episode 2 ledger, Scene 40 is Wednesday **14 October, 12:20–12:35**, with Alex distracted by an ordinary school assignment before DeDe's later visit; Scene 41 is a separate Nathan/Phil encounter at approximately **20:40–20:50** after the Dunphy dinner. Those timings are internally explicit but do not establish the missing Cece event. Until her intended profile/scene is restored or created, do not give a school scene consequences from an unrecorded encounter. Before prose, record Cece's background, exact event time, what she knows/feels afterward, and any corresponding state change in the affected scene ledger.

This is an unresolved implementation dependency, not a new author decision.



## Author revision instructions — 2026-10-14

These are explicit author directions for the current continuity/revision pass. Apply them unless the author explicitly overrides them. They govern implementation choices; they do not silently promote provisional story facts to canon.

### REV-001 — Reserve Alex's observation about Nathan's apologies

The line **"You know you don't have to apologize every time you're right."** is liked and should be preserved for possible use much later in the story. Do not use it when Alex has only just met Nathan. Save it until both Alex and the reader have witnessed the habit repeatedly across many chapters, so the line is recognition of an established pattern rather than premature insight. Early scenes may show ordinary hesitation or one isolated apology, but must not have Alex diagnose the habit yet.

### REV-002 — Give CA-MATH-01 a complete human profile

Replace the internal-only teacher label with a plausible person's name and build a coherent background: teaching experience, mathematical interests, classroom manner, strengths, flaws, habits, motivations, family/personal context and boundaries of what the teacher knows. Keep the profile proportionate to the story, but detailed enough to make classroom choices and dialogue consistent. The teacher must respond to evidence actually observed and information actually shared by Nathan.

### REV-003 — Use clock times to protect scene causality

Where the order within a day affects what a character knows or feels, record specific local times (hours and minutes), not just a date or vague morning/evening label. In particular, Alex's school state must follow the actual timing of her encounter with Cece if that encounter is established. If it occurs before school, it may affect her later state; if it occurs afterward, it cannot. A school scene may instead be affected by a different, already established cause. Do not invent a causal link or silently equate Cece with another character.

### REV-004 — The game must be release-ready

The game should launch without known blocking or reproducible defects. Any defect Nathan discovers must be corrected and retested before release/submission; do not leave a known launch blocker open and then launch anyway. Non-blocking polish may be consciously deferred, but state why it is non-blocking and preserve the distinction between simulator and physical-device results. If a required fix cannot be completed, the release date must move rather than ignoring the defect.

### REV-005 — Testers need independent lives and personality-consistent feedback

Develop recurring testers' personalities, family/background context, interests, habits, skills, blind spots and reasons for trying the game. Their feedback must arise naturally from those traits and the game's actual mechanics; do not make them interchangeable sources of generic praise or bug reports. Record what each tester notices, misses, misunderstands or enjoys and whether Nathan changes the game in response.

### REV-006 — Program with the established time budget, not an invented pacing problem

Do not treat the earlier estimate of 10–14 focused programming hours per week as a hard limit or use it to manufacture a rhythm problem. On an ordinary/casual day Nathan can use about 2 hours; on a free day he can use up to 8 hours; Friday and weekend sessions may run 4–5 hours per day when appropriate. A few such days can supply roughly 9–15 hours, and 60–85 total hours across six weeks is plausible. Schedule against his actual schoolwork, football/training and personal obligations. Increase or reduce work only when that week's story provides a concrete reason (for example, a match, extra training, school pressure or a personal problem). Do not force late nights; they are possible only when the plot and consequences justify them.

### REV-007 — Audit the remaining gaps instead of assuming they are errors

Resolve genuine contradictions and missing causal steps, but do not label a workable schedule or workload a problem without demonstrating a conflict. Keep changes incremental: each batch should cover one or two closely related issues, followed by a fresh check of adjacent outlines, ledgers, timeline, profiles and cross-references. Track what is fixed, what remains unresolved, and any new inconsistency introduced. The author has authorized these corrections unless explicitly countermanded.
