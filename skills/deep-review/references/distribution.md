# Distribution

This skill is packaged as a Claude Code plugin with Codex-style skill metadata.

## Claude Code

Install Deep Review from the direct marketplace hosted in this repository:

```text
/plugin marketplace add dipakkrishnan/deep-review-skill
/plugin install deep-review@deep-review-marketplace
/reload-plugins
```

This is the recommended path while the community marketplace listing is propagating. Once Deep Review lands in `anthropics/claude-plugins-community`, users can also install it from there:

```text
/plugin marketplace add anthropics/claude-plugins-community
/plugin install deep-review@claude-community
/reload-plugins
```

For local iteration, point `/plugin marketplace add` at a checkout of this repository:

```text
/plugin marketplace add /path/to/deep-review-skill
```

The skill is also usable as a project-scoped skill by copying `skills/deep-review` into a project's `.claude/skills/deep-review` directory.

References:

- https://code.claude.com/docs/en/plugin-marketplaces
- https://code.claude.com/docs/en/discover-plugins
- https://docs.claude.com/en/docs/claude-code/skills

## Claude.ai

Claude.ai has no marketplace mechanism for plugins, so distribution is via the zip-upload Skills flow. The lowest-friction path for users:

1. Download `deep-review.zip` from the repository's GitHub Releases page.
2. In Claude.ai, go to **Customize → Skills → + → Upload a skill** and drop the zip in.

Custom uploads are private to the uploading user's account by default.

To build the zip from a checkout, run `scripts/package-skill.sh`. The output (`dist/deep-review.zip`) contains a single `deep-review/` folder with `SKILL.md` at its root, which is the layout Claude.ai expects.

Reference: https://support.claude.com/en/articles/12512180-using-skills-in-claude

## Claude Team And Enterprise

Organization owners can provision a zipped skill for all users. Depending on organization settings, users can also share skills directly with colleagues or publish them to an organization directory.

Reference: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization

## Codex

Codex does not yet expose a marketplace-style installer for third-party plugins. Distribution today is by copying the skill into a Codex skills directory and restarting Codex:

```bash
cp -R skills/deep-review "$CODEX_HOME/skills/deep-review"
```

The Codex-facing metadata in `.codex-plugin/plugin.json` and `skills/deep-review/agents/openai.yaml` lets Codex-aware interfaces display a name, short description, and default prompt once the skill is loaded.
