#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_FILE="$REPO_DIR/.tmp/agents-setup-state.json"
PLUGIN_ROOT="${PLUGIN_ROOT:-$REPO_DIR/.codex/skills}"
PLUGIN_NAME="${PLUGIN_NAME:-mem}"

declare -a SURFACES=(
  "AGENT.md=AGENTS.md"
  ".github/copilot-instructions.md=AGENTS.md"
)
declare -a COPIES=()

usage() {
  cat <<'EOF'
Usage: setup-repo-for-agents.sh [--surface DEST=SOURCE]... [--copy DEST=SOURCE]... [--plugin-root PATH] [--state-file PATH]

Defaults:
  AGENT.md=AGENTS.md
  .github/copilot-instructions.md=AGENTS.md
  plugin root: .codex/skills
  state file: .tmp/agents-setup-state.json

Examples:
  bash scripts/setup-repo-for-agents.sh
  bash scripts/setup-repo-for-agents.sh --surface CLAUDE.md=AGENTS.md
  bash scripts/setup-repo-for-agents.sh --surface .claude/CLAUDE.md=AGENTS.md
  bash scripts/setup-repo-for-agents.sh --copy CLAUDE.md=AGENTS.md
  bash scripts/setup-repo-for-agents.sh --plugin-root /tmp/skills --state-file .tmp/agents.json
EOF
}

add_surface() {
  local spec="$1"
  if [[ "$spec" != *"="* ]]; then
    printf 'Invalid --surface spec: %s\n' "$spec" >&2
    exit 2
  fi
  SURFACES+=("$spec")
}

