import csv


def load_paper_metadata(csv_path):
    metadata_by_filename = {}

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pdf_filename = row.get("pdf_filename", "").strip()
            if not pdf_filename:
                raise ValueError("Encountered a row with a missing or empty pdf_filename")

            if pdf_filename in metadata_by_filename:
                raise ValueError(f"Duplicate pdf_filename found in metadata CSV: {pdf_filename}")

            metadata_by_filename[pdf_filename] = row

    return metadata_by_filename


def enrich_chunks_with_paper_metadata(chunks, paper_metadata):
    paper_id = paper_metadata.get("paper_id", "").strip()
    paper_title = paper_metadata.get("title", "").strip()
    pdf_filename = paper_metadata.get("pdf_filename", "").strip()

    if not paper_id:
        raise ValueError("paper_metadata is missing a non-empty paper_id")
    if not paper_title:
        raise ValueError("paper_metadata is missing a non-empty title")
    if not pdf_filename:
        raise ValueError("paper_metadata is missing a non-empty pdf_filename")

    enriched = []
    for chunk in chunks:
        enriched_chunk = dict(chunk)
        enriched_chunk["chunk_id"] = f"{paper_id}-{chunk['chunk_id']}"
        enriched_chunk["paper_id"] = paper_id
        enriched_chunk["paper_title"] = paper_title
        enriched_chunk["pdf_filename"] = pdf_filename
        enriched.append(enriched_chunk)

    return enriched
