# Nathan's First Mobile Game — Technical/Narrative Design

Status: WORKING / established design
Updated: 2026-10-14

## Purpose

This document fixes the first substantial programming project Nathan builds after the opening arc.
It is intentionally small enough for one talented thirteen-year-old to finish, but technically unusual
enough to establish the beginning of his long-term relationship with game AI.

The game is not supposed to make Nathan famous immediately. The important result is that he creates a
credible example of a young programmer applying several strong ideas to a very constrained platform.

Important historical correction: flow fields themselves are not a post-2009 invention. Bob Alexander
published "Flow Fields for Movement and Obstacle Avoidance" in *AI Game Programming Wisdom 3* in 2006,
and Treuille, Cooper and Popović published *Continuum Crowds* in 2006 using dynamic potential fields for
large-crowd navigation. Nathan therefore must not be portrayed as inventing flow-field navigation.
His future-memory advantage is subtler: he remembers later games where related field-based or collective
movement ideas became much more practical and visible, and he adapts a known flow-field approach into a
small, unusually effective mobile-game implementation by combining what he remembers with ordinary 2009 knowledge. citeturn580221search2turn873536search2

## Period and target hardware

The story is set in 2009.

The safest baseline target is hardware no better than the original iPhone 3G class rather than relying
on the faster iPhone 3GS. The iPhone 3G had a 412 MHz ARM11 CPU, 128 MB RAM, a 320x480 display and
OpenGL ES 1.1-class graphics. The iPhone 3GS, released in June 2009, was substantially faster and had
256 MB RAM, with OpenGL ES 2.0 support.

Nathan owns a much stronger development computer because of his family's wealth, but he deliberately
tests on ordinary period hardware. His game should feel surprisingly sophisticated without requiring
modern hardware.

Working performance target:
- 30 FPS on conservative 2009 hardware;
- 320x480 portrait or landscape display;
- short levels and small maps;
- roughly 10–20 active enemies in the most demanding normal scene;
- occasional stress test with about 24 enemies;
- no network dependence;
- no large physics simulation;
- no 3D rendering requirement.

The design is therefore constrained by mobile CPU, memory and battery rather than by Nathan's development
machine.

## Basic game concept

Working title: **Current**.

Genre: compact 2D top-down stealth/action game.

The player moves through small rooms or outdoor compounds, completes a simple objective and reaches an
exit while avoiding or outsmarting guards.

The game loop is intentionally narrow:
1. enter a small map;
2. move, hide and make noise;
3. attract or evade guards;
4. reach the objective;
5. escape.

There are only a few enemy archetypes. The depth comes from movement and decision-making rather than from
content quantity.

The game does not need dozens of weapons, inventory systems, dialogue trees or a large campaign.

## Art and asset strategy

**Actual choice for Current 1.0:** Nathan uses simple original geometric shapes for the title screen, tiles, guards, objective/exit indicators and icons, with simple original/generated tones for sound. The visual presentation is intentionally restrained rather than professional-looking. This is the asset set represented in the release packet; no third-party sprite pack, borrowed music, or unlicensed typeface enters build 19.

Other options—buying inexpensive commercial sprite packs, commissioning art, using licensed sound libraries or purchasing interface assets—remain things Nathan could choose for a later version, but none is part of the 15 October candidate. If he adds any external asset later, record its source and license before it enters a build, and generate a new version with affected regression tests.

Nathan knows he is weak in visual arts and does not waste months trying to become an illustrator. He creates the technical architecture, gameplay rules and important AI systems himself and keeps the first release's art scope deliberately small. This reinforces a recurring characterization point: Nathan knows where he is weak and does not pretend to be equally good at everything.

## Development environment

Nathan writes the important game logic in C++.

He does not need to write a complete rendering engine. A plausible 2009 workflow is to use a small mobile
2D framework or engine for scene management, sprites, input, audio and tile maps, while keeping the AI and
gameplay core under his control.

cocos2d for iPhone is a period-appropriate example: it was already an open-source framework
for 2D iPhone/iPod Touch games, with tile-map support, touch input, audio support and OpenGL ES
integration. The framework layer is Objective-C; Nathan's pathfinding, prediction and gameplay logic can
remain C++ and be connected through a small Objective-C++ bridge. Do not describe this as a modern
cross-platform build workflow.

### 2009 toolchain and device constraints — working decision

