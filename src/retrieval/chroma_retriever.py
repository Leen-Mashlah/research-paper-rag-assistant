from vector_store.chroma_store import get_persistent_client


def retrieve_from_chroma(db_path, collection_name, query_embedding, top_k=5):
    if top_k <= 0:
        raise ValueError("top_k must be positive")

    client = get_persistent_client(db_path)

    try:
        collection = client.get_collection(name=collection_name)
    except Exception as e:
        raise ValueError(
            f"Collection '{collection_name}' not found at '{db_path}': {e}"
        ) from e

    count = collection.count()
    if count == 0:
        raise ValueError(
            f"Collection '{collection_name}' at '{db_path}' contains zero records"
        )

    n_results = min(top_k, count)

    if hasattr(query_embedding, "tolist"):
        query_embedding = query_embedding.tolist()
    else:
        query_embedding = list(query_embedding)

    raw = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    results = []
    for chunk_id, metadata, distance, document in zip(
        raw["ids"][0], raw["metadatas"][0], raw["distances"][0], raw["documents"][0]
    ):
        results.append({
            "chunk_id": chunk_id,
            "paper_id": metadata["paper_id"],
            "paper_title": metadata["paper_title"],
            "pdf_filename": metadata["pdf_filename"],
            "page_number": metadata["page_number"],
            "text": document,
            "distance": distance,
        })

    return results
