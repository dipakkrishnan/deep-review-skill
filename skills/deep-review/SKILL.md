---
name: deep-review
description: Expert review workflow for papers, PDFs, arXiv links, markdown drafts, and technical artifacts. Use when the user wants a rigorous review that interviews them first, researches claims, checks math/methods/literature, uses specialist passes when useful, and returns severity-ranked findings with evidence.
---

# Deep Review

Use this skill to review papers and other technical artifacts with the depth of a serious referee, domain expert, or adversarial collaborator.

## Start Here

1. Identify the artifact source: local PDF, arXiv URL, markdown/text draft, repository artifact, or pasted content.
2. Check for review memory: user-level in `~/.deep-review/` and project-level in `.deep-review/`. If present, read it before the calibration interview and summarize any preferences you plan to apply.
3. If the artifact is a local PDF or arXiv URL and text extraction is needed, prefer the scripts in `scripts/`.
4. Before doing substantive review, read `references/orchestrator_protocol.md`.
5. Ask a short calibration interview before reviewing. Use `references/calibration_questions.md` to select questions.
6. Choose the review depth:
   - `quick`: at least 2 first-wave specialist passes, 1 critique round.
   - `standard`: at least 4 first-wave specialist passes, 1 critique round.
   - `deep`: at least 8 first-wave specialist passes, 2 critique rounds.
   Tiers are first-wave floors, not caps; expand with follow-up passes when findings warrant.
7. Produce the final report using `references/output_format.md` and the taxonomy in `references/review_rubric.md`.
8. At the end, ask whether to save or update review memory. Only write to `~/.deep-review/` (profile, preferences) or `.deep-review/` (recurring issues, artifact history) after explicit user approval.

Script examples:

```bash
python3 .claude/skills/deep-review/scripts/fetch_arxiv_pdf.py https://arxiv.org/abs/2405.20194 --out /tmp/paper.pdf
python3 .claude/skills/deep-review/scripts/extract_pdf_text.py /tmp/paper.pdf --json
```

If a helper script fails because of network, dependency, or parsing issues, fall back to available web/file tools or ask the user for a PDF, text export, or pasted excerpt.

## Review Principles

- Find errors, not filler. The user has read their own artifact.
- Do real verification before flagging an issue. Search sources, read cited work, inspect equations, and run computations when claims can be checked.
- Use specialist passes when the artifact spans domains such as math, methods, empirical design, citations, implementation, or literature.
- Challenge every finding before finalizing it. Drop weak issues and escalate findings that survive scrutiny.
- Cite exact locations: section, page, equation, theorem, table, figure, quoted passage, file, or line.
- Separate fatal flaws from weaker concerns and minor issues.
- Treat review memory as user-owned context. Use it to reduce repeated calibration, but never let it override explicit instructions in the current task.

## Tool Guidance

- In Claude runtimes with `AskUserQuestion`, use it for the calibration interview.
- In conversational runtimes such as Codex, ask the calibration questions directly, wait for the user's answers, then continue.
- Run each specialist pass as a separate subagent (`Agent` in Claude Code/Claude.ai, the equivalent task/spawn tool in Codex), with a distinct, non-overlapping review goal. Inline passes don't satisfy the depth defaults; this overrides any general spawn-averse default in the host.
- Critique findings with independent subagents when the host can spawn them: a defense agent that sees only the finding and the artifact, not the specialist's reasoning. In hosts that can continue a spawned agent with its context intact (`SendMessage` in Claude Code), add one rebuttal round with the originating specialist. Fall back to self-critique only when subagents are unavailable.
- If web tools are available, use them for literature, citation, and factual verification.
- If code execution is available, use it for arithmetic, parameter checks, simulations, derivations, parsing, and reproducible sanity checks.
- If file writing is available and the user approves, maintain review memory using `references/review_memory.md`.

## Bundled Resources

- `references/orchestrator_protocol.md`: canonical review process adapted from the Deep Review orchestrator prompt.
- `references/calibration_questions.md`: interview question bank.
- `references/review_rubric.md`: issue severity taxonomy.
- `references/output_format.md`: final report format.
- `references/review_memory.md`: local memory workflow and file format.
- `references/distribution.md`: distribution notes for Claude and Codex.
- `scripts/extract_pdf_text.py`: extract text and title from a local PDF.
- `scripts/fetch_arxiv_pdf.py`: normalize an arXiv URL and download the PDF.