The story needs a real causal path from source code to a mobile build. The current working choice is an
**Intel Mac running Mac OS X 10.5 Leopard with an era-appropriate Xcode 3.1.x / iPhone OS SDK 3.x
installation**. Apple’s archived Xcode 3.1 notes state that the iPhoneOS SDK could target iPhone/iPod
touch and simulator, but iPhone OS cross-development required a Macintosh with an Intel processor.
Do not silently assume a Windows-only machine can compile and sign the historical iOS app. If later canon
shows different hardware, reopen this decision and choose a technically credible toolchain.

The working test device is a **second-generation iPod touch**, released in September 2008 and documented
for iPhone OS 3.1, owned by Nathan before the opening. Its provenance should be a normal family gift/purchase
before 7 September 2009, not a device that appears for the first time when a benchmark needs it. This gives
Nathan a plausible personal device for music/games and a conservative real-hardware target. The simulator is
still useful for rapid iteration, but a simulator run is not evidence of actual-device performance.

Actual-device development needs a valid signing/provisioning route. Working assumption: Clifford, as the
adult in the household and an experienced technology executive, handles any required developer-account
enrollment/provisioning administratively with Nathan; Nathan writes the game, not the legal account
agreement. Private ad-hoc builds are for controlled tests only. Once Nathan's technical checks and peer playability tests pass, Clifford can handle the adult account/submission administration for a public App Store release; publishing still requires Apple's review and does not make the family famous overnight. Record the
device, OS version, build identifier, test scenario and actual outcome whenever a device test is shown.

