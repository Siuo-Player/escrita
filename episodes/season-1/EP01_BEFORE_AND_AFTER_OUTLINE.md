# Season 1, Episode 1 — Before and After

Status: DRAFT OUTLINE / expanded working draft
Updated: 2026-10-13

## Story window

**7–30 September 2009**

Drafting references: use [the dialogue naturalness standard](../../canon/narrative/DIALOGUE_NATURALNESS_STANDARD.md), [Season 1 relationship pacing](../../canon/narrative/SEASON_1_RELATIONSHIP_PACING.md), [the foreknowledge/intervention policy](../../canon/narrative/FOREKNOWLEDGE_INTERVENTION_POLICY.md), and [the source-backed opening calendar audit](../../research/narrative/OPENING_CALENDAR_AUDIT.md). Scene beats are constraints, not dialogue to expand mechanically; do not force a canon rescue into the opening just to prove Nathan remembers the show.

Target finished length: **10,000–14,000+ words**.

The episode should feel broad rather than rushed. It covers almost a month, but routine days are compressed.
The reader should experience several complete "windows" into Nathan's life and understand what happens
between them.

## Central movement

**Nathan already has a life. The move does not create him; it displaces him.**

The episode begins on his thirteenth birthday before school starts, with computing, football and an
established social/academic identity. His father's promotion then abruptly redirects the family's future.
The new school introduces Alex and a second social world. The episode closes with Nathan no longer entirely
new, but still unfinished in both his new life and his game.

## Persistent threads

### A — Nathan / game
Prototype → A* baseline → stress test → bottleneck → flow-field adaptation → first integrated field movement.

### B — Old school
Teachers and teammates already know Nathan. The reader sees why through interactions rather than exposition.

### C — Football
Nathan is already captain and comfortable inside an established team.

### D — Callahan family
Birthday → promotion → logistics → relocation → temporary rental setup.

### E — New school
New kid → teacher reactions → classmates → first foothold.

### F — Nathan + Alex
Recognition → observation → avoidance → Alex initiates → repeated contact.

### G — Modern Family AU
Pilot on 23 Sep and The Bicycle Thief on 30 Sep, shown in parallel unless Nathan has a genuine reason to
intersect them.

### H — Living background
Shopping, packing, household setup, teammates, teachers, family members' independent plans, objects acquiring
provenance.

---

## MOVEMENT I — 7–13 SEPTEMBER
### Old life before the move

### 7 September — birthday / opening image

**Calendar:** Labor Day. No ordinary school day. citeturn275803search0turn275803search1

#### Scene 1 — Nathan at the computer
Open quietly with action rather than explaining reincarnation.

Nathan is thirteen today.

He is working on the game. On 3–4 September he planned the core loop, enemy behavior, small scope and first map; on 5–6 September he set up the project and wrote the minimum functions to get it running. His Intel Mac has the period-appropriate C++/iOS development environment already configured. A second-generation iPod touch, bought or gifted by his parents in 2008, sits beside the computer; he uses it for games, but has not yet ported this prototype to it.

The build running on screen is a very early proof of life, not a polished game. It has:
- a crude rendered tile/grid test map;
- basic input and player movement;
- one rudimentary enemy archetype with a simple update/patrol loop;
- an initial, unmeasured route-finding attempt.

Several functions are placeholders, enemy behavior is simple, and no performance or gameplay claim has been established yet. The important point is that Nathan can run the build and inspect a real result on his first on-page day.

He is using A* because it is the sensible baseline, not because he lacks better ideas.

Character beats:
- he notices a small inefficiency before anyone else would care;
- refuses to call the prototype "good";
- thinks about the problem mathematically;
- has a notebook with sketches rather than polished design documents.

The reader should infer advanced competence from the way he works.

#### Scene 2 — birthday breakfast
Clifford and Heather celebrate him.

Keep it domestic and ordinary.

Useful characterization:
- Nathan tries to say he does not need much;
- parents know he always says that;
- a gift connected to football/computing can show they understand his interests;
- he is more comfortable receiving practical gifts than emotional praise.

Do not make the birthday a monologue about destiny.

#### Scene 3 — informal football
Labor Day is a holiday, so do not stage a coach-led team practice or scheduled fixture. If this scene is retained, make it an informal pickup/kickabout with one or two teammates Nathan already knows, arranged casually rather than as official practice; solo touches or conditioning is also plausible. No lineup, official attendance or match result is needed.

Nathan is already captain of his regular Seattle team, although this scene itself is informal.

