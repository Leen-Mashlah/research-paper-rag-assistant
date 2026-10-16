import os
from collections import Counter

from ingestion.pdf_extractor import extract_pdf_pages
from ingestion.paper_metadata import load_paper_metadata, enrich_chunks_with_paper_metadata
from chunking.text_chunker import chunk_pages
from embeddings.embedding_generator import load_embedding_model, embed_passages
from vector_store.chroma_store import get_persistent_client, get_or_create_collection, add_chunks


def build_corpus_index(
    raw_papers_dir,
    metadata_csv_path,
    db_path,
    collection_name="research_papers",
    model_path=None,
    device="cpu",
    chunk_size=1200,
    overlap=200,
):
    client = get_persistent_client(db_path)
    collection = get_or_create_collection(client, collection_name)

    existing_count = collection.count()
    if existing_count > 0:
        raise RuntimeError(
            f"Collection '{collection_name}' at '{db_path}' already contains "
            f"{existing_count} records. Refusing to add duplicates."
        )

    metadata_by_filename = load_paper_metadata(metadata_csv_path)

    all_enriched = []
    for pdf_filename, paper_meta in metadata_by_filename.items():
        pdf_path = os.path.join(raw_papers_dir, pdf_filename)
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(
                f"PDF file not found for paper '{paper_meta.get('paper_id')}': {pdf_path}"
            )

        pages = extract_pdf_pages(pdf_path)
        chunks = chunk_pages(pages, chunk_size=chunk_size, overlap=overlap)
        enriched = enrich_chunks_with_paper_metadata(chunks, paper_meta)
        all_enriched.extend(enriched)

    if not all_enriched:
        raise ValueError("No chunks were produced from the corpus")

    chunk_ids = [chunk["chunk_id"] for chunk in all_enriched]
    if len(chunk_ids) != len(set(chunk_ids)):
        raise ValueError("Duplicate chunk IDs detected while building the corpus index")

    model = load_embedding_model(model_path=model_path, device=device)
    embeddings = embed_passages(model, all_enriched)

    add_chunks(collection, all_enriched, embeddings.tolist())

    chunk_count_by_paper = dict(Counter(chunk["paper_id"] for chunk in all_enriched))

    return {
        "total_papers_indexed": len(metadata_by_filename),
        "total_chunks_indexed": len(all_enriched),
        "embedding_dimension": embeddings.shape[1],
        "chunk_count_by_paper": chunk_count_by_paper,
        "database_path": db_path,
        "collection_name": collection_name,
    }
