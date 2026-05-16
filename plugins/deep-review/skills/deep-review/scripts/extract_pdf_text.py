#!/usr/bin/env python3
"""Extract title and text from a local PDF."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract title and text from a local PDF.")
    parser.add_argument("pdf", help="Path to the PDF file.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit a JSON object with title, page_count, and text.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pdf_path = Path(args.pdf).expanduser()

    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 2
    if not pdf_path.is_file():
        print(f"Not a file: {pdf_path}", file=sys.stderr)
        return 2

    try:
        import fitz
    except ImportError:
        print("Missing dependency: install PyMuPDF with 'pip install pymupdf'.", file=sys.stderr)
        return 3

    try:
        doc = fitz.open(pdf_path)
        title = ""
        if doc.metadata:
            title = (doc.metadata.get("title") or "").strip()
        pages = [page.get_text() for page in doc]
        page_count = doc.page_count
        doc.close()
    except Exception as exc:  # pragma: no cover - depends on external PDF parser.
        print(f"Failed to read PDF: {exc}", file=sys.stderr)
        return 1

    text = "\n".join(pages)
    if args.json:
        print(
            json.dumps(
                {
                    "path": str(pdf_path.resolve()),
                    "title": title or pdf_path.stem,
                    "page_count": page_count,
                    "text": text,
                },
                ensure_ascii=False,
            )
        )
    else:
        print(f"# Title\n{title or pdf_path.stem}\n")
        print(f"# Pages\n{page_count}\n")
        print("# Text")
        print(text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