Show the contrast with **Calvin Baxter**, Nathan's usual midfield partner:
- in computing Nathan works alone and overthinks;
- in a familiar football context, he jokes easily once Calvin starts talking;
- Nathan suggests a small adjustment to their passing/spacing;
- Calvin follows it without drama because they have an established tactical shorthand.

Keep the interaction informal and brief. Calvin's wish to improve the team's play is not a new rivalry or a new friendship arc; his established profile already explains why he values practical, positional advice.

#### Scene 4 — quiet family undercurrent
A very small domestic detail:
- Clifford takes a work call;
- Heather notices the tone of the conversation;
- Nathan notices but does not know what it means.

This plants the promotion before the reveal.

#### Scene 5 — evening coding
Nathan resumes the benchmark from the small baseline he checked in Scene 1; he does not need to repeat the one- and five-guard cases without a reason.

He increases the same scenario to ten guards, then fifteen. The game still runs, but Nathan notices that multiple guards repeatedly calculate routes through the same corridors toward the same region. He records the count and what he sees rather than declaring the cause proven.

The benchmark is not introduced as exposition. We see the number on his screen increase and watch him compare the behavior.

End beat:
**"Why are fifteen different guards all spending time finding essentially the same road?"**

---

### 9 September — first day at the old school

#### Scene 6 — mathematics
**Time:** 10:20–11:15, Wednesday 9 September, Nathan's scheduled mathematics class.
Nathan arrives at school already comfortable with the material.

Teacher gives a problem.

Nathan solves it quickly.

Teacher asks him to explain it.

Nathan:
- starts explaining at too high a level;
- realizes it;
- simplifies;
- worries he has sounded arrogant.

Teacher does not praise him as a genius. Instead:
- asks one harder follow-up;
- notices he can actually explain the reasoning;
- quietly decides he may need harder work later.

This teacher should be a possible recurring academic relationship.

#### Scene 7 — lunch / classmates
Calvin Baxter, Nathan's regular midfield partner and a returning classmate at the same Seattle middle school in this working baseline, starts a low-stakes conversation about the new term's science/lab work.

Nathan responds easily and makes one small joke. The reader sees that he is **not socially awkward in conversation**; his problem is initiating contact, especially with someone he does not already know. Calvin's pre-existing trust comes from their football partnership, not from an instant new friendship.

#### Scene 8 — football / captaincy outside practice
**Time:** 14:50–15:00, Wednesday 9 September, school exit/pickup area.
After the last class, Calvin asks Nathan about the midfield spacing from Tuesday's practice. Nathan suggests one concrete change to the distance between the holding and attacking midfielders. Calvin agrees that it may help the shape, but no one else has heard the exchange and the whole team has not adopted the adjustment yet. They can try it at Thursday's scheduled practice.

This is a short tactical conversation, not another training session. Nathan's leadership is visible outside the pitch, but a suggestion is not the same as a team decision. Calvin knows the proposed adjustment; other teammates and Coach Holloway learn it only if Nathan or Calvin tells them or it is tested at practice. Nathan credits the team's execution rather than taking the praise for himself.

This establishes leadership without self-confidence.

#### Scene 9 — game / first profiling pass
**Time:** 19:30–20:30, Wednesday 9 September, home computer.
Nathan re-runs the same fifteen-guard scenario from Scene 5 with the profiler enabled; he does not simply increase the count again. He compares it with the small one- and five-guard baselines.

The profiler gives him the first evidence that repeated path-search work is a real cost, not just an impression from watching the screen. It does not yet provide a finished diagnosis or solution.

Important visual/narrative point: the computer is doing work Nathan considers wasteful. Do not explain profiling extensively; show him comparing the same operation repeating and recording what the tool actually reports.

---

### 10 September — school and relocation pressure

#### Scene 10 — science/lab
**Time:** 09:00–09:55, Thursday 10 September, Nathan's scheduled science class.
The class is comparing how quickly sugar dissolves in water at different temperatures. Nathan points out that the groups also need to keep the sugar mass, water volume and stirring method consistent, and they need one shared rule for when the sugar counts as dissolved. Otherwise they will change several variables at once.

The teacher asks him to justify which variable each group is testing and how they will compare results. Nathan explains calmly, using the experiment in front of them rather than giving a lecture. The class reaction is modest: a couple of students follow the explanation or nod, but nobody treats him as a prodigy. Do not give an unnamed student a memorable line or a recurring role.

#### Scene 11 — football / playing-time tension
**Time:** 15:10–16:30, Thursday 10 September, scheduled team practice.
At the previous Saturday's fixture, Devon Carver came on late and felt he had too little time to show what he could do. He asks for a clear path toward more meaningful minutes; he is not asking Nathan to overrule the coach.

