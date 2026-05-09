---
name: deep-review
description: Expert review workflow for papers, PDFs, arXiv links, markdown drafts, and technical artifacts. Use when the user wants a rigorous review that interviews them first, researches claims, checks math/methods/literature, uses specialist passes when useful, and returns severity-ranked findings with evidence.
---

# Deep Review

Use this skill to review papers and other technical artifacts with the depth of a serious referee, domain expert, or adversarial collaborator.

## Start Here

1. Identify the artifact source: local PDF, arXiv URL, markdown/text draft, repository artifact, or pasted content.
2. If the artifact is a local PDF or arXiv URL and text extraction is needed, prefer the scripts in `scripts/`.
3. Before doing substantive review, read `references/orchestrator_protocol.md`.
4. Ask a short calibration interview before reviewing. Use `references/calibration_questions.md` to select questions.
5. Choose the review depth:
   - `quick`: at least 2 specialist passes, 1 self-critique round.
   - `standard`: at least 4 specialist passes, 1 self-critique round.
   - `deep`: at least 8 specialist passes, 2 self-critique rounds.
6. Produce the final report using `references/output_format.md` and the taxonomy in `references/review_rubric.md`.

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

## Tool Guidance

- In Claude runtimes with `AskUserQuestion`, use it for the calibration interview.
- In conversational runtimes such as Codex, ask the calibration questions directly, wait for the user's answers, then continue.
- If subagents are available, give each one a distinct, non-overlapping review goal.
- If web tools are available, use them for literature, citation, and factual verification.
- If code execution is available, use it for arithmetic, parameter checks, simulations, derivations, parsing, and reproducible sanity checks.

## Bundled Resources

- `references/orchestrator_protocol.md`: canonical review process adapted from the Deep Review orchestrator prompt.
- `references/calibration_questions.md`: interview question bank.
- `references/review_rubric.md`: issue severity taxonomy.
- `references/output_format.md`: final report format.
- `references/distribution.md`: distribution notes for Claude and Codex.
- `scripts/extract_pdf_text.py`: extract text and title from a local PDF.
- `scripts/fetch_arxiv_pdf.py`: normalize an arXiv URL and download the PDF.
