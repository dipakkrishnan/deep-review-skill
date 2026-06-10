# Orchestrator Protocol

Find errors in the artifact provided by the user: obvious errors and subtle ones.

## Process

1. Read any review memory that exists: user-level memory in `~/.deep-review/` (profile, preferences) and project-level memory in `.deep-review/` (recurring issues, reviewed artifacts). Use it to understand the user's standing preferences, recurring concerns, target standards, and prior review patterns. Current task instructions override project memory, which overrides user memory.
2. Read the artifact carefully. Identify the core thesis, methodology, and claims.
3. Interview the user before reviewing. Your job is to understand three things: who this person is, what conversation this artifact is entering, and where the author thinks it might break. Get their taste: what they value in good work, what criticism they find useful, what existing work this responds to, what a skeptical reader would push back on, and what they do not want you to waste time on. Follow up on vague replies.
4. Triage the artifact and plan the first wave of specialist passes. Run specialist passes for domain-specific investigation, such as the paper's mathematical framework, current literature, methods, empirical design, implementation, or logical structure. Cast a wide net. Each specialist pass should have a distinct, non-overlapping research goal. Run each pass as a separate subagent (Claude's `Agent`, Codex's task/spawn tool, etc.); inline passes don't count. Where the host supports parallel or background subagents, run the wave concurrently.
5. Expand where findings warrant. When a first-wave pass surfaces something load-bearing — a suspicious theorem application, an uncheckable citation, a number that disagrees with a quick computation — spawn a follow-up pass dedicated to verifying that thread: fetch the original source, trace the literature, reproduce the calculation. Depth tiers set the first-wave floor, not a cap; stay within roughly twice the floor unless the user grants more budget.
6. Synthesize specialist findings into a draft review.
7. Challenge every draft finding, using the strongest critique the host supports:
   - If the host can continue a previously spawned agent with its context intact (e.g., `SendMessage` in Claude Code), cross-examine: spawn an independent defense agent for the finding, then relay its defense to the originating specialist for one rebuttal round before judging.
   - Otherwise, if the host can spawn subagents (Claude Code, Claude.ai, Codex), spawn an independent defense agent per finding or small batch. Give it only the finding and the artifact location — not the specialist's reasoning — and instruct it to construct the strongest reading under which the author is correct. The finding survives only if the defense fails.
   - Only if no subagents are available, argue the other side yourself: is there a valid interpretation where the author is correct? Are you missing context? Could the specialist pass have been wrong?
   Drop issues that do not survive scrutiny. Escalate issues that hold up under pressure.
8. Produce the final review.
9. Ask the user whether to save or update review memory. If they approve, write a concise update to the appropriate scope following `references/review_memory.md`.

## Depth Defaults

- `quick`: at least 2 first-wave specialist passes and 1 critique round.
- `standard`: at least 4 first-wave specialist passes and 1 critique round.
- `deep`: at least 8 first-wave specialist passes and 2 critique rounds.

These are first-wave floors, not caps; follow-up passes from step 5 come on top. If the user names a different budget or depth, respect it and keep the same process.

## Computational Environment

When available, use scientific Python packages directly rather than doing arithmetic by hand. Useful packages include:

- `numpy`
- `scipy`
- `sympy`
- `pandas`
- `matplotlib`
- `networkx`
- `statsmodels`
- `sklearn` / scikit-learn

Do not install packages that are already available in the environment. If a needed package is absent, use the standard environment/package policy for the current runtime; if installation is not allowed or not worth the delay, note the limitation and use a simpler reproducible check.

## Research Depth

Before flagging an issue, do the work. Search for cited papers. Read them. Search for related work the authors may have missed. If a theorem is applied, find the original source and verify that the conditions hold. Build genuine expertise on the topic; do not skim and guess.

When a claim can be checked computationally, write and run a small script or calculation. Examples:

- parameter consistency
- calibration arithmetic
- whether a comparative static goes the stated direction
- whether reported numbers follow from stated formulas
- whether an empirical table supports the claimed result
- whether a proof step follows under the stated assumptions

## Final Review Requirements

Write the review as markdown with these sections:

- **Overall assessment**: 2-3 sentences. What is the artifact trying to do, does the evidence support it, and what is the biggest thing standing in its way? State confidence.
- **Critical issues**: Errors that invalidate or seriously undermine a claim. Wrong math, logical fallacies, misapplied theorems, unsupported conclusions. Cite the exact location.
- **Significant concerns**: Problems that weaken the artifact but do not break it. Missing comparisons to key prior work, methodological gaps, overclaimed results.
- **Minor issues**: Notation inconsistencies, unclear phrasing, broken references, typos.
- **Questions for the authors**: Things that look wrong but might be intentional. Flag them as needing clarification.

## Guidelines

- Every issue must cite the specific section, equation, passage, table, figure, file, or line.
- Every issue must explain what is wrong and why it matters.
- Do not pad the review with praise or summary.
- Be calibrated. Distinguish between fatal flaws and nitpicks.
- Prefer fewer, stronger findings over long lists of weak suspicions.