The team first tests the spacing suggestion Nathan and Calvin discussed on Wednesday. Calvin and Nathan adjust the distance between holding and attacking midfield during a positional drill; it helps once, but the players still have to communicate and execute it. Coach Leonard Holloway decides whether to keep testing it and makes no permanent tactical or selection change on the strength of one drill.

During the next rotation, Nathan asks Devon if he wants a concrete pointer rather than a promise. He suggests Devon scan over his shoulder before receiving and take his first touch away from pressure, then play the simple pass if no forward lane is open. Devon tries it in the drill and improves on one repetition but still misses a cue later. Leonard sees Nathan give useful, specific feedback without deciding selection for him. No promise of minutes and no immediate selection change occurs.

#### Scene 12 — evening / Clifford's news approaches
Clifford's work day becomes more urgent.

A short parallel family scene with Clifford and Heather establishes:
- the California role has been under discussion for weeks;
- the outcome is still uncertain;
- relocation support is already being discussed as a possibility.

This means the later "sudden" news is sudden **to Nathan**, not magically produced overnight.

---

### 11 September — game + first emotional disruption

#### Scene 13 — A* stress test
**Time:** 16:00–18:00, Friday 11 September, Nathan's computer, before the family announcement.
Nathan reruns the benchmark at 10, 15, 20 and 24 guards. The first serious performance degradation appears in the larger cases.

He experiments with fewer path/update refreshes, a simple cache and different destinations. The cache only helps when a request can actually be reused, and reducing update frequency makes some movement feel less responsive. The result is better in one or two cases but not good enough; the trade-offs create work for a later design pass rather than a finished fix.

He gets irritated at the program rather than himself: the code is doing exactly what he told it to do. He records the test cases and the trade-offs instead of inventing a frame-rate number.

#### Scene 14 — family
**Time:** 18:45–19:00, Friday 11 September, Callahan home.
Clifford receives the formal confirmation that the promotion is approved and the role is California-based, after the company has been discussing the option and preparing relocation contingencies for weeks. He tells Heather and Nathan that evening; Nathan had not known the decision was final.

The scene should begin with practical questions:
- When?
- Where?
- What about school?
- What happens to football?
- What about his computer?

Then the emotional reaction arrives later.

He realizes:
- he had a team;
- teachers knew him;
- routines were established;
- he was not looking for a new life.

#### Scene 15 — parents' explanation
**Time:** 19:00–19:20, Friday 11 September, the same family conversation.
Clifford explains that the company has been discussing the California role and preparing contingencies for weeks, but the final approval was only received today. The relocation coordinator can move quickly because a temporary rental, movers and a vehicle were shortlisted or held conditionally; the family did not secretly settle every detail before the offer was confirmed.

They will initially use an employer-arranged furnished rental. Buying a home later is only a possibility if Clifford's role proves stable and the family likes the area; nobody promises or decides to buy now. Heather may express that hope, but the temporary lease is not a purchase plan.

This explains the short logistics window without making the family's future housing a settled fact.

#### Scene 16 — Nathan alone
**Time:** 19:30–20:15, Friday 11 September, Nathan's room/computer area.
Nathan withdraws for a little while after the family conversation. He returns to the game because it is the one problem he can still control; this is a coping choice, not a melodramatic refusal to talk.

Before resuming a short, familiar task, he sends a plain group SMS using the team's existing text-message distribution list for practice updates. It tells Coach Leonard and the squad that he is moving on Monday. He does not make a speech or start separate farewell conversations. The message is information; any teammate's specific reaction should be shown only if it matters to a later scene. Nathan then spends a short block reviewing the existing test notes rather than beginning another major coding task.

---

### 12 September — last football weekend

#### Scene 17 — final Seattle-team match
**Time:** Saturday 12 September, 09:00–10:25, Seattle field.
Nathan plays his final match before leaving. Before warm-up, Coach Leonard confirms the move to the squad and checks that everyone knows Nathan leaves on Monday; this catches anyone who has not read Friday's SMS. No one is required to react in a particular way.

Keep emotions restrained and leave the score, scorers, minutes and specific match incidents open until drafting requires them.

After the final whistle, **Calvin Baxter**, who shares the midfield workload with Nathan, tells him the team will miss having him organize the transitions. Nathan immediately assumes, "They're being nice." Keep the line quiet and specific. Calvin's statement reflects their actual football partnership, not a generic farewell speech.

This shows self-undervaluation outside romance.

#### Scene 18 — coach
**Time:** 10:30–10:42, Saturday 12 September, field-side as the squad disperses.
Coach Leonard Holloway tells Nathan that he has leadership qualities. Nathan is embarrassed.