add_copy() {
  local spec="$1"
  if [[ "$spec" != *"="* ]]; then
    printf 'Invalid --copy spec: %s\n' "$spec" >&2
    exit 2
  fi
  COPIES+=("$spec")
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --plugin-root)
      shift
      [ $# -gt 0 ] || { usage >&2; exit 2; }
      PLUGIN_ROOT="$1"
      ;;
    --state-file)
      shift
      [ $# -gt 0 ] || { usage >&2; exit 2; }
      STATE_FILE="$1"
      ;;
    --surface)
      shift
      [ $# -gt 0 ] || { usage >&2; exit 2; }
      add_surface "$1"
      ;;
    --copy)
      shift
      [ $# -gt 0 ] || { usage >&2; exit 2; }
      add_copy "$1"
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

if [ ! -e "$REPO_DIR/AGENTS.md" ]; then
  printf 'Missing canonical AGENTS.md at %s\n' "$REPO_DIR/AGENTS.md" >&2
  exit 1
fi

mkdir -p "$PLUGIN_ROOT"

ensure_link() {
  local dest="$1"
  local source="$2"
  local dest_path="$REPO_DIR/$dest"
  local source_path="$REPO_DIR/$source"
  local dest_dir

  if [ ! -e "$source_path" ]; then
    printf 'Missing source for surface %s: %s\n' "$dest" "$source" >&2
    return 1
  fi

  dest_dir="$(dirname "$dest_path")"
  mkdir -p "$dest_dir"

  if [ -L "$dest_path" ]; then
    local current_target
    current_target="$(readlink "$dest_path")"
    if [ "$current_target" = "$source" ]; then
      printf '%s: already linked\n' "$dest"
      return 0
    fi
    rm -f "$dest_path"
    ln -s "$source" "$dest_path"
    printf '%s: relinked\n' "$dest"
    return 0
  fi

  if [ -e "$dest_path" ]; then
    if cmp -s "$dest_path" "$source_path"; then
      printf '%s: already present\n' "$dest"
      return 0
    fi
    printf '%s: conflict, leaving existing file untouched\n' "$dest" >&2
    return 0
  fi

  ln -s "$source" "$dest_path"
  printf '%s: created\n' "$dest"
}

ensure_copy() {
  local dest="$1"
  local source="$2"
  local dest_path="$REPO_DIR/$dest"
  local source_path="$REPO_DIR/$source"
  local dest_dir

  if [ ! -e "$source_path" ]; then
    printf 'Missing source for copy %s: %s\n' "$dest" "$source" >&2
    return 1
  fi

  dest_dir="$(dirname "$dest_path")"
  mkdir -p "$dest_dir"

  if [ -e "$dest_path" ]; then
    if cmp -s "$dest_path" "$source_path"; then
      printf '%s: already present\n' "$dest"
      return 0
    fi
    printf '%s: conflict, leaving existing file untouched\n' "$dest" >&2
    return 0
  fi

  cp "$source_path" "$dest_path"
  printf '%s: copied\n' "$dest"
}

printf 'Agent setup complete.\n'
printf 'Canonical guide: %s\n' "$REPO_DIR/AGENTS.md"

PLUGIN_PATH="$PLUGIN_ROOT/$PLUGIN_NAME"
PLUGIN_STATUS="unknown"
if [ -L "$PLUGIN_PATH" ]; then
  CURRENT_TARGET="$(readlink "$PLUGIN_PATH")"
  if [ "$CURRENT_TARGET" = "$REPO_DIR" ]; then
    PLUGIN_STATUS="already linked"
  else
    rm -f "$PLUGIN_PATH"
    ln -s "$REPO_DIR" "$PLUGIN_PATH"
    PLUGIN_STATUS="relinked"
  fi
elif [ -e "$PLUGIN_PATH" ]; then
  if cmp -s "$PLUGIN_PATH/AGENTS.md" "$REPO_DIR/AGENTS.md" 2>/dev/null; then
    PLUGIN_STATUS="already present"
  else
    printf 'Existing plugin path is not the expected repo instantiation; leaving it untouched.\n' >&2
    PLUGIN_STATUS="conflict"
  fi
else
  if ln -s "$REPO_DIR" "$PLUGIN_PATH" 2>/dev/null; then
    PLUGIN_STATUS="created"
  else
    if mkdir -p "$PLUGIN_PATH" 2>/dev/null; then
      cp -R "$REPO_DIR/"* "$PLUGIN_PATH/" 2>/dev/null || true
      cp -R "$REPO_DIR/.[!.]*" "$PLUGIN_PATH/" 2>/dev/null || true
      PLUGIN_STATUS="copied"
    else
      PLUGIN_STATUS="unavailable"
    fi
  fi
fi

for surface in "${SURFACES[@]}"; do
  dest="${surface%%=*}"
  source="${surface#*=}"
  ensure_link "$dest" "$source"
done

if [ "${#COPIES[@]}" -gt 0 ]; then
  for copy in "${COPIES[@]}"; do
    dest="${copy%%=*}"
    source="${copy#*=}"
    ensure_copy "$dest" "$source"
  done
fi

mkdir -p "$(dirname "$STATE_FILE")"
surfaces_json="$(for surface in "${SURFACES[@]}"; do dest="${surface%%=*}"; source="${surface#*=}"; printf '    {"kind":"symlink","dest":"%s","source":"%s"}\n' "$dest" "$source"; done | sed '$!s/$/,/')"
copies_json=""
if [ "${#COPIES[@]}" -gt 0 ]; then
  copies_json="$(for copy in "${COPIES[@]}"; do dest="${copy%%=*}"; source="${copy#*=}"; printf '    {"kind":"copy","dest":"%s","source":"%s"}\n' "$dest" "$source"; done | sed '$!s/$/,/')"
fi
cat >"$STATE_FILE" <<EOF
{
  "repo_dir": "$REPO_DIR",
  "canonical_guide": "$REPO_DIR/AGENTS.md",
  "plugin_root": "$PLUGIN_ROOT",
  "plugin_name": "$PLUGIN_NAME",
  "plugin_path": "$PLUGIN_PATH",
  "plugin_status": "$PLUGIN_STATUS",
  "surfaces": [
${surfaces_json}
  ],
  "copies": [
${copies_json}
  ],
  "timestamp_utc": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

printf 'Plugin artifact: %s (%s)\n' "$PLUGIN_PATH" "$PLUGIN_STATUS"
printf 'State file: %s\n' "$STATE_FILE"
printf 'If this guide changed, restart the session to pick up the new context.\n'
