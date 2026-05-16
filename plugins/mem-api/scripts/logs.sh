#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

docker compose -f "$PLUGIN_DIR/docker-compose.yml" --env-file "$ENV_FILE" logs -f

