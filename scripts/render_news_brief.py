#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path


def load_payload(path: str) -> dict:
    if path == "-":
        return json.load(sys.stdin)
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_item(item: dict, index: int) -> None:
    required = ["headline", "why_it_matters", "publication_date", "sources"]
    missing = [key for key in required if key not in item or not item[key]]
    if missing:
        raise ValueError(f"item {index} missing required fields: {', '.join(missing)}")
    if not isinstance(item["sources"], list) or not item["sources"]:
        raise ValueError(f"item {index} sources must be a non-empty list")


def render_item(item: dict) -> list[str]:
    source_text = ", ".join(item["sources"])
    return [
        f"- {item['headline']}",
        f"Why it matters: {item['why_it_matters']}",
        f"Publication date: {item['publication_date']}.",
        f"Sources: {source_text}",
        "",
    ]


def render(payload: dict) -> str:
    title = payload.get("title", "AI news snapshot")
    items = payload.get("items", [])

    if not isinstance(items, list) or not items:
        raise ValueError("items must be a non-empty list")
    if len(items) > 8:
        raise ValueError("items must contain at most 8 entries")

    for index, item in enumerate(items, start=1):
        validate_item(item, index)

    lines = [title, ""]
    for item in items:
        lines.extend(render_item(item))

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a structured AI news brief JSON payload into markdown."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Path to a JSON file, or '-' to read from stdin.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Optional output file path. Defaults to stdout.",
    )
    args = parser.parse_args()

    payload = load_payload(args.input)
    markdown = render(payload)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
