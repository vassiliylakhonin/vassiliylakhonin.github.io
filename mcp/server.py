#!/usr/bin/env python3
"""Read-only MCP server for profile discovery resources.

Exposes machine-readable resources from the CV site:
- resume.json
- evidence.json
- availability.json
- capabilities.json
- engage.json
- agent-card.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HOST = "https://vassiliylakhonin.github.io"

RESOURCE_DEFS = [
    ("site://resume.json", "resume.json", "JSON Resume profile", "resume.json"),
    ("site://evidence.json", "evidence.json", "Claim-to-metric evidence map", "evidence.json"),
    ("site://availability.json", "availability.json", "Availability and role targets", "availability.json"),
    ("site://capabilities.json", "capabilities.json", "Capabilities and service metadata", "capabilities.json"),
    ("site://engage.json", "engage.json", "Structured outreach and intake schema", "engage.json"),
    ("site://agent-card.json", "agent-card.json", "Agent discovery capability card", "agent-card.json"),
]


def json_rpc_result(message_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def json_rpc_error(message_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "error": {"code": code, "message": message}}


def write_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
    sys.stdout.buffer.write(header)
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}

    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break

        text = line.decode("utf-8", errors="replace")
        key, separator, value = text.partition(":")
        if separator:
            headers[key.strip().lower()] = value.strip()

    content_length = int(headers.get("content-length", "0"))
    if content_length <= 0:
        return None

    content = sys.stdin.buffer.read(content_length)
    if not content:
        return None

    return json.loads(content.decode("utf-8"))


def list_resources() -> list[dict[str, Any]]:
    resources = []
    for uri, name, description, filename in RESOURCE_DEFS:
        resources.append(
            {
                "uri": uri,
                "name": name,
                "description": description,
                "mimeType": "application/json",
                "annotations": {
                    "readOnlyHint": True,
                    "audience": ["assistant", "user"],
                    "priority": 0.9,
                },
                "metadata": {
                    "sourceUrl": f"{HOST}/{filename}",
                },
            }
        )
    return resources


def read_resource(uri: str) -> dict[str, Any]:
    uri_to_file = {entry[0]: entry[3] for entry in RESOURCE_DEFS}
    if uri not in uri_to_file:
        raise KeyError(uri)

    path = ROOT / uri_to_file[uri]
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")
    return {
        "contents": [
            {
                "uri": uri,
                "mimeType": "application/json",
                "text": text,
            }
        ]
    }


def handle_request(message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    message_id = message.get("id")
    params = message.get("params", {})
    is_notification = message_id is None

    if method == "notifications/initialized":
        return None

    if method == "initialize":
        protocol_version = params.get("protocolVersion", "2024-11-05")
        result = {
            "protocolVersion": protocol_version,
            "capabilities": {
                "resources": {
                    "listChanged": False,
                    "subscribe": False,
                }
            },
            "serverInfo": {"name": "vassiliy-profile-mcp", "version": "1.0.0"},
            "instructions": (
                "Read-only profile server. Use resources/list then resources/read "
                "to access resume, evidence, availability, capability, and intake data."
            ),
        }
        return json_rpc_result(message_id, result) if not is_notification else None

    if method == "ping":
        return json_rpc_result(message_id, {}) if not is_notification else None

    if method == "resources/list":
        return json_rpc_result(message_id, {"resources": list_resources()}) if not is_notification else None

    if method == "resources/read":
        uri = params.get("uri")
        if not uri:
            return json_rpc_error(message_id, -32602, "Missing required parameter: uri")
        try:
            return json_rpc_result(message_id, read_resource(uri))
        except KeyError:
            return json_rpc_error(message_id, -32002, f"Unknown resource URI: {uri}")
        except FileNotFoundError:
            return json_rpc_error(message_id, -32003, f"Resource file missing for URI: {uri}")

    if method == "tools/list":
        return json_rpc_result(message_id, {"tools": []}) if not is_notification else None

    if method == "prompts/list":
        return json_rpc_result(message_id, {"prompts": []}) if not is_notification else None

    if is_notification:
        return None

    return json_rpc_error(message_id, -32601, f"Method not found: {method}")


def main() -> int:
    while True:
        message = read_message()
        if message is None:
            break
        try:
            response = handle_request(message)
        except Exception as exc:  # pragma: no cover
            message_id = message.get("id")
            response = json_rpc_error(message_id, -32603, f"Internal error: {exc}")

        if response is not None:
            write_message(response)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
