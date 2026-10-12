# Narrative Architecture and Causal Drafting Method

Status: ESTABLISHED PROJECT METHOD; individual plot decisions remain revisable
Updated: 2026-10-12

## The two directions are complementary, not competing

The series is designed **top-down** and written/causally developed **forward in time**. Backpropagation then checks whether the forward story has earned the states promised by the high-level design.

The top-down model provides destination, meaning, proportionality and long-range setup. The forward causal model provides believable transitions, lived detail, independent character agency and consequences. Neither is allowed to replace the other.

## Track A — recursive top-down architecture

Treat the intended long-form narrative as an interval from (t=0) (opening state) to (t=1) (intended end state).

1. **Endpoints:** define the beginning, the end, and what has fundamentally changed between them. The endpoint is a target state, not a list of mandatory scenes.
2. **Midpoint:** define (t=0.5) as the most important intermediate transformation that connects the opening to the ending.
3. **Quarter points:** use the known endpoints and midpoint to propose (t=0.25) and (t=0.75), then check that each state follows plausibly from its neighbors.
4. **Recursive refinement:** continue subdividing the intervals—(0.125), (0.375), (0.625), (0.875), and so on—only where the story needs another decision layer. Each new point inherits constraints from the nearest established points on both sides.
5. **Nested levels:** perform this at series, season, major arc, episode and sequence level. A point at one level can be an interval at the level below it.

This is a planning technique, not a demand that events land at mathematically equal distances. Emotional change, school calendars, canon anchors and causal dependencies determine actual spacing. If a midpoint does not work, revise the proposed midpoint or the interval; do not fill the gap with arbitrary events just to complete a symmetrical outline.

Each anchor should describe:
- the starting character/world state;
- the desired or unavoidable change;
- why that change matters to the larger story;
- constraints inherited from canon, dates and previous decisions;
- which causal links still need to be built.

## Track B — linear causal construction

Once the major anchors are credible, develop the lived timeline from the beginning forward. The conceptual example is a series divided into 1,000 fragments: work from the first fragment to the next and continue in order until the ending. The exact count is illustrative; do not create 1,000 artificial sections.

For every scene or meaningful fragment, record the smallest useful causal chain:

**prior state → trigger → character perception/knowledge → desire or obligation → choice/action → immediate result → other characters' response → persistent state change.**

A scene must arise from the state that precedes it. The author may know the season midpoint and ending, but characters only act on what they know, want, fear, notice, misunderstand or can reasonably access at that point.

### What makes the story feel lived rather than assembled

- People keep pursuing their own schedules and goals while the protagonist is absent.
- A character can act on a wrong belief if that belief has a traceable origin.
- Practical details persist: possessions have provenance and location, homework and projects take time, a person remembers what was actually said, travel takes time, and relationships accumulate shared history.
- Subplots continue, pause, intersect and resume because of causes—not because each episode needs an equal quota of them.
- New information changes decisions; it does not silently overwrite what was known in an earlier scene.
- The narration may show the reader a causal link before Nathan notices it, but it must not invent a link after the fact without support.
- Not every detail needs to be shown in prose. The continuity model keeps the unshown days coherent so selected scenes can safely skip them.

## The decision/state ledger

For every durable decision or reveal that can affect later scenes, preserve:

| Field | Required content |
|---|---|
| Decision ID / date | Stable reference and date recorded |
| Question | The actual unresolved choice |
| Current result | What is currently established |
| Status | CANON, DERIVED, USER-LOCKED, WORKING, CREATED, INCERTAIN or RETIRED |
| Alternatives | Plausible alternatives considered, including the rejected ones that may be worth revisiting |
| Method | Source check, causal deduction, constraint optimization, expert/tool comparison, random draw from a frozen pool, or explicit author choice |
| Validation | What evidence or test made the result acceptable; what it did **not** prove |
| Provenance | Source URLs, Git paths, commit/PR, generated seed and exact pool/order when relevant |
| Dependencies | Other characters, timeline points, objects, scenes or later payoffs affected |
| Confidence / revisit trigger | How strong the decision is and what new information would justify reopening it |
| Change log | Previous result, why it changed, and the consequences that must be migrated |

A decision is not made permanent just because it is recorded. The record exists so that future revision is deliberate: the author can replace a working choice, preserve the reasoning that led to it, and identify all downstream consequences instead of silently contradicting it.

