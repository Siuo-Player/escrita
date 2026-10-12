# AI Writing Tool Selection and Evaluation

Status: RECOMMENDED WORKFLOW
Updated: 2026-10-12

## Decision

Use the existing **OpenWrite deployment** as the drafting/manuscript interface and keep `Siuo-Player/escrita` as the authoritative store for canon, research, dates, and continuity. Use the OpenAI provider already connected to OpenWrite as the first model family to evaluate. Do not add a paid writing subscription merely because it advertises “natural” prose; no commercial claim establishes that its dialogue will fit this story better.

**Do not choose a model on reputation alone.** Model availability can vary by provider, account, and the model list exposed by OpenWrite. Test only models that actually appear in the connected provider. If available, compare a cost-conscious current GPT model (for example, `gpt-6.1-sol`) with the stronger option exposed by the account (for example, `gpt-6-astra`). These are candidates, not a pre-judged winner. Re-run the small comparison after a material model change.

If OpenWrite cannot expose the desired model or preserve useful project context, use its normal editor for the manuscript and the repository for planning; do not move the canon source of truth into an opaque third-party tool.

## Why this is evidence-led

- OpenAI's current prompting guidance says outputs are nondeterministic, that behavior can differ between models and snapshots, and that representative evaluations should be run when prompts or models change. Therefore this project should use a fixed dialogue test, version the prompt and compare outputs instead of relying on a model name or a generic “write naturally” instruction: [OpenAI — Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) and [Prompting](https://developers.openai.com/api/docs/guides/prompting).
- **LitBench** contains human preference comparisons for creative writing. Its authors report that the strongest off-the-shelf LLM judge in their tested setup agreed with human preferences 73% of the time, while trained reward models reached 78%. The result supports structured comparison, not letting an AI critic decide what is good: [LitBench paper](https://arxiv.org/abs/2507.00769).
- Research on long-form literary fiction reports differences between human- and LLM-authored fiction at macro, meso and micro levels, including a “high-starting, low-ending” pattern in model-generated works. A fluent opening is not proof that a chapter remains natural or coherent: [Towards a “Novel” Benchmark](https://aclanthology.org/2025.findings-acl.1114/).
- A separate study of creativity evaluation found that LLM evaluators can be consistent while still missing nuanced, culturally specific and context-dependent qualities. This matters for age, regional speech, family subtext and the gradual Nathan/Alex relationship: [Evaluating Creativity](https://www.mdpi.com/2076-3417/15/6/2971).

These findings do **not** establish that one currently available model writes the best dialogue for this particular story. The project-specific comparison below is the evidence we need.

## Fixed dialogue benchmark

Keep one small benchmark outside the finished manuscript. It should not be treated as canon and should not be copied into an episode.

**Scenario:** Nathan and Alex's first practical school conversation on 18 September 2009. Alex asks about the *How to Solve It* book/resource and the assigned chapters. Nathan knows the answer but is nervous because he already finds her attractive. She is interested in the resource, not yet in a romantic connection. Each should want something ordinary; neither is allowed to explain their personality or the planned relationship arc.

**Shared context:** Nathan is twelve until his birthday on 7 September 2009, then thirteen; Alex is in seventh grade and Nathan is one school year above her. He has only recently transferred. This is their first real exchange, initiated by Alex. Keep it brief, school-appropriate and rendered in natural European Portuguese. No instant flirtation, confession, overt teasing, dramatic coincidence, canon quotations, or generic “you are smarter than you think” reassurance.

**Test procedure:**
1. Use the same scene objective, canon notes, prompt version, output length, and generation settings for each candidate model. Avoid giving one candidate more context.
2. Generate two versions per candidate if the interface allows; one lucky sample is not a fair comparison.
3. Remove model names and randomize the samples before reading.
4. Score each version 1–5 on spoken rhythm, responsiveness, differentiated voices, subtext, age-appropriate behavior, restraint, continuity, and whether it avoids sounding like outline exposition.
5. Choose the passage you would actually keep—not the most ornate, witty or polished one. Record the model ID, date, prompt version, approximate cost, scores, and short reason.
6. If the models tie or neither works, revise the prompt or edit the scene manually before spending money on another service.

The author/user's judgment is the acceptance signal. A second model may highlight suspicious lines but must not replace that judgment.

## Production workflow when drafting begins

1. **Context packet:** provide only the relevant scene beats, canon files, relationship state, voices, dated facts and necessary research. Avoid dumping the entire Codex into every prompt.
2. **Outline before prose:** preserve character intention, cause/effect, parallel plots and the scene's state change. Do not ask a model to fill every bullet with a speech.
3. **Scene-size generation:** produce one scene or a pair of connected scenes at a time; carry forward only established changes.
4. **Dedicated dialogue pass:** apply `canon/narrative/DIALOGUE_NATURALNESS_STANDARD.md`. The editing prompt must diagnose named lines first and only then make targeted changes.
5. **Continuity pass:** compare the draft against the timeline, characters, props, and the previous/next scene.
6. **Human review and backpropagation:** accept or reject revisions on their merits; update earlier scenes only when later development justifies them.

Do not ask the drafting model to “sound human” and assume the result is done. That vague instruction often yields generic contractions, banter and gestures rather than convincing character-specific speech.

## Tool choices and boundaries

| Need | First choice | Reason / boundary |
|---|---|---|
| Authoring and manuscript storage | Existing OpenWrite instance | Already deployed and has the connected OpenAI provider. Verify autosave/export before major drafting. |
| Canon, research, continuity | `Siuo-Player/escrita` in Git | Versioned, diffable, reviewable, and independent of a model's memory. |
| Model selection | Small blinded comparison in OpenWrite | Measures this story's needs instead of trusting model marketing. |
| Dialogue diagnosis | Separate critic pass using the project's rubric | Useful for finding suspect turns; not authoritative for artistic judgment. |
| Read-aloud rhythm | Read aloud or basic local text-to-speech | Helps catch breathless or over-polished lines; voice synthesis itself is not a literary-quality metric. |
| Optional external writer tools | Defer | Paid tools such as Sudowrite or Novelcrafter are not prerequisites. Consider them only after the current setup is tested and a concrete shortcoming is demonstrated. |

A wider automated literary-analysis suite should remain deferred until there is a substantial Season 1 manuscript to evaluate, as previously planned. For the opening episodes, use the targeted dialogue rubric and continuity review; do not mistake a large battery of scores for a substitute for revision.
