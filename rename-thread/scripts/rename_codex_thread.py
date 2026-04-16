#!/usr/bin/env python3
"""Rename a Codex thread by writing an overlay to session_index.jsonl."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def default_codex_home() -> Path:
    raw_home = os.environ.get("CODEX_HOME")
    if raw_home:
        return Path(raw_home).expanduser()
    return Path.home() / ".codex"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rename a Codex thread by writing an override entry into "
            "session_index.jsonl."
        )
    )
    parser.add_argument(
        "--thread-id",
        default=os.environ.get("CODEX_THREAD_ID", ""),
        help=(
            "Thread ID to rename. Defaults to $CODEX_THREAD_ID for the "
            "current Codex extension session."
        ),
    )
    parser.add_argument(
        "--name",
        required=True,
        help="New thread name to write into session_index.jsonl.",
    )
    parser.add_argument(
        "--codex-home",
        default=str(default_codex_home()),
        help="Codex home directory. Defaults to $CODEX_HOME or ~/.codex.",
    )
    return parser.parse_args()


def load_session_index(path: Path) -> list[dict]:
    rows = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def lookup_updated_at(state_db_path: Path, thread_id: str) -> str:
    if not state_db_path.exists():
        raise FileNotFoundError(f"Missing Codex state database: {state_db_path}")

    with sqlite3.connect(state_db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT updated_at FROM threads WHERE id = ?", (thread_id,))
        row = cur.fetchone()

    if row is None:
        raise ValueError(f"Thread ID not found in {state_db_path}: {thread_id}")

    updated_at_unix = int(row[0])
    return datetime.fromtimestamp(updated_at_unix, tz=timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def create_timestamped_backup(session_index_path: Path, backup_dir: Path) -> Path:
    backup_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S-%fZ")
    backup_path = backup_dir / f"backup_{timestamp}.jsonl"
    shutil.copy2(session_index_path, backup_path)
    return backup_path


def write_session_index(session_index_path: Path, rows: list[dict]) -> None:
    text = "".join(json.dumps(row, separators=(",", ":")) + "\n" for row in rows)
    session_index_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=session_index_path.parent,
        delete=False,
    ) as tmp:
        tmp.write(text)
        tmp_path = Path(tmp.name)
    tmp_path.replace(session_index_path)


def rename_thread(codex_home: Path, thread_id: str, new_name: str) -> tuple[str, Path]:
    session_index_path = codex_home / "session_index.jsonl"
    state_db_path = codex_home / "state_5.sqlite"
    backup_dir = codex_home / "session_index_manual_backup"

    if not session_index_path.exists():
        raise FileNotFoundError(f"Missing session index: {session_index_path}")

    rows = load_session_index(session_index_path)
    for row in rows:
        if row.get("id") == thread_id:
            row["thread_name"] = new_name
            backup_path = create_timestamped_backup(session_index_path, backup_dir)
            write_session_index(session_index_path, rows)
            return "updated", backup_path

    rows.append(
        {
            "id": thread_id,
            "thread_name": new_name,
            "updated_at": lookup_updated_at(state_db_path, thread_id),
        }
    )

    backup_path = create_timestamped_backup(session_index_path, backup_dir)
    write_session_index(session_index_path, rows)
    return "appended", backup_path


def main() -> int:
    args = parse_args()
    codex_home = Path(args.codex_home).expanduser()
    thread_id = args.thread_id.strip()
    new_name = args.name.strip()

    if not thread_id:
        raise ValueError(
            "--thread-id was not provided and CODEX_THREAD_ID is not set."
        )
    if not new_name:
        raise ValueError("--name must not be empty.")

    action, backup_path = rename_thread(codex_home, thread_id, new_name)
    print(
        f"{action} thread rename for {thread_id} -> {new_name}\n"
        f"backup: {backup_path}\n"
        "Reload the VS Code or code-server window to refresh the sidebar."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
