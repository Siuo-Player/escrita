# Character Name Registry

Status: AUTHORITATIVE NAME AND NAMING-DECISION LEDGER
Updated: 2026-10-12

This file is the place to check before asking the author about a name or introducing a new original character. The [Character Naming Standard](../narrative/CHARACTER_NAMING_STANDARD.md) defines the selection method.

## Author-locked and canon-locked

| Character / group | Name | Status | Rule |
|---|---|---|---|
| Protagonist | **Nathan** (given name) | USER-LOCKED | The author chose Nathan after rejecting Ethan Brooks. Do not change his given name just because Nathan is statistically common. |
| Modern Family characters | Claire, Phil, Haley, Alex and Luke Dunphy; Jay and Gloria Pritchett; Manny Delgado; Mitchell Pritchett; Cameron Tucker; DeDe Pritchett; Dylan Marshall; others from the show | CANON-LOCKED | Preserve source-canon names and relationships. |
| Protagonist's family | Shared surname | PENDING AUTHOR CHOICE | All documents currently use Pierce, but the author has said the surname may change. Once chosen, parents and any later siblings must follow the same family-name rules. |

## Pending protagonist surname

A reproducible draw generated a shortlist of three U.S. surnames for the author to review. The pool excludes the surname currently assigned to the working original peer so the two unrelated characters cannot accidentally receive the same name. The candidates are ordered by the random draw, not by a model's personal taste.

| Draw order | Candidate | 2020 U.S. Census surname rank | Notes |
|---:|---|---:|---|
| 1 | **Gentry** | 821 | English-language surname; plausible in the United States. |
| 2 | **Callahan** | 682 | Often associated with Irish origin; use only if that background fits the family the author wants. |
| 3 | **Ellison** | 829 | English-language surname; plausible in the United States. |

**Current document placeholder:** Pierce. It remains in paths and working profiles until the author selects a replacement or confirms that Pierce should remain. No name-dependent family details should be finalized on the assumption that Pierce is permanent.

If all three are rejected, do not repeatedly reroll the same pool. Ask for any cultural/phonetic preference that materially narrows the set, then rebuild and record a new candidate pool and seed.

## Original character selected by the naming process

### Maxwell Whitaker — recurring football peer

