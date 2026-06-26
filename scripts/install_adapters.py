#!/usr/bin/env python3
"""Install portable agent instruction files for Interview Answer Pack Builder."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTERS = ROOT / "assets" / "adapters"

FILES = {
    "agents": ("AGENTS.md", "AGENTS.md"),
    "claude": ("CLAUDE.md", "CLAUDE.md"),
    "gemini": ("GEMINI.md", "GEMINI.md"),
    "cursor": (
        ".cursor/rules/interview-answer-pack-builder.mdc",
        ".cursor/rules/interview-answer-pack-builder.mdc",
    ),
}


def copy_file(source: Path, destination: Path, force: bool, dry_run: bool) -> str:
    if destination.exists() and not force:
        return f"SKIP exists: {destination}"
    if dry_run:
        action = "OVERWRITE" if destination.exists() else "CREATE"
        return f"{action}: {destination}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    return f"WROTE: {destination}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default=".", help="Target project directory")
    parser.add_argument(
        "--tools",
        default="all",
        help="Comma-separated tools: all,agents,claude,cursor,gemini",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Show planned writes")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    requested = [tool.strip() for tool in args.tools.split(",") if tool.strip()]
    tools = list(FILES) if "all" in requested else requested

    unknown = [tool for tool in tools if tool not in FILES]
    if unknown:
        raise SystemExit(f"Unknown tools: {', '.join(unknown)}")

    for tool in tools:
        source_rel, dest_rel = FILES[tool]
        source = ADAPTERS / source_rel
        destination = target / dest_rel
        print(copy_file(source, destination, args.force, args.dry_run))


if __name__ == "__main__":
    main()
