# Deep Review

Deep Review is an experimental skill for rigorous review of papers and technical artifacts.

It asks a short calibration interview, reads the artifact carefully, decomposes the review into specialist passes, checks claims against sources and computations where possible, self-critiques its own findings, and returns a severity-ranked review.

The goal is simple: find the errors a generic chat-with-file pass is likely to miss.

Deep Review can also maintain optional review memory — user-level taste in `~/.deep-review/` and project-level history in `.deep-review/` — so future reviews can pick up the user's preferred standards, recurring concerns, and review taste. It only writes memory after explicit user approval.

## What It Is Good For

- pre-submission paper review
- theorem or proof stress tests
- empirical / methods audits
- literature positioning checks
- technical memo review
- AI-generated draft review

## Status

This is early. I am distributing it personally for now while I learn where it is most useful.

If you want to try it on a real paper or artifact, open an issue or reach out.

## Install

### Claude Code

Add the direct Deep Review marketplace:

```text
/plugin marketplace add dipakkrishnan/deep-review-skill
/plugin install deep-review@deep-review-marketplace
/reload-plugins
```

This is the fastest install path while the approved community marketplace listing propagates.

Or copy the skill folder into a project directly:

```bash
mkdir -p .claude/skills
cp -R /path/to/deep-review-skill/skills/deep-review .claude/skills/deep-review
```

Then ask Claude Code:

```text
Use $deep-review to review this paper for theorem correctness and literature positioning.
```

### Claude.ai

Download [`deep-review.zip`](https://github.com/dipakkrishnan/deep-review-skill/releases/latest/download/deep-review.zip) (always points at the latest release), then in Claude.ai go to **Customize → Skills → + → Upload a skill** and drop the zip in.

To build the zip yourself from a checkout:

```bash
scripts/package-skill.sh
# produces dist/deep-review.zip
```

### Codex

Codex does not yet expose a marketplace-style installer for third-party plugins. Copy the skill into a Codex skills directory and restart Codex:

```bash
cp -R skills/deep-review "$CODEX_HOME/skills/deep-review"
```

## Example Prompts

```text
Use $deep-review to review this PDF as a skeptical economics referee. Focus on model correctness, calibration, and missing literature.
```

```text
Use $deep-review to stress-test the proof of Theorem 2 and identify assumptions that do not hold.
```

```text
Use $deep-review to review this technical memo. Skip copy edits and focus on unsupported claims.
```

## What To Expect

Deep Review will usually ask a few calibration questions first:

- What is your relationship to the artifact?
- What kind of criticism is most useful?
- Which parts worry you most?
- What should it avoid spending time on?

Then it produces a markdown review with:

- overall assessment
- critical issues
- significant concerns
- minor issues
- questions for the authors

Optionally, Deep Review can save local memory for future runs:

- standing review preferences
- target venues or standards
- recurring issue patterns
- lightweight history of reviewed artifacts

## Requirements

The skill itself is instructions and references.

The helper scripts require Python. PDF extraction uses PyMuPDF:

```bash
pip install pymupdf
```

## Privacy

Deep Review does not collect telemetry or send data to any third-party service controlled by this plugin. See [PRIVACY.md](PRIVACY.md).

## Notes

Deep Review is not a replacement for expert human judgment. It is a way to make review cheaper, sharper, and more adversarial before you ask humans to spend scarce attention on the artifact.