Leonard gives him one practical piece of advice: "When you join a new side, learn where their holding midfielder drops and when their wide players expect the ball before you start changing the distances." It comes from Nathan's habit of giving useful instructions to a familiar team. This is a brief, specific coaching note, not a grand farewell speech. Nathan remembers it when he first assesses the California team's routines on 19 September.

#### Scene 19 — moving logistics
**Time:** 11:15–14:30, Saturday 12 September, Callahan home.
The movers began packing at 08:00 while Nathan was at his final match. When he gets home after Coach Leonard's advice, the house is already changing around him; the crew continues inventorying, wrapping and loading the household shipment.

Nathan sorts books into a small personal-luggage selection ("must have now") and the larger shipment ("can wait"). The external monitor and bulky peripherals are packed with the household goods. His Intel MacBook, charger, compact input peripherals, essential notes, second-generation iPod touch and its cable stay together in his personal luggage, so the working project remains accessible until he leaves on Monday. The unfinished game is not installed on the iPod yet.

Heather labels an **essentials box** containing first-night kitchen items, basic linens and school/move documents, and ensures it will be accessible when unloaded in California. The movers keep an inventory and prepare the household shipment for its planned southbound leg; this is packing and logistics, not a shopping sequence or a new purchase.

---

### 13 September — last quiet Sunday

#### Scene 20 — final travel check
**Time:** 09:00–09:45, Sunday 13 September, Callahan kitchen/table.
The main shipment has been inventoried and loaded; the truck is on its southbound logistics schedule. The family does not re-decide which computer equipment or books are shipped—that was settled with the movers on Saturday.

Instead, they check the personal luggage and Monday itinerary: travel documents, school/relocation folder, chargers, Nathan's notebook and one book for the flight. Nathan confirms that his football kit stays in a separate tagged personal bag rather than in the bulk shipment, so it remains available after arrival. Clifford and Heather confirm the prebooked airport car for 05:30 Monday; their own family car is being transported separately, and the relocation vehicle will be collected in Los Angeles.

Nathan gets a small say in the personal items and room essentials he wants first, while the adult transport and housing arrangements remain his parents' responsibility.

#### Scene 21 — technical reading
**Time:** 10:00–11:00, Sunday 13 September, Nathan's study area.
Nathan revisits saved technical reading and his own notes on pathfinding and field-based navigation; he does not need a new book or a miraculous memory.

He recognizes a technique he has studied before. A* is solving a useful problem, but each guard is paying to solve much of the same route again. A shared cost/direction field could represent the reusable part: calculate the map toward a chosen target once, then let each guard consult the directions locally.

He sketches only the concept—a target, walkable cells and arrows pointing toward lower accumulated cost. He has not chosen the exact update scheme, solved dynamic obstacles or implemented a working flow field. This is a promising design hypothesis, not a finished answer.

#### Scene 22 — follow-up messages
**Time:** 18:30–19:00, Sunday 13 September, Nathan's room.
Nathan sends three separate SMS messages to **Calvin Baxter, Tristan Morrow and Devon Carver**. They already know about the move from Friday's team message and Saturday's pre-match confirmation; these messages are individual follow-ups, not a second announcement.

The replies reflect the boys' different concerns:
- **Calvin** asks how the new team sets up its midfield and says he would be interested to hear how its shape compares. This is practical curiosity from his usual midfield partner, not a promise to stay in constant contact.
- **Tristan** says the back line will take time to get used to organizing without Nathan's familiar cues. He does not turn it into a speech or ask Nathan to solve the replacement plan from another state.
- **Devon** says he is going to try Nathan's scanning/first-touch advice at the next practice. He asks one concrete question about when to play the safe pass; Nathan answers briefly and leaves selection decisions to Coach Leonard.

Nathan is glad they replied but discounts some of the warmth as ordinary politeness. No one promises a fixed call schedule or guarantees future minutes, friendship or results. The old life is ending through ordinary logistics rather than one dramatic farewell.

---

## MOVEMENT II — 14–15 SEPTEMBER
### The move

### 14 September

#### Scene 23 — travel from Seattle to the rental
**Time:** 05:30–11:30, Monday 14 September.
The family leaves home early, checks in at Seattle–Tacoma airport around 06:15, takes a morning flight to Los Angeles (working timeline: 07:30 departure, around 10:15 arrival), collects the temporary vehicle provided through Clifford's relocation package, and reaches the rental around 11:30. Keep the flight and ground transfers brisk but not instantaneous.

