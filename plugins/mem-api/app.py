from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="mem-api", version="0.1.0")


class CaptureRequest(BaseModel):
    text: str = Field(min_length=1)
    source: str = Field(default="manual", min_length=1)


class ConnectRequest(BaseModel):
    days: int = Field(default=7, ge=1)
    limit: int = Field(default=5, ge=1)


class BriefRequest(BaseModel):
    topic: str = Field(min_length=1)

REPO_ROOT = Path(__file__).resolve().parents[2]
CLI = REPO_ROOT / "scripts" / "neurona.py"
DEFAULT_INSTANCE_FILE = REPO_ROOT / "docs" / "05-NEURONA" / "instance.json"


def resolve_instance_file() -> Path:
    raw = os.environ.get("NEURONA_INSTANCE_FILE")
    if raw:
        return Path(raw).expanduser().resolve()
    return DEFAULT_INSTANCE_FILE


def load_instance() -> dict[str, Any]:
    path = resolve_instance_file()
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_vault() -> str:
    env_vault = os.environ.get("NEURONA_VAULT")
    if env_vault:
        return str(Path(env_vault).expanduser().resolve())

    instance = load_instance()
    project_vault = instance.get("project_vault")
    if project_vault:
        return str(Path(project_vault).expanduser().resolve())

    return str((REPO_ROOT / "docs").resolve())


def cli(command: str, *extra: str) -> dict[str, Any]:
    vault = resolve_vault()
    if not CLI.exists():
        return {
            "ok": False,
            "command": command,
            "vault": vault,
            "warnings": ["CLI not found at scripts/neurona.py"],
        }

    cmd = [sys.executable, str(CLI), command, "--vault", vault, *extra]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    try:
        payload: dict[str, Any] = json.loads(proc.stdout) if proc.stdout.strip() else {}
    except json.JSONDecodeError:
        payload = {
            "ok": False,
            "command": command,
            "vault": vault,
            "warnings": ["CLI returned non-JSON output"],
            "raw_stdout": proc.stdout,
        }
    payload.setdefault("command", command)
    payload.setdefault("vault", vault)
    payload.setdefault("warnings", [])
    if proc.returncode != 0:
        payload["ok"] = False
        payload["warnings"] = [*payload["warnings"], proc.stderr.strip() or f"CLI exited with {proc.returncode}"]
    return payload


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "ok": "true",
        "service": "mem-api",
        "mode": os.environ.get("NEURONA_MODE", "service"),
        "vault": resolve_vault(),
        "instance_file": str(resolve_instance_file()),
        "cwd": str(Path.cwd()),
    }


@app.get("/config")
def config() -> dict[str, Any]:
    instance = load_instance()
    return {
        "service_kind": os.environ.get("NEURONA_SERVICE_KIND", "fastapi"),
        "service_name": os.environ.get("NEURONA_SERVICE_NAME", "mem-api"),
        "vault": resolve_vault(),
        "instance_file": str(resolve_instance_file()),
        "instance": instance,
    }


@app.get("/instance")
def instance() -> dict[str, Any]:
    return load_instance()


@app.get("/status")
def status() -> dict[str, Any]:
    return cli("status")


@app.post("/capture")
def capture(payload: CaptureRequest) -> dict[str, Any]:
    return cli("capture", "--text", payload.text, "--source", payload.source)


@app.post("/process-inbox")
def process_inbox() -> dict[str, Any]:
    return cli("process-inbox")


@app.post("/connect")
def connect(payload: ConnectRequest) -> dict[str, Any]:
    return cli("connect", "--days", str(payload.days), "--limit", str(payload.limit))


@app.post("/brief")
def brief(payload: BriefRequest) -> dict[str, Any]:
    return cli("brief", "--topic", payload.topic)
