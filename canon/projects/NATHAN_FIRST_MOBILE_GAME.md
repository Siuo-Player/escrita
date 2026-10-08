# Nathan's First Mobile Game — Technical/Narrative Design

Status: WORKING / established design
Updated: 2026-10-08

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
movement ideas became much more practical and visible, and he reconstructs a small, unusually effective
mobile-game implementation by combining what he remembers with ordinary 2009 knowledge. citeturn580221search2turn873536search2

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

Nathan is deliberately not responsible for producing high-quality art himself.

He knows he is weak in visual arts and does not waste months trying to become an illustrator.

He can:
- buy inexpensive commercial sprite packs or commissions;
- use period-appropriate public or commercial sound libraries;
- purchase interface assets;
- adapt simple placeholder graphics during development;
- eventually pay a small amount for better title-screen and character art.

He creates the technical architecture, gameplay rules and important AI systems himself.

This reinforces a recurring characterization point: Nathan knows where he is weak and spends money or
asks for help instead of pretending he is equally good at everything.

## Development environment

Nathan writes the important game logic in C++.

He does not need to write a complete rendering engine. A plausible 2009 workflow is to use a small mobile
2D framework or engine for scene management, sprites, input, audio and tile maps, while keeping the AI and
gameplay core under his control.

cocos2d for iPhone is a period-appropriate example: it was already an established open-source framework
for 2D iPhone/iPod Touch games, with tile-map support, touch input, audio support and OpenGL ES
integration.

Nathan can therefore spend his limited time on the part he actually cares about: how the enemies move
and decide.

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

He initially thinks about it as a set of arrows spread over the map.

Only after testing it does he recognize that this is effectively a reusable flow field.

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

The game is developed over roughly **7–8 calendar weeks**, with about **6 weeks of substantial technical
development** and the final week or two devoted mainly to playtesting, packaging and release preparation.

A strong narrative calendar is:

- **17–23 Aug:** concept, map grid, input/rendering and one enemy prototype.
- **24–30 Aug:** conventional A* baseline working with several enemies.
- **31 Aug–6 Sep:** stress testing and profiling reveal that repeated pathfinding is the major cost.
- **7–13 Sep:** Nathan reviews flow-field material and builds the first shared cost/direction field.
- **14–20 Sep:** flow field stabilizes; local steering is added; the family moves and Nathan enters school.
- **21–27 Sep:** player prediction/influence map, integration and update-frequency tuning.
- **28 Sep–4 Oct:** device testing, balancing and optimization.
- **5–11 Oct:** final playtesting and release preparation.

Because Nathan already knows the general shape of the project, has strong C++ skills and does not waste time
on dead ends apart from the A* → flow-field redesign, a believable total is roughly **70–100 focused
development hours**.

During school weeks he usually has only about **10–14 focused programming hours**, concentrated on Monday,
Wednesday, Friday, Saturday and Sunday. Tuesday and Thursday are normally football nights. This prevents
the game from consuming every part of his life while still allowing unusually rapid progress for a
thirteen-year-old who is already highly prepared.

The scope is what makes the schedule credible:

- one small game;
- few enemy archetypes;
- compact maps;
- simple assets;
- no network system;
- no large physics system;
- no custom engine;
- the technical ambition is concentrated in AI, navigation and optimization.

The important milestone for the story is therefore not simply "Nathan finishes a game." It is that a very
small game reaches a polished vertical slice unusually quickly because Nathan understands the problem,
measures his implementation and spends his effort on the part that actually matters.

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