The movers packed and inventoried the household goods on Saturday 12 September; their truck travelled south on Sunday 13 September and is expected at the rental in the early afternoon. The family's personal luggage is separate from the moving shipment. Nathan carries his Intel MacBook, charger, compact peripherals, notebook, school/relocation folder and second-generation iPod touch with him; his football kit travels in its own tagged personal bag, not in the moving truck. Clifford carries his company laptop, credentials and handoff notes. The MacBook already has the current project and development tools. The main monitor, bulk books, furniture, kitchen boxes and most other belongings are in the moving truck. The family car is being transported separately and is not available yet.

#### Scene 24 — Clifford's California role begins
**Time:** 12:00–12:30, temporary rental, after key handoff and entry.
Once the family has entered the furnished house, Clifford uses the already-active internet connection and his company laptop for a short scheduled remote handoff call. The call confirms the transition plan, immediate priorities and the next day's contacts; it is not a full office day and he is not simultaneously working in a California office. Heather and Nathan handle the rental keys, relocation paperwork and immediate practical questions nearby.

The rental was chosen by the relocation coordinator for availability, commute and school-boundary reasons, not because anyone knew the Dunphys. The next-door location is coincidence.

#### Scene 25 — temporary rental / moving crew arrives
**Time:** 13:00–14:15, rental house.
The moving crew starts unloading the household shipment. The employer-arranged furnished rental already has beds, basic seating, a dining table and enough kitchen basics for the first days. The Callahans do not immediately replace every rented item with their own: bulky furniture, duplicate kitchen boxes, most books and nonessential cartons are staged in the garage/secondary storage area, while the essentials box and clothes/school items are brought into accessible rooms. A few boxes still block passageways and the family is far from settled.

Nathan puts his carried MacBook on the existing dining table and checks that the current project opens. He does not need the bulky monitor or to unpack the main computer setup to verify the build, and he makes no substantial new feature on moving day. Relocation interrupts his normal work block.

Heather checks the moving inventory and keeps the documents needed for the next day's school enrollment together. Utilities and internet were active before arrival, but the family car, bulk books and most peripherals remain out of normal use until delivery/unpacking.

#### Scene 26 — neighborhood introduction
**Time:** 14:20–14:35, driveway during unloading.
Phil introduces himself to the new neighbors and offers to carry one light box. Claire joins the introduction; Luke is nearby and asks Nathan about the football he has brought outside. Keep the exchange short, friendly and ordinary. The moving crew continues its work in the background, giving the encounter a practical reason to happen.

By the end, Phil and Claire know the Callahans' names and that they have moved next door. Luke knows Nathan as the new neighbor and has seen his football gear. Alex and Haley need not be present, and none of the three discovers anything about Nathan's private memories or feelings. The relocation company did not arrange the introduction; the neighbors simply notice the unloading.

#### Scene 27 — first night in California
**Time:** 19:00–20:00, rental.
After the main unloading activity has ended and a simple dinner is possible, Nathan checks the provisional school route and the instructions Heather has received. He also opens the unfinished game on the MacBook and reviews the current build without pretending that moving day offered a full programming session. The two problems are suddenly connected: he must rebuild a life and finish a project at the same time.

### 15 September — settling-in and school registration (mostly off-page)
**Working time:** 09:00–10:15, school office; later, back at the rental.
Heather and Nathan take the signed temporary lease, transfer documents and health/immunization paperwork to the school office. The address and initial enrollment have already been checked provisionally; this visit completes the in-person records review, confirms the timetable and first-day instructions, and ensures the previous school has been asked to forward any remaining records. Nathan is expected on campus on Wednesday 16 September. This is administrative preparation, not a school day or an early meeting with Alex.

Clifford uses the morning for the first in-person transition with the Southern California office; the 14 September remote handoff was only a short check-in, not his first full workday. Heather continues the relocation leave until her approved transfer begins on Monday 21 September. Back at the rental, they unpack immediate school essentials and make the route practical. The family car and most nonessential household goods are still not assumed available until their delivery is confirmed. No new major event is required; the move-day neighbor introduction remains on 14 September.

---

## MOVEMENT III — 16–23 SEPTEMBER
### First week at the new school / first contact with Alex

### 16 September — first school day

#### Scene 28 — arrival
Nathan is early.

He knows where the classrooms are only in theory.

He checks his schedule.

His new timetable differs enough from Seattle that the day feels unfamiliar.

#### Scene 29 — mathematics
Ms. Connie Harrington (the teacher tracked internally as `CA-MATH-01`) is teaching this eighth-grade section. She has transfer paperwork but no prior personal knowledge of Nathan.

Nathan answers carefully.

Teacher notices.

No reputation has followed him here.

This is important:
**he has to earn the new reputation from zero.**

#### Scene 30 — hallway: Alex
Nathan sees Alex.

Recognition.

He knows exactly who she is.

For several seconds he considers approaching.

