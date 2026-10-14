# Episode 1 — Scene-State Ledger: Before and After

Status: WORKING SCENE-STATE RECORD — required before prose  
Story window: 7–30 September 2009  
Updated: 2026-10-13

## Operating rule

Each scene's complete state is reconstructed from (1) the latest character profile/baseline, (2) canon and AU events dated before the scene, (3) the recurring schedule/location constraints, and (4) the scene-specific entry below. Then apply its ending delta to all later scenes. This avoids copying every biography into every scene while still preserving the full accumulated state.

UNKNOWN is not a negative: it never means no family, no allergy, no injury, no skill, no promise, or nothing happened. A background aggregate stays anonymous only while no individual has dialogue, a unique action, a promise, a secret, or a later payoff. If an individual affects an outcome, profile them before prose approval.

Use the character-state standard, Nathan's profile and skill ledger, Callahan family file, team roster, secondary social circles, recurring schedules, and first-game design as the persistent sources of truth. Use the Modern Family core-character baseline for the canon characters' pre-AU state. None of the canon characters knows about Nathan's reincarnation or private show memories.

## Reusable minor-character profiles

These internal IDs prevent an outline from silently replacing the same teacher with a different person between scenes. Their legal names are not required unless dialogue needs them.

- **SEA-MATH-01:** Nathan's returning Seattle mathematics teacher. Values reasoning over speed, asks follow-up questions instead of flattering students, and is re-establishing classroom routines in the first week of term. Knows Nathan only through ordinary school records and prior classwork; does not know his private memories. Family and health details remain UNKNOWN unless causally relevant.
- **SEA-SCI-01:** Seattle science teacher. Wants students to justify experimental methods and observe evidence. Has no knowledge of Nathan's game or move before someone tells them. A brief class scene does not make them a confidant.
- **CA-MATH-01:** Nathan's new-school mathematics teacher. Has taught the existing class since 9 September, has only transfer paperwork and limited first-week evidence about Nathan, and values precise explanations. Later offers an enrichment opportunity because of observed work, not intuition. Knows nothing of Nathan's family history, attraction, reincarnation, or full ability ceiling.
- **CA-ENG-01:** new-school English teacher. Values clear writing and revision but notices when revision prevents completion. Their comment is based on Nathan visibly editing an answer repeatedly, not on a diagnosis of his personality.
- **Classmates:** Seattle lunch peers remain aggregate unless individualized. In California, Wesley Moss is the planned recurring technology/library peer; use the profile in SECONDARY_SOCIAL_CIRCLES.md rather than inventing a new recurring classmate for the later acceptance beat.

## Opening state on 7 September

**Nathan:** turns 13 today. His prior-life transition roughly two weeks earlier is a separate event. He lives with Clifford and Heather in the Seattle area; he has a real school/football history and is captain of his established team. He already has an Intel Mac development computer with a period-appropriate C++ environment and a second-generation iPod touch obtained by the family before the opening, plausibly a 2008 gift/purchase. Clifford handles any adult developer-account/signing administration needed for actual iOS device builds; these are WORKING technical details under DEC-013. During **3–4 September**, Nathan planned the game's core loop, enemy behavior, deliberately small scope and first map. During **5–6 September**, he set up the project skeleton and wrote the minimum functions for a runnable loop. The first on-page scene therefore starts with a very early but genuinely running build: a crude grid, basic player input/movement, one simple enemy update loop, and a first crude A* route-finding implementation. In Scene 1 Nathan checks it with one and then five instances of the same enemy archetype; both cases run acceptably, but repeated independent searches become a question to investigate, not a diagnosed bottleneck yet. The usable A* baseline already exists in rough form; its behavior and cost are measured/refined during the visible story. No profiler diagnosis, flow field, prediction layer, optimized build or polished game exists at the opening. No flow field, prediction layer, release build, fame, or outside audience yet. He is advanced in maths/programming and football, but limited by time, tools available in 2009, debugging, fatigue, perfectionism, and social hesitation. No allergy, chronic condition, injury, or dominant foot has been established.

**Clifford and Heather:** love Nathan and understand his preference for practical gifts and quiet praise. Clifford's California leadership role has been discussed at work for weeks, but the final decision has not been confirmed to Nathan. Heather knows the option exists and is watching the work situation. Neither parent knows about reincarnation.

**Seattle football:** use the team roster for each player's independent motive and behavior. A normal Tuesday practice occurs on **8 September** off-page because Scene 8 discusses the previous session: ordinary positional drills, Calvin and Nathan discuss midfield spacing, and no injury or decisive match result is created. Change this only by editing this record and dependent scenes.

**Canon families:** before the Callahans move in, the Dunphy, Pritchett, and Tucker-Pritchett households have no special knowledge of them. Their existing school, work, and relationship concerns continue on their own schedules.

---

## Scene-by-scene state and carry-forward rules

### Scene 1 — Nathan at the computer
**Date:** Monday, 7 September 2009.
**Date/location:** 7 Sep, Callahan home. **Cast:** Nathan.  
**Pre-state:** opening game build and birthday as above; Intel Mac is already configured for period-appropriate C++/iOS development; the second-generation iPod touch sits beside the computer as stated in the outline, but the prototype has not yet been ported to it. **Boundary:** competence appears through testing and decisions, not a reincarnation monologue. **Carry forward:** one and five enemies run acceptably; repeated path searches become a concrete question. No profiler diagnosis or flow field yet.

