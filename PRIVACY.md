# Privacy Policy

Deep Review is a Claude Code plugin and skill for reviewing papers and technical artifacts.

## Data Collection

Deep Review does not collect, transmit, sell, or share user data.

The plugin does not include telemetry, analytics, tracking pixels, external logging, or background network services.

## Review Memory

Deep Review can optionally write review memory to local markdown files:

- `~/.deep-review/` for user-level profile and review preferences
- `.deep-review/` in the working directory for project-level recurring issues and reviewed-artifact history

Review memory is disabled by default. Deep Review only creates or updates these files after explicit user approval, and it proposes the exact update before writing it.

Review memory should not contain full artifact text, private reviewer comments, credentials, API keys, or personal data that is not needed to guide future reviews. Users can inspect, edit, or delete the files at any time using normal filesystem tools.

## User Artifacts

Users may provide papers, PDFs, arXiv links, markdown drafts, code, or other technical artifacts to Claude while using this plugin.

Those artifacts are handled by the Claude or Codex environment in which the user runs the skill. Deep Review itself does not receive or store a copy of those artifacts outside the user's local/runtime environment. Review memory stores only the concise, user-approved context described above.

## Helper Scripts

Deep Review includes optional helper scripts for:

- extracting text from local PDFs
- downloading PDFs from arXiv links

These scripts run only when invoked by the user or agent. They do not send data to any service controlled by Deep Review.

The arXiv helper downloads a PDF from `arxiv.org` when given an arXiv URL.

## Third-Party Services

Deep Review does not integrate with third-party analytics or storage services.

Use of Claude, Claude Code, Claude Cowork, Codex, GitHub, arXiv, or other tools is governed by those services' own privacy policies.

## Contact

For privacy questions, open an issue at:

https://github.com/dipakkrishnan/deep-review-skill/issues
