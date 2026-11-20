# Season 1, Episode 3 — Vector Trajectories and Street Physics

<!-- WD-001 -->
<!-- WD-002 -->
<!-- WD-003 -->
<!-- WD-004 -->

**Story Window:** October 16–31, 2009  
**Status:** COMPLETE STRUCTURAL DRAFT — BELOW THE OUTLINE'S 10,000–14,000 WORD TARGET  
**World-canon note:** Episode titles are labels from Nathan's previous-life memories. In this timeline, the families are experiencing real events; no current-world broadcast is implied.

**Active Threads:**
- Thread A: C++ Engine / Spatial Partitioning & AABB Physics on 3GS (Nathan solo)
- Thread B: Midterm Science Preparation & Algorithmic Kinship (Nathan & Alex Dunphy)
- Thread C: The Slingshot, the Ball, and the Lost Compass (Nathan & Luke Dunphy)
- Thread D: Callahan Family & California Suburban Rhythm (Nathan, Clifford, Heather)
- Thread E: The Westwood Antiquarian Bookshop / Feynman Discovery (Nathan & Heather)
- Thread F: Neighborhood Encounters & The Front Porch (Nathan, Phil Dunphy, Haley Dunphy)

---

## MOVEMENT I: OCTOBER 16–21 — SPATIAL PARTITIONS AND LIBRARY SILENCE

### Scene 1 — October 16, 2009 (Friday): The Square Root Bottleneck

The cooling fan inside the fifteen-inch unibody MacBook Pro [PROP-001] hummed at 4,200 RPM, exhausting a steady plume of lukewarm air against the dark mahogany surface of the desk.

Nathan sat with his bare heels hooked over the lowest rung of his swivel chair, a white ceramic mug of room-temperature tap water resting on a cork coaster by his elbow. In the center of the display, the Instruments profiling utility painted an unforgiving picture in jagged red lines.

The mobile CPU was gasping for air.

At two hundred autonomous agents, the flow field pathfinding algorithms he had stabilized two weeks earlier still routed entities cleanly across the discrete potential gradient. But the moment Nathan activated pairwise entity-to-entity collision avoidance, the frame rate dropped off a cliff: twenty-four frames per second, accompanied by intermittent hitching that turned smooth motion into a staccato slide-show.

Nathan reached for his black ballpoint pen and tapped the metal spiral of his grid notebook [CLUE-002].

The mathematics behind naive collision detection was brutally straightforward, and that was precisely the trap. Two hundred agents meant checking each entity against every other entity in the simulation loop. That was $N \times (N - 1) / 2$ checks every single tick: nineteen thousand, nine hundred pairwise distance evaluations per frame. At sixty frames per second, the routine demanded roughly 1.194 million pair checks — and up to 1.194 million square-root evaluations — every second. The iPhone 3GS's six-hundred-megahertz ARM Cortex-A8 also included a NEON SIMD unit, but this version of the engine was scalar C++ and made no use of those vector instructions. The problem was the number of pairwise comparisons, not an absence of vector hardware.

`sqrtf()` was killing the pipeline.

— Inefficient, — Nathan murmured to the quiet bedroom.

He closed the terminal window running the OpenGL debug view, stretched his arms above his head until his thoracic spine gave three crisp pops, and took a small sip of water.

The solution was not to optimize the square-root calculation; the solution was to never ask the question in the first place. Entities at opposite corners of the map had zero probability of colliding. Testing distance between an actor at coordinate `(12, 45)` and an actor at `(580, 420)` was wasted silicon cycles.

Nathan leaned forward and opened a clean buffer in his text editor: `SpatialGrid.hpp`.

He drafted a uniform regular spatial partitioning grid. The virtual screen—four hundred and eighty by three hundred and twenty pixels—was segmented into a two-dimensional array of square cells, thirty-two pixels on a side. Fifteen columns by ten rows: one hundred and fifty lightweight memory buckets.

Instead of computing expensive Euclidean distances with floating-point square roots, an entity determined its cell occupancy through integer bit-shifting:

```cpp
inline uint32_t GetCellIndex(int32_t x, int32_t y) {
    return (uint32_t)((x >> 5) + ((y >> 5) * GRID_COLS));
}
```

Bit-shifting by five divided a non-negative screen coordinate by thirty-two. During each frame tick, an entity registered its pointer into its local bucket. Because the moving agents' collision boxes were kept smaller than a cell, an actor only needed to inspect its own bucket and the eight adjacent neighbors. Larger static bounds were registered in every cell they overlapped, so the local query could not miss an obstacle merely because its box crossed a cell boundary.

Nathan saved the header, linked it into the collision manager, and refactored the bounding volumes into Axis-Aligned Bounding Boxes (AABB). The inner loop was reduced to four simple integer comparisons:

```cpp
inline bool CheckOverlapAABB(const Box& a, const Box& b) {
    return (a.maxX >= b.minX && a.minX <= b.maxX &&
            a.maxY >= b.minY && a.minY <= b.maxY);
}
```

He typed `make clean && make -j2` into the terminal. The compiler chewed through the translation units without a single warning.

Nathan plugged the white 30-pin dock connector into the test iPhone 3GS [PROP-004] lying beside his mousepad. Xcode built the bundle, signed the binary with Clifford’s provisioning certificate, and uploaded the executable to the device.