### Scene 2 — Birthday breakfast
**Date:** Monday, 7 September 2009.
**Date/location:** 7 Sep, Callahan kitchen. **Cast:** Nathan, Clifford, Heather.  
**Pre-state:** parents know it is his birthday and know his interests; promotion not yet confirmed. **Boundary:** Nathan's minimization of a gift is discomfort with praise, not ingratitude. **Carry forward:** any gift shown becomes a persistent object with owner and storage location; don't add a gift only for a later payoff without recording it. Parents remain unaware of reincarnation.

### Scene 3 — Informal football
**Date:** Monday, 7 September 2009.
**Date/location:** 7 Sep, local park/yard. **Cast:** Nathan and Calvin Baxter.  
**Pre-state:** Calvin is Nathan's established holding-midfield partner and respects concrete positional reasoning. **Boundary:** Labor Day; informal kickabout/solo touches only, no coach-led practice, official attendance, lineup or fixture. Calvin happens to be available and joins casually; this is not a scheduled club event. **Carry forward:** reinforce their existing midfield shorthand. Calvin remembers the specific spacing/passing adjustment only if it is made explicit in prose.

### Scene 4 — Quiet family undercurrent
**Date:** Monday, 7 September 2009.
**Date/location:** 7 Sep, Callahan home. **Cast:** Clifford and Heather; Nathan only if he observes from nearby.  
**Pre-state:** California role has been discussed for weeks but is unconfirmed. **Boundary:** Nathan may notice a tone shift but cannot know private call content unless he hears it. **Carry forward:** work pressure exists; Nathan does not yet know about the promotion.

### Scene 5 — Evening coding
**Date:** Monday, 7 September 2009.
**Date/location:** 7 Sep, computer area. **Cast:** Nathan.
**Pre-state:** Scene 1 already established that one and five instances of the same enemy archetype run acceptably; Scenes 2–4 introduced no code changes.
**Boundary:** Nathan resumes the benchmark instead of pointlessly repeating the same tests. He raises the count to ten and fifteen guards on the same small scenario and observes repeated route calculations through shared corridors toward the same region. He records this as a suspected source of wasted work, not a profiler-confirmed diagnosis.
**Carry forward:** repeated independent A* searches become the next question to measure; the crude baseline still works and no flow field or prediction system exists yet.

### Scene 6 — Mathematics
**Date:** Wednesday, 9 September 2009.
**Date/time/location:** 10:20–11:15, Wednesday 9 September, Seattle school. **Cast:** Nathan, SEA-MATH-01, class aggregate.  
**Pre-state:** first formal school week; teacher has returning-student context but no private knowledge. **Boundary:** Nathan initially explains too abstractly, notices the mismatch and simplifies. Teacher asks one harder follow-up rather than calling him a genius. **Carry forward:** teacher has evidence of genuine reasoning and may later consider enrichment; Nathan worries he sounded arrogant.

### Scene 7 — Lunch/Calvin
**Date:** Wednesday, 9 September 2009.
**Date/location:** 9 Sep, school. **Cast:** Nathan and Calvin Baxter.  
**Pre-state:** Calvin is Nathan's regular midfield partner and, in the working school assignment, a returning classmate in the same year group. They have known each other since the previous school year, but their bond is primarily practical football trust. **Boundary:** Calvin starts a low-stakes conversation about the new term's science/lab work; Nathan responds easily and makes a small joke. This shows that initiation is harder with unfamiliar people, not that Nathan cannot converse. No new promise or deep friendship is created. **Carry forward:** Calvin knows Nathan is still the same capable, approachable teammate; he does not know about reincarnation or the move yet.

### Scene 8 — Football/captaincy outside practice
**Date/time/location:** Wednesday 9 September 2009, 14:50–15:00, school exit/pickup area.
**Cast:** Nathan and Calvin Baxter only.
**Pre-state:** the off-page Tuesday 8 September practice occurred; the two midfielders already share responsibility for linking defense and attack.
**Boundary:** Calvin asks about the previous practice's spacing. Nathan proposes one adjustment to the distance between holding and attacking midfield. Calvin agrees it may help, but no whole-team adoption or coach approval occurs in this scene. They may try it at Thursday's scheduled practice; do not write that as already successful.
**Carry forward:** Calvin knows the proposal and can raise it at practice. Other teammates and Coach Holloway do not yet know unless one of them is told or directly observes the test. Nathan's captaincy remains established, but he has not made an official formation/lineup decision.

### Scene 9 — Game / first profiling pass
**Date/time/location:** Wednesday 9 September 2009, 19:30–20:30, Callahan home computer.
**Cast:** Nathan.
**Pre-state:** Scene 5 has already raised the same scenario to fifteen guards and recorded repeated path calculations as a suspected source of wasted work. No code changed between Scenes 5 and 9.
**Boundary:** Nathan re-runs the fifteen-guard scenario with the profiler enabled and compares it against the one- and five-guard baselines. The profiler now provides evidence that repeated A* path searches account for measurable work; it does not yet give him a complete redesign or solution. Only record timings/call counts that the eventual prose explicitly shows him measuring.
**Carry forward:** independent repeated A* calls are a measured bottleneck to investigate; flow fields and prediction are still absent, and performance under larger guard counts remains inadequate.

