#!/usr/bin/env bash
set -euo pipefail

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_ROOT="$(cd "$PLUGIN_DIR/../.." && pwd)"
ENV_FILE="$PLUGIN_DIR/.env"
EXAMPLE_ENV_FILE="$PLUGIN_DIR/.env.example"
IMAGE="${IMAGE:-mem-api:local}"
PORT="${PORT:-8000}"

