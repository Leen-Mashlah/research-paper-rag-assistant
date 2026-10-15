import numpy as np


def cosine_similarity_scores(query_embedding, passage_embeddings):
    return passage_embeddings @ query_embedding


def retrieve_top_k(query_embedding, passage_embeddings, chunks, top_k=5):
    if len(passage_embeddings) != len(chunks):
        raise ValueError("Number of passage embeddings must match number of chunks")
    if top_k <= 0:
        raise ValueError("top_k must be positive")

    scores = cosine_similarity_scores(query_embedding, passage_embeddings)
    k = min(top_k, len(chunks))
    ranked_indices = np.argsort(-scores)[:k]

    results = []
    for idx in ranked_indices:
        result = dict(chunks[idx])
        result["similarity_score"] = float(scores[idx])
        results.append(result)

    return results