On the 3.5-inch glass screen, two hundred green circular entities bloomed inside the maze.

Nathan touched the screen, dragging the target crosshair diagonally across the viewport. The green swarm surged through the corridors, parting around concrete pillars, sliding past each other through the choke points without overlapping, without jittering, and without pausing to recalculate global matrices.

In the bottom-right corner of the overlay, the green diagnostics readout held firm:

`FPS: 60.0 | CPU: 21.4% | MEM: 27.8 MB`

Nathan rested his chin on his knuckles, his blue eyes softening as the tension in his shoulders released.

— Clean, — he whispered. — Fast, predictable, and quiet.

Down the hallway, the floorboards creaked as his mother walked past to start the laundry. Outside, the Southern California twilight settled over Cheviot Hills in long streaks of indigo and amber. Nathan closed the laptop lid to sleep mode, set his pen neatly across his notebook, and went downstairs to help set the table for dinner.

---

### Scene 2 — October 19, 2009 (Monday): The Grid Notebook and the Library Table

By three-twenty on Monday afternoon, the school library was a sanctuary of filtered air and muted fluorescent hum.

Outside, the October sun beat down on the blacktop courts where seventh-graders were shouting over a four-square ball, but inside the stacks, the heavy scent of aging buckram bindings and lemon furniture oil deadened the noise of the campus to an indistinct murmur.

Nathan sat at a four-top oak reading table in the corner of the 500-level science section. Before him lay an open lined binder containing Mr. Henderson’s biology review packet, his Casio digital watch reading 3:24 p.m. To his left, propped at a forty-five-degree angle against his canvas pencil case, his spiral grid notebook [CLUE-002] was open to a double-page spread of handwritten vector diagrams: flow direction arrows penciled in blue ink, potential-field gradient curves plotted on millimeter Cartesian grids, and pseudocode notes on neighbor-cell queries.

The opposite chair was pulled back with a deliberate, assertive scrape.

Alex Dunphy sat down.

She did not ask if the seat was taken; in the social economy of the eighth-grade honors track, the quiet table by the science stacks had become their unspoken demilitarized zone. She swung her heavy backpack onto the floor with a dull thud of textbooks, immediately arranging four spiral notebooks in a descending stair-step pattern across the wood. She was wearing a plum-colored cotton cardigan over a white button-down shirt, her dark hair pulled back into a utilitarian ponytail that revealed the sharp, alert line of her jaw.

Between her eyebrows, a faint vertical crease testified to four consecutive hours of hyper-focused pre-exam tension.

— The district chemistry curriculum is an insult to basic thermodynamics, — Alex announced without looking up, clicking a black ballpoint pen three times with machine-gun velocity. — Henderson spent forty minutes trying to explain enthalpy using an analogy about baked potatoes. Potatoes, Callahan. Like we’re in an agricultural vocational school in 1890.

Nathan did not lift his head immediately, finishing the chemical equation for cellular respiration on his worksheet with steady, unhurried strokes.

— Potatoes have high specific heat capacity, — he said mildly, his voice keeping to the library’s lower octave. — From an experiential standpoint, middle-schoolers understand burning the roof of their mouth on starch better than they understand Joules per mole Kelvin.

Alex paused her pen mid-stroke and glared across the oak surface.

— You always do that, — she said.

— Do what?

— You defend mediocrity by finding a functional justification for it. It’s infuriating. Henderson gets paid a district salary to teach eighth-graders physical science, not to comfort people who can’t conceptualize a thermal gradient.

Nathan capped his pencil and looked across at her. Behind her rectangular wireframes, her dark brown eyes were rimmed with faint violet shadows—the unmistakable signature of someone who studied until one in the morning, woke up at six to review vocabulary flashcards, and considered seven hours of sleep a character flaw.

— It’s not defending mediocrity, — Nathan replied gently. — It’s recognizing the audience. If you teach the optimal algorithm to hardware that doesn't have the registers to execute it, the system crashes. Henderson is just throttling the bitrate so the room doesn't catch fire.

Alex stared at him for three seconds, her lips pursed in that razor-thin line she used whenever someone presented an argument that was inconveniently logical.

Her gaze drifted down from his face to the open pages on his left.

Her eyes tracked the neat Cartesian grids, the blue vector arrows originating from discrete cell centers, and the handwritten algebraic formulas for linear interpolation. She leaned forward half an inch, her ponytail swinging over her shoulder.

— What is that? — she asked, her tone shifting instantly from combative to analytically forensic.

Nathan felt that instinctive, familiar reflex tighten in his throat: the urge to pull the notebook shut, to slide it under his textbook, to minimize his presence before someone accused him of being arrogant or showing off. In his previous life, drawing attention to advanced technical work in middle school usually earned you either resentful mockery from peers or isolating expectations from teachers.

He forced his hands to remain flat on the table.

— It’s personal notes, — he said quietly.

Alex didn't accept the deflection. She reached across the wood, planted two index fingers on the top wire spiral of his notebook [CLUE-002], and pulled it three inches closer to her side of the table.

— That’s not eighth-grade math, — she said, scanning the pencil annotations. — These are directional vector derivatives on a discrete grid. Are you calculating fluid dynamics?

— Not fluid dynamics, — Nathan said, feeling a warmth rise beneath his collar. — Pathfinding. It’s for navigation in a simulation. Instead of having every entity calculate its own path using an A-star search tree, you calculate a global potential field once for the entire grid. Every cell stores a vector pointing downhill along the gradient toward the goal.

