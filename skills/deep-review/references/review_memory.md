# Review Memory

Deep Review can maintain user-owned memory at two scopes. This is optional. Never create or update these files without explicit user approval.

- **User scope** (`~/.deep-review/`): who the user is and their standing taste. Follows the user across projects.
- **Project scope** (`.deep-review/` in the working directory): patterns and history tied to this body of work.

Precedence: current task instructions override project memory, which overrides user memory.

## Purpose

Use review memory to reduce repeated calibration and make future reviews more aligned with the user's taste.

Good memory captures:

- the user's role and field
- target venues or standards
- preferred review style
- topics or checks to prioritize
- things to avoid spending time on
- recurring weaknesses in prior artifacts
- prior reviewed artifacts and high-level outcomes

Do not store sensitive artifact text, full paper contents, private reviewer comments, API keys, credentials, or personal data that is not needed for future review behavior.

## Files

Use these files when helpful:

```text
~/.deep-review/          # user scope
  profile.md
  preferences.md
.deep-review/            # project scope
  recurring-issues.md
  reviewed-artifacts.md
```

If an older project `.deep-review/` still contains `profile.md` or `preferences.md`, read them as usual, and on the next approved memory write offer to move them to `~/.deep-review/`.

`profile.md` describes the user or group:

```markdown
# Deep Review Profile

- Role:
- Fields:
- Typical artifact types:
- Target standards:
- Standing context:
```

`preferences.md` records how the user likes reviews run:

```markdown
# Review Preferences

- Preferred review style:
- Default depth:
- Prioritize:
- Deprioritize:
- Always check:
- Avoid:
```

`recurring-issues.md` tracks patterns across reviews:

```markdown
# Recurring Issues

- Pattern:
  - Seen in:
  - Why it matters:
  - Suggested preventive check:
```

`reviewed-artifacts.md` records lightweight history:

```markdown
# Reviewed Artifacts

## YYYY-MM-DD - Title or short description

- Artifact type:
- Review focus:
- Most important finding:
- User-approved memory update:
```

## Start Of Review

If `~/.deep-review/` or `.deep-review/` exists:

1. Read the relevant memory files from both scopes.
2. Summarize the preferences you plan to apply in one short paragraph.
3. Ask any calibration questions still needed for this artifact.

If memory conflicts with the current user request, follow the current request and mention the conflict briefly.

## End Of Review

After the final review, ask:

```text
Should I save or update Deep Review memory for future reviews?
```

If the user says yes:

1. Propose the exact memory update.
2. Keep it concise and inspectable.
3. Write each fact to its scope: profile and preferences to `~/.deep-review/`, recurring issues and artifact history to `.deep-review/`. Write nowhere else.
4. Do not save artifact text unless the user explicitly asks.

If the user says no or does not answer, do not write memory.
