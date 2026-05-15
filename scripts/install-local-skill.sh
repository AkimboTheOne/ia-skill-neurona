#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if git -C "$SKILL_DIR" rev-parse --show-toplevel >/dev/null 2>&1; then
  REPO_DIR="$(git -C "$SKILL_DIR" rev-parse --show-toplevel)"
else
  REPO_DIR="$SKILL_DIR"
fi

INSTALL_ROOT="${1:-$REPO_DIR/.codex/skills}"
INSTALL_ROOT="$(mkdir -p "$INSTALL_ROOT" && cd "$INSTALL_ROOT" && pwd)"
LINK_PATH="$INSTALL_ROOT/mem"
REFERENCE_NAME="ia-skill-neurona"

if [ -L "$LINK_PATH" ]; then
  CURRENT_TARGET="$(readlink "$LINK_PATH")"
  if [ "$CURRENT_TARGET" = "$REPO_DIR" ]; then
    printf 'Local skill symlink already installed: %s -> %s\n' "$LINK_PATH" "$REPO_DIR"
    printf 'Use this only for developing this skill or installing it as a command-line plugin-style local skill.\n'
    printf 'Normal vault usage does not require this symlink.\n'
    exit 0
  fi
  printf 'Refusing to replace existing symlink: %s -> %s\n' "$LINK_PATH" "$CURRENT_TARGET" >&2
  exit 1
fi

if [ -e "$LINK_PATH" ]; then
  printf 'Refusing to replace existing path: %s\n' "$LINK_PATH" >&2
  exit 1
fi

ln -s "$REPO_DIR" "$LINK_PATH"

printf 'Installed local skill symlink: %s -> %s\n' "$LINK_PATH" "$REPO_DIR"
printf 'Historical reference name remains: %s\n' "$REFERENCE_NAME"
printf 'Use this only for developing this skill or installing it as a command-line plugin-style local skill.\n'
printf 'Normal vault usage does not require this symlink. This is repo-local only and does not install into ~/.codex/skills.\n'
