#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ "${1:-}" != "" ]; then
  REPO_DIR="$(cd "$1" && pwd)"
elif git -C "$SKILL_DIR" rev-parse --show-toplevel >/dev/null 2>&1; then
  REPO_DIR="$(git -C "$SKILL_DIR" rev-parse --show-toplevel)"
else
  REPO_DIR="$SKILL_DIR"
fi

"$SCRIPT_DIR/neurona.sh" init --vault "$REPO_DIR" >/dev/null

printf 'export NEURONA_VAULT=%q\n' "$REPO_DIR"
printf 'export NEURONA_SKILL_DIR=%q\n' "$SKILL_DIR"

cat >&2 <<EOF
Initialized Neurona vault at: $REPO_DIR

To set the temporary variables in your current shell, run:
  eval "\$($SCRIPT_DIR/init-repo-vault.sh${1:+ "$1"})"

Then the CLI can omit --vault:
  scripts/neurona.sh status
EOF
