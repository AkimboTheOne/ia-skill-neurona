#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

[ -f "$ENV_FILE" ] || bash "$PLUGIN_DIR/scripts/setup.sh"

docker compose -f "$PLUGIN_DIR/docker-compose.yml" --env-file "$ENV_FILE" up --build
