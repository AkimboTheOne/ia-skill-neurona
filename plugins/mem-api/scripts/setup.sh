#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

if [[ ! -f "$ENV_FILE" ]]; then
  cp "$EXAMPLE_ENV_FILE" "$ENV_FILE"
  printf 'created %s\n' "$ENV_FILE"
else
  printf 'exists %s\n' "$ENV_FILE"
fi

printf 'repo_root=%s\n' "$REPO_ROOT"
printf 'plugin_dir=%s\n' "$PLUGIN_DIR"
printf 'edit %s to bind the vault consumed by the service\n' "$ENV_FILE"

