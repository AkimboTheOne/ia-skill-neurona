#!/usr/bin/env python3
"""CLI para la bóveda local de memoria Markdown $mem."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

VERSION = "0.2.0"

CAPTURE_TYPES = ("observations", "reactions", "patterns", "questions", "numbers")
SKILL_SPACE_DIRNAME = "ia-skill-neurona"
DEFAULT_VAULT_DIRNAME = "vault"
REQUIRED_DIRS = (
    "00-INBOX",
    "01-CAPTURES",
    "01-CAPTURES/observations",
    "01-CAPTURES/reactions",
    "01-CAPTURES/patterns",
    "01-CAPTURES/questions",
    "01-CAPTURES/numbers",
    "02-CONNECTIONS",
    "03-BRIEFS",
    "05-NEURONA",
)

DEFAULT_INSTANCE = {
    "mode": "project",
    "skill_root": "",
    "project_repo": "",
    "vault_repo": "",
    "skill_tmp": ".tmp",
    "contexts": {
        "user": [],
        "project": [],
        "skill": [],
        "external": [],
    },
    "vaults": {
        "active": "default",
        "named": {"default": ""},
    },
}


def emit(payload: dict[str, Any], code: int = 0) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    raise SystemExit(code)


def error(command: str, vault: str | None, message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    emit(
        {
            "ok": False,
            "command": command,
            "vault": str(Path(vault).expanduser()) if vault else "",
            "created_files": [],
            "updated_files": [],
            "warnings": [message],
            "summary": {},
        },
        code,
    )


def vault_path(raw: str) -> Path:
    return Path(raw).expanduser().resolve()


def repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists() or (candidate / "AGENTS.md").exists():
            return candidate
    return current


def skill_space_root(vault: Path) -> Path:
    return vault.parent


def workspace_root_from_vault(vault: Path) -> Path:
    return vault.parent.parent


def workspace_root_from_cwd() -> Path:
    return repo_root(Path.cwd())


def default_vault_dir(workspace_dir: Path) -> Path:
    return workspace_dir / SKILL_SPACE_DIRNAME / DEFAULT_VAULT_DIRNAME


def default_instance_path(workspace_dir: Path) -> Path:
    return workspace_dir / "instance.json"


def resolve_vault(args: argparse.Namespace, command: str) -> Path:
    raw = args.vault or os.environ.get("NEURONA_VAULT")
    if not raw:
        raw = str(default_vault_dir(workspace_root_from_cwd()))
    return vault_path(raw)


def require_initialized(command: str, vault: Path) -> None:
    missing = [name for name in REQUIRED_DIRS if not (vault / name).is_dir()]
    if missing:
        error(
            command,
            str(vault),
            "La bóveda no está inicializada. Ejecuta primero `scripts/neurona.sh init --vault <path>`. "
            f"Missing: {', '.join(missing[:5])}",
            1,
        )


def instance_path_for(vault: Path) -> Path:
    return default_instance_path(workspace_root_from_vault(vault))


def read_instance(vault: Path) -> dict[str, Any]:
    path = instance_path_for(vault)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def slugify(text: str, fallback: str = "note") -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    cleaned = re.sub(r"-{2,}", "-", cleaned)
    return (cleaned[:54].strip("-") or fallback)


def first_sentence(text: str) -> str:
    compact = " ".join(line.strip() for line in text.splitlines() if line.strip())
    if not compact:
        return "Empty capture."
    match = re.search(r"(.+?[.!?])(?:\s|$)", compact)
    sentence = match.group(1) if match else compact
    return sentence[:280].strip()


def unique_path(directory: Path, stem: str, suffix: str = ".md") -> Path:
    candidate = directory / f"{stem}{suffix}"
    counter = 2
    while candidate.exists():
        candidate = directory / f"{stem}-{counter}{suffix}"
        counter += 1
    return candidate


def markdown_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(path for path in directory.rglob("*.md") if path.is_file())


def strip_frontmatter(content: str) -> str:
    if content.startswith("---\n"):
        parts = content.split("---\n", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return content


def extract_raw(content: str) -> str:
    content = strip_frontmatter(content)
    marker = "## Raw"
    if marker in content:
        return content.split(marker, 1)[1].strip()
    marker = "## Raw Capture"
    if marker in content:
        return content.split(marker, 1)[1].strip()
    return content.strip()


def classify(text: str) -> tuple[str, list[str]]:
    lowered = text.lower()
    has_number = bool(re.search(r"\b\d+(?:[.,]\d+)?%?\b", text))
    has_question = "?" in text or lowered.startswith(("why ", "how ", "what ", "when ", "where "))
    reaction_words = ("i think", "i feel", "surprised", "hate", "love", "disagree", "agree", "prefiero", "siento", "creo")
    pattern_words = ("pattern", "always", "repeats", "same", "principle", "framework", "patron", "siempre", "repite")

    if has_question:
        note_type = "questions"
    elif has_number:
        note_type = "numbers"
    elif any(word in lowered for word in pattern_words):
        note_type = "patterns"
    elif any(word in lowered for word in reaction_words):
        note_type = "reactions"
    else:
        note_type = "observations"

    tags = [note_type.rstrip("s") or note_type, "capture", "mem"]
    return note_type, tags[:3]


def title_from_text(prefix: str, text: str) -> str:
    title = first_sentence(text).rstrip(".!?")
    title = title[:72].strip() or "Untitled"
    return f"{prefix}: {title}"


def yaml_scalar(value: str | int | float | bool) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if not text:
        return '""'
    if re.fullmatch(r"[A-Za-z0-9_./:@+-]+", text):
        return text
    return json.dumps(text, ensure_ascii=False)


def frontmatter(properties: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in properties.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {yaml_scalar(item)}")
        else:
            lines.append(f"{key}: {yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def command_init(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "init")
    created: list[str] = []
    updated: list[str] = []
    warnings: list[str] = []
    repo_dir = workspace_root_from_vault(vault)
    instance_path = instance_path_for(vault)

    for name in REQUIRED_DIRS:
        path = vault / name
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(str(path))

    manifest = {
        "name": "mem",
        "reference_name": "ia-skill-neurona",
        "version": VERSION,
        "description": "Memoria operativa del proyecto en Markdown para captura, síntesis y gobierno de la red. Activación: $mem. La bóveda contextual vive en `$BASE_DEL_REPO/ia-skill-neurona/vault/` y la instancia activa en `$BASE_DEL_REPO/ia-skill-neurona/instance.json`.",
        "auth": {"type": "none"},
        "commands": [
            {"name": "init", "description": "Create or validate the vault structure."},
            {"name": "init-repo-vault", "description": "Initialize the current repo as the vault and emit NEURONA_VAULT exports."},
            {"name": "config", "description": "Declare the active instance, contexts, and temporary skill memory."},
            {"name": "capture", "description": "Write a raw capture into 00-INBOX."},
            {"name": "process-inbox", "description": "Classify inbox notes into 01-CAPTURES."},
            {"name": "connect", "description": "Generate a heuristic connection report."},
            {"name": "brief", "description": "Generate a five-field brief for a topic."},
            {"name": "ask", "description": "Query the vault across stages with heuristic matching."},
            {"name": "status", "description": "Report vault health and counts."},
        ],
        "vault_structure": list(REQUIRED_DIRS),
        "property_contract": {
            "required": ["created", "type", "status", "source", "tags"],
            "optional": ["aliases", "source_file", "reviewed", "confidence"],
            "format": "YAML frontmatter at the top of Markdown notes.",
        },
        "instance_contract": {
            "vocabulary": [
                "skill_root",
                "project_repo",
                "vault_repo",
                "skill_tmp",
                "context",
            ],
            "modes": ["project", "cli-cross", "plugin", "server"],
            "project_vault": "vault/ under the repo-local skill space by default",
            "skill_tmp": ".tmp/ for temporary planning and maps",
            "contexts": ["user", "skill", "project", "external"],
            "reference_template": "instance-adjusted references derived from the agnostic base",
            "vaults": "named vaults with one active default vault per repo",
        },
        "reference_model": {
            "default": "agnostic",
            "templates": [
                "memory-temporal-work",
                "documentary-memory",
                "cognitive-memory",
            ],
        },
        "output_contract": {
            "ok": "boolean",
            "command": "string",
            "vault": "string",
            "created_files": "string[]",
            "updated_files": "string[]",
            "warnings": "string[]",
            "summary": "object",
        },
    }
    manifest_path = vault / "05-NEURONA" / "agent.json"
    llms_path = vault / "05-NEURONA" / "llms.txt"
    instance_exists = instance_path.exists()

    for path, content in (
        (manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"),
        (
            llms_path,
            "# Memoria\n\n"
            "Memoria operativa del proyecto en Markdown para agentes.\n\n"
            "Identificador de activación: `$mem`.\n"
            "Referencia histórica: `ia-skill-neurona`.\n"
            "La neurona define la unidad viva del proyecto: no almacena todo el conocimiento, sino el modelo operativo que mantiene coherente la red.\n\n"
            "## Capacidades\n"
            "- Capturar texto crudo en `00-INBOX` con propiedades canónicas.\n"
            "- Procesar capturas en notas Markdown tipadas y curadas en español.\n"
            "- Generar reportes de conexiones y briefs del proyecto.\n\n"
            "## Instancias\n"
            f"- `{vault}` es la bóveda contextual activa por defecto para este repo.\n"
            f"- `{instance_path}` declara la instancia activa y sus bóvedas nombradas.\n"
            "- `.tmp/` es memoria de trabajo temporal del skill.\n"
            "- El skill puede instanciarse como CLI cross, plugin o servidor futuro.\n\n"
            "## Referencias\n"
            "- `references/` es agnóstico por defecto.\n"
            "- Las instancias pueden ajustar plantillas de referencias según caso de uso.\n"
            "- El agente/LLM debe proponer esos ajustes cuando el propósito lo requiera.\n\n"
            "## Interfaz\n"
            "Usa `scripts/neurona.sh <comando> --vault <ruta>` o exporta `NEURONA_VAULT`.\n"
            "Los comandos devuelven JSON.\n\n"
            "## Properties\n"
            "New notes use YAML frontmatter with `created`, `type`, `status`, `source`, `tags`, `aliases`, `source_file`, `reviewed`, and `confidence` as needed.\n",
        ),
        (
            instance_path,
            json.dumps(
                {
                    **DEFAULT_INSTANCE,
                    "project_vault": str(vault),
                    "skill_tmp": str((vault / ".tmp").resolve()) if (vault / ".tmp").exists() else ".tmp",
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
        ),
    ):
        if path.exists():
            updated.append(str(path))
        else:
            created.append(str(path))
        path.write_text(content, encoding="utf-8")

    instance_payload = {
        **DEFAULT_INSTANCE,
        "skill_root": str(repo_dir),
        "project_repo": str(repo_dir),
        "vault_repo": str(vault),
        "skill_tmp": str(repo_dir / ".tmp"),
        "vaults": {
            "active": "default",
            "named": {"default": str(vault)},
        },
    }
    instance_path.parent.mkdir(parents=True, exist_ok=True)
    instance_path.write_text(json.dumps(instance_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    created.append(str(instance_path)) if not instance_exists else updated.append(str(instance_path))

    emit(
        {
            "ok": True,
            "command": "init",
            "vault": str(vault),
            "created_files": created,
            "updated_files": updated,
            "warnings": warnings,
            "summary": {"version": VERSION, "directories": len(REQUIRED_DIRS), "instance": str(instance_path)},
        }
    )


def command_config(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "config")
    require_initialized("config", vault)
    instance_path = instance_path_for(vault)
    instance_exists = instance_path.exists()
    current = read_instance(vault)

    current_contexts = current.get("contexts", {})
    current_mode = current.get("mode", "project")
    current_skill_tmp = current.get("skill_tmp", ".tmp")
    current_vaults = current.get("vaults", {"active": "default", "named": {}})
    contexts = {
        "user": [item for item in (args.user_context if args.user_context else current_contexts.get("user", [])) if item],
        "project": [item for item in (args.project_context if args.project_context else current_contexts.get("project", [])) if item],
        "skill": [item for item in (args.skill_context if args.skill_context else current_contexts.get("skill", [])) if item],
        "external": [item for item in (args.external_context if args.external_context else current_contexts.get("external", [])) if item],
    }
    named_vaults = dict(current_vaults.get("named", {})) or {"default": str(vault)}
    named_vaults.update({item.split("=", 1)[0]: item.split("=", 1)[1] for item in (args.vault_map or []) if "=" in item})
    payload = {
        "mode": args.mode or current_mode,
        "skill_root": str(workspace_root_from_vault(vault)),
        "project_repo": str(workspace_root_from_vault(vault)),
        "vault_repo": str(vault),
        "skill_tmp": args.skill_tmp or current_skill_tmp,
        "contexts": contexts,
        "vaults": {
            "active": args.active_vault or current_vaults.get("active", "default"),
            "named": named_vaults,
        },
    }
    current.update(payload)
    instance_path.parent.mkdir(parents=True, exist_ok=True)
    instance_path.write_text(json.dumps(current, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    emit(
        {
            "ok": True,
            "command": "config",
            "vault": str(vault),
            "created_files": [] if instance_exists else [str(instance_path)],
            "updated_files": [str(instance_path)],
            "warnings": [],
            "summary": payload,
        }
    )


def command_capture(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "capture")
    require_initialized("capture", vault)
    text = args.text.strip()
    if not text:
        error("capture", str(vault), "Capture text cannot be empty.", 2)

    now = datetime.now().astimezone().replace(microsecond=0).isoformat()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    slug = slugify(first_sentence(text), "capture")
    path = unique_path(vault / "00-INBOX", f"{stamp}-{slug}")
    title = title_from_text("Capture", text)
    content = frontmatter(
        {
            "created": now,
            "type": "inbox",
            "status": "raw",
            "source": args.source,
            "tags": ["capture", "inbox", "mem"],
            "aliases": [title],
        }
    ) + (
        f"# {title}\n\n"
        "## Raw\n\n"
        f"{text}\n"
    )
    path.write_text(content, encoding="utf-8")
    emit(
        {
            "ok": True,
            "command": "capture",
            "vault": str(vault),
            "created_files": [str(path)],
            "updated_files": [],
            "warnings": [],
            "summary": {"chars": len(text), "source": args.source},
        }
    )


def command_process_inbox(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "process-inbox")
    require_initialized("process-inbox", vault)
    inbox_files = markdown_files(vault / "00-INBOX")
    created: list[str] = []
    updated: list[str] = []
    warnings: list[str] = []
    counts = {name: 0 for name in CAPTURE_TYPES}

    for source in inbox_files:
        content = source.read_text(encoding="utf-8")
        raw = extract_raw(content)
        note_type, tags = classify(raw)
        counts[note_type] += 1
        now = datetime.now().astimezone().replace(microsecond=0).isoformat()
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        slug = slugify(first_sentence(raw), note_type)
        destination = unique_path(vault / "01-CAPTURES" / note_type, f"{stamp}-{slug}")
        title = title_from_text("Capture", raw)
        processed = frontmatter(
            {
                "created": now,
                "type": note_type,
                "status": "processed",
                "source": "inbox",
                "source_file": str(source.relative_to(vault)),
                "tags": tags,
                "aliases": [title],
            }
        ) + (
            f"# {title}\n\n"
            "## Sharpened\n\n"
            f"{first_sentence(raw)}\n\n"
            "## Raw Capture\n\n"
            f"{raw}\n"
        )
        destination.write_text(processed, encoding="utf-8")
        source.unlink()
        created.append(str(destination))
        updated.append(str(source))

    emit(
        {
            "ok": True,
            "command": "process-inbox",
            "vault": str(vault),
            "created_files": created,
            "updated_files": updated,
            "warnings": warnings,
            "summary": {"processed": len(inbox_files), "by_type": counts},
        }
    )


def note_keywords(text: str) -> set[str]:
    stop = {
        "about",
        "after",
        "antes",
        "capture",
        "captured",
        "desde",
        "date",
        "file",
        "para",
        "porque",
        "raw",
        "sharpened",
        "source",
        "tags",
        "that",
        "this",
        "type",
        "with",
        "sobre",
        "their",
        "there",
        "tiene",
        "will",
    }
    content_lines = []
    for line in strip_frontmatter(text).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("- "):
            continue
        content_lines.append(stripped)
    words = re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]{4,}", " ".join(content_lines).lower())
    return {word for word in words if word not in stop and not any(char.isdigit() for char in word)}


def evidence_text(text: str) -> str:
    body = strip_frontmatter(text)
    lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("- Sources:"):
            continue
        lines.append(stripped)
    return "\n".join(lines)


def recent_capture_notes(vault: Path, days: int) -> list[Path]:
    cutoff = datetime.now().timestamp() - timedelta(days=days).total_seconds()
    files = markdown_files(vault / "01-CAPTURES")
    return [path for path in files if path.stat().st_mtime >= cutoff]


def command_connect(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "connect")
    require_initialized("connect", vault)
    notes = recent_capture_notes(vault, args.days)
    created: list[str] = []
    warnings: list[str] = []
    connections: list[dict[str, Any]] = []
    indexed = []

    for path in notes:
        text = path.read_text(encoding="utf-8")
        indexed.append((path, text, note_keywords(text)))

    for idx, (left_path, left_text, left_terms) in enumerate(indexed):
        for right_path, right_text, right_terms in indexed[idx + 1 :]:
            overlap = sorted(left_terms & right_terms)
            if len(overlap) >= 2:
                connections.append(
                    {
                        "type": "same-principle",
                        "terms": overlap[:5],
                        "sources": [str(left_path.relative_to(vault)), str(right_path.relative_to(vault))],
                        "summary": f"Both notes share terms: {', '.join(overlap[:5])}.",
                    }
                )
            if "?" in left_text and len(right_terms & left_terms) >= 1:
                connections.append(
                    {
                        "type": "question-answer",
                        "terms": sorted(right_terms & left_terms)[:5],
                        "sources": [str(left_path.relative_to(vault)), str(right_path.relative_to(vault))],
                        "summary": "The second note may help answer a question raised by the first.",
                    }
                )
            if len(connections) >= args.limit:
                break
        if len(connections) >= args.limit:
            break

    if not connections:
        warnings.append("No strong heuristic connections found. Ask Codex to inspect notes manually for deeper synthesis.")

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    destination = unique_path(vault / "02-CONNECTIONS", f"{stamp}-connections")
    lines = [
        frontmatter(
            {
                "created": datetime.now().astimezone().replace(microsecond=0).isoformat(),
                "type": "connection",
                "status": "draft",
                "source": "generated",
                "tags": ["connection", "synthesis", "mem"],
            }
        ).rstrip(),
        f"# Connections: last {args.days} days",
        "",
        f"- Notes scanned: {len(notes)}",
        "",
    ]
    if connections:
        for number, item in enumerate(connections, 1):
            lines.extend(
                [
                    f"## {number}. {item['type']}",
                    "",
                    item["summary"],
                    "",
                    f"- Terms: {', '.join(item['terms'])}",
                    f"- Sources: {', '.join(item['sources'])}",
                    "",
                ]
            )
    else:
        lines.extend(["## No heuristic connection found", "", "Use Codex reasoning over the capture notes for a deeper pass.", ""])
    destination.write_text("\n".join(lines), encoding="utf-8")
    created.append(str(destination))

    emit(
        {
            "ok": True,
            "command": "connect",
            "vault": str(vault),
            "created_files": created,
            "updated_files": [],
            "warnings": warnings,
            "summary": {"notes_scanned": len(notes), "connections": connections},
        }
    )


def command_brief(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "brief")
    require_initialized("brief", vault)
    topic = args.topic.strip()
    if not topic:
        error("brief", str(vault), "Topic cannot be empty.", 2)

    topic_terms = note_keywords(topic)
    all_notes = markdown_files(vault / "01-CAPTURES") + markdown_files(vault / "02-CONNECTIONS")
    matches = []
    for path in all_notes:
        text = path.read_text(encoding="utf-8")
        score = len(topic_terms & note_keywords(text))
        if topic.lower() in text.lower():
            score += 2
        if score > 0:
            matches.append((score, path, text))
    matches.sort(key=lambda item: item[0], reverse=True)
    selected = matches[:5]
    proof = "Evidence is weak; add a concrete number, example, or source note."
    for _, _, text in selected:
        number = re.search(r"\b(?!20\d{2}\b)\d+(?:[.,]\d+)?%?\b", evidence_text(text))
        if number:
            proof = f"Available numeric proof: {number.group(0)}."
            break

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    destination = unique_path(vault / "03-BRIEFS", f"{stamp}-{slugify(topic, 'brief')}")
    sources = [str(path.relative_to(vault)) for _, path, _ in selected]
    content = frontmatter(
        {
            "created": datetime.now().astimezone().replace(microsecond=0).isoformat(),
            "type": "brief",
            "status": "draft",
            "source": "generated",
            "source_file": sources,
            "tags": ["brief", "content", "mem"],
            "aliases": [f"Brief: {topic}"],
        }
    ) + (
        f"# Brief: {topic}\n\n"
        f"- Sources: {', '.join(sources) if sources else 'none'}\n\n"
        "## ONE THING\n\n"
        f"{topic} needs one clear claim supported by the vault.\n\n"
        "## PROOF\n\n"
        f"{proof}\n\n"
        "## READER TRANSFORMATION\n\n"
        f"The reader understands what matters about {topic} and what to inspect next.\n\n"
        "## THREE HOOKS\n\n"
        f"1. The hidden problem with {topic} is not what most people think.\n"
        f"2. What changes when {topic} is treated as a system?\n"
        f"3. I keep returning to {topic} because the notes point to unfinished work.\n\n"
        "## THREE CLOSERS\n\n"
        "1. If the proof stays vague, the idea is not ready.\n"
        "2. The next useful step is to turn the strongest source note into a testable claim.\n"
        "3. A memory system compounds only when it produces decisions.\n"
    )
    destination.write_text(content, encoding="utf-8")
    emit(
        {
            "ok": True,
            "command": "brief",
            "vault": str(vault),
            "created_files": [str(destination)],
            "updated_files": [],
            "warnings": [] if selected else ["No matching source notes found for topic."],
            "summary": {"topic": topic, "sources": sources},
        }
    )


def command_ask(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "ask")
    require_initialized("ask", vault)
    query = args.query.strip()
    if not query:
        error("ask", str(vault), "Query cannot be empty.", 2)

    stage_map = {
        "inbox": vault / "00-INBOX",
        "captures": vault / "01-CAPTURES",
        "connections": vault / "02-CONNECTIONS",
        "briefs": vault / "03-BRIEFS",
        "neurona": vault / "05-NEURONA",
    }
    stages = [stage for stage in (args.stage or stage_map.keys()) if stage in stage_map]
    query_terms = note_keywords(query)
    if not query_terms:
        query_terms = {slugify(query)}

    matches: list[dict[str, Any]] = []
    scanned = 0
    for stage in stages:
        for path in markdown_files(stage_map[stage]):
            scanned += 1
            text = path.read_text(encoding="utf-8")
            score = len(query_terms & note_keywords(text))
            if query.lower() in text.lower():
                score += 2
            if score > 0:
                matches.append(
                    {
                        "stage": stage,
                        "path": str(path.relative_to(vault)),
                        "score": score,
                        "preview": first_sentence(evidence_text(text)),
                    }
                )

    matches.sort(key=lambda item: item["score"], reverse=True)
    limit = max(args.limit, 1)
    selected = matches[:limit]
    emit(
        {
            "ok": True,
            "command": "ask",
            "vault": str(vault),
            "created_files": [],
            "updated_files": [],
            "warnings": [] if selected else ["No matching notes found for the query."],
            "summary": {
                "query": query,
                "stages": stages,
                "scanned": scanned,
                "matches": selected,
            },
        }
    )


def command_status(args: argparse.Namespace) -> None:
    vault = resolve_vault(args, "status")
    missing = [name for name in REQUIRED_DIRS if not (vault / name).is_dir()]
    counts = {
        "inbox": len(markdown_files(vault / "00-INBOX")),
        "captures": len(markdown_files(vault / "01-CAPTURES")),
        "connections": len(markdown_files(vault / "02-CONNECTIONS")),
        "briefs": len(markdown_files(vault / "03-BRIEFS")),
    }
    emit(
        {
            "ok": not missing,
            "command": "status",
            "vault": str(vault),
            "created_files": [],
            "updated_files": [],
            "warnings": [f"Missing: {', '.join(missing)}"] if missing else [],
            "summary": {"version": VERSION, "counts": counts, "initialized": not missing},
        },
        0 if not missing else 1,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Opera la bóveda de memoria Markdown $mem.")
    subcommands = parser.add_subparsers(dest="command", required=True)

    init_parser = subcommands.add_parser("init", help="Create or validate a vault structure.")
    init_parser.add_argument("--vault")
    init_parser.set_defaults(func=command_init)

    config_parser = subcommands.add_parser("config", help="Declare the active instance and contexts.")
    config_parser.add_argument("--vault")
    config_parser.add_argument(
        "--mode",
        choices=["project", "cli-cross", "plugin", "inception", "server"],
        default="project",
    )
    config_parser.add_argument("--skill-tmp", default=".tmp")
    config_parser.add_argument("--active-vault")
    config_parser.add_argument("--vault-map", action="append", default=[], help="Map a named vault as NAME=PATH.")
    config_parser.add_argument("--user-context", action="append", default=[])
    config_parser.add_argument("--project-context", action="append", default=[])
    config_parser.add_argument("--skill-context", action="append", default=[])
    config_parser.add_argument("--external-context", action="append", default=[])
    config_parser.set_defaults(func=command_config)

    capture_parser = subcommands.add_parser("capture", help="Capture raw text into 00-INBOX.")
    capture_parser.add_argument("--vault")
    capture_parser.add_argument("--text", required=True)
    capture_parser.add_argument("--source", default="manual")
    capture_parser.set_defaults(func=command_capture)

    process_parser = subcommands.add_parser("process-inbox", help="Classify inbox notes into captures.")
    process_parser.add_argument("--vault")
    process_parser.set_defaults(func=command_process_inbox)

    connect_parser = subcommands.add_parser("connect", help="Generate a connection report.")
    connect_parser.add_argument("--vault")
    connect_parser.add_argument("--days", type=int, default=7)
    connect_parser.add_argument("--limit", type=int, default=5)
    connect_parser.set_defaults(func=command_connect)

    brief_parser = subcommands.add_parser("brief", help="Generate a five-field brief.")
    brief_parser.add_argument("--vault")
    brief_parser.add_argument("--topic", required=True)
    brief_parser.set_defaults(func=command_brief)

    ask_parser = subcommands.add_parser("ask", help="Query the vault across stages.")
    ask_parser.add_argument("--vault")
    ask_parser.add_argument("--query", required=True)
    ask_parser.add_argument(
        "--stage",
        action="append",
        choices=["inbox", "captures", "connections", "briefs", "neurona"],
        help="Limit the query to specific stages.",
    )
    ask_parser.add_argument("--limit", type=int, default=5)
    ask_parser.set_defaults(func=command_ask)

    status_parser = subcommands.add_parser("status", help="Report vault health and counts.")
    status_parser.add_argument("--vault")
    status_parser.set_defaults(func=command_status)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