**Historical references:**
- Apple, [Xcode 3.1 release notes](https://leopard-adc.pepas.com/releasenotes/DeveloperTools/RN-Xcode/index.html), archived developer documentation on Intel-Mac/iPhoneOS SDK requirements.
- Apple, [2008 second-generation iPod touch announcement](https://www.apple.com/newsroom/2008/09/09Apple-Introduces-New-iPod-touch/).
- Apple Support, [iPod touch (2nd generation)](https://support.apple.com/pt-pt/docs/ipod/132054), which lists documentation for iPhone OS 3.1.

Nathan can therefore spend his limited time on the part he actually cares about: how the enemies move
and decide, while the platform layer remains period-correct.

## First implementation: conventional pathfinding

Nathan deliberately does not begin by trying to be clever.

The first enemy version uses conventional grid pathfinding. A* is a sensible baseline and was already
well established in games by 2009.

This first version is useful because it gives Nathan something measurable to improve.

A level with a small number of guards works well.

Then he increases the number of guards.

The problem is not that A* is wrong.

The problem is repeated work.

Several guards often need to travel through substantially the same part of the map toward the same
region. Calculating a separate path for each of them throws away that shared structure.

This is the moment where Nathan's optimization obsession becomes part of the story.

## How Nathan reaches the flow-field idea

Nathan's future memory is incomplete.

He is not a game-AI researcher from his previous life. He does not remember implementation details or
source code from future games. He remembers impressions:

- some later games had crowds of agents that seemed to move intelligently;
- some enemies seemed to choose paths collectively;
- he remembers seeing behaviours that felt more coordinated than a simple independent path search;
- he remembers that mobile hardware eventually handled larger groups than the phones of 2009 seemed able
  to afford.

He does not remember the exact technical recipe.

The actual breakthrough therefore happens through a mixture of:
- ordinary A* knowledge;
- his C++ ability;
- basic graph and grid reasoning;
- measurement;
- experimentation;
- prior reading about flow fields;
- fragmented memories of later games.

He realizes that when many agents share a destination, the useful thing is not a path for each agent.
It is a map that says, for every cell, which direction generally leads toward the destination at the
lowest accumulated cost.

He initially thinks about it as the same kind of set of arrows he remembers reading about: a shared map
of useful directions rather than a separate path for every guard.

The key step is adapting that known technique to his particular map representation, update strategy and
mobile constraints.

The important narrative moment is not a magical memory that hands Nathan a finished implementation.
He has genuinely read about flow fields before; the important moment is recognizing that the technique
fits the bottleneck he has measured and then adapting it correctly to his own game.

## Flow field

For each small level, Nathan can build a navigation field that encodes the cheapest direction toward a
chosen destination.

The field is generated once, or regenerated only when the walkable map meaningfully changes.

Each enemy then samples the field at its current position instead of running a complete independent
global path search.

This is especially valuable when:
- many enemies want the same destination;
- the map is small;
- movement can be represented on a grid;
- enemies can tolerate approximate local steering.

The technique is far more interesting in Nathan's story than its implementation complexity suggests.

The underlying idea is simple once explained. The unusual part is seeing that it can replace many
repeated searches in a mobile game.

A 2013 chapter of *Game AI Pro* later described flow-field tiles specifically for crowd pathfinding and
steering in mobile games, using *Fieldrunners 2* as the case study. The chapter notes that the game's
flow fields and steering behaviors supported thousands of units on mobile hardware, and it also lists
a 2006 book chapter on flow fields as prior art. *Fieldrunners 2* itself first released on iOS in July
2012. This makes the historical position much cleaner: Nathan is not inventing flow fields; he is
bringing a known specialist technique into a small 2009 mobile stealth game and combining it with a
player-behaviour influence system and severe workload reduction. citeturn754349view1turn800115search39turn800115search11

## Enemy prediction: separate from navigation

The enemies also learn something about the player, but this is deliberately a different system.

The flow field answers:

**How do I move efficiently to a chosen place?**

The prediction system answers:

**Which place should I move toward?**

Each guard remembers a small amount of recent information:
- last known player location;
- direction the player was moving;
- recent noises;
- places where the player was seen;
- the player's recent escape choices;
- whether the player tends to favour a route or side of a room.

Nathan converts this into a lightweight prediction/influence map.

It is not a neural network.

It is not a large simulation.

It is essentially a small, constantly decaying map of where the game thinks the player is more likely to
be next.

## The connection between prediction and flow fields

The two systems meet at the goal-selection stage.

Example:

A guard sees the player disappear around a corner.

A naive guard runs to the last visible position.

Nathan's guard instead:
- records the last sighting;
- considers the player's recent direction;
- considers nearby exits and previous choices;
- increases the likelihood of several nearby cells;
- chooses a likely search/interception point;
- requests the appropriate navigation field toward that point;
- then follows that field while using inexpensive local steering to avoid obstacles and other guards.

This produces a useful illusion.

The prediction system makes the enemy appear to know where the player might be.

The flow field makes the enemy cheap to move there.

Because those jobs are separated, Nathan does not need every guard to perform expensive global reasoning every
frame.

## Different guards can still behave differently

Nathan does not want every enemy to become the same robot.

Each guard can have small behavioural differences:
- one tends to investigate noises;
- one prefers direct pursuit;
- one is cautious and checks likely escape routes;
- one is more likely to return to a patrol route;
- one reacts more strongly to repeated player behaviour.

They can still use the same underlying navigation field.

This is another major optimization: expensive shared information is shared, while inexpensive personality
parameters remain individual.

## Update frequency

One of Nathan's main optimizations is separating visual frequency from decision frequency.

The game can update the display continuously while not recomputing high-level enemy decisions every frame.

For example:
- movement and rendering remain frequent;
- high-level intent updates periodically;
- path/influence fields change only when useful;
- local steering fills the gaps between decisions.

The player therefore sees continuous movement without the phone constantly recomputing the most expensive
parts of the AI.

## Precomputation and caching

Nathan deliberately performs as much work as possible before the game needs it.

For static maps:
- basic navigation information can be prepared when the level is built;
- integration costs can be stored compactly;
- flow directions can be stored compactly;
- static obstacle information never needs to be rediscovered every frame.

For dynamic events:
- only the affected area is reconsidered;
- previous results are reused whenever still valid;
- repeated destinations can reuse existing fields.

The exact implementation is deliberately described in the novel at the level of ideas, not source code.

## Why not a real fluid simulation?

Nathan considers a more literal "fluid/current" model because he likes the intuition that movement can
look as though enemies are being carried by a field.

He decides against making a full physical fluid simulation the core of the game.

A true fluid simulation adds complexity that does not improve the gameplay enough.

Instead, he uses the simpler and more useful abstraction:
- a cost map;
- a direction field;
- optional influence values;
- inexpensive local steering.

The final result can look fluid without pretending that the phone is solving fluid dynamics.

Aesthetic "current" language can still influence the name and presentation.

## Approximate size and mobile budget

A conservative working level is a 64 x 64 navigation grid: 4,096 cells.

A small set of compact navigation/influence values across this grid is tiny by mobile memory standards.
Even with several maps and extra state, the AI data remains in the order of tens or hundreds of kilobytes,
not tens of megabytes.

A plausible first playable build can be kept approximately in this range:
- executable and engine/framework pieces: around 1–2 MB;
- sprites, tiles and UI art: around 0.5–1.5 MB;
- compressed audio: around 0.5–1.5 MB;
- maps and AI data: well below 1 MB;
- configuration and miscellaneous assets: a few hundred KB.

Working total: roughly **3–6 MB installed**, with considerably less active AI data in RAM.

Runtime memory can remain comfortably below **10 MB** for the game's own active structures, leaving the old
phones' constrained memory mainly to the operating system, framework and rendering surfaces.

This is deliberately conservative. The exact number is not a canon hardware benchmark; the important
story fact is that the game is small enough that the AI, not the artwork, is the impressive part.

## Stress test

Nathan's private benchmark is simple:

1. one guard;
2. five guards;
3. ten;
4. fifteen;
5. twenty;
6. twenty-four.

The ordinary implementation gets increasingly wasteful as every guard repeats similar path searches.

The flow-field version scales much better because the expensive navigation calculation is shared.

The enemies still need local movement and collision handling, so performance is not free. Nathan's
perfectionism therefore continues after the clever idea:

- he reduces unnecessary updates;
- reuses calculations;
- keeps maps compact;
- simplifies collision checks;
- avoids floating-point work when an integer representation is enough;
- separates slow-changing state from fast-changing state;
- measures rather than guessing.

The phone is not made faster.

The workload is made smaller.

## Pre-release defect closure record

The game must not be submitted with any of the known reproducible defects below. The dates are the current story plan and must be mirrored in Episode 2's scene ledger. A fix is not considered complete until the relevant reproducer passes on the current build. Peer feedback is a report of experience, not a diagnosis of code.

| ID / first observed | User-visible problem | Fix and causal work window | Required retest and closure condition |
|---|---|---|---|
| BUG-01 — 9 Oct; Maxwell reproduces it on 10 Oct | Guards bunch in a narrow corridor and make player movement feel stuck. | On 11 Oct, Nathan adjusts local steering so agents yield/space themselves at a bottleneck instead of repeatedly contesting the same immediate tile. The shared navigation field remains; the fix is local behavior, not a new global pathfinder. | Replay the same corridor with opposing guards and the player approaching from either end. No permanent pile-up; player movement remains responsive; guards can clear the bottleneck without becoming identical or psychic. |
| BUG-02 — 9 Oct | A guard switches from chase to search too abruptly when line of sight is briefly interrupted. | By 14 Oct, add a short, bounded lost-sight grace interval, then search around the last observed position. Old information must expire, so guards cannot track the player indefinitely without seeing them. | Break line of sight briefly and then for a longer interval. A brief interruption does not cause an implausible instant reset; a longer escape eventually ends the chase and begins a search of the last known area. |
| BUG-03 — 9 Oct | At a tight corner, collision handling and local steering disagree; movement can stick or clip into a blocked cell. | By 14 Oct, validate the proposed next position against walkable-cell/collision constraints before committing movement, then resolve the local-steering choice without repeatedly pushing into the same obstacle. | Repeat the original corner case with player and guards. No blocked-cell entry, visible clipping, permanent jitter or stuck input. Retest the corridor case too, since the fixes interact. |
| BUG-04 — 9 Oct; Cory's 10 Oct playtest confirms it | Objective completion and exit state are unclear. A player can reach the exit and not know whether an objective remains or the game failed to register an action. | On 11 Oct, add a simple period-appropriate visual state change: the objective has a clear completed state and the exit visibly changes when it becomes available. Use existing/simple assets; do not add a large UI system. | Cory's reported route is replayed without coaching. A player can tell whether the objective is complete and why the exit is or is not available. The indicator changes only when the underlying state changes. |
| BUG-05 — 9 Oct | Restart feels slow and can leave the player waiting before another attempt. | On 11 Oct, reset transient player/guard/objective state while keeping static map and asset resources loaded; show an immediate, clear restart response. | Repeat restart ten times across the test map. Every run starts from the defined initial state with no stale guard memory, old objective state or delayed input lock. |
| BUG-06 — 9 Oct; measured again on 13 Oct device test | Rebuilding the shared path field creates small performance spikes, especially with many guards. | On 12 Oct, cache fields against the map version and target cell, and coalesce redundant rebuild requests. On 13 Oct, use the iPod touch stress test to find any remaining device-specific redundant work and reduce it before retesting. | Run the documented 1/5/10/15/20/24-guard scenarios on simulator and actual iPod touch. Record build, OS, scenario and measured outcome; all target cases pass without a recurring rebuild spike that disrupts play. A simulator result never substitutes for the device run. |

### Acceptance state before public submission

- **10 Oct:** Maxwell and Cory confirm BUG-01 and BUG-04 from their own play experience; Nathan records reproduction steps instead of dismissing the feedback.
- **11 Oct:** BUG-01, BUG-04 and BUG-05 receive targeted fixes and their specified regression checks.
- **12–13 Oct:** BUG-06 is optimized and checked first on the current build and then on the real device. Any fresh, reproducible failure blocks closure until fixed and rerun.
- **14 Oct:** BUG-02 and BUG-03 are fixed and retested alongside the full guard-count scenarios. Cross-test the corridor/collision changes rather than considering them independent.
- **15 Oct:** Wesley's supervised real-device playtest confirms that the submitted candidate still behaves correctly, including objective/exit feedback, movement and restart. Any release-blocking or reproducible defect exposed in this final pass is fixed and retested before submission; the schedule must move if required time exceeds the evening window.

**Release rule:** the 15 October candidate has no known reproducible defect remaining. Later wishes such as extra levels, additional polish or more content may be recorded as future ideas, but must not be used as a euphemism for a known broken control, unclear required objective, stuck guard, bad restart, or failing performance test. Do not invent numeric benchmark results unless the scene records the actual measured number.

## Candidate build history and public submission packet

These identifiers make the testing chain concrete. The numbers are working continuity values; don't describe a test as passing on a build different from the one the scene says was tested. If code changes after a passing test, issue a new build and rerun the affected tests.

| Date | Version/build | State and evidence |
|---|---|---|
| **9 Oct** | **0.7.0 (build 14)** | First complete playthrough. The game reaches an end-to-end win, but BUG-01 through BUG-06 are recorded as open. A completed playthrough is not release approval. |
| **10 Oct** | **0.7.0 (build 14)** | Maxwell and Cory test this Mac/simulator build. They reproduce corridor movement crowding (BUG-01) and unclear objective/exit feedback (BUG-04). Nathan records the build and reproduction steps. |
| **11 Oct** | **0.8.0 (build 15)** | Local steering, objective/exit state feedback and restart behavior are changed. BUG-01, BUG-04 and BUG-05 close only after their reproducers and restart repetition test pass. |
| **12 Oct** | **0.8.1 (build 16)** | Shared-field caching and coalescing reduce repeated rebuild work in the simulator. BUG-06 improves, but stays open until the actual-device stress test passes. |
| **13 Oct** | **0.8.2 (build 17)** | The iPod touch stress test exposes remaining redundant work; Nathan fixes it and reruns the same scenario plus the 1/5/10/15/20/24-guard matrix. BUG-06 closes only after the recorded target cases pass. |
| **14 Oct** | **0.9.0 (build 18)** | Lost-sight grace/search handling and tight-corner collision validation are corrected. Nathan retests brief/prolonged loss of line of sight, the original corner and corridor reproducers, and the guard-count matrix. BUG-02 and BUG-03 close only after these tests pass. |
| **15 Oct** | **1.0 (build 19)** | Versioned release candidate compiled from the validated code, tested on the real iPod touch by Wesley without coaching, then run through the final acceptance matrix. This exact binary is the one Clifford submits for review. No known reproducible blocker remains. |

### App Store record — working choices

- **Public title:** Current.
- **Marketing version / build:** 1.0 / 19.
- **Bundle/App ID:** `com.cliffordcallahan.current`.
- **SKU:** `CALLAHAN-CURRENT-001`. Treat it as fixed after the record is created.
- **Developer/seller display name:** Clifford Callahan, using his already-active adult developer membership. Clifford handles the signing, provisioning, iTunes Connect record and submission. The seller name is not a claim that he wrote the game.
- **Creator credit:** the title/credits screen and the listing description attribute design and programming to Nathan Callahan and note that Clifford provided account/submission administration. This avoids pretending the thirteen-year-old independently contracts with the store, while preserving his authorship.
- **Primary language:** English. **Initial distribution:** U.S. storefront. **Price:** Free. No ads, in-app purchases, network access, user account or external service are included.
- **Category:** Games / Puzzle. **Working age rating:** 9+ because the game uses stylized guard pursuit/stealth tension; the actual 2009 rating questionnaire must match the submitted content. No graphic violence, blood, gambling or sexual content is included.
- **Working store description:** “A compact single-player stealth puzzle. Read the guards' patrols, find a route through the room, and reach the exit. Built around simple controls and adaptive guard behavior.”
- **Required submission materials:** correctly sized 57×57 PNG device icon; matching 512×512 store icon created from the same artwork; simple 320×480 launch image; three real screenshots from build 19 (title/start screen, mid-level with guards, and the completed-objective/open-exit state); description, category, copyright/version, SKU, application/support URLs, monitored support email, age rating and signed distribution binary. Never depict features or results from an untested build.
- **Asset provenance:** the title art, tiles, guards and objective/exit indicators use original simple shapes made for this project. Sound uses simple original/generated tones. No borrowed music, third-party sprite pack or unlicensed typeface is included. Record any later external asset and license before it enters a build.
- **Administrative checklist:** Clifford confirms the developer membership/agreements, app record and distribution profile already exist; checks the App ID/bundle ID, version, SKU, rating, asset dimensions and binary signature; answers export-compliance questions truthfully (the game itself has no networking or custom encryption); chooses 23 October as the availability date; and submits the binary for review by about 21:30 on 15 October.
- **Support details:** a monitored project support mailbox and a minimal support page on a domain Clifford already controls are entered in the store record. Their literal addresses are admin metadata, not dialogue, unless a later scene needs them.

### Release acceptance gate

Submission requires all six known defects to be closed on the tested code and the final build 19 to pass the documented matrix. A new reproducible defect reopens the relevant item; code or resource changes after build 19 require another build and affected regression tests. If a fix or review outcome pushes the date, the public launch moves—the story must not preserve 23 October by skipping a necessary test or implying approval before it happens.

The 2009-specific App Store details above follow Apple's period presentation, [WWDC 2009 — Publishing on the App Store](https://nonstrict.eu/wwdcindex/wwdc2009/702/), including its metadata, rating, icon and screenshot requirements. The identity, pricing and release date are working creative choices, not facts from that source.

## The visual effect

The player does not see the algorithm.

What the player sees is:
- guards crossing a room without getting stuck;
- several guards taking sensible but not identical routes;
- guards splitting up after a sighting;
- one guard moving to cut off an obvious exit;
- another checking a different likely location;
- groups not collapsing into a single identical train.

The game therefore feels much smarter than the amount of content would suggest.

## Why it is not an instant industry sensation

Nathan's use of the technique can reasonably go unnoticed at first.

There are several reasons:
- it is a small mobile game;
- players judge the result, not the implementation;
- most people cannot identify why the enemies move well;
- the game has limited visual production value;
- the underlying method is easy to miss if nobody sees his implementation;
- the mobile market is crowded enough that a technically clever small title can remain niche.

A technically minded player or developer can notice the unusually large number of enemies and ask how he
is doing it, but that is different from the wider public noticing or understanding the implementation.

The key distinction is:

**the technique is not unknown; Nathan is unusual.**

In 2009, a specialist who inspected the project could recognize that flow-field-style navigation was a
real, established idea. What is exceptional is that a thirteen-year-old recognized a specialist technique he had actually
studied, adapted it correctly to a mobile game, connected it to a separate lightweight player-prediction
system, and then optimized the whole arrangement for constrained hardware.

Therefore the story should not give Nathan an implausible immediate reputation as the "inventor" of a
new AI technique.

The first people who look closely may react more like:
- "You wrote this yourself?"
- "How old are you?"
- "Why did you use a shared field here?"
- "How are you updating this without killing the frame rate?"

The deeper recognition can happen much later, through deliberate inspection or disclosure.

One especially plausible route is Nathan's later university application.

When he is applying to strong computer-science/AI programmes, Nathan describes the project in an
application essay, portfolio, research statement, or supplementary technical material. He can explain
that at thirteen he built a complete mobile game, implemented shared field-based navigation, added a
separate lightweight behaviour model, and spent significant time optimizing it for 2009-era hardware.

At that point, the game has a very different context. Admissions readers or a professor interested in
game AI can recognize that the interesting accomplishment is not "he invented flow fields" but that a
very young student independently understood and applied a nontrivial technique, designed an efficient
architecture around it, and demonstrated the discipline to profile and optimize a real program.

Another possible route is a developer discovering the implementation because Nathan publishes a short
technical explanation or source excerpt. This can create modest technical attention years before the
university application without making him famous.

Recognition should therefore be **conditional on someone looking under the hood**. The code and design,
not the game's download count, are what make the project noteworthy.

A plausible route is that Nathan eventually posts a technical explanation or a small source fragment after
someone asks about the game's performance. A programmer recognizes the idea as an interesting solution to
shared crowd navigation. Later, as flow-field approaches become more openly discussed in game-AI circles,
someone notices that Nathan had been using a small version years earlier.

The story should not claim that everyone in the industry somehow missed an obvious revolution.

The believable version is smaller: **the technique is ahead of the scale at which Nathan applies it, the
game is niche, and the implementation becomes recognized before it becomes famous.**

## What Nathan remembers from the future

Nathan's memory of this subject remains deliberately imperfect.

He remembers examples more readily than terminology.

He may think:
- "I remember enemies in that game doing something like this."
- "There was a game where they stopped feeling like they were just following the player."
- "I know this general idea appeared later."

He does not remember:
- the exact algorithmic steps;
- source code;
- implementation constants;
- the exact year a particular technique was published;
- who invented every part of it.

When he cannot remember a detail, he has to derive it.

This keeps his advantage from becoming a cheat sheet.

## Development calendar and school-night workload

The active prototype/build cycle runs from **3 September to 15 October 2009**: 43 calendar days inclusive, a little over six weeks. The story's first on-page scene is still 7 September. During **3–4 September**, Nathan makes the high-level plan: core loop, enemy behavior, small scope and a simple map. During **5–6 September**, he sets up the period-appropriate framework/project skeleton and writes only the minimum functions needed to render a grid, accept player input, update a basic enemy and run a crude first loop. By the first on-page scene, this is a very early but genuinely running build—not a polished vertical slice. The A* baseline and the wider playable slice are developed and refined during the visible story. After submission on 15 October, App Store review runs separately; 23 October is the working public-launch target.

This is deliberately fast because Nathan already knows C++, has studied game programming, uses an existing
2D framework, keeps the game scope narrow, and does not attempt custom rendering, a large campaign or a
network system. The A* → flow-field redesign is the important architectural detour, not his first contact
with programming.

A useful narrative target is roughly **60–85 focused development hours**, including the short pre-opening
prototype period.

### Compressed development phases

- **3–4 Sep (off-page):** high-level game plan, deliberately small scope, core loop, enemy concept and first map.
- **5–6 Sep (off-page):** framework/project skeleton and minimum runnable functions: render the grid, move the player, update one crude enemy and execute the first game loop. Budget roughly 8–10 focused hours across both days; the build is deliberately rough.
- **7–9 Sep:** the first on-screen build runs, but is very early. Nathan extends the minimum loop, establishes/refines the A* baseline and tests increasing enemy counts; repeated global searches become the measurable bottleneck and profiling begins.
- **10–13 Sep:** stress-test 10/15/20/24 enemies; cache/update-frequency experiments help but do not solve
  repeated global work; first playable map remains functional.
- **14–15 Sep:** relocation interrupts work; technical work continues only in fragments.
- **16–23 Sep:** Nathan revisits material he has already studied and adapts shared flow-field navigation.
- **24–30 Sep:** field navigation stabilizes; local steering and shared navigation integrate; first prediction
  experiments.
- **1–7 Oct:** player prediction/influence field becomes more useful and connects to goal selection.
- **8–12 Oct:** profiling, caching, update-frequency reduction, device tests and balancing.
- **10–15 Oct:** Nathan's technical/regression tests and small playability sessions with peers identify the final changes. He packages the candidate and submits it for App Store review by 15 October.
- **23 Oct (working target):** public launch after review approval. This is a release, not an instant industry breakthrough; audience size and response remain uncertain.

### Why the shorter schedule is credible

Nathan is not learning programming or game development from zero.

He already has:

- strong C++ ability;
- substantial self-study in computer science and game AI;
- a clear design target;
- experience with the tools he is using;
- a narrow game scope;
- simple original geometric assets and simple original/generated tones for the first release, avoiding a third-party art/audio pipeline.

The work is accelerated by the absence of large side systems:

- few enemy archetypes;
- compact maps;
- simple assets;
- no custom engine;
- no network system;
- no large physics simulation;
- no major debugging disaster.

The one important architectural detour is **A* → flow field**. Once Nathan recognizes that the expensive
part of his prototype is repeated global navigation for agents sharing destinations, progress becomes much
faster.

Treat **10–14 focused programming hours per week as an approximate average, not a ceiling or fixed quota**.
On an ordinary school day, Nathan has about **2 focused programming hours available**; on a genuinely
free day, he can devote **up to 8 hours**. Availability is an upper bound, not an obligation: schoolwork,
football training and matches, relocation, family plans and fatigue can use that time. Across roughly six
weeks, **60–85 focused hours is feasible** without requiring every day to be a long session. Friday/weekend
blocks can be longer when the calendar permits, and during a genuine late-stage crunch (including
12–15 October) Nathan may, when needed, work until **04:00–05:00** on a particular night. This is possible,
not mandatory every night. If a late finish is used, the following day's sleep, fatigue and school/training
state must reflect it. Adjust a given day's work only when a specific event or constraint explains the
change; do not treat a late finish as inherently implausible.

The story should therefore present the achievement as:

**a small game completed unusually quickly by a highly prepared thirteen-year-old who knows what he is
doing, measures his work, and keeps the scope under control.**

The technical achievement is the quality of the architecture and the optimization discipline, not the
quantity of content.

## Novel presentation rules

The novel should show the development rather than summarize it after the fact.

Important development scenes should include:
- Nathan measuring the first implementation;
- watching performance degrade when the enemy count rises;
- realizing that several enemies are solving nearly the same navigation problem;
- sketching the map as a grid;
- experimenting with shared directional information;
- testing the first field-based movement;
- observing an enemy overshoot or choose a bad local direction;
- adding inexpensive steering;
- noticing that last-known-position pursuit is easy for the player to exploit;
- adding the separate prediction/influence field;
- tuning how quickly that memory fades;
- testing repeated player routes;
- stress-testing on an older phone;
- optimizing something that already works because he cannot leave well enough alone.

The narration should explain his reasoning in natural internal dialogue.

Do not present source code in the prose.

Do not turn the chapter into a computer-science lecture.

Nathan can skip obvious explanations to himself. The reader only needs enough detail to understand why
the system works and why the implementation is impressive for the period.

## Character function of the project

The game establishes several recurring aspects of Nathan:

- his competence is real rather than magical;
- his future memory is useful but incomplete;
- his first major breakthrough comes from recognizing and applying something he genuinely studied, not
  from remembering a finished answer;
- his perfectionism is especially visible in optimization;
- he knows enough to use existing tools instead of rebuilding everything;
- he delegates art because he knows it is not his strength;
- he is humble to an almost absurd degree about the result;
- when someone compliments the game, he assumes they are being polite or encouraging him;
- he can produce something genuinely unusual while still thinking mostly about what he did wrong.

The project is therefore both a technology milestone and a personality scene-generator.

## Historical/reference basis

The following sources are research references, not facts that Nathan must explicitly know in 2009.

- Apple, WWDC 2009 material on iPhone game development and OpenGL ES device capabilities.
- Apple, June 2009 announcement of iPhone 3GS.
- iFixit hardware reference for the iPhone 3G and 3GS specifications.
- cocos2d for iPhone project/archive documentation.
- Elijah Emerson, "Crowd Pathfinding and Steering Using Flow Field Tiles," *Game AI Pro*, 2013.
- Graham Pentheny, "Efficient Crowd Simulation for Mobile Games," *Game AI Pro*, 2013.
- Historical examples of later games that made sophisticated enemy search and player-modeling behaviour
  visible include *Alien: Isolation* (2014) and *Middle-earth: Shadow of Mordor* (2014). These are inspiration
  for the *kind* of player-facing effect, not technologies Nathan literally ports from those games.

Research note: the story should not claim that flow fields were impossible in 2009. The point is that
Nathan applies a concept that would later be explicitly documented/popularized for large-scale crowd
movement and mobile constraints, at a time when his own small project would have had little reason to
draw broad technical attention.
