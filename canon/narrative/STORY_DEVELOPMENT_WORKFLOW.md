# Story Development Workflow

<!-- WD-001 -->
<!-- WD-004 -->

Status: ESTABLISHED / reusable project method
Updated: 2026-10-08

## Purpose

The story is built in layers rather than written from episode one to the end without revision.

The project maintains a rich underlying timeline, but the finished prose is selective. Not every event that
exists in the timeline needs to be shown.

The workflow is:

**timeline and plot bank → episode outline → partial outline expansion → a small batch of episodes →
backpropagation → continuity/refinement → continue forward → final prose pass**

The goal is to make a long episodic story feel as though it was lived rather than assembled.

## OpenWrite Codex

OpenWrite is used as the interactive working Codex and manuscript environment.

The version-controlled repository **escrita** remains the authoritative source for dated canon, research
evidence, continuity decisions and the rich underlying plot bank. OpenWrite mirrors the stable planning
state so it is fast to consult while drafting.

Recommended mapping:

| Story concept | OpenWrite representation |
|---|---|
| Entire series | **Project** with type **series** |
| Season | **Work** under the series project, with season number in metadata |
| Episode | **Chapter** under the season/work |
| Scene / beat | Story-map **scene/beat** graph nodes when useful |
| Series/season arcs | **Act / plot-point** graph nodes and plot points |
| Character | Project-level **Character** |
| Location | Project-level **Location**, nested with parent locations when appropriate |
| World/canon rules | Project-level **Lore** |
| Plot thread | **Plot point** + graph **plot_thread** connections |
| Notes for a chapter | Chapter notes |
| Loose notes/ideas | Custom lore/plot metadata or story-map nodes until a dedicated note type exists |
| Relationships | Graph connections such as character_arc, setting, thematic and reference |

Recurring characters and locations should normally exist once at project level rather than being recreated
for each episode. Episode-specific material can be attached to the relevant work/chapter.

When a canon fact changes, update **escrita first**, then mirror the stable result into OpenWrite. This
avoids having two competing versions of truth.

The Codex should contain enough information to answer "who, where, what is happening, why, and what has
already changed?" without forcing the finished prose to explain all of it.


## Layer 1 — Rich timeline

Important events receive exact dates whenever the calendar permits them.

Record:

- school events;
- football training and matches;
- technology milestones;
- relationship changes;
- family events;
- lived family events corresponding to *Modern Family* episodes Nathan remembers from his previous life;
- purchases and prop provenance;
- background character goals;
- consequences that may occur later;
- small seeds for future relationships, jokes or conflicts.

This layer can contain substantially more information than the prose.

## Layer 2 — Episode outline

For each episode, create a dated outline before drafting.

Every substantial subplot gets:

- start state;
- dated beats;
- escalation or development;
- outcome;
- state carried into the next episode.

The outline should explicitly mark whether a canon thread is:

- **Nathan-present**;
- **parallel**;
- **consequence-only**.

## Layer 3 — Draft

Write the episode naturally rather than following the outline mechanically.

Dates are continuity anchors, not headings that must appear in every scene.

Use time compression when nothing important changes.

A scene can contain several layers at once: Nathan's immediate problem, a relationship beat, a technical
detail and a background character's objective.

## What not to show

Do not show a scene merely because an event exists in the timeline.

Keep information off-page when:

- the event is routine;
- the reader already understands the implication;
- showing it would slow a stronger plot;
- uncertainty is more interesting;
- the same information can be communicated through a later consequence.

The underlying timeline should therefore feel richer than the visible story.

## Background-life principle

Recurring characters should have goals even when those goals are not currently plot.

Examples:

- a teammate wants more playing time;
- a teacher is considering recommending Nathan for an academic opportunity;
- Alex is balancing schoolwork with her own ambitions;
- Claire is organizing the house after the move;
- Phil is pursuing one of his hobbies;
- Haley has plans unrelated to Nathan;
- Luke is interested in some new activity;
- Clifford is adapting to increased responsibility;
- Heather is trying to establish a workable family routine.

A background goal can remain dormant for several episodes before becoming relevant.

