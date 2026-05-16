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

VAULT_DIR="$REPO_DIR/ia-skill-neurona/vault"
mkdir -p "$VAULT_DIR"

if [ ! -d "$VAULT_DIR" ]; then
  printf 'Missing vault directory: %s\n' "$VAULT_DIR" >&2
  exit 1
fi

printf 'export NEURONA_VAULT=%q\n' "$VAULT_DIR"
printf 'export NEURONA_SKILL_DIR=%q\n' "$SKILL_DIR"

cat >&2 <<EOF
Initialized Neurona vault at: $VAULT_DIR

To set the temporary variables in your current shell, run:
  eval "\$($SCRIPT_DIR/init-repo-vault.sh${1:+ "$1"})"

Then the CLI can omit --vault:
  scripts/neurona.sh status
EOF