Alex traced an arrow with the back of her fingernail, her brow smoothing out as she absorbed the abstraction.

— So the actors don't think, — she murmured. — They just read the vector of the square they're standing on.

— Exactly. It changes the complexity from polynomial to linear.

Alex studied the diagram for another moment.

— I tried to borrow Feynman's first volume from the municipal library last month, — she said. — Their copy had disappeared. Someone apparently walked off with it; the later volumes are still there.

Alex looked up from the page, her brown eyes inspecting Nathan with an intensity that felt like a full system diagnostic. There was no mockery in her expression, nor the patronizing indulgence adults often used when a child did something clever. There was only that rare, pure, slightly stunned recognition that she was looking at a peer.

— Why aren't you in the high school math placement track? — she asked abruptly. — You could have tested into pre-calculus at the district center in September.

Nathan picked up his eraser and rubbed away a stray graphite smudge on his binder margin.

— Moving from Seattle was enough disruption for one semester, — he said softly. — Skipping grades just puts you in classrooms with kids who have driving permits and resent you for existing. I’d rather keep my head down and write code in the evenings.

Alex leaned back against her chair, studying him across the table. Her yellow highlighter rested forgotten between her fingers.

— You're terrified of people noticing you, aren't you? — she asked. The question wasn't cruel; it was delivered with the blunt, surgical clarity of a girl who spent her life underestimating nobody and forgiving nothing. — You spend half your energy pretending you’re just an average transfer kid who likes soccer, because if people realize how fast your brain works, they’ll start demanding things.

Nathan felt his pulse thud against his ribs. He didn't look away, but his voice was quiet enough that the librarian two aisles over didn't even twitch.

— It’s not about demands, Alex. It’s about quiet. If you make too much noise about what you know, people stop treating you like a person and start treating you like an appliance. You end up alone on a pedestal, and the view up there isn't worth the draft.

Alex went very still. For a fleeting heartbeat, behind the defensive armor of her GPA and her color-coded binders, something raw and vulnerable flickered across her face—the ghost of a girl who lived in a loud house where nobody understood why she couldn't just relax, where her sister thought she was a freak and her parents cheered for soccer goals while her academic awards gathered dust on the hall credenza.

She swallowed, looked down at her biology packet, and picked up her pen.

— Henderson’s still an idiot about the potatoes, — she muttered, though her voice lacked its earlier sting.

— On that point, — Nathan said with the faintest shadow of a smile, — the consensus is unanimous.

They worked in silence for the next twenty minutes of the after-school library block, the rhythmic scratching of their pens against the paper the only sound between them.

---

### Scene 3 — October 21, 2009 (Wednesday): Parallel Domestic Evenings

Wednesday night brought a dry Santa Ana breeze down through the canyons, rattling the dry palm fronds along the driveway and filling the evening air with the scent of sagebrush and warm asphalt.

Nathan sat at the round oak dining table in the Cheviot Hills house, peeling potatoes into a stainless-steel bowl of salted cold water while Heather sliced zucchini on the cutting board. At the kitchen island, Clifford had his corporate laptop open beside an uncorked bottle of Central Coast Pinot Noir, his reading glasses perched low on his nose as he scanned server uptime metrics for his division's California rollout.

— The latency spikes between the San Jose datacenter and the El Segundo hub are down four milliseconds since Tuesday, — Clifford said, reaching for his wine glass without lifting his eyes from the terminal. — The routing tables had three redundant hops through Denver. Someone in network operations was sleeping on legacy fiber contracts.

— As long as you don't have to fly up to the Bay Area before the weekend, — Heather replied, the rhythmic *thok-thok-thok* of her chef's knife keeping steady meter. — The relocation coordinator called today about the rental's extension clause and the utility transfers. They want to know before Friday whether we need to keep the place through December.

— I’ll sign the declaration form before Friday, — Clifford said, closing the laptop with a crisp snap that signaled the formal boundary between the workday and family dinner. He looked over at Nathan, watching his son's economical, methodical peeling motion. — How’s the school soccer squad looking, Nathan? Whitaker still trying to take your shins off in practice?

Nathan placed a cleanly peeled Yukon Gold potato into the water.

— We played an intra-squad scrimmage yesterday, — Nathan said evenly. — Maxwell scored twice from the right touchline. He’s fast if you give him a leading ball into open space.

— And you?

— Anchored defensive midfield, — Nathan said. — Distributed from the back. Coach Reynolds had us working on shape recovery.

Clifford nodded, a quiet paternal pride settling in the corners of his eyes.

— Good. Soccer is like a distributed systems cluster: the team that wins isn't the one with the flashiest node; it's the one with the lowest communication packet loss. Keep feeding the front line, but don't let them drag you out of position.

— I won't, Dad.

Across town, four miles to the north, Nathan knew from his previous-life memories that this was the evening corresponding to the family events he remembered under the *Coal Digger* label: the Pritchett and Dunphy families gathering at Jay and Gloria’s house, Luke repeating an overheard insult and setting off a domestic storm, Claire finally jumping into the pool with her clothes on after Gloria challenged her, and Jay pulling Gloria into the water moments later before the rest of the family joined them. Nathan remembered the awkward reconciliation as clearly as the chaos that preceded it.

