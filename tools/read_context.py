"""
read_context.py
---------------
Loads all files from the context/ directory in priority order and concatenates
them into a single structured text block.

Usage:
    python tools/read_context.py
    python tools/read_context.py --summary   # Print only section summaries
    python tools/read_context.py --output .tmp/context_snapshot.txt

Output:
    A labeled, concatenated text block ready for Claude to ingest as session context.
"""

import argparse
import os
import sys
from pathlib import Path

# Priority order for context files
CONTEXT_FILES = [
    "club.md",
    "brand.md",
    "audience.md",
    "channels.md",
    "assets.md",
]

# Section header template
SECTION_HEADER = "=" * 60


def find_context_dir() -> Path:
    """Locate the context/ directory relative to project root."""
    # Walk up from the script's location to find the project root
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    context_dir = project_root / "context"

    if not context_dir.exists():
        print(f"ERROR: context/ directory not found at {context_dir}", file=sys.stderr)
        sys.exit(1)

    return context_dir


def is_placeholder(content: str) -> bool:
    """Check if a file is still mostly placeholder text."""
    placeholder_markers = ["_[יש להשלים]_", "placeholder", "_[יש להשלים]_"]
    filled_lines = sum(
        1 for line in content.splitlines()
        if line.strip() and not any(m in line for m in placeholder_markers)
        and not line.startswith("#") and not line.startswith("_") and line.strip() != "---"
    )
    return filled_lines < 3


def load_context(summary_only: bool = False) -> str:
    """Load all context files and return a concatenated string."""
    context_dir = find_context_dir()
    sections = []
    warnings = []

    for filename in CONTEXT_FILES:
        filepath = context_dir / filename

        if not filepath.exists():
            warnings.append(f"  MISSING: context/{filename}")
            continue

        content = filepath.read_text(encoding="utf-8").strip()

        if not content:
            warnings.append(f"  EMPTY: context/{filename}")
            continue

        if is_placeholder(content):
            warnings.append(f"  PLACEHOLDER: context/{filename} — not yet filled in")

        if summary_only:
            # Extract only the first non-empty paragraph (summary block)
            lines = content.splitlines()
            summary_lines = []
            in_summary = False
            for line in lines:
                if line.startswith("> ") or line.startswith("**סיכום"):
                    in_summary = True
                if in_summary:
                    summary_lines.append(line)
                    if line.strip() == "" and summary_lines:
                        break
            content = "\n".join(summary_lines) if summary_lines else lines[0] if lines else ""

        section = f"{SECTION_HEADER}\n## {filename.replace('.md', '').upper()}\n{SECTION_HEADER}\n\n{content}"
        sections.append(section)

    output_parts = []

    if warnings:
        output_parts.append("⚠️  CONTEXT WARNINGS:\n" + "\n".join(warnings) + "\n")

    output_parts.append(
        f"CLUB CONTEXT SNAPSHOT — {len(sections)}/{len(CONTEXT_FILES)} files loaded\n"
        + ("(summary mode)\n" if summary_only else "")
    )
    output_parts.extend(sections)

    return "\n\n".join(output_parts)


def main():
    parser = argparse.ArgumentParser(description="Load club context for Claude sessions")
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Load only summary sections from each file (faster, smaller output)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Save output to a file (e.g. .tmp/context_snapshot.txt)",
    )
    args = parser.parse_args()

    context_text = load_context(summary_only=args.summary)

    if args.output:
        output_path = Path(__file__).resolve().parent.parent / args.output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(context_text, encoding="utf-8")
        print(f"Context snapshot saved to: {output_path}")
    else:
        print(context_text)


if __name__ == "__main__":
    main()