The reader does not need an exposition paragraph explaining it. A few visible actions are enough.

## Prop continuity principle

Objects that become meaningful later should have plausible provenance.

Record important recurring objects in the timeline when they are:

- purchased;
- delivered;
- unpacked;
- gifted;
- borrowed;
- repaired;
- moved from one room to another.

Then decide later whether the finished prose shows the provenance scene.

The timeline answers **where did this come from?**

The prose answers **is it interesting enough to show?**

## Parallel-world principle

For every important family event Nathan remembers from the *Modern Family* series in his previous life, first ask:

**Would Nathan realistically be there in this world and at this point in the changed timeline?**

If yes, allow a natural intersection.

If no, show the lived family event in parallel or show its consequences later. The episode title is a memory label, not a current-world broadcast or a script that people must repeat.

Never alter geography, timing or character behaviour solely to place Nathan inside a scene he remembers.

## Backpropagation passes

Backpropagation should happen in deliberate passes.

### Pass A — causal continuity

Check that every major later event has an earlier cause, setup or motivation.

### Pass B — relationship continuity

Check that relationships develop through accumulated interactions rather than sudden jumps.

### Pass C — world continuity

Check homes, possessions, school routines, football teams, schedules and other material details.

### Pass D — character continuity

Check that later personality developments have early manifestations and that characters retain their
independent motives.

### Pass E — prose economy

After richness has been built into the timeline, remove scenes that do not earn their space.

The objective is **rich world, selective narration**.

## Episode acceptance test

Before an episode is considered ready:

1. It has a clear primary movement.
2. It contains several genuine subplots.
3. At least one secondary thread progresses independently of the main plot.
4. Canon is either naturally intersected, shown in parallel, or represented through consequences.
5. Dates and carry-over states are recorded.
6. At least one detail from an earlier episode matters.
7. At least one new detail can matter later.
8. Routine time is compressed rather than dramatized.
9. The episode does not feel empty after removing the canon plot.
10. The episode does not feel overloaded because every timeline event was shown.

## Target length

The default finished target is **10,000 words or more per episode**.

A shorter episode is acceptable when its dramatic structure is genuinely smaller, but the first response
should not be to pad it. Instead, enrich the underlying world and see whether one or more parallel threads,
stronger scene detail, consequences or character interactions naturally deserve page time.

The prose should grow because the story contains more life, not because a word counter demands it.


## Dialogue and model-selection discipline

Dialogue must pass the project's separate [Natural Dialogue Standard](DIALOGUE_NATURALNESS_STANDARD.md); do not expand outline beats mechanically or generate a whole episode in one prompt. Draft one scene or two connected scenes at a time, evaluate the spoken lines separately, then run a targeted critic pass that flags specific lines rather than rewriting the entire scene.

Use the [AI Writing Tool Selection and Evaluation protocol](../../research/narrative/AI_WRITING_TOOL_SELECTION.md) to compare only models available through the existing OpenWrite provider. A blind comparison on a fixed scene comes before any claim that a model or paid writing product is more natural. The project author's reading and judgment remain the acceptance signal; AI judges are advisory.

Final prose is written in natural American English (period-accurate 2009 Southern California; locked via DEC-008). Planning and technical canon documents can stay in English or be bilingual. Preserve the Southern California context and character-specific voices without caricature or mechanical imitation of exact lines from the source series.


## Foreknowledge and intervention pass

Before Nathan acts on a remembered canon event, use [the Foreknowledge and Intervention Policy](FOREKNOWLEDGE_INTERVENTION_POLICY.md). Separate how clearly he remembers the original event from how likely it is to recur after the timeline has changed. Check the present trigger, whether he has access to someone who can act, and the smallest credible intervention. A decision not to intervene is valid when access or a plausible action is missing; ignoring an immediate, actionable risk is not. Keep the detailed ledger out of finished prose.


## Character naming discipline