Nathan set the peeler down on the counter.

He felt no compulsion to drive up to Brentwood, to peek through the privacy hedges, or to confirm whether the pool water was cold. Those were real people living real, messy, vulnerable lives. They had their own private gravity, their own misunderstandings, and their own resilience. His presence in Los Angeles was an original factor, not a license to treat their family dinner as an entertainment broadcast.

— Dinner in fifteen minutes, — Heather said, wiping her hands on her linen apron. — Nathan, grab the salad tongs from the drawer, please.

— Right away, Mom, — Nathan said, stepping toward the pantry.

The parallel world spun on its axis: stable, grounded, and entirely sufficient.

---

## MOVEMENT II: OCTOBER 22–24 — THE SLINGSHOT AND THE ANTIQUARIAN BOOKSHOP

### Scene 4 — October 22, 2009 (Thursday): The Soccer Ball, the Catapult, and the Compass <!-- EVT-014 | 2009-10-22 | 2009-10-22 -->

The late afternoon sun slanted low across Rancho Park, casting long, razor-sharp shadows across the dry municipal berms.

Nathan was sixty minutes into an individual conditioning session on the lower athletic field. His gray T-shirt was darkened with sweat across the shoulder blades, his Casio watch [PROP-005] beeping softly to mark the conclusion of his forty-yard interval sprints. At his feet sat his scuffed Seattle training ball [PROP-003], the black-and-white hexagonal panels worn smooth from two seasons of Pacific Northwest rain and California turf.

He set the ball on the penalty arc, stepped back three paces at a thirty-degree angle, approached with a low center of gravity, and drove his right instep through the center of the leather.

The ball launched with a sharp, concussive *thwack*, rising in a tight spiral toward the upper-right corner of the goalframe.

It caught the underside of the galvanized crossbar with a loud metallic clang, rebounded upward at an extreme trajectory, cleared the ten-foot chain-link safety fence at the park boundary, and disappeared into the dry, tangled vegetation bordering the pedestrian walking trail.

Nathan exhaled, wiping his forearm across his forehead.

— Too much lift on the follow-through, — he murmured to himself.

He unlatched the pedestrian gate at the corner of the fence and jogged down the dirt embankment toward the walking path.

Ten yards ahead, crouching behind a dusty oleander bush like an infantry sniper in cargo shorts, was ten-year-old Luke Dunphy.

Luke was wearing a faded graphic T-shirt featuring a cartoon skateboarder, high tube socks pulled up to his shins, and dirty skate sneakers with the laces untied. In his left hand, he held an extraordinary homemade launcher: a Y-shaped fork carved from a thick sycamore branch, reinforced with gray duct tape, and fitted with two thick strips of red rubber tubing attached to a shallow pouch cut from an old leather work boot.

Beside Luke’s sneakers sat Nathan’s soccer ball [PROP-003].

Luke was trying to force the regulation size-five soccer ball into the boot-leather pouch. It was plainly too large, but he kept adjusting the tubing with his tongue clamped firmly between his teeth in an expression of terrifying scientific concentration.

Nathan stopped six feet away, his hands resting lightly on his hips.

— Physics is going to win that argument, you know, — Nathan said quietly.

Luke jumped half an inch, startled, and swung the sycamore branch toward Nathan with wild theatrical defensiveness before realizing the older boy wasn't angry.

— I'm returning your ball! — Luke announced, his voice carrying that breathless, high-frequency enthusiasm of a boy whose brain generated seventy-five ideas a minute and executed seventy-four of them without a safety helmet. — But kicking it back through the gate is boring. I built an artillery catapult! I think it has three hundred pounds of draw weight!

Nathan glanced at the red surgical tubing, which was stretched to its absolute elastic limit around the sycamore fork, creaking ominously under tension.

— That tubing is already stretched too far, — Nathan observed mildly. — If it snaps, the fork can kick back toward your face. And the ball is too large for that pouch; it could slip sideways before you even release it.

Luke blinked, looking down at his weapon, then back up at Nathan. He loosened the draw tension by half an inch.

— Are you sure?

— Newton's third law means the band pulls back on the fork as hard as it pulls the pouch forward, — Nathan said. — If you don't brace the frame, it can kick toward your face. And because the ball doesn't fit the pouch, it could slip out sideways. Set it down and let me show you a safer way to return it.

Luke considered this for two seconds, deeply impressed by the mechanical diagnosis.

— Wow. You really are like a cyborg. My dad says you run at atomic clock speed.

— I run at sixty-five percent max heart rate, — Nathan corrected politely. — It just looks steady because I don't sprint until the final interval.

Luke let the rubber tubing go slack and picked up the soccer ball with both hands.

— Anyway, you got lucky, — Luke said, digging into the deep side pocket of his baggy cargo shorts. — When your ball flew over the fence, it hit that thick ivy bush over there. And when I went in to get it, I found this stuck in the roots right next to the park bench.

Luke held out his hand.

In his grubby palm lay a heavy, circular object of tarnished brass: a vintage pocket compass on a braided leather cord [CLUE-001]. The bevel was scratched from tumbling into the brush two weeks earlier, but the sapphire-jeweled needle still floated freely, its red magnetic tip trembling toward magnetic north.

Nathan felt a sudden, genuine jolt of relief. He hadn't realized how much he’d missed the tactile familiarity of that compass—a gift from his maternal grandfather before the family left Washington.