### Scene 10 — Science/lab
**Date/time/location:** Thursday 10 September 2009, 09:00–09:55, Seattle science classroom.
**Cast:** Nathan, SEA-SCI-01 and class aggregate.
**Pre-state:** first formal week and ordinary introductory lab work; teacher knows Nathan only through returning-student context.
**Boundary:** groups compare dissolving time of sugar in water at different temperatures. Nathan points out that sugar mass, water volume, stirring method and the criterion for “dissolved” must be consistent if temperature is the variable. SEA-SCI-01 asks him to justify the controls; he does so calmly and stays with the experiment. Class reaction is modest; no one treats him as a prodigy.
**Carry forward:** teacher has evidence that Nathan thinks about fair tests. No science-club offer, special mentorship or knowledge of his game is implied.

### Scene 11 — Football practice/playing-time tension
**Date/time/location:** Thursday 10 September 2009, 15:10–16:30, Seattle field.
**Cast:** Nathan, Devon Carver, Calvin Baxter, Coach Leonard Holloway, and the players taking part in the positional drill.
**Pre-state:** Devon was a late substitute in the previous Saturday's fixture and feels he had too little time to demonstrate his usefulness. Calvin knows Nathan's proposed midfield-spacing adjustment from Scene 8; the rest of the squad and coach have not yet seen it tested.
**Boundary:** the team tests the spacing adjustment during a positional drill. It helps on one repetition but is not adopted as a permanent change on that evidence alone. Later, Devon asks about earning more minutes. Nathan gives a specific target—scan before receiving, open his body and take the first touch away from pressure, then play the simple pass if no forward lane is open. Devon improves once but misses a cue on a later repetition. Leonard sees the interaction; he retains all selection authority and promises no minutes.
**Carry forward:** the proposed spacing adjustment has one observed practice result and still needs repeated evidence. Devon knows the specific skill to work on; his minutes and role remain unchanged until Leonard decides otherwise. Nathan has mediated without claiming the coach's authority.

### Scene 12 — Clifford's news approaches
**Date:** Thursday, 10 September 2009.
**Date/location:** 10 Sep evening, separate parent conversation. **Cast:** Clifford and Heather; Nathan absent unless the outline is changed.  
**Pre-state:** promotion option has existed for weeks, outcome uncertain. **Boundary:** parents may discuss negotiations and relocation logistics; Nathan has not learned the result. **Carry forward:** quick logistics are plausible because relocation support was already considered; final decision is pending.

### Scene 13 — A* stress test
**Date/time/location:** Friday 11 September 2009, 16:00–18:00, Nathan's computer; before the family announcement.
**Cast:** Nathan.
**Pre-state:** the 15-guard profiler pass on 9 September established repeated A* work as a measurable cost; no code changed between Scenes 9 and 13.
**Boundary:** Nathan runs the 10/15/20/24-guard cases. He tests fewer path/update refreshes, a simple cache and different destinations. Reuse helps only when the request actually matches; reducing refreshes also makes some movement less responsive. These are measured experiments, not a finished fix. Record only results actually observed; do not invent frame-rate numbers.
**Carry forward:** A* still functions but remains too expensive at higher counts. Nathan has learned that quick caching/update tweaks trade performance against responsiveness; no flow field exists yet. The family has not announced the promotion to him during this scene.

### Scene 14 — Family: promotion confirmed
**Date/time/location:** Friday 11 September 2009, 18:45–19:00, Callahan home.
**Cast:** Nathan, Clifford and Heather.
**Pre-state:** parents knew the promotion was possible; Nathan noticed work pressure only. At 16:00–18:00 Nathan ran the A* stress test and does not know the company decision is final.
**Boundary:** Clifford receives the formal confirmation and tells Heather and Nathan that evening. The company has been considering the role and preparing relocation contingencies for weeks, but this is Nathan's first clear confirmation. Practical questions come before the emotional reaction.
**Carry forward:** all three Callahans know the move is required. Nathan has not yet told the football team; that message happens in Scene 16 after he has had time alone.

### Scene 15 — Parents' explanation
**Date/time/location:** Friday 11 September 2009, 19:00–19:20, Callahan home; immediate continuation of Scene 14.
**Cast:** Nathan, Clifford and Heather.
**Pre-state:** Nathan has just learned that the promotion is approved; the family needs the move to happen on 14 September.
**Boundary:** parents explain that negotiations and relocation preparation predated the final approval. The coordinator had conditionally shortlisted a temporary furnished rental, movers and a vehicle, making the short timetable plausible. The family will initially rent; buying later is only a possibility if the role proves stable and they like the area. No purchase decision or promise is made.
**Carry forward:** temporary move remains scheduled for 14 September; computer/books/football-kit packing must now happen quickly. Nathan understands why logistics can proceed fast without believing the family had secretly finalized the move weeks earlier.

### Scene 16 — Nathan alone
**Date/time/location:** Friday 11 September 2009, 19:30–20:15, Nathan's room/computer area.
**Cast:** Nathan.
**Pre-state:** Nathan, Clifford and Heather know the promotion is confirmed; the Seattle team has not yet been told. Nathan has already spent two focused hours testing the game from 16:00–18:00.
**Boundary:** Nathan withdraws briefly and returns to the game because it is a controllable problem. He sends a plain group SMS through the team's existing text-message distribution list used for practice updates, telling Coach Leonard and the squad that the family leaves Monday. This is information, not a dramatic farewell or an invitation to a long chat. He then reviews existing test notes for a short block; he does not start a major coding task or add another lengthy session.
**Carry forward:** a team SMS has been sent. Players who receive/read it know the move before Saturday's match; do not assume every player has reacted or even read it until the scene establishes that. Nathan's private sense of loss coexists with continuing work.