Then:
- too awkward;
- she is with someone;
- he does not want to bother her;
- he will have another chance.

He walks away.

This is the first visible romantic self-sabotage.

#### Scene 31 — after-school football contact
Nathan speaks directly to **Coach Lance Conley** about joining the local side. Lance explains the next step and invites him to a coach-approved assessment; it is not a full practice or match yet.

Nathan observes that the new group has different habits from his Seattle team, but he has not earned local trust yet and is not captain. The first assessment remains scheduled for Saturday, 19 September, as an internal scrimmage.

#### Scene 32 — game
Evening coding.

Nathan's first flow-field attempt starts from his notes.

He gets the field mostly right.

Movement is fast.

Then two guards collide and behave badly.

He marks it rather than abandoning the method.

---

### 17 September

#### Scene 33 — school / Alex at distance
Library/academic context.

Alex is working.

Nathan notices.

He deliberately focuses on his own assignment.

A student asks Nathan a technical question.

Nathan explains naturally.

Alex may overhear part of it.

Nathan does not notice her noticing.

#### Scene 34 — English
Teacher catches Nathan over-editing a written answer.

The teacher says the answer was already good before he changed it five times.

Nathan is mildly embarrassed.

This becomes an early seed for his perfectionism.

#### Scene 35 — Haley's independent social life
At home, Haley arranges a social plan with Kristina Barlow while Claire asks about schoolwork and timing. Their disagreement is ordinary and specific rather than a new family crisis. Nathan is not present and is not the subject of the conversation.

This establishes Haley's existing social circle and Claire's parenting routine before the Pilot. The plan or scheduling disagreement should be recorded so it can be remembered if referenced later; any phone behavior and language must fit 2009.

#### Scene 36 — flow-field review
Nathan opens the reference material again.

He sees the connection between his measured bottleneck and the field representation.

Technical thought:
the expensive information should be shared; the cheap differences can stay individual.

---

### 18 September — first Alex conversation

#### Scene 37 — practical reason
Nathan is consulting the library's reference copy of a problem-solving book with mathematical maze/logic puzzles because he is thinking about grid pathfinding. Alex has come to check one section for an optional class problem-solving challenge and asks how long he needs the book.

The request is ordinary and practical, not a contrived romantic setup. Nathan knows exactly who she is.

Alex does not know that.

Conversation:
- practical;
- brief;
- mildly awkward;
- not romantic.

Nathan explains the material correctly.

He then worries that he sounded like he was correcting her.

Alex leaves thinking something closer to:
"He's weirdly helpful."

#### Scene 38 — after the conversation
Nathan replays the conversation in his head.

Not:
"She likes me."

Instead:
"She probably just needed the book."

This is the central self-undervaluation.

#### Scene 39 — evening coding
The first flow-field version works better.

Nathan smiles once.

Then notices a steering defect.

Perfect.

---

### 19–20 September — weekend bridge

#### Scene 40 — new football environment
On Saturday, Nathan attends a **coach-run internal assessment scrimmage**, not an official league match. This follows the contact with Coach Lance Conley on 16 September and gives the coach a reason to evaluate Nathan.

Nathan remembers Coach Leonard Holloway's advice to learn a new side's shape before trying to change it. He first watches how the California midfield and back line move together, then makes one useful adjustment only when a clear opportunity appears. His small gain in respect comes from adapting to the existing team's habits, not from immediately taking control.