— My compass, — Nathan said, stepping forward. — I looked for this under the bench for an hour after practice on the eighth. I thought it was gone for good.

He took the compass from Luke’s hand, turning it over to check the brass casing. It was intact.

— It has real glass on top! — Luke said, bouncing on his heels. — And an arrow that moves without batteries! Are you an undercover tracker? Like in the movies where the government guy has to find a fallen satellite before the Russians get it?

Nathan slipped the leather cord around his wrist, looking down at Luke with quiet amusement.

— I’m just an eighth-grader who likes old navigation tools, Luke. No satellites, no Russians.

— That’s exactly what a secret agent would say, — Luke said wisely, nodding to himself with utter certainty. — Don't worry. I know how to keep classified secrets. My dad tells me classified things all the time, like where Mom hides the emergency chocolate chips in the laundry room.

Nathan smiled—a real, uncalculated smile that reached his eyes.

— Well, classified or not, you saved me having to buy a new compass. Thank you, Luke. That was honest of you.

Luke puffed out his chest, delighted by the sincere praise.

— No problem! If you ever need anything launched over a wall, I'm modifying this slingshot with garage door springs next week!

— Let's test the spring tension on an empty cardboard box first, — Nathan suggested tactfully, tucking his soccer ball under his arm. — Your eyebrows will thank you.

Luke grinned, gave an exaggerated, two-fingered military salute, and went bounding down the path toward the Dunphy house, trailing his sycamore branch through the dust like an explorer returning from uncharted territory.

---

### Director's Cut 1 — October 22, 2009 (Thursday Evening): The Treehouse Bureau of Investigation

Up in the crown of the old camphor tree in the Dunphy backyard, the wooden floorboards of Luke's treehouse creaked under the weight of three milk crates and a vintage Coleman battery lantern.

Outside, the darkness was complete, punctuated only by the occasional bark of a neighborhood dog and the distant whine of traffic along the freeway.

Luke sat cross-legged on a damp foam cushion, an unpeeled banana resting on his knee, examining his operations desk: an overturned plastic recycling bin covered in classified evidence.

He pulled a gray metal shoe box out from beneath a bundle of frayed nylon rope. Inside lay his most prized possessions: a fossilized shark tooth from a third-grade field trip, three burnt-out nine-volt batteries, a plastic magnifying glass with a cracked lens, an Allen wrench wrapped in blue electrical tape, and a notebook where he drew schematics for a rocket powered by mentos and diet cola.

Luke picked up his red crayon.

On the back of a folded pizza receipt, he drew a stick figure with spiky hair, labeled it `NATHAN (AGENT X)`, and drew an arrow pointing to a circle labeled `MAGNETIC COMPASS`.

— Subject does not run like a normal person, — Luke whispered aloud, narrating his official intelligence report into the empty darkness of the tree canopy. — Subject moves in straight lines. Subject knows about Newton's three laws of explosives. Subject has a brass compass from World War Two.

Down in the kitchen, the back door opened, and Phil's voice drifted through the screen door into the autumn night:

*«Luke! Ten minutes until bath time! If you aren't downstairs by seven-thirty, I’m letting your mother supervise the shampoo rinse and you know she doesn't care about the tear-free formula!»*

— Copy that, Base Command! — Luke yelled back into the darkness.

He carefully placed the crayon back into the shoe box, closed the metal lid with a satisfying metallic latch, and secured it under his foam cushion.

Nathan Callahan was definitely a secret agent. And Luke Dunphy was officially his primary field contact.

---

### Scene 5 — October 24, 2009 (Saturday): Second Chance Books in Westwood <!-- EVT-015 | 2009-10-24 | 2009-10-24 -->

Saturday morning in Westwood Village had that distinctly collegiate, slow-waking rhythm of an autumn weekend near a major university.

The air was brisk and clean, smelling of roasted espresso beans from the corner cafes and eucalyptus leaves damp from morning sprinklers. UCLA students in gray athletic hoodies hurried toward the campus libraries with travel tumblers, while suburban families browsed the sidewalk displays outside the boutique shops on Westwood Boulevard.

Nathan accompanied Heather down the brick sidewalk. His mother looked relaxed in cream-colored slacks and a charcoal knit sweater, holding an architectural folder under her arm.

— The district planning office is reviewing the facility permits on the Wilshire campus, — Heather said, checking the store directory on her mobile phone. — I need twenty minutes in the blueprint drafting center to verify the scale drawings for the mechanical retrofits. Do you want to come inside, or do you want to explore the block?

Nathan pointed across the street to a narrow storefront nestled between a vintage record shop and a Mediterranean bakery. A forest-green canvas awning hung over a recessed bay window filled with stacked volumes, bearing faded gold leaf lettering: *Second Chance Books — Rare, Academic & Out-of-Print*.

— I’ll browse the bookstore, — Nathan said. — I have my watch. I’ll meet you back at the drafting center steps at eleven-fifteen.

Heather smiled, reaching over to smooth the collar of his jacket with maternal warmth.

— Don't spend all your allowance on dusty engineering manuals, Nathan. We have twenty boxes of books still waiting for shelf space in the study.

— Only looking, Mom.

He waited for the pedestrian signal, crossed the street, and pushed through the heavy wooden door of the bookshop.

A small brass bell tinkled overhead.

