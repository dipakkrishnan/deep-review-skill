#!/usr/bin/env python3
"""Download an arXiv PDF from an abs or pdf URL."""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


ARXIV_PDF_PREFIX = "https://arxiv.org/pdf/"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download an arXiv PDF.")
    parser.add_argument("url", help="arXiv abs or pdf URL.")
    parser.add_argument(
        "--out",
        default=None,
        help="Output PDF path. Defaults to the arXiv id plus .pdf in the current directory.",
    )
    return parser.parse_args()


def arxiv_url_to_pdf_url(url: str) -> tuple[str, str]:
    cleaned = url.strip().rstrip("/")
    parsed = urlparse(cleaned)
    if parsed.netloc not in {"arxiv.org", "www.arxiv.org"}:
        raise ValueError(f"Not an arXiv URL: {url}")

    if parsed.path.startswith("/abs/"):
        paper_id = parsed.path.removeprefix("/abs/")
        return f"{ARXIV_PDF_PREFIX}{paper_id}", paper_id

    if parsed.path.startswith("/pdf/"):
        paper_id = parsed.path.removeprefix("/pdf/").removesuffix(".pdf")
        pdf_url = cleaned if cleaned.endswith(".pdf") else f"{cleaned}.pdf"
        return pdf_url, paper_id

    raise ValueError(f"Not a recognized arXiv abs/pdf URL: {url}")


def main() -> int:
    args = parse_args()

    try:
        pdf_url, paper_id = arxiv_url_to_pdf_url(args.url)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    out_path = Path(args.out or f"{paper_id.replace('/', '_')}.pdf").expanduser()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    request = urllib.request.Request(
        pdf_url,
        headers={"User-Agent": "deep-review-skill/0.1"},
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            content_type = response.headers.get("content-type", "")
            data = response.read()
    except urllib.error.URLError as exc:
        print(f"Failed to download {pdf_url}: {exc}", file=sys.stderr)
        return 1

    if not data.startswith(b"%PDF"):
        print(
            f"Downloaded content does not look like a PDF: content-type={content_type!r}",
            file=sys.stderr,
        )
        return 1

    out_path.write_bytes(data)
    print(str(out_path.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