### Scene 17 — Final Seattle-team match
**Date/time/location:** Saturday 12 September 2009, 09:00–10:25, Seattle field.
**Cast:** Nathan, Coach Leonard Holloway and the active Seattle squad; individual players gain scene-level detail only when they speak or affect the result.
**Pre-state:** Nathan sent the team's existing group SMS during Scene 16 on Friday night. Before warm-up, Leonard confirms the move to the squad and checks that everyone knows Nathan leaves Monday; no one needs to have read the SMS for the fact to reach them. Nathan's final match has not yet started.
**Boundary:** goodbye context, not guaranteed sentimental triumph. Do not assign a score, scorer, minutes or individual reaction until drafting establishes it; no injury is created by the outline. After the final whistle, Calvin tells Nathan the team will miss having him organize midfield transitions. This reflects their established partnership, not a generic farewell speech.
**Carry forward:** all active players and the coach know Nathan is moving before kickoff; individual emotions remain varied and only become canon if shown. Calvin's remark is a specific known exchange, and the squad's relationships persist after the move.

### Scene 18 — Coach advice
**Date:** Saturday, 12 September 2009.
**Date/location:** 12 Sep after the match. **Cast:** Nathan and Leonard.  
**Pre-state:** Leonard has watched Nathan lead through the season and knows he is moving; Nathan is embarrassed by praise. **Boundary:** Leonard advises Nathan to learn the new side's shape and habits before trying to change them; this is practical coaching, not a grand speech. **Carry forward:** Nathan remembers this principle when he first assesses the California team, but still has to observe and learn their actual routines.

### Scene 19 — Moving logistics
**Date:** Saturday, 12 September 2009.
**Date/location:** 12 Sep, Callahan home. **Cast:** Nathan, Clifford, Heather; movers as aggregate.  
**Pre-state:** move around 14 Sep; Intel Mac, peripherals/cables, second-generation iPod touch and its cable, books, football gear and notebook are owned items. **Boundary:** selective physical detail, not a shopping documentary. **Carry forward:** fragile computer gear and cables travel together; keep the iPod and its cable accessible enough for the first unpacking, without implying that the unfinished game is already installed on it.

### Scene 20 — Family planning
**Date:** Sunday, 13 September 2009.
**Date/location:** 13 Sep, Callahan kitchen/table. **Cast:** Nathan, Clifford, Heather.  
**Pre-state:** confirmed move and approximate schedule. **Boundary:** Nathan can choose room/equipment priorities while parents manage adult logistics. **Carry forward:** packing priorities are known; equipment access is limited by what is unpacked.

### Scene 21 — Technical reading
**Date:** Sunday, 13 September 2009.
**Date/location:** 13 Sep, Nathan's study area. **Cast:** Nathan.  
**Pre-state:** profiler proves repeated searches; he has previously read about pathfinding/field-based methods. **Boundary:** a promising recognition, not a finished algorithm. **Carry forward:** notebook has the rough idea of sharing global navigation information; implementation incomplete.

### Scene 22 — Follow-up messages
**Date:** Sunday, 13 September 2009.
**Date/location:** 13 Sep, Nathan's room. **Cast:** Nathan; Calvin Baxter, Tristan Morrow and Devon Carver.  
**Pre-state:** the team already knows the move from the 11 Sep group message; these three have separate relationships and home/school commitments. **Boundary:** the messages are individual follow-ups, not the first reveal. Nathan may discount sincere replies, but that is his interpretation. **Carry forward:** record who replied, the exact knowledge shared, and any promise to keep in touch; do not invent promises if the scene does not make them.

### Scene 23 — Travel from Seattle to the rental
**Date/time:** Monday 14 September 2009, 05:30–11:30.
**Location/cast:** Seattle–Tacoma airport, flight, Los Angeles airport and transfer to the rental; Nathan, Clifford and Heather, with public travellers as aggregate.
**Pre-state:** relocation coordinator has arranged temporary housing, transport and mover dates; household goods were packed/inventoried on 12 September and the truck travelled south on 13 September.
**Boundary:** working schedule: leave home 05:30, airport check-in around 06:15, flight around 07:30–10:15, temporary vehicle and drive to rental by around 11:30. Nathan carries the Intel MacBook, charger, compact peripherals, notes and second-generation iPod touch; Clifford carries his work laptop/credentials. Main monitor, books, furniture, kitchen boxes and the family car travel separately.
**Carry forward:** family arrives in California without the bulk of its property. The MacBook and project copy remain accessible; the house is not yet unpacked and the family car is still in transit.

### Scene 24 — Clifford's California role begins
**Date/time:** Monday 14 September 2009, 11:45–12:30, furnished rental.
**Cast:** Clifford; coworkers aggregate unless a named person is introduced.
**Pre-state:** family has reached the rental; internet is active; Clifford's work laptop and credentials travelled with him.
**Boundary:** Clifford makes a short remote handoff call confirming immediate priorities and next-day contacts. This is a transition check-in, not a full office day; he is not also physically present in a California office. Heather and Nathan handle keys, paperwork and immediate questions nearby.
**Carry forward:** promotion has practical demands, but the family has not started normal work/school routines. The rental was selected for availability, commute and school-boundary reasons; adjacency to the Dunphys is coincidence.

### Scene 25 — Temporary rental and moving crew
**Date/time:** Monday 14 September 2009, 13:00–14:15, rental house.
**Cast:** Nathan, Clifford, Heather and moving crew as aggregate.
**Pre-state:** family has arrived with personal luggage; the truck carrying household goods is due in the early afternoon.
**Boundary:** movers unload boxes, books, furniture, kitchen goods and the main monitor/peripherals. Boxes block several rooms; essentials are findable but the house is far from settled. Nathan opens his carried MacBook on a stable table and checks that the existing project runs; relocation interrupts his normal programming block and he adds no substantial feature that day. Heather keeps the school documents together for the 15 September enrollment check.
**Carry forward:** project is accessible on the MacBook; bulky gear and most books remain boxed, and the family car is still being transported. Do not require a monitor or unpacked desktop for coding.