The interior was a labyrinth of floor-to-ceiling cedar bookshelves, organized in narrow, towering aisles that smelled intoxicatingly of lignin, vanilla, dried binding glue, and decades of quiet human curiosity. At the front counter, an elderly clerk with wire-rimmed spectacles and a beige wool cardigan was engrossed in a crossword puzzle, acknowledging Nathan with a brief, approving nod before returning to his pencil.

Nathan navigated intuitively toward the back of the store: past the twentieth-century American literature, past the European history stacks, into the quiet, dust-mottled alcove marked *Exact Sciences, Physics & Applied Mathematics*.

His eyes skimmed the titles: *Landau & Lifshitz Course of Theoretical Physics*, *Goldstein's Classical Mechanics*, vintage Dover paperbacks on partial differential equations with yellowed spine creases.

Then, on the second shelf from the bottom, his gaze stopped.

A heavy, clothbound volume bound in deep, saturated crimson cloth, stamped with clean gilt lettering along its broad spine:

*THE FEYNMAN LECTURES ON PHYSICS — VOLUME 1: MAINLY MECHANICS, RADIATION, AND HEAT.*

Nathan approached the shelf with deliberate slowness, extending his right hand.

He lifted the volume carefully by its cloth spine, feeling the substantial weight of the thick, cream-colored pages. He opened the front board. The title page confirmed the edition: Addison-Wesley Publishing Company, 1964 printing. The iconic red cloth binding [PROP-006] was intact, the corners square and unbruised, the cloth pristine except for a faint pencil price marking on the top corner of the flyleaf: `$25.00`.

Nathan opened the table of contents: *Chapter 4: Conservation of Energy. Chapter 7: The Theory of Gravitation. Chapter 11: Vectors.*

His mind flashed back to Monday afternoon in the school library: Alex Dunphy sitting across the oak table, her tired brown eyes tracing his vector diagrams, her voice dropping as she admitted her frustration that the middle-school curriculum treated physics like a series of recipes to memorize rather than a coherent language to explore. She had also mentioned trying to borrow Feynman's first volume from the municipal library, only to discover that the copy had gone missing. Someone had apparently walked off with it.

Nathan turned the smooth cream pages under his fingertips.

Richard Feynman’s voice leapt off the paper—vivid, irreverent, brilliant, grounding the most complex cosmological mechanics in tangible, physical common sense.

Nathan checked his canvas wallet. Inside were two five-dollar bills and a crumpled one-dollar bill: eleven dollars of saved weekly allowance. He was fourteen dollars short.

He closed the volume with reverence, feeling the satisfying, solid thud of the binding.

He did not hide the book behind other volumes—that was dishonest, and the universe had a way of punishing small petty cheats. Instead, he slid the crimson volume [PROP-006] back into its precise slot between an oversized volume on quantum electrodynamics and a monograph on statistical mechanics, ensuring the spine was flush with the shelf edge.

He had four weeks until Thanksgiving. With two weeks of saved allowance and fifteen dollars for helping Clifford sort the corporate hardware inventory in the garage next weekend, he would have thirty-five dollars.

Nathan checked his Casio watch: 11:12.

He stepped out of the alcove, thanked the clerk at the register, and pushed open the front door into the bright Westwood sunshine. He knew exactly what Alex’s Christmas gift was going to be.

---

## MOVEMENT III: OCTOBER 28–31 — THE MORNING RUN, THE PORCH, AND HALLOWEEN NIGHT

### Scene 6 — October 28, 2009 (Wednesday): The Morning Run and Phil Dunphy

Wednesday dawn broke crisp and cool over Cheviot Hills, a bank of coastal fog hovering low over the western horizon toward Santa Monica. There was no matching scene in the television series Nathan remembered from his previous life; Phil and Claire's run this morning was an original parallel-world event, not part of the plot Nathan remembers under *Run for Your Wife*. The episode's 28 October broadcast date in his previous life did not make this ordinary run a remembered scene.

At 06:45, Nathan was on the second mile of his morning conditioning circuit, running north along the broad residential avenue shaded by towering sycamores and flowering magnolias. His footfalls were virtually silent on the concrete, his breathing rhythmic: three strides per inhalation, three strides per exhalation.

Ahead of him, seventy yards up the gentle incline of the avenue, a commotion of brightly colored nylon disrupted the neighborhood peace.

Phil Dunphy was locked in mortal combat with the pavement.

Phil was wearing a canary-yellow technical running jersey, royal blue split-side marathon shorts that fluttered violently in the morning breeze, and a thick white terrycloth headband pulled low over his eyebrows. Fifty yards ahead of Phil, Claire Dunphy was powering up the hill with ruthless, efficient stride mechanics, her blonde ponytail swinging like a metronome, visibly pulling away from her husband with every passing second.

Phil was panting with concussive force: *«Hoo-hoo... can’t let her win... cardiovascular supremacy... hoo-hoo...»*

Nathan closed the distance with effortless, steady pacing. As he drew alongside Phil on the sidewalk, he adjusted his speed by five percent to match Phil’s laboring stride, staying two arm-lengths wide to avoid crowding him.

— Morning, Mr. Dunphy, — Nathan said in an even, unhurried voice that betrayed zero respiratory distress.

Phil turned his head, his eyes bulging beneath the sweatband, sweat flying from his chin in glistening droplets.

