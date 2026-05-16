#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

[ -f "$ENV_FILE" ] || bash "$PLUGIN_DIR/scripts/setup.sh"

docker compose -f "$PLUGIN_DIR/docker-compose.yml" --env-file "$ENV_FILE" up -d --build
trap 'docker compose -f "$PLUGIN_DIR/docker-compose.yml" --env-file "$ENV_FILE" down >/dev/null 2>&1 || true' EXIT

python3 - <<'PY'
from pathlib import Path
import urllib.request
import json
import time

for _ in range(30):
    try:
        with urllib.request.urlopen("http://127.0.0.1:8000/health", timeout=2) as response:
            data = json.loads(response.read().decode("utf-8"))
            assert data["service"] == "mem-api"
            assert data["vault"]
            assert data["instance_file"]
            break
    except Exception:
        time.sleep(1)
else:
    raise SystemExit("health endpoint did not become ready")
PY

printf 'smoke ok\n'
