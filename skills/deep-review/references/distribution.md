# Distribution

This skill is packaged as a Claude Code plugin with Codex-style skill metadata.

## Claude Code

Claude Code can load this repository as a plugin. For local testing, run:

```bash
claude --plugin-dir /path/to/deep-review-skill
```

The skill is also usable as a project skill by copying `skills/deep-review` into a project's `.claude/skills/deep-review` directory.

Reference: https://docs.claude.com/en/docs/claude-code/skills

## Claude.ai

Zip the `skills/deep-review` skill folder and upload it through Claude's Customize > Skills flow. Custom uploads are private to the uploading user's account by default.

Reference: https://support.claude.com/en/articles/12512180-using-skills-in-claude

## Claude Team And Enterprise

Organization owners can provision a zipped skill for all users. Depending on organization settings, users can also share skills directly with colleagues or publish them to an organization directory.

Reference: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization

## Codex

Codex can use this repository either as a plugin or as a standalone skill.

Plugin install shape:

```bash
npx codex-marketplace add OWNER/REPO --plugin
```

Standalone skill install shape:

```text
repo: OWNER/REPO
path: skills/deep-review
```

Codex skills can be installed into `$CODEX_HOME/skills`. Practical skill distribution is via a GitHub repository path or a curated skills collection. This package includes `agents/openai.yaml` so Codex-style interfaces can display a name, short description, and default prompt.

Typical Codex skill-installer shape:

```bash
# Run through Codex's skill installer tooling, not as a generic shell command:
install-skill-from-github.py --repo OWNER/REPO --path skills/deep-review
```

After installing a skill into Codex, restart Codex so it can discover the new skill.
