#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

docker build -t "$IMAGE" -f "$PLUGIN_DIR/Dockerfile" "$REPO_ROOT"

