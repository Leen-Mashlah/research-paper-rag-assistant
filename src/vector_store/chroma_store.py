import chromadb


def get_persistent_client(path):
    return chromadb.PersistentClient(path=path)


def get_or_create_collection(client, name):
    return client.get_or_create_collection(
        name=name,
        metadata={"hnsw:space": "cosine"},
    )


def add_chunks(collection, chunks, embeddings):
    ids = [chunk["chunk_id"] for chunk in chunks]
    documents = [chunk["text"] for chunk in chunks]
    metadatas = [
        {
            "paper_id": chunk["paper_id"],
            "paper_title": chunk["paper_title"],
            "pdf_filename": chunk["pdf_filename"],
            "page_number": chunk["page_number"],
        }
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )
