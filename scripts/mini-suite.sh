#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VAULT_DIR="${1:-$SKILL_DIR/ia-skill-neurona/vault}"

rm -rf "$VAULT_DIR"
mkdir -p "$VAULT_DIR"

assert() {
  local condition="$1"
  local message="$2"
  if ! eval "$condition"; then
    printf 'FAIL: %s\n' "$message" >&2
    exit 1
  fi
}

run_json() {
  local output
  output="$("$SCRIPT_DIR/neurona.sh" "$@" --vault "$VAULT_DIR")"
  printf '%s\n' "$output"
}

init_out="$(run_json init)"
printf '%s\n' "$init_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["directories"] == 10'

bash "$SCRIPT_DIR/setup-repo-for-agents.sh" >/dev/null 2>&1

status_out="$(run_json status)"
printf '%s\n' "$status_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["initialized"] is True'

capture_out="$(run_json capture --text "La documentación del proyecto debe ser consistente y legible para personas y agentes.")"
printf '%s\n' "$capture_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["source"] == "manual"'

process_out="$(run_json process-inbox)"
printf '%s\n' "$process_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["processed"] == 1'

connect_out="$(run_json connect --days 7 --limit 5)"
printf '%s\n' "$connect_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["notes_scanned"] == 1'

brief_out="$(run_json brief --topic "documentacion editorial")"
printf '%s\n' "$brief_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["topic"] == "documentacion editorial"'

health_out="$("$SCRIPT_DIR/agents-healthcheck.sh")"
printf '%s\n' "$health_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and "next_step" in data'

assert "[[ \$(find \"$VAULT_DIR/01-CAPTURES/observations\" -maxdepth 1 -type f -name '*.md' | wc -l) -eq 1 ]]" "Processed capture missing"
assert "[[ \$(find \"$VAULT_DIR/02-CONNECTIONS\" -maxdepth 1 -type f -name '*.md' | wc -l) -eq 1 ]]" "Connections file missing"
assert "[[ \$(find \"$VAULT_DIR/03-BRIEFS\" -maxdepth 1 -type f -name '*.md' | wc -l) -eq 1 ]]" "Brief file missing"

printf 'Mini suite passed in %s\n' "$VAULT_DIR"
printf 'If AGENTS.md changed, restart the session or reload the agent context.\n'