Maxwell Whitaker is introduced as a possible friend. He wants more playing time and is wary of being overlooked, but he is not hostile. See [Maxwell's working profile](../../canon/characters/MAXWELL_WHITAKER.md).

Nathan does not become captain.

#### Scene 41 — home/family adjustment
Parents unpack.

Heather begins establishing a household routine.

Clifford spends long hours working.

Nathan finds the kitchen / local street / route to school unfamiliar.

The family opens an essentials box and gets a few daily routines working, but most belongings remain packed. Do not add a new purchase here unless it is named and entered in the object ledger first.

#### Scene 42 — Nathan + game
He works on local steering.

The enemies no longer get trapped as often.

Prediction remains absent or primitive.

#### Scene 43 — Alex echo
Nathan thinks about Friday's conversation while coding.

He notices that he has been smiling.

He immediately becomes annoyed with himself for losing concentration.

---

### 21 September — one ordinary weekday

There is **no birthday here** anymore.

#### Scene 44 — school
Nathan is beginning to know where things are. Ms. Harrington remembers his name and work from the first week. Wesley Moss, an eighth-grade technology/library peer, asks Nathan a concrete technology or homework question. Nathan responds helpfully without trying to show off.

This is the first evidence that a school acquaintance is becoming routine, not instant friendship. Wesley has his own workload and interests; record the specific question and answer if they become a later callback.

#### Scene 45 — Alex
Alex acknowledges him first.

A small exchange.

No big romantic beat.

The important change is that they now recognize each other.

#### Scene 46 — game
Flow field stable enough for multi-guard movement.

Nathan begins thinking about the second half:
What should the guard pursue?

Last-known position is too exploitable.

---

### 22 September

#### Scene 47 — school / Alex conversation 2
The practical reason is smaller.

The conversation lasts slightly longer.

Nathan begins speaking first for perhaps one sentence.

This is a genuine character milestone.

#### Scene 48 — football
Coach notices Nathan's tactical ability.

Maxwell asks him to help with a tactical situation.

The first shift toward friendship begins, but Maxwell still has his own goal of earning more playing time. They are not instant best friends.

#### Scene 49 — technical night
Nathan writes down:
**navigation ≠ destination selection**

This sentence can become the conceptual bridge to the prediction/influence field.

---

### 23 September — Pilot day

#### Parallel canon thread
The *Modern Family* Pilot occurs on its established date. The story uses the Pilot as background canon,
not as an excuse for Nathan to enter the central family reunion.

Potential parallel snippets:
- Dunphy household;
- Jay/Gloria/Manny;
- Mitchell/Cameron/Lily;
- their independent conflicts.

Nathan is elsewhere.

#### Nathan thread
- school is now his sixth school day in the building (16–18 and 21–23 September);
- Alex is no longer a stranger;
- he has a small football foothold;
- at night he works on the game.

#### Scene 50 — technical realization
He notices that a guard should not need to "know where the player is."

It needs a **weighted guess** about where to go.

He sketches:
- last sighting;
- direction;
- likely exits;
- recent choices.

This becomes the first version of the influence map.

#### End beat
Nathan has solved the conceptual problem.

He has **not** finished the implementation.

---

## MOVEMENT IV — 24–30 SEPTEMBER
### Consequences of the first week

### 24–25 September

#### Scene 51 — school reputation
Ms. Harrington, the same mathematics teacher who has seen Nathan's September work, asks a harder follow-up question. Nathan reasons through it.

The teacher then mentions the school's optional maths-enrichment/competition group as a possible next step. Nathan assumes the suggestion may be generic encouragement because he is new; he does not sign up on the spot. The exact meeting date and commitment are not fixed until the follow-up is developed and recorded.

#### Scene 52 — Alex
Brief conversation without homework.

Alex is curious about the computer project.

Nathan gives a deliberately simplified explanation.

He is relieved she understands.

#### Scene 53 — football
**Maxwell Whitaker** cooperates with Nathan on one specific attacking/defensive transition. Maxwell still wants to earn more playing time; he is willing to use Nathan's suggestion because it solves a real problem in the drill, not because he instantly admires the new arrival.

Their relationship moves one step.

#### Scene 54 — household detail
In the Callahan rental, Heather unpacks a blue ceramic mixing bowl that travelled from the Seattle kitchen in a kitchen box. It is placed in the usable kitchen and helps a routine meal feel less temporary. The bowl is established family property, not a new purchase or a symbolic object by default. Track its location and condition from here on.

#### Scene 55 — prediction layer
Nathan tests a route:
- player always escapes left;
- guards begin searching left.

Then he makes the model more uncertain.

The behavior becomes more believable.

---

### 26–27 September

#### Scene 56 — weekend football
Nathan starts becoming part of the team without being appointed captain.

The social identity is transferring.

#### Scene 57 — the rental starts to feel lived-in
Clifford, Heather, or Nathan unpacks a framed family photograph from a Washington-coast outing in summer 2008 and places it on a shelf. Keep the exact outing broad unless later detail becomes necessary; do not invent unnamed people in the photograph.

The photograph has travelled with the family and is now visible in California. This quiet prop gives the old home a physical presence without requiring a speech about missing Seattle. Track its location if it is moved later.

#### Scene 58 — game test
20+ enemies.

Flow field handles the global navigation.

Prediction field handles destination.

Local steering handles the mess.

The architecture finally feels coherent.

---

### 28–29 September

#### Scene 59 — school
Nathan now has one classmate who regularly talks to him.

Important:
the classmate is not suddenly a best friend.

#### Scene 60 — Alex / ordinary exchange
A short, ordinary exchange at school gives Nathan a chance to minimize a small success or begin an unnecessary apology over something minor. Alex does not call attention to it or interpret it as a settled pattern; at this point, they have only spoken a handful of times.

The conversation moves on naturally. This is, at most, another small observation—not a diagnosis or a relationship milestone.

**Reserved for much later:** keep the line "You know you don't have to apologize every time you're right" as a possible future line, but do not use it until Nathan's habit has been shown repeatedly over many chapters to both the reader and Alex, and their relationship has earned that directness.

#### Scene 61 — evening
Game is almost a real vertical slice.

Nathan discovers:
- unnecessary updates;
- a cache opportunity;
- one collision bug.

He keeps working.

#### Scene 62 — Alex's independent evening
At the Dunphy home, Alex practices cello, becomes frustrated with a passage, and returns to homework. Nathan is not present. This is about Alex's own high standards and school routine, not a message about Nathan or a romantic beat.

Alex's life continues off-page; unless she actually mentions Nathan in this scene, he learns nothing from it.

---

### 30 September — The Bicycle Thief / Episode ending

#### Parallel canon
*The Bicycle Thief* occurs on this date. Its main story can be shown independently:
Phil/Luke/bike, Jay/Manny and Mitchell/Cameron/Lily threads. citeturn191690search0turn191690search2

Nathan does not suddenly become part of it.

If a later consequence matters, note it in the plot bank instead of forcing an interaction.

#### Nathan thread
The current build has:
- stable shared flow field;
- functional local steering;
- early prediction layer;
- enough content to feel like a real game.

But the build is unfinished.

#### Final image
Nathan watches 20+ guards move through the map.

It looks good.

He opens the profiler.

He sees things he still wants to fix.

**Episode ends.**

## State transfer to Episode 2

Nathan:
- 13;
- relocated;
- old life established in memory;
- new school foothold;
- one recurring classmate/teammate;
- increasingly comfortable with Alex;
- still severely underestimates himself.

Alex:
- knows Nathan;
- has initiated contact;
- has begun noticing his personality;
- has curiosity beyond schoolwork.

Football:
- Nathan is not captain;
- Maxwell Whitaker is becoming a friend through specific tactical cooperation, though the friendship is still early;
- coach respects him.

Family:
- temporary rental now feels less temporary;
- Clifford's job is consuming more time;
- permanent house purchase remains a later story.

Game:
- flow field is the main navigation method;
- steering works;
- prediction layer exists;
- optimization and release remain.

## Word-count architecture

Target **10k–14k+**.

A useful distribution is:

- 2,000–2,500 words: old life / birthday / school / football;
- 1,500–2,000: promotion and move;
- 2,500–3,000: new school / Alex first week;
- 2,000–2,500: game development;
- 1,500–2,000: parallel family/canon/background material.

This is a guide, not a quota. Strong scenes should expand naturally.

## Drafting warning

Do not show every day.

Use dates heavily in the underlying timeline, but let prose jump:
"By Friday..."
"Over the weekend..."
"Three days later..."

The reader should feel time passing without reading a diary.


## Scene-state and cast continuity gate (updated 13 October)

The outline is not permission to improvise whoever happens to be present. Before prose drafting, use the [Episode 1 Scene-State Ledger](EP01_SCENE_STATE_LEDGER.md) for the date-specific pre-state and carry-forward delta of every scene. Use [Character State Continuity Standard](../../canon/characters/CHARACTER_STATE_CONTINUITY_STANDARD.md), [Modern Family Core Character State Baselines](../../canon/characters/MODERN_FAMILY_CORE_STATE_BASELINES.md), [Football Teams and Player Backgrounds](../../canon/characters/FOOTBALL_TEAMS_AND_PLAYERS.md), and the [Knowledge and Skill Ledger](../../canon/characters/NATHAN_KNOWLEDGE_AND_SKILL_LEDGER.md) as persistent sources of truth.

Specific controls for this episode:
- On 7 September, any football beat must be solo/informal rather than scheduled school practice, because the date is Labor Day.
- Scenes around 9–12 September use the Seattle lineup, coach Leonard Holloway and the squad's existing relationships. Record the reason and date when the team learns that Nathan is moving.
- The scene around 19 September uses the new Southern California squad and coach Lance Conley; Nathan is a new teammate, not captain. Treat the activity as a scrimmage until an official fixture is justified.
- Every old-team player who speaks, makes a meaningful run, responds to the move or affects the match needs a scene-date state update, including minutes, knowledge of the move, mood, relevant past exchanges and physical condition.
- Alex's school peers and Haley's friends are not invented in the moment of a conversation. Use [Secondary Social Circles](../../canon/characters/SECONDARY_SOCIAL_CIRCLES.md), then deepen anyone who takes a meaningful role.
- Nathan turns thirteen on 7 September 2009. The prior-life transition roughly two weeks earlier is a distinct event, not a contradiction; see DEC-012.
