import csv

from embeddings.embedding_generator import load_embedding_model, embed_query
from retrieval.chroma_retriever import retrieve_from_chroma


def load_evaluation_questions(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def _build_valid_paper_set(row):
    primary = row["primary_expected_paper_id"].strip()
    acceptable_raw = row.get("acceptable_paper_ids", "").strip()
    acceptable = [p.strip() for p in acceptable_raw.split(";") if p.strip()] if acceptable_raw else []
    return set([primary]) | set(acceptable)


def evaluate_question(model, db_path, collection_name, row, top_k=5):
    valid_papers = _build_valid_paper_set(row)

    query_embedding = embed_query(model, row["question"])
    results = retrieve_from_chroma(db_path, collection_name, query_embedding, top_k=top_k)

    first_valid_rank = None
    for rank, result in enumerate(results, start=1):
        if result["paper_id"] in valid_papers:
            first_valid_rank = rank
            break

    top1_hit = first_valid_rank == 1
    hit_at_3 = first_valid_rank is not None and first_valid_rank <= 3
    hit_at_5 = first_valid_rank is not None and first_valid_rank <= 5
    reciprocal_rank_at_5 = (1.0 / first_valid_rank) if hit_at_5 else 0.0

    return {
        "question_id": row["question_id"],
        "question": row["question"],
        "primary_expected_paper_id": row["primary_expected_paper_id"],
        "acceptable_paper_ids": row.get("acceptable_paper_ids", ""),
        "question_category": row["question_category"],
        "first_valid_rank": first_valid_rank,
        "top1_hit": top1_hit,
        "hit_at_3": hit_at_3,
        "hit_at_5": hit_at_5,
        "reciprocal_rank_at_5": reciprocal_rank_at_5,
        "retrieved_top5_paper_ids": [result["paper_id"] for result in results],
        "retrieved_top5_chunk_ids": [result["chunk_id"] for result in results],
    }


def run_evaluation(csv_path, db_path, collection_name="research_papers", model_path=None, device="cpu", top_k=5):
    questions = load_evaluation_questions(csv_path)
    model = load_embedding_model(model_path=model_path, device=device)

    return [
        evaluate_question(model, db_path, collection_name, row, top_k=top_k)
        for row in questions
    ]


def _aggregate(results):
    n = len(results)
    if n == 0:
        return {"count": 0, "top1_accuracy": 0.0, "hit_at_3": 0.0, "hit_at_5": 0.0, "mrr_at_5": 0.0}

    return {
        "count": n,
        "top1_accuracy": sum(1 for r in results if r["top1_hit"]) / n,
        "hit_at_3": sum(1 for r in results if r["hit_at_3"]) / n,
        "hit_at_5": sum(1 for r in results if r["hit_at_5"]) / n,
        "mrr_at_5": sum(r["reciprocal_rank_at_5"] for r in results) / n,
    }


def compute_metrics(results):
    by_paper = {
        paper_id: _aggregate([r for r in results if r["primary_expected_paper_id"] == paper_id])
        for paper_id in sorted(set(r["primary_expected_paper_id"] for r in results))
    }

    by_category = {
        category: _aggregate([r for r in results if r["question_category"] == category])
        for category in sorted(set(r["question_category"] for r in results))
    }

    return {
        "overall": _aggregate(results),
        "by_paper": by_paper,
        "by_category": by_category,
    }