- **Full name:** Maxwell Whitaker.
- **Status:** WORKING; replaces the provisional name Jordan Reyes.
- **Narrative role:** a competitive but fair teammate who wants more meaningful playing time, tests whether Nathan listens, gradually trusts him, and maintains goals outside Nathan.
- **Name evidence:** the SSA's 1990s male names table lists Maxwell at rank **161**; Whitaker ranked **610** in the U.S. Census Bureau's 2020 surname data.
- **Random selection audit:** seed `687708412`; first-name candidate pool size 95; zero-based selected index 58; selected given name Maxwell. The surname pool, filtered to plausible non-top-frequency U.S. surnames and ordered as Whitaker (#610), Callahan (#682), Ellison (#829), Gentry (#821), was shuffled from the same seeded random stream. Its order was Gentry, Callahan, Ellison, Whitaker: the first three became the protagonist's candidate slate and Whitaker was assigned to the peer without reuse.
- **Sources:** [SSA — Top names of the 1990s](https://www.ssa.gov/OACT/babynames/decades/names1990s.html); [U.S. Census Bureau — 2020 Census names data](https://www.census.gov/topics/population/genealogy/data/2020_names.html); rank cross-check for Whitaker: [2020 surname frequency derived from Census data](https://www.namecensus.com/last-names/whitaker-surname-popularity/).

Keep Maxwell's existing role and personality beats. Do not create relatives, ancestry or additional personal history simply to justify the name; decide those details only when the timeline needs them.

## Existing names that are provisional or need review

| Current working name | Status | Instruction |
|---|---|---|
| Nathan Pierce | PENDING AUTHOR CHOICE on surname; USER-LOCKED on Nathan | Do not replace Nathan. Do not assume Pierce is final. |
| David / Melissa [family surname currently Pierce] | Existing WORKING labels in the established story bible | They are already used as the protagonist's parents. Preserve the roles and continuity; do not rename them casually inside a scene. If the author later wants to apply the random-name process retroactively to their first names, regenerate and migrate all references together. |
| Jordan Reyes | RETIRED | Provisional assistant-generated name superseded by Maxwell Whitaker. Do not reuse for this character or another new original character. |
| Ethan Brooks | REJECTED / RETIRED | The author rejected it as an overused fan-fiction-style choice. Never revive it as the protagonist or a new character. |
| Pierce | PENDING | Existing placeholder for the protagonist's family surname, not a user-locked choice. |

## Duplicate prevention

Before committing any new original name:
1. Search this registry and the Git tree for the full name, given name, surname, and known aliases.
2. Check existing outlines, character schedules, the character episode grid, open PRs, and the OpenWrite seed.
3. Keep original characters' given names unique unless the author explicitly approves a deliberate exception.
4. Do not assign a sibling, parent, child, or spouse an independently randomized surname; derive it from the established family/legal naming rules.
5. Update this registry in the same PR that adds or renames the character.


### Reproducibility appendix for seed `687708412`

This is the **exact first-name candidate pool**, in the order used for the seeded draw. It is the male-name list at SSA 1990s ranks 101–200, after removing names already in use, the retired Ethan/Jordan choices, the protagonist's name and close/likely-confusing variants. The order follows the SSA source table, with removed candidates omitted. The list is frozen for this record; changing it requires a new draw and a new log entry.

```text
00 Tanner
01 Angel
02 Vincent
03 Isaiah
04 Dalton
05 Brett
06 George
07 Alejandro
08 Elijah
09 Cory
10 Cole
11 Joel
12 Erik
13 Jake
14 Mason
15 Jorge
16 Dillon
17 Raymond
18 Colton
19 Ricardo
20 Casey
21 Brendan
22 Devon
23 Keith
24 Colin
25 Wesley
26 Oscar
27 Julian
28 Johnathan
29 Eduardo
30 Chad
31 Donald
32 Bryce
33 Ronald
34 Alec
35 Dominic
36 Grant
37 Martin
38 Henry
39 Mario
40 Xavier
41 Manuel
42 Alan
43 Derrick
44 Frank
45 Tristan
46 Collin
47 Omar
48 Jeremiah
49 Jackson
50 Troy
51 Edgar
52 Javier
53 Douglas
54 Clayton
55 Jonathon
56 Nicolas
57 Andre
58 Maxwell
59 Ivan
60 Levi
61 Sergio
62 Roberto
63 Darius
64 Andres
65 Cristian
66 Hector
67 Fernando
68 Curtis
69 Gary
70 Riley
71 Johnny
72 Max
73 Dennis
74 Malik
75 Wyatt
76 Cesar
77 Edwin
78 Gavin
79 Preston
80 Marco
81 Allen
82 Ruben
83 Calvin
84 Mathew
85 Randy
86 Brent
87 Jerry
88 Hayden
89 Parker
90 Brady
91 Tony
92 Pedro
93 Craig
94 Larry
```

With Python's `random.Random(687708412).randrange(95)`, the selected zero-based index was **58**, yielding **Maxwell**. The same seeded generator was then used to shuffle the surname pool. Input order and ranks were `Whitaker (#610), Callahan (#682), Ellison (#829), Gentry (#821)`; the shuffled order was `Gentry, Callahan, Ellison, Whitaker`. The first three became the protagonist's pending surname slate; Whitaker was assigned to Maxwell without reuse.

Filtering notes for this draw: the pool excluded existing canon/registered first names and variants, including Nathan, David, Melissa, Claire, Phil/Philip/Phillip, Haley, Alex/Alexis, Luke, Jay, Gloria, Manny, Mitchell, Cameron, DeDe, Dylan, Ethan, Jordan, Nathaniel and Drew. This is the selection history for this draw, not an instruction to exclude every one of those names from all future demographic data; the general duplicate/rejection filters in the naming standard govern future pools.
