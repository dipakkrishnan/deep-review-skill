#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_SRC="$REPO_ROOT/skills/deep-review"
OUT_DIR="$REPO_ROOT/dist"
ARCHIVE="$OUT_DIR/deep-review.zip"
STAGING="$(mktemp -d)"

trap 'rm -rf "$STAGING"' EXIT

if [[ ! -f "$SKILL_SRC/SKILL.md" ]]; then
  echo "error: $SKILL_SRC/SKILL.md not found" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
cp -R "$SKILL_SRC" "$STAGING/deep-review"

find "$STAGING/deep-review" \( \
    -name '.DS_Store' -o \
    -name '__pycache__' -o \
    -name '*.pyc' -o \
    -name '.pytest_cache' \
  \) -exec rm -rf {} +

rm -f "$ARCHIVE"
(cd "$STAGING" && zip -rq "$ARCHIVE" deep-review)

echo "Built $ARCHIVE"
echo "Upload via Claude.ai → Customize → Skills → + → Upload a skill"
