#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_FILE="${1:-$REPO_DIR/.tmp/agents-setup-state.json}"

if [ ! -f "$STATE_FILE" ]; then
  printf 'Missing agent setup state: %s\n' "$STATE_FILE" >&2
  printf 'Re-run scripts/setup-repo-for-agents.sh and restart the session if instructions changed.\n' >&2
  exit 1
fi

python3 - "$STATE_FILE" <<'PY'
import json, sys, pathlib
path = pathlib.Path(sys.argv[1])
data = json.loads(path.read_text())
repo = pathlib.Path(data["repo_dir"])
plugin = pathlib.Path(data["plugin_path"])
instance = repo / "ia-skill-neurona" / "instance.json"
guide = repo / "AGENTS.md"
errors = []
if not guide.exists():
    errors.append("missing AGENTS.md")
if not plugin.exists():
    if data.get("plugin_status") != "unavailable":
        errors.append("missing plugin path")
if not instance.exists():
    errors.append("missing instance.json")
if data.get("plugin_status") == "conflict":
    errors.append("plugin conflict recorded")
if errors:
    for err in errors:
        print(err, file=sys.stderr)
    raise SystemExit(1)
print(json.dumps({
    "ok": True,
    "repo_dir": str(repo),
    "plugin_path": str(plugin),
    "instance_path": str(instance),
    "next_step": "If AGENTS.md changed, restart the session or reload the agent context."
}, ensure_ascii=False))
PY
