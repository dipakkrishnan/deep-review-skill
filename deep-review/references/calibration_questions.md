# Calibration Questions

Ask 3-7 targeted questions before beginning substantive review. Prefer fewer questions when the user is impatient or the artifact is small. Ask follow-ups when answers are vague.

## Core Questions

- What is your relationship to this artifact: author, co-author, reviewer, advisor, reader, or evaluator?
- What kind of review is most useful right now: fatal flaw hunt, referee report, math/proof check, empirical/methods audit, literature positioning, implementation audit, or broad review?
- What target standard should I use: top journal, workshop, internal memo, preprint, production readiness, investment diligence, or another bar?
- Which parts worry you most?
- What existing work, code, dataset, author, or debate is this artifact responding to?
- What would a skeptical expert push back on?
- What should I avoid spending time on?

## Domain-Specific Follow-Ups

For theory or math:

- Which theorem, lemma, derivation, or assumption is most load-bearing?
- Should missing proof details be treated as flaws or deferred to appendices?
- Are there known edge cases or counterexamples you want checked?

For empirical work:

- Which results are central to the claim?
- Are data, code, or replication files available?
- Which robustness checks matter for the target audience?

For literature positioning:

- Which community or conversation is this entering?
- Which papers or authors should be treated as must-cite context?
- Is novelty, correctness, or usefulness the main question?

For code or implementation artifacts:

- What behavior is the artifact supposed to guarantee?
- Which failure modes are most costly?
- Should the review include running tests or writing reproduction scripts?

## Answer Handling

Summarize the scope back to the user in one short paragraph before beginning the review. In Claude runtimes that expose `AskUserQuestion`, use it. Otherwise ask directly in chat and wait for answers.