### Scene 26 — Neighborhood introduction
**Date/time:** Monday 14 September 2009, 14:20–14:35, driveway during unloading.
**Cast:** Nathan, Clifford, Heather, Phil, Claire and Luke; moving crew as aggregate.
**Pre-state:** movers are unloading the household shipment. The Callahans were placed in this rental through the corporate-relocation process and have no prior knowledge of the Dunphys.
**Chosen beat:** Phil introduces himself and offers to carry one light box; Claire joins; Luke is nearby and asks Nathan about the football he brought outside. The crew continues unloading, giving the conversation a natural setting.
**Knowledge limit:** Phil and Claire know only the names and ordinary details exchanged; Luke knows Nathan as the new neighbor and has seen his football gear. Alex and Haley need not be present. No one learns Nathan's school performance, private memories or attraction to Alex.
**Carry forward:** three plausible pre-Pilot acquaintances are established. No friendship, invitation or promise about football is implied unless the scene actually creates it.

### Scene 27 — First California evening
**Date/time:** Monday 14 September 2009, 19:00–20:00, rental.
**Cast:** Nathan.
**Pre-state:** the main unloading has progressed; the MacBook is accessible, while books, larger peripherals and many household items remain boxed. School enrollment paperwork is provisionally arranged for 15 September.
**Boundary:** Nathan checks the provisional school route and the first-day information Heather has received, then opens his unfinished game on the MacBook to review the current build. He does not treat moving day as a full coding session or claim to know the school layout before attending.
**Carry forward:** the move feels real; Nathan has to rebuild his routine while keeping the existing project alive.

### Scene 28 — First school arrival
**Date:** Wednesday, 16 September 2009.
**Date/location:** 16 Sep, middle school. **Cast:** Nathan, school staff/classmates aggregate.  
**Pre-state:** timetable from transfer paperwork, layout unfamiliar. California team hasn't practiced with him. **Boundary:** early arrival and schedule-checking; his Seattle reputation has not transferred. **Carry forward:** new-school status starts at zero; retain 8th/7th grade separation.

### Scene 29 — New-school mathematics
**Date:** Wednesday, 16 September 2009.
**Date/location:** 16 Sep, CA-MATH-01's class. **Cast:** Nathan, CA-MATH-01, class aggregate.  
**Pre-state:** teacher has class routine and transfer paperwork only. **Boundary:** Nathan explains an answer carefully; one answer is evidence, not proof of the whole skill ledger. **Carry forward:** CA-MATH-01 remembers real mathematical reasoning and may follow up.

### Scene 30 — Hallway: Alex at a distance
**Date:** Wednesday, 16 September 2009.
**Date/location:** 16 Sep, shared campus. **Cast:** Nathan and Alex; students aggregate.  
**Pre-state:** Alex has not met Nathan; Nathan recognizes her privately from the show. **Boundary:** Nathan considers approaching and avoids it. Alex may notice a glance but cannot know why. **Carry forward:** Nathan knows who she is; Alex has at most a first impression of the transfer student.

### Scene 31 — After-school football contact
**Date:** Wednesday, 16 September 2009.
**Date/location:** 16 Sep, office/field-side introduction. **Cast:** Nathan and Coach Lance Conley; Maxwell only if explicitly introduced.  
**Pre-state:** transfer is new; local trust absent. **Boundary:** logistics or invitation to an assessment, not a full training session or match. Nathan is not captain. **Carry forward:** set a coach-approved controlled scrimmage for Saturday 19 Sep; record any permission/form needed.

### Scene 32 — First flow-field attempt
**Date:** Wednesday, 16 September 2009.
**Date/location:** 16 Sep evening. **Cast:** Nathan.  
**Pre-state:** Seattle notes travelled with him; computer/development environment is working. **Boundary:** promising implementation, not proof of strong steering. **Carry forward:** global navigation looks better; local steering/prediction incomplete. Record code/build state in the game project.

### Scene 33 — School/Alex at a distance
**Date:** Thursday, 17 September 2009.
**Date/location:** 17 Sep, library/shared academic space. **Cast:** Nathan and Alex; others aggregate.  
**Pre-state:** they have seen one another, not spoken; Alex's school/cello life continues. **Boundary:** Nathan notices her working but focuses on his task; she need not notice him. **Carry forward:** private attraction changes Nathan's attention, not the external relationship.

### Scene 34 — English/over-editing
**Date:** Thursday, 17 September 2009.
**Date/location:** 17 Sep, CA-ENG-01's class. **Cast:** Nathan, teacher, classmates aggregate.  
**Pre-state:** only a few days of evidence. **Boundary:** teacher comments on visible repeated revisions, not a diagnosis of perfectionism. **Carry forward:** this becomes one concrete example of Nathan over-editing.

### Scene 35 — Haley's independent social life
**Date:** Thursday, 17 September 2009.
**Date/location:** 17 Sep evening, Dunphy home. **Cast:** Haley, Claire, Kristina Barlow by phone if included.  
**Chosen working beat:** Haley arranges a social plan with Kristina while Claire asks about schoolwork/timing. Keep the disagreement ordinary and specific, not a new family crisis. Claire knows the new neighbors from the driveway; Haley has not met Nathan.  
**Carry forward:** record the plan or scheduling disagreement and who knows it. Phone behavior/language fits 2009; don't make Nathan the topic without a reason.

