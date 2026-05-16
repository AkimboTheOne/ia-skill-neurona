#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VAULT_DIR="${1:-$SKILL_DIR/.tmp/mini-suite-vault}"

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

status_out="$(run_json status)"
printf '%s\n' "$status_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["initialized"] is True'

templates_list_out="$(run_json templates list)"
printf '%s\n' "$templates_list_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and [item["phase"] for item in data["summary"]["phases"]] == ["prepare","capture","conversation","connect","brief","close"]'

templates_show_out="$(run_json templates show --phase conversation)"
printf '%s\n' "$templates_show_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["phase"] == "conversation" and "Contexto operativo" in data["summary"]["template"]'

capture_out="$(run_json capture --text "La documentación del proyecto debe ser consistente y legible para personas y agentes.")"
printf '%s\n' "$capture_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["source"] == "manual"'

process_out="$(run_json process-inbox)"
printf '%s\n' "$process_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["processed"] == 1'

connect_out="$(run_json connect --days 7 --limit 5)"
printf '%s\n' "$connect_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["notes_scanned"] == 1'

brief_out="$(run_json brief --topic "documentacion editorial")"
printf '%s\n' "$brief_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["summary"]["topic"] == "documentacion editorial"'

conversation_id="demo-session"
conversation_capture_out="$(run_json conversation capture --conversation-id "$conversation_id" --text $'## Contexto operativo\n- Mini suite over a temporary vault.\n## Resumen sustantivo\n- Initial scope defined.\n## Decisiones\n- Use a conversation_id.\n## Evidencia y enlaces\n- scripts/mini-suite.sh validates the command.\n## Relaciones sugeridas\n- Connect conversation capture with operational templates.\n## Pendientes\n- Should we store full transcript?\n## Próximos pasos\n- Update the same note.\n## Riesgos\n- Escueto summaries lose context.\n## Transcripción relevante\n- User asked to preserve dense context.')"
printf '%s\n' "$conversation_capture_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["warnings"] == [] and data["summary"]["conversation_id"] == "demo-session"'

conversation_update_out="$(run_json conversation update --conversation-id "$conversation_id" --text $'## Contexto operativo\n- Mini suite over a temporary vault.\n## Resumen sustantivo\n- Initial scope defined.\n- Updated scope includes sync semantics.\n## Decisiones\n- Use a conversation_id.\n## Evidencia y enlaces\n- scripts/mini-suite.sh validates the command.\n## Relaciones sugeridas\n- Connect conversation capture with operational templates.\n## Pendientes\n- Should we store full transcript?\n## Próximos pasos\n- Sync the same note.\n## Riesgos\n- Escueto summaries lose context.\n## Transcripción relevante\n- User asked to preserve dense context.')"
printf '%s\n' "$conversation_update_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["warnings"] == [] and data["summary"]["conversation_id"] == "demo-session"'

conversation_sync_out="$(run_json conversation sync --conversation-id "$conversation_id" --text $'## Contexto operativo\n- Mini suite over a temporary vault.\n## Resumen sustantivo\n- Initial scope defined.\n- Updated scope includes sync semantics.\n- Sync reuses the same note.\n## Decisiones\n- Use a conversation_id.\n## Evidencia y enlaces\n- scripts/mini-suite.sh validates the command.\n## Relaciones sugeridas\n- Connect conversation capture with operational templates.\n## Pendientes\n- Should we store full transcript?\n## Próximos pasos\n- Finish validation.\n## Riesgos\n- Escueto summaries lose context.\n## Transcripción relevante\n- User asked to preserve dense context.')"
printf '%s\n' "$conversation_sync_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["warnings"] == [] and data["summary"]["conversation_id"] == "demo-session"'

conversation_warning_out="$(run_json conversation sync --conversation-id "$conversation_id" --text $'## Resumen sustantivo\n- Warning path keeps operating.')"
printf '%s\n' "$conversation_warning_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and any("Contexto operativo" in item for item in data["warnings"])'

conversation_final_sync_out="$(run_json conversation sync --conversation-id "$conversation_id" --text $'## Contexto operativo\n- Mini suite over a temporary vault.\n## Resumen sustantivo\n- Initial scope defined.\n- Updated scope includes sync semantics.\n- Sync reuses the same note.\n## Decisiones\n- Use a conversation_id.\n## Evidencia y enlaces\n- scripts/mini-suite.sh validates the command.\n## Relaciones sugeridas\n- Connect conversation capture with operational templates.\n## Pendientes\n- Should we store full transcript?\n## Próximos pasos\n- Finish validation.\n## Riesgos\n- Escueto summaries lose context.\n## Transcripción relevante\n- User asked to preserve dense context.')"
printf '%s\n' "$conversation_final_sync_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and data["warnings"] == []'

health_out="$("$SCRIPT_DIR/agents-healthcheck.sh")"
printf '%s\n' "$health_out" | python3 -c 'import json,sys; data=json.load(sys.stdin); assert data["ok"] is True and "next_step" in data'

assert "[[ \$(find \"$VAULT_DIR/01-CAPTURES/observations\" -maxdepth 1 -type f -name '*.md' | wc -l) -eq 2 ]]" "Unexpected observation count"
assert "[[ \$(find \"$VAULT_DIR/02-CONNECTIONS\" -maxdepth 1 -type f -name '*.md' | wc -l) -eq 1 ]]" "Connections file missing"
assert "[[ \$(find \"$VAULT_DIR/03-BRIEFS\" -maxdepth 1 -type f -name '*.md' | wc -l) -eq 1 ]]" "Brief file missing"
assert "grep -q 'conversation_id: demo-session' \"$VAULT_DIR/01-CAPTURES/observations\"/*.md" "Conversation note missing conversation_id"
assert "grep -q 'Sync reuses the same note.' \"$VAULT_DIR/01-CAPTURES/observations\"/*.md" "Conversation sync did not update note"

printf 'Mini suite passed in %s\n' "$VAULT_DIR"
printf 'If AGENTS.md changed, restart the session or reload the agent context.\n'