## Controlled randomization for underdetermined choices

Language models tend to return familiar, high-probability options. For **ordinary choices with several equally valid possibilities**, use explicit randomization to reduce predictable defaults.

Suitable examples: names from a prefiltered demographic pool, the order in which compatible everyday options are considered, or a choice among several equally plausible low-stakes scene details.

Procedure:
1. State the decision and the hard constraints.
2. Gather evidence and construct a pool of **reasonable** candidates.
3. Filter the pool for canon conflicts, duplicate names, chronology, character motivation, cultural plausibility and established preferences.
4. Freeze the candidate list and generate a seed.
5. Draw reproducibly and record the full list, source/rank, seed and selected index.
6. Validate the result against causality, continuity and tone. The draw may select among plausible candidates; it cannot make an implausible candidate true.
7. Keep rejected results and reasons available for future review. Never repeatedly reroll until the model's favourite option appears.
8. If the user has a preference, the author's choice overrides the draw. Record that the process proposed a shortlist and that the author made the final selection.

Do **not** randomize factual canon, historical dates, safety-critical facts, core character motivations, causal outcomes that already have dependencies, or major story decisions where the choice changes the meaning of the series. For consequential decisions, generate alternatives, compare causal costs and benefits, and ask the author only when a genuine value/creative preference remains unresolved.

Randomness is a defence against model-default repetition, not a substitute for logic. Narrative causality can accept or reject a randomly generated candidate; it may not be reversed just to preserve the random result.

## Track C — backpropagation and causal audit

Backpropagation happens after a substantial group of episodes and after each season, not after every paragraph.

Start from an earned later state and trace backwards:
1. What choice, belief, relationship or external event made this state possible?
2. What did the character need to know, want, fear or experience before making that choice?
3. Which earlier scene could naturally establish that prerequisite?
4. What else would that prerequisite change—other characters' knowledge, schedules, objects, relationships and plot threads?
5. Can the seed be shown as part of an ordinary scene, rather than a conspicuous clue inserted only for the payoff?

Then re-read forward from the opening:
- Does each later action still follow from the state actually established in the preceding scene?
- Did a new seed contradict an earlier fact or make a character implausibly prescient?
- Did the revision change the timing or reliability of Nathan's remembered canon?
- Does every important relationship change have enough shared experience behind it?
- Does each object, promise, message, injury, assignment, project and secret remain consistent until it is changed on-page?

A backpropagation change must be **propagated** into dependent scenes, outlines, character records and ledgers. A note in one character file is not enough if the episode outline still assumes the old state.

## Production cycle

1. **World/canon evidence:** distinguish canon facts, historical facts, deductions and invention.
2. **Global architecture:** define beginning/end, midpoint, recursive anchors, character end states and major causal constraints.
3. **Chronology:** put known anchors on a dated timeline and reconcile ages, schedules, travel and canon events.
4. **Forward causal development:** expand the first portion linearly, state by state, scene by scene. Build side plots from the actual time available.
5. **Scene drafting:** write one scene or two connected scenes at a time using the dialogue-naturalness rules and the current state packet.
6. **Immediate state update:** record what changed in knowledge, relationships, objects, obligations and project progress.
7. **Episode audit:** continuity regression, causal links, character-specific voice, missing transitions and accidental duplicated beats.
8. **Arc/season backpropagation:** compare the draft with the top-down anchors; add only seeds that can fit the earlier state naturally.
9. **Forward regression:** read from the beginning again to ensure backpropagation has improved causes without creating contradictions.
10. **Decision-log update:** preserve decisions, alternatives, sources and reasons, and list dependencies if a choice remains revisable.

## Acceptance test

The method is working when:
- the reader can believe the characters have lives between the scenes shown;
- later changes have traceable prerequisites;
- revisiting an earlier episode reveals earned meaning rather than a newly pasted explanation;
- details remain consistent without every detail being repeated explicitly;
- major story direction is purposeful, while the path between milestones feels discovered through choices and consequences;
- an author can revise a working choice without losing the evidence and reasoning behind the current version.

Backpropagation cannot guarantee a perfect narrative. It is a disciplined way to find missing causes and continuity errors, and its effectiveness must be evaluated against actual episode drafts and reader experience.