### Scene 36 — Flow-field review
**Date:** Thursday, 17 September 2009.
**Date/location:** 17 Sep evening. **Cast:** Nathan.  
**Pre-state:** first field implementation. **Boundary:** he reasons from the measured bottleneck and reference material, not an unexplained flash of perfect recall. **Carry forward:** understands that global information can be shared while local movement still needs distinct logic.

### Scene 37 — Practical first Alex conversation
**Date:** Friday, 18 September 2009.
**Date/location:** 18 Sep, school-library reference area. **Cast:** Alex, Nathan.  
**Pre-state:** two distant sightings, no conversation. Nathan is consulting the library's reference copy of a problem-solving book with mathematical maze/logic puzzles because he is thinking about grid pathfinding. Alex has come to check one section for an optional class problem-solving challenge and asks how long he needs the book. Nathan knows her identity privately; she does not know why.  
**Boundary:** the request is practical, not a contrived romantic setup. Nathan gives her a useful answer, adds a clarification, then hedges/apologizes unnecessarily. Alex's impression is based on this brief exchange only.  
**Carry forward:** they meaningfully meet; Alex learns his name through an ordinary introduction, Nathan already knows hers. The book is library property, shared briefly and returned to the correct place the same day; neither character owns it.

### Scene 38 — After the conversation
**Date:** Friday, 18 September 2009.
**Date/location:** 18 Sep, corridor/walk home. **Cast:** Nathan only.  
**Pre-state:** first practical conversation just ended. **Boundary:** Nathan interprets politeness as no evidence of interest; that's his fallible view, not objective truth. **Carry forward:** no external relationship change beyond having spoken; his private attraction/anxiety rise.

### Scene 39 — Evening coding
**Date:** Friday, 18 September 2009.
**Date/location:** 18 Sep evening. **Cast:** Nathan.  
**Pre-state:** better flow-field movement; steering defect still open. **Boundary:** improvement reveals another defect, not automatic complete collision avoidance. **Carry forward:** log symptom and reproduction conditions.

### Scene 40 — New California football environment
**Date:** Saturday, 19 September 2009.
**Date/location:** 19 Sep, local field, controlled internal scrimmage. **Cast:** Nathan, Coach Lance, Maxwell Whitaker, California roster/substitutes who take part.  
**Pre-state:** only introductions/logistics so far; local squad has a shared history without Nathan. **Boundary:** assessment scrimmage, not official competition unless eligibility is independently established. Nathan is a new midfielder, not captain. He remembers Coach Leonard Holloway's advice to learn the new side's shape before trying to change it, so he observes how the California midfield and back line move together before proposing one adjustment. Coach Lance assesses communication/adaptation as well as skill.  
**Carry forward:** record attendance, sides/roles, approximate minutes, physical state, tactical exchanges and what each player learns. Maxwell wants playing time but isn't hostile by default; trust remains preliminary.

### Scene 41 — Home/family adjustment
**Date:** Saturday, 19 September 2009.
**Date/location:** 19–20 Sep, rental. **Cast:** Nathan, Clifford, Heather.  
**Pre-state:** several days in California; boxes remain, Clifford works long hours, Heather builds household routines. **Boundary:** no one is fully settled. **Carry forward:** record unpacked rooms/items; computer works, daily routines are still new.

### Scene 42 — Nathan and the game
**Date:** Saturday, 19 September 2009.
**Date/location:** 19–20 Sep, computer area. **Cast:** Nathan.  
**Pre-state:** flow field with steering defects, predictor absent/primitive. **Boundary:** testing and iteration, not a nearly complete game. **Carry forward:** enemies get stuck less often; prediction remains an open task.

### Scene 43 — Alex echo
**Date:** 19–20 September 2009 (weekend bridge).
**Date/location:** 20 Sep, Nathan alone. **Cast:** Nathan.  
**Pre-state:** one short conversation with Alex, no later contact. **Boundary:** he notices his own smile and redirects attention; cannot infer she is thinking about him. **Carry forward:** private emotion grows, external relationship unchanged.

### Scene 44 — School acceptance begins
**Date:** Monday, 21 September 2009.
**Date/location:** 21 Sep, school/library. **Cast:** Nathan, Wesley Moss; teacher/classmates only if active.  
**Pre-state:** Wesley has heard of the transfer but hasn't meaningfully spoken to Nathan. He has his own workload/interests. **Chosen working beat:** Wesley asks a concrete technology/homework question; Nathan responds usefully without showing off.  
**Boundary:** a first useful exchange, not instant friendship or an assistant role. **Carry forward:** Wesley sees Nathan as capable and approachable; track any topic they agree to revisit.

### Scene 45 — Alex acknowledges Nathan
**Date:** Monday, 21 September 2009.
**Date/location:** 21 Sep, shared school space. **Cast:** Alex and Nathan.  
**Pre-state:** library conversation three days earlier. **Boundary:** Alex initiates a small greeting, Nathan responds. Any hesitation is an ordinary moment, not yet an established pattern. **Carry forward:** natural recognition, not a romantic turn; Alex still knows nothing about reincarnation.

### Scene 46 — Flow-field stability
**Date:** Monday, 21 September 2009.
**Date/location:** 21 Sep evening. **Cast:** Nathan.  
**Pre-state:** local steering improved, destination prediction still crude. **Boundary:** multiple guards can use the shared field, but deciding what to pursue is separate. **Carry forward:** navigation layer stable; retain only defects not yet solved.