— Nathan! — Phil wheezed, attempting to maintain an expression of relaxed athletic mastery while his quadriceps visibly shook. — Beautiful... morning... for an ultra-marathon... right?

— You're reaching a little with your front foot, Mr. Dunphy, — Nathan said, measuring his words to Phil’s labored exhalations. — Shorten your stride a fraction and relax your shoulders. You look like you're trying to outrun the hill itself.

Phil blinked through the stinging sweat, immediately attempting to shorten his stride. His sneakers slapped the asphalt with slightly less violence.

— Shorten... relax... like a cheetah? — Phil gasped.

— Exactly like a cheetah, — Nathan said with a small smile. — Keep your breathing steady. Two steps in, two out, if that rhythm feels comfortable. Don't try to match Claire's pace until you reach the crest.

Phil sucked in two sharp breaths through his nostrils, puffing his cheeks out on the exhale.

— Hoo! Hoo! Ha! Ha! — Phil proclaimed, suddenly finding half a gear of extra forward propulsion. — Hear that, California? I’m an African predator with high-efficiency lung capacity!

— Keep that cadence to the crest of the hill, Mr. Dunphy, — Nathan said, offering a respectful nod as he resumed his standard training pace. — You’ve got the elevation advantage.

— Thanks, Nathan! — Phil yelled after him, pumping his arms with renewed, theatrical vigor. — If Claire asks, I let her draft behind me for the first mile!

Nathan rounded the corner of the magnolia avenue with a quiet shake of his head, his sneakers carrying him toward home as the morning sun broke through the coastal marine layer.

---

### Scene 7 — October 29, 2009 (Thursday): The Dunphy Porch and the Hex Key <!-- EVT-016 | 2009-10-29 | 2009-10-29 -->

At five-fifteen on Thursday afternoon, the suburban quiet of the Dunphy front yard was broken only by the hum of a distant lawnmower and the chatter of scrub jays in the liquidambar tree.

Nathan walked up the flagstone walkway to the Dunphy residence. He had showered after school, dressed in clean khaki trousers, a navy-blue polo shirt with the top button neatly fastened, and his scuff-free sneakers. In his right hand, he held a small, polished L-shaped steel tool: a four-millimeter metric hex wrench that Luke had dropped by the park bench during their slingshot demonstration two days earlier.

Nathan stepped onto the covered porch, took two paces to the solid wood door, and pressed the illuminated brass doorbell button once.

*Ding-dong.*

From within the house came the immediate, familiar soundtrack of Dunphy domestic entropy: an electric blender whirring violently, someone shouting from the second floor about a missing sweater, and the rapid, rhythmic clatter of high-heeled boots descending the hardwood staircase.

The front door swung open with aggressive speed.

Haley Dunphy stood in the doorway.

She was fifteen, wearing low-rise flare jeans, a fitted turquoise baby-tee, and a silver charm bracelet that jangled furiously with every movement. In her left hand, she pressed a hot pink Motorola Razr flip phone to her ear, her glossy lips chewing berry-flavored bubblegum with rapid, practiced detachment.

Her wide hazel eyes swept over Nathan: taking in the parted brown hair, the pressed collar, the quiet posture, and the complete absence of the nervous, slouching adolescent stammer she was accustomed to seeing from boys her age.

— Hold on, Sarah, — Haley said into the phone, not bothering to take it away from her ear as she leaned one shoulder against the doorframe. She looked Nathan up and down with that devastating, dismissive scrutiny that only high school sophomores can muster. — Can I help you? If you’re here for Alex, she’s upstairs having a nervous breakdown over a practice quiz because she only got a ninety-eight.

Nathan maintained polite, neutral eye contact, his chin steady.

— Good afternoon. I’m not here for Alex, — he said in his measured, clear cadence.

Haley’s eyebrows arched slightly.

— Okay... then why are you standing on our porch?

Nathan held out the steel hex wrench.

— Luke dropped this near the municipal park bench during soccer practice on Tuesday. It’s a four-millimeter metric Allen wrench. He said he was using it to adjust the tension bolts on his treehouse platform. I didn't want him stripping the screw heads with the wrong size.

Haley looked from the gleaming piece of steel to Nathan’s face, her gum-chewing pausing for half a second.

— You walked across three cul-de-sacs to return a piece of metal?

— It belongs to Luke, — Nathan said simply. — And proper tools are easy to lose if nobody puts them back in the toolbox.

Haley stared at him for a moment, completely thrown off balance by a thirteen-year-old boy who spoke like an estate attorney and possessed better manners than her father and her boyfriend combined. A faint, amused smirk softened the corner of her lips.

She reached out, her silver charms jangling, and took the wrench from his hand.

— Right. Luke’s weird garage club, — she said, tucking the tool into the back pocket of her jeans. — Well, thanks, kid. I’ll make sure he doesn't swallow it.

— Thank you, — Nathan said with a brief, respectful nod. — Have a pleasant evening.

He turned on his heel and walked down the flagstone path with the quiet, balanced stride of an athlete.

Haley watched his back for three seconds before putting the pink Razr back to her ear.

— Sarah? Yeah, no, it was just the new neighbor kid from down the hill. No, not a weirdo. He was wearing ironed pants and called me *ma’am* without even blushing. I swear he looks like he escaped from a black-and-white television show.

---

### Director's Cut 2 — October 29, 2009 (Thursday Night): Haley's Bedroom

