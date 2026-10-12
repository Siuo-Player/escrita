# Character Naming Standard

Status: ESTABLISHED PROJECT RULE
Updated: 2026-10-12

## Non-negotiable rule

Do not invent character names from habit, familiarity, or a writer's recycled shortlist. Before naming an original character, inspect the current [Character Name Registry](../characters/CHARACTER_NAME_REGISTRY.md), the story decisions file, existing canon/outline files, and any open planning PR that may contain newer character decisions.

**A name explicitly chosen by the author or fixed by source canon is never replaced by the randomizer.** The method applies to new original characters and to provisional assistant-generated names that have not been confirmed. An explicit user rejection is recorded in the registry and is never reused as a candidate.

## Sources and period matching

### First names

For a character born in the United States, begin with the U.S. Social Security Administration's official baby-name tables:
- [Popular names by decade](https://www.ssa.gov/oact/babynames/decades/)
- [Top names of the 1990s](https://www.ssa.gov/OACT/babynames/decades/names1990s.html)
- [Top names of the 1960s](https://www.ssa.gov/oact/babynames/decades/names1960s.html)

Use the character's birth year or decade rather than today's baby names. When state-level tables exist and the character's birthplace is known, use the state list as additional context. These tables show actual name frequency, so "plausible for the period" is evidence-based rather than intuition.

Default filter for a new recurring original character:
- Prefer names outside the cohort's **top 100** unless a common name is an intentional part of the character design.
- Names in roughly ranks **101–200** are a useful first candidate pool for characters of the relevant historical cohort. They are still real, attested names; the goal is to avoid defaulting to the same handful of exceptionally common names, not to make every person sound exotic.
- Filter out all given names already used by a canon character, a registered original character, a family member whose name is already assigned, or a previously rejected name.
- Do not give two recurring characters the same first name merely because their full names differ. A deliberate canon exception must be recorded.

If the character is from another country, use official demographic or birth-name sources from that country and the relevant years. Do not use the U.S. list by default for a foreign-born character.

### Surnames

Use the U.S. Census Bureau's [2020 Census names data](https://www.census.gov/topics/population/genealogy/data/2020_names.html) for U.S. surname frequency and the [2010 Census surname data](https://www.census.gov/topics/population/genealogy/data/2010_surnames.html) when an older historical comparison is useful.

For ordinary U.S. original characters, build a candidate pool from plausible surnames outside the very highest-frequency group—usually from the middle/lower portion of the Census top-1,000 list. Record the Census year and rank where available. Avoid both ends of the common failure: ubiquitous surnames by default and extremely obscure surnames selected only because they sound dramatic.

The character's background, location, family history and naming traditions constrain the candidate pool. Frequency alone does not establish a surname's cultural fit, and a surname alone does not authorize the writer to invent a character's ethnicity.

## Random selection procedure

The random number must determine the choice, rather than being added afterward as decoration.

1. Build and freeze the candidate pool from the relevant demographic source.
2. Apply canon, duplicate, rejection and cultural-plausibility filters **before** drawing.
3. Generate a fresh integer seed using a secure random-number generator. Record it.
4. Sort the pool in a documented, reproducible order (normally source rank, with name as the tie-breaker).
5. Use a deterministic seeded draw to select from the frozen pool—for example, `random.Random(seed).randrange(len(pool))` in Python. For a full name, draw surname candidates from its own documented pool without replacement.
6. Record the seed, pool size, selected index, source and rank, date, and name assigned. Do not keep drawing until a preferred result appears. If the result is unsuitable, record the reason, revise the candidate pool for a substantive reason, generate a new seed, and retain the earlier draw in the audit trail.
7. Do a final human plausibility check. Randomness cannot override timeline, culture, pronunciation, character function, or the author's preferences.

A name selection is reproducible only when the seed **and** candidate pool/order are recorded. A seed without the pool is not enough.

## Family and surname continuity

- Canon families keep their canonical names and relationships.
- In a contemporary English-speaking U.S. family, the default is that children share the household's established legal family surname unless the story specifies a plausible adoption, stepfamily, blended-family, or other naming history. Marriage does not automatically require a woman to change her surname.
- Once the protagonist's surname is selected, both parents and any later siblings must use the same established family surname unless a documented family/legal reason says otherwise. Do not generate surnames independently for people who are relatives.
- For Hispanic/Latino characters, do not assume that every U.S. family follows one naming pattern. Confirm the character's family/country tradition and the family's actual U.S. legal-use choice; where relevant, account for paternal and maternal surnames.
- For East Asian, South Asian, Middle Eastern, African, European or other foreign naming traditions, research the character's specific national/cultural context and period. Given-name order, family-name placement, family-name inheritance, diacritics and transliteration vary. Do not combine conventions from different cultures without a story-grounded reason.
- A family name shared by unrelated characters is not automatically forbidden, but it is avoided for new original characters unless coincidence, marriage, adoption or a real relationship makes it useful.

## Approval and persistence

- The registry marks each name as **USER-LOCKED**, **CANON-LOCKED**, **WORKING**, **PENDING AUTHOR CHOICE**, or **RETIRED**.
- Never ask again about a recorded decision. Before asking a question, check the registry, story decisions, character profile, outline, and relevant PR history.
- If the author rejects or changes a name, update the registry and all references in the same reviewed change. Do not leave an old name in one outline, Codex seed, or character file.
- Keep display names, character file paths, plot outlines and the OpenWrite seed synchronized when a final surname changes.
- During drafting, name selection stops being a source of improvisation: use the registry.

## Current application

The protagonist's first name **Nathan** remains author-locked from the prior story decisions. His surname **Pierce is not treated as final**: the author has explicitly said it may change. See the registry for the randomly generated candidate slate and the one outstanding author decision.

The original football-peer name **Jordan Reyes** was a provisional assistant-generated choice and is now retired. The reproducible draw recorded in the registry selects **Maxwell Whitaker** instead. This is a working recurring character name, not an immutable canon fact.