### Scene 47 — Second Alex conversation
**Date:** Tuesday, 22 September 2009.
**Date/location:** 22 Sep, school. **Cast:** Alex and Nathan.  
**Pre-state:** practical conversation plus greeting. **Boundary:** smaller reason to speak, slightly longer exchange; Nathan starts one sentence and feels self-conscious. This is another isolated data point, not yet a pattern Alex would verbalize. **Carry forward:** one incremental step toward comfort, no confession or promise.

### Scene 48 — Football/team trust
**Date:** Tuesday, 22 September 2009.
**Date/location:** 22 Sep, scheduled/coach-approved California session only. **Cast:** Nathan, Maxwell, Coach Lance, players in the drill.  
**Pre-state:** 19 Sep scrimmage; Nathan still learning team shorthand. Maxwell fears being overlooked and wants minutes. **Boundary:** Maxwell asks about a tactical situation; Nathan observes/listens before suggesting. **Carry forward:** coach sees a concrete coordination example; track role/minutes and whether the activity was formal practice or a limited assessment.

### Scene 49 — Technical note
**Date:** Tuesday, 22 September 2009.
**Date/location:** 22 Sep evening. **Cast:** Nathan.  
**Pre-state:** global navigation works; destination selection crude. **Boundary:** the thought "navigation is not destination selection" organizes the problem, but isn't a finished influence map. **Carry forward:** next tasks split into destination estimation and movement to that destination.

### Scene 50 — Technical realization
**Date:** Wednesday, 23 September 2009.
**Date/location:** 23 Sep after school/evening. **Cast:** Nathan.  
**Pre-state:** this is Nathan's sixth school day at the California school (16–18 and 21–23 Sep); stable navigation field, no robust predictor; school/team footholds remain new. **Boundary:** weighted guess from last sighting, direction, likely exits and recent choices is a design concept/rough representation. The Pilot occurs separately; Nathan is not a witness. **Carry forward:** prediction prototype exists on paper or in code, not finished.

### Scene 51 — School reputation/academic opportunity
**Date:** Thursday, 24 September 2009.
**Date/location:** 24–25 Sep, CA-MATH-01's class. **Cast:** Nathan, teacher, class aggregate.  
**Pre-state:** teacher has observed several pieces of work, not just one answer. **Boundary:** CA-MATH-01 poses a harder follow-up and mentions the school's optional maths-enrichment/competition group based on several observed pieces of work. Nathan may misread the suggestion as generic encouragement; no enrollment occurs here. **Carry forward:** exact meeting date/deadline and Nathan's commitment remain undecided until the follow-up is developed; do not assume membership.

### Scene 52 — Alex asks about the project
**Date:** Thursday, 24 September 2009.
**Date/location:** 24–25 Sep, shared school space. **Cast:** Alex and Nathan.  
**Pre-state:** Alex knows him through the resource conversation and greetings. **Boundary:** she asks from curiosity; Nathan gives a simplified explanation and checks comprehension. She doesn't become a technical expert instantly. **Carry forward:** Alex knows the game has unusual enemy movement; she has not seen all code or future plans. Nathan gains evidence that talking can go well.

### Scene 53 — Football cooperation
**Date:** Thursday, 24 September 2009.
**Date/location:** 24–25 Sep, California practice/team activity. **Cast:** Nathan and Maxwell Whitaker, with Coach Lance and other players only if they materially act.  
**Pre-state:** first scrimmage and Scene 48 tactical exchange. Maxwell still wants minutes; coach makes selections. **Boundary:** show one specific attacking/defensive transition that works because Nathan and Maxwell coordinate; it is practical cooperation, not instant admiration. **Carry forward:** update selection, minutes, trust and tactical shorthand only if it is explicitly agreed and used.

### Scene 54 — Callahan household/blue bowl
**Date:** Friday, 25 September 2009.
**Date/location:** 24–25 Sep, rental kitchen. **Cast:** Heather and Nathan; Clifford only if present in the final beat.  
**Chosen prop:** a blue ceramic mixing bowl from the Seattle kitchen is unpacked and placed in the usable kitchen. It travelled in a kitchen box; it has no secret meaning by default. **Carry forward:** bowl is no longer packed; later scenes must respect its location and whether it is intact.

### Scene 55 — Prediction prototype
**Date:** Friday, 25 September 2009.
**Date/location:** 24–25 Sep evening. **Cast:** Nathan.  
**Pre-state:** influence-map concept and stable navigation. **Boundary:** repeated leftward escape causes guards to search left predictably. Nathan introduces uncertainty; it remains exploitable. **Carry forward:** log observed behavior and intended fix. Do not treat this as a solved predictor.

### Scene 56 — Weekend football
**Date:** Saturday, 26 September 2009.
**Date/location:** 26 Sep, California field. **Cast:** Nathan, Coach Lance, Maxwell and players who materially participate.  
**Pre-state:** one week of local adjustment and coach-approved work. **Boundary:** training/internal scrimmage unless a formal fixture is established; Nathan not captain. **Carry forward:** attendance, roles/minutes, concrete improvement and individual reaction. Don't make all players accept him simultaneously.