Upstairs on the second floor, the smell of strawberry body spray and drying nail polish filled Haley Dunphy’s bedroom.

Haley lay sprawled across her floral duvet, her bare feet propped against the white headboard, her pink Razr phone wedged between her shoulder and ear while she painted her toenails with a brush dipped in coral enamel.

On the desk across the room, the four-millimeter hex wrench lay beside her hair straightener, catching the warm yellow glow of her bedside lamp.

— No, Sarah, listen to me, — Haley said, rolling her eyes toward the ceiling plaster as her friend rambled on the other end of the line. — Dylan’s friends come over and they literally just stand in our kitchen staring at the refrigerator like they forgot how to speak English. They slouch so hard their chins touch their belt buckles.

She paused, blowing a gentle stream of air over her wet toenails.

— This kid... Callahan, I think his name is... he’s thirteen, right? He stood on our porch with his back straight, looked me right in the eye, and spoke in full, complete sentences. He didn't even look down at my top once! It was almost creepy how polite he was.

A pause on the line.

— No, he’s not hot, Sarah, he’s an eighth-grader! — Haley laughed, kicking her heels against the wall. — But he’s Alex’s study buddy or whatever. Alex pretends she doesn't care, but she spent twenty minutes cleaning her desk yesterday before he even walked past our street. If those two ever get married, their kids are going to be born with calculators attached to their wrists.

From across the hallway came the sharp, unmistakable sound of Alex’s bedroom door slamming shut, followed by the muffled thud of a heavy textbook hitting a laminate desktop.

Haley smirked, dipped her brush back into the coral enamel, and changed the subject to Friday night’s football game.

---

### Scene 8 — October 31, 2009 (Saturday): Halloween and the v0.8 Milestone

Saturday evening brought the full, theatrical pageant of an American suburban Halloween to Cheviot Hills.

Carved pumpkins with flickering tea-light candles grinned from the porch railings along the avenue. Strands of orange fairy lights were wound around sycamore trunks, and cardboard tombstones sprouted from manicured front lawns. In the street, clusters of neighborhood children in superhero capes, ghost sheets, and pirate hats wandered between the driveways, their plastic pumpkin buckets rattling with candy wrappers under the cool October stars.

Downstairs in the Callahan house, Heather was answering the front door every ten minutes, laughing warmly as she distributed miniature chocolate bars and caramel chews to neighborhood toddlers.

Upstairs, in Nathan's bedroom, the only illumination was the crisp, white anti-glare screen of the MacBook Pro [PROP-001] and the small, vibrant rectangle of the iPhone 3GS [PROP-004] lying on the wooden desk pad.

Nathan sat motionless in his chair, his stopwatch running on the secondary monitor.

The build was version 0.8.

On the iPhone’s display, the full game simulation was running its ultimate endurance test: two hundred dynamic agent entities, navigating a labyrinth of solid stone masonry using the flow field potential gradient. As entities crowded into intersections, the new spatial partitioning grid resolved all AABB collision boundaries in real time. Entities nudged against each other, slid along perimeter walls, and reached their destination targets without overlapping and without a single dropped frame.

The diagnostic overlay painted a clean, unbroken horizontal line:

`UPTIME: 15:02 | FPS: 60.1 | CPU: 19.8% | APP HEAP: 28.6 MB | ENGINE DATA: 8.6 MB | LEAKS: 0`

No memory-warning callbacks were delivered during the run. Instruments showed no frame-rate drop over the fifteen-minute stress test, and the engine's own allocator reported no leaked blocks.

Nathan leaned back, exhaling a breath he felt like he had been holding since September.

He touched the stop button on the compiler console.

The spatial engine was stable—not just an isolated collision test, but a working core integrated into the game. The game itself was not finished: asset integration, level progression, longer playtests, and a proper submission build still lay ahead in November. For the first time, though, the hardest technical part no longer looked impossible.

Nathan stood up, turned off the desk lamp, and walked down the stairs.

In the kitchen, Clifford was pouring two mugs of hot spiced apple cider from a simmer pot on the stove, the fragrance of cinnamon and clove filling the warm room.

Clifford turned, handing a mug to Nathan.

— How did the memory profile hold up on the stress loop? — Clifford asked, his dark eyes assessing his son with that quiet, professional engineering shorthand they shared.

Nathan took the mug with both hands, feeling the heat seep into his palms.

— Fifteen minutes continuous execution, Dad, — Nathan said, his voice quiet but grounded in deep, earned confidence. — Instruments recorded twenty-eight point six megabytes of live allocations across the app; the engine's own active data stayed around eight point six. Sixty frames a second, flat.

Clifford paused, looked at his thirteen-year-old son, and allowed a broad, proud smile to break across his face. He raised his mug in a silent toast.

— That’s clean engineering, Nathan. Tomorrow we start setting up the iTunes Connect packaging pipeline.

— Thanks, Dad.

The front doorbell rang with a sharp double chime. Heather’s laughter echoed from the foyer as another group of neighborhood trick-or-treaters shouted *«Trick or treat!»* into the crisp California night.

Nathan took a slow sip of the hot cider and looked through the dining room window at the lanterns glowing along the quiet, tree-lined street.

For the first time since the moving vans had left Seattle, the unfamiliar streets of Los Angeles didn't feel like a foreign transit hub. They felt like home.
