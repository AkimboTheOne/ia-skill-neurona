from __future__ import annotations

import json
import os
import tempfile
import importlib.util
from pathlib import Path
from unittest.mock import patch

from fastapi.testclient import TestClient


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"
SPEC = importlib.util.spec_from_file_location("mem_api_app", APP_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
app = MODULE.app


def test_health_uses_instance_binding() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        vault = root / "vault"
        vault.mkdir()
        instance_file = root / "instance.json"
        instance_file.write_text(
            json.dumps(
                {
                    "project_vault": str(vault),
                    "mode": "server",
                    "skill_tmp": ".tmp/vault",
                    "contexts": {"user": [], "project": [], "skill": [], "external": []},
                }
            ),
            encoding="utf-8",
        )

        with patch.dict(os.environ, {"NEURONA_INSTANCE_FILE": str(instance_file), "NEURONA_VAULT": ""}, clear=False):
            client = TestClient(app)
            response = client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["vault"] == str(vault.resolve())
    assert data["instance_file"] == str(instance_file.resolve())


def test_capture_delegates_to_cli_contract() -> None:
    with TestClient(app) as client:
        with patch.object(MODULE, "cli", return_value={"ok": True, "command": "capture"}) as mocked:
            response = client.post("/capture", json={"text": "hello world", "source": "manual"})

    assert response.status_code == 200
    assert response.json()["ok"] is True
    mocked.assert_called_once_with("capture", "--text", "hello world", "--source", "manual")
