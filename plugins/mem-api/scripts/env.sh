#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

if [[ -f "$ENV_FILE" ]]; then
  grep -v '^\s*#' "$ENV_FILE" | sed '/^\s*$/d'
else
  cat "$EXAMPLE_ENV_FILE"
fi

