# OpenWrite Codex Specification — Modern Family AU / Nathan Pierce

Status: WORKING / aligned with current OpenWrite implementation
Updated: 2026-10-08

## OpenWrite is the Codex

OpenWrite is the intended structured Codex/manuscript environment for this project.

The separate `escrita` repository remains the versioned planning/canon source.

The OpenWrite project's role is to hold the same universe in connected entities so drafting can query:

- characters;
- locations;
- lore/rules;
- plot threads;
- season-level story elements;
- episode/chapter elements;
- scenes;
- beats;
- relationships between all of them.

The current OpenWrite schema supports project-level characters, locations, lore and plot points, and a unified
graph whose story elements can be premise, act, chapter, scene, beat or plot point. Graph connections include
story flow, character arc, setting, plot thread, thematic and reference links.

## Hierarchy for this story

### Project

**Modern Family AU — Nathan Pierce**

Contains the complete series universe.

### Work

Use one Work for each story season.

A Work is **not** an individual episode.

This matters because a season follows one year and may contain many substantial chapters.

### Chapter

Use each final story episode/chapter as a Chapter inside the season Work.

There is deliberately no fixed number of Chapters per Work.

### Graph

Use graph nodes for:

- season-level acts/movements;
- episode/chapter structures;
- scenes;
- beats;
- plot threads;
- characters;
- locations;
- lore.

Use connections to represent causal and narrative structure.

## Core entities to create

### Characters

Project-level characters should include Nathan, the Pierce family, the Dunphy family, and relevant wider
Modern Family characters.

Character descriptions should contain stable canon + AU identity.

Dynamic season state belongs in the season/episode graph and timeline rather than overwriting the permanent
character identity.

### Locations

Project-level locations:

- Seattle-area Pierce home;
- old school;
- old football environment;
- California temporary rental;
- new middle school;
- recurring school library/academic spaces;
- football locations;
- Dunphy home;
- wider family homes;
- local shops/supermarket;
- useful routes and neighborhood places.

### Lore

Core lore entries:

- reincarnation rules;
- previous-life/current-life memory coexistence;
- Modern Family memory limits;
- fragmented future knowledge;
- Nathan's intervention philosophy;
- butterfly-effect rules;
- causal foreshadowing;
- backpropagation method;
- narrative camera / epistemic limits;
- season = approximately one year;
- school/age continuity;
- technology realism;
- 2009 technical context;
- prop provenance rule.

### Plot threads

At project level:

- Nathan's life / coming of age;
- Nathan/Alex;
- Pierce family;
- school;
- football;
- technology / AI trajectory;
- canon divergence;
- butterfly-effect chains;
- wider Dunphy/Pritchett relationships.

At season level:

- Season 1 adaptation/belonging;
- first technical achievement;
- first friendship network;
- first major canon divergence;
- Nathan learning the difference between prediction and understanding.

## Graph structure

The graph should preserve the distinction:

**series macro arc**
→ **season master plot**
→ **episode/chapter**
→ **scene**
→ **beat**

Cross-cutting threads connect horizontally across all these levels.

Examples:

`Nathan/Alex` — character_arc —> scene
`Nathan first game` — plot_thread —> multiple scenes
`California temporary rental` — setting —> multiple scenes
`A* bottleneck` — reference —> flow-field adaptation scene
`first intervention` — plot_thread —> consequence scene

## Important modelling rule

Do not create a graph node merely because an outline contains a bullet.

The Codex should represent stable entities and meaningful causal/narrative relationships.

Detailed daily schedule data remains better suited to the versioned continuity files in `escrita`.

OpenWrite is where those stable facts become interconnected and useful during drafting.

## Current seed priority

The Codex should first contain:

1. stable core characters;
2. recurring locations;
3. core lore/rules;
4. Season 1 master plot;
5. Episodes 1–2;
6. Season 1 plot threads;
7. Episodes 3–4 as working chapters;
8. only then further seasonal material.

This ordering mirrors the actual narrative workflow and prevents a huge unverified database from becoming
another source of canon drift.

## Source-of-truth policy

When information differs:

1. explicitly accepted narrative decisions are authoritative;
2. `escrita` versioned canon/timeline records the current resolved form;
3. OpenWrite mirrors those facts for connected drafting;
4. an OpenWrite-generated suggestion is **not** automatically canon;
5. later AI-generated material must be reconciled before entering the stable Codex.

This prevents the Codex from silently becoming another source of accidental retcons.