Before adding an original character, consult [the Character Naming Standard](CHARACTER_NAMING_STANDARD.md) and [the Character Name Registry](../characters/CHARACTER_NAME_REGISTRY.md). Use cohort- and country-appropriate public frequency data, filter duplicates and rejected names, then record a reproducible random draw. User-locked and source-canon names are exceptions; do not silently change them. Family surnames must be inherited/recorded consistently rather than independently randomized for each relative.


## Global architecture, linear causality and backpropagation

Follow [Narrative Architecture and Causal Drafting Method](NARRATIVE_AND_CAUSAL_METHOD.md) together with the [Decision Log](../DECISION_LOG.md). Plan the whole series recursively from beginning/end to midpoint and finer anchors; then build the story's lived state forward in chronological order, scene by scene, with causes, choices, outcomes and persistent state changes. After an episode or season, trace promised outcomes backward to identify missing prerequisites, then re-read forward to catch regressions. Randomize only among constrained, reasonable candidates when a choice is underdetermined; record the pool, seed, validation and dependencies. Do not let random draws overrule canon, causal constraints or explicit author choices.


## Narrative quality and agency gate

Use the [Narrative Quality and Character Agency Standard](NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md) as a required review gate, alongside chronology, causality, dialogue and foreknowledge checks.

### Antes de redigir

- Complete ou atualize a ficha de agência das personagens diretamente afetadas.
- Identifique os objetivos independentes de Alex, Haley e das restantes personagens canon envolvidas.
- Verifique se Nathan está a receber uma sequência artificial de elogios ou a resolver problemas fora da sua competência.
- Confirme que cada trama tem objetivo, obstáculo, escolha e consequência; a quota mínima de linhas não substitui substância.
- Especifique como as tramas se cruzam causalmente e quem paga o custo de cada decisão.

### Depois de redigir

- Faça uma passagem dedicada à agência: quem decide, quem recusa, quem discorda e quem tem razão?
- Procure cenas em que Alex ou Haley existem apenas para apoiar, corrigir ou curar Nathan.
- Verifique se as famílias mantêm relações e conflitos independentes do protagonista.
- Verifique se a tecnologia cria compromissos e consequências, não apenas uma sucessão de conquistas.
- Registe consequências que persistem e atualize as dependências narrativas.

Os testes automatizados protegem a existência deste processo e os seus contratos determinísticos. Não certificam qualidade literária, voz, humor, naturalidade ou credibilidade emocional; isso exige revisão humana.


## Grounded slice-of-life and supernatural-boundary gate

Apply DEC-017 and the genre boundary in the [Story Scope and Protagonist Design](../STORY_SCOPE_AND_PROTAGONIST_DESIGN.md) and the [Narrative Quality and Character Agency Standard](NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md).

### Antes de redigir

- Confirmar que o conflito nasce de relações, escola, família, trabalho, dinheiro, saúde, interesses, projetos ou responsabilidades quotidianas.
- Confirmar que o renascimento é a única exceção sobrenatural e que a memória da vida anterior não está a ser tratada como poder de previsão.
- Verificar que nenhuma solução depende de gacha, sistemas, missões, níveis, atributos, recompensas, magia, bênçãos, poderes ou intervenção divina.
- Verificar que cada competência resulta de aptidão, estudo, prática, experiência e recursos humanos plausíveis.
- Quando se usar uma inspiração externa, registar o aspeto narrativo específico que está a ser estudado e confirmar que nenhum sistema ou poder dessa obra foi importado.

### Depois de redigir

- Procurar qualquer capacidade que Nathan não pudesse obter através de meios humanos plausíveis.
- Procurar coincidências ou recompensas que funcionem como intervenção sobrenatural disfarçada.
- Confirmar que conhecimento da série televisiva é memória parcial e falível, não omnisciente.
- Confirmar que os obstáculos e soluções mantêm custos, limites e consequências quotidianas.
- Se uma cena só funciona por causa de uma mecânica sobrenatural que não seja o renascimento, reestruturar a cena em vez de acrescentar uma exceção ao cânone.

Esta verificação é obrigatória em outlines, cenas e drafts. Qualquer alteração à fronteira exige uma decisão explícita do autor e atualização de DEC-017 antes de alterar o cânone.
