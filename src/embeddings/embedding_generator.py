from sentence_transformers import SentenceTransformer

DEFAULT_MODEL_NAME = "intfloat/multilingual-e5-small"


def load_embedding_model(model_path=None, device="cpu"):
    model_name_or_path = model_path if model_path else DEFAULT_MODEL_NAME
    return SentenceTransformer(model_name_or_path, device=device, local_files_only=True)


def embed_passages(model, chunks):
    texts = ["passage: " + chunk["text"] for chunk in chunks]
    return model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)


def embed_query(model, query):
    text = "query: " + query
    return model.encode(text, convert_to_numpy=True, normalize_embeddings=True)
