import csv
import os
import re
import urllib.request

import pymupdf

USER_AGENT = "research-paper-rag-assistant/1.0 (arxiv_downloader.py)"
REQUEST_TIMEOUT = 30


def load_download_targets(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {
                "paper_id": row["paper_id"],
                "paper_url": row["paper_url"],
                "pdf_filename": row["pdf_filename"],
            }
            for row in reader
        ]


def arxiv_abs_url_to_pdf_url(paper_url):
    match = re.search(r"arxiv\.org/abs/([^/?#]+)", paper_url)
    if not match:
        raise ValueError(f"Not a recognized arXiv abstract URL: {paper_url}")
    arxiv_id = match.group(1)
    return f"https://arxiv.org/pdf/{arxiv_id}"


def _is_valid_pdf(path):
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        return False

    with open(path, "rb") as f:
        header = f.read(5)
    if header != b"%PDF-":
        return False

    try:
        with pymupdf.open(path) as doc:
            return doc.page_count >= 1
    except Exception:
        return False


def download_pdf(paper_url, dest_path, timeout=REQUEST_TIMEOUT):
    if _is_valid_pdf(dest_path):
        return {"status": "skipped", "reason": "already exists and is valid", "path": dest_path}

    pdf_url = arxiv_abs_url_to_pdf_url(paper_url)
    part_path = dest_path + ".part"

    request = urllib.request.Request(pdf_url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response, open(part_path, "wb") as out_file:
            out_file.write(response.read())

        if not _is_valid_pdf(part_path):
            raise ValueError("Downloaded file failed PDF validation")

        os.replace(part_path, dest_path)
        return {"status": "downloaded", "path": dest_path}

    except Exception as e:
        if os.path.exists(part_path):
            os.remove(part_path)
        return {"status": "failed", "reason": str(e), "path": dest_path}


def download_papers(csv_path, raw_papers_dir, paper_id=None):
    targets = load_download_targets(csv_path)

    if paper_id is not None:
        targets = [t for t in targets if t["paper_id"] == paper_id]
        if not targets:
            raise ValueError(f"paper_id '{paper_id}' not found in {csv_path}")

    results = []
    for target in targets:
        dest_path = os.path.join(raw_papers_dir, target["pdf_filename"])
        result = download_pdf(target["paper_url"], dest_path)
        result["paper_id"] = target["paper_id"]
        results.append(result)

    return results