### Scene 57 — California home begins to form
**Date:** Saturday, 26 September 2009.
**Date/location:** 26–27 Sep, rental. **Cast:** Clifford, Heather, Nathan as chosen.  
**Chosen prop:** a framed family photograph from a Washington-coast outing in summer 2008 is unpacked and put on a shelf. Keep the exact occasion broad; don't invent other people in the photograph. **Pre-state:** bowl from Scene 54 is already unpacked; other boxes remain. **Carry forward:** photograph is now visible in California and represents a memory of Seattle; track its location if moved later.

### Scene 58 — Integrated multi-enemy test
**Date:** Sunday, 27 September 2009.
**Date/location:** 26–27 Sep evening. **Cast:** Nathan.  
**Pre-state:** flow field, local steering and preliminary prediction integrated. **Boundary:** 20-plus enemies demonstrate architectural coherence but not release readiness. **Carry forward:** three separate components—shared navigation, destination prediction, local steering—plus remaining performance/collision/testing defects.

### Scene 59 — Recurring classmate
**Date:** Monday, 28 September 2009.
**Date/location:** 28–29 Sep, school/library. **Cast:** Nathan and Wesley Moss.  
**Pre-state:** first meaningful exchange on 21 Sep; Wesley knows Nathan is capable but not a best friend. **Boundary:** recurring contact comes from shared school/technology routines; Wesley has independent interests and deadlines. **Carry forward:** developing acquaintance/friendship. Record how much Wesley has learned about the game.

### Scene 60 — Alex / ordinary exchange
**Date:** Monday, 28 September 2009.
**Date/location:** 28–29 Sep, school. **Cast:** Alex and Nathan.  
**Pre-state:** Alex and Nathan have had a handful of short conversations, including the library exchange and later greetings. She may have seen an isolated hesitation or unnecessary apology, but she has not seen the habit consistently enough to call it a pattern.  
**Boundary:** keep this as a brief, ordinary exchange. Nathan may underplay one small success or begin to apologize over a minor inconvenience; Alex does not challenge him, diagnose him, or make the reserved remark. Do not force a second or third confirming incident just to make an early payoff work.  
**Carry forward:** no explicit conversation about Nathan's insecurity and no relationship milestone based on his self-undervaluation. Reserve "You know you don't have to apologize every time you're right" for much later, after many chapters have shown the habit repeatedly to Nathan and the reader and Alex has accumulated enough direct experience.

### Scene 61 — Vertical-slice/performance review
**Date:** Monday, 28 September 2009.
**Date/location:** 28–29 Sep evening. **Cast:** Nathan.  
**Pre-state:** integrated three-part architecture, successful 20-plus-enemy test. **Boundary:** discovers unnecessary updates, a caching opportunity and a collision bug. These are separate defects; fixing one doesn't solve the others. **Carry forward:** near-vertical-slice, not release-ready. Add the defects to the game changelog and only mark them fixed after testing.

### Scene 62 — Alex's independent evening
**Date:** Tuesday, 29 September 2009.
**Date/location:** 28–29 Sep, Dunphy home. **Cast:** Alex; Claire only if actually active. Nathan absent.  
**Chosen beat:** Alex practices cello, becomes frustrated with a passage, then returns to homework. This is about her own standards and school routine. **Pre-state:** she has spoken to Nathan several times but hasn't presented him to the family as a romantic interest. **Carry forward:** no Nathan knowledge changes unless she actually mentions him. Nathan learns nothing from a scene he does not witness.

### Episode-ending canon parallel — 30 September
**Cast if shown:** Phil/Luke, Jay/Manny, Mitchell/Cameron/Lily; add other family members only if the source scene requires them.  
**Pre-state:** the Pilot happened in parallel on 23 Sep. Phil, Claire and Luke know the Callahans through the 14 Sep driveway introduction; Alex knows Nathan from school. Jay, Gloria, Manny, Mitchell, Cameron and Lily have no established Nathan contact.  
**Boundary:** preserve the original cause/knowledge of *The Bicycle Thief*. Nathan is not present and cannot recount private events he has not been told.  
**Carry forward:** canon continues independently; any AU divergence must have a specific action and knowledge channel.

### Episode-ending Nathan thread — 30 September
**Cast:** Nathan.  
**Pre-state:** partially settled rental; shared flow field, local steering and early prediction layer. **Boundary:** a vertical slice is not a release; satisfaction can coexist with a bug list.  
**Carry forward to Episode 2:** Nathan is 13, relocated, attending school, has a developing acquaintance with Wesley and teammates, and has had several short conversations with Alex. The game is unfinished and not publicly released. Seattle friends remain in his past rather than disappearing from the story's memory.

## End-state gate

- [ ] Seattle teammates know of the move before the 12 September match; only message recipients know the exact message content.
- [ ] The Seattle and California teams remain separate; Nathan's captaincy does not transfer.
- [ ] The 19 September assessment is an internal scrimmage; later official eligibility is not assumed.
- [ ] Scene 60 stays an ordinary early interaction: no premature diagnosis or direct comment about Nathan's habit. Keep the reserved line for a much later point after repeated examples across many chapters.
- [ ] Phil, Claire and Luke meet the Callahans only through the 14 September intro; Alex's school contact is independent.
- [ ] Nathan's private show memories remain private; Pilot and 30 September canon scenes are parallel, not witnessed by him.
- [ ] The game advances cumulatively: A* baseline → profiling/stress failure → field movement → local steering → early prediction → integrated vertical slice; release is in Episode 2.
- [ ] The blue bowl and framed photograph have provenance and a recorded location.
- [ ] One-off people with causal action are micro-profiled before prose approval; aggregates remain anonymous only if no individual outcome depends on them.
- [ ] No allergy/injury/health fact is inferred from silence; unknown values remain unknown.
