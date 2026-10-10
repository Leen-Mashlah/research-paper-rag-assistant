import re

from ingestion.text_cleaner import clean_text

_SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9])")


def _split_into_sentences(text):
    if not text:
        return []

    sentences = []
    last_end = 0
    for match in _SENTENCE_BOUNDARY.finditer(text):
        end = match.end()
        sentences.append(text[last_end:end])
        last_end = end

    if last_end < len(text):
        sentences.append(text[last_end:])

    return sentences


def _split_long_text_on_whitespace(text, size):
    pieces = []
    start = 0
    length = len(text)

    while start < length:
        end = min(start + size, length)

        if end < length:
            split_at = max(
                text.rfind(" ", start, end),
                text.rfind("\n", start, end),
            )
            if split_at <= start:
                split_at = end
                next_start = end
            else:
                next_start = split_at + 1
        else:
            split_at = end
            next_start = end

        piece = text[start:split_at]
        if piece.strip():
            pieces.append(piece)
        start = next_start

    return pieces


def _build_overlap_sentences(sentences, overlap_budget):
    if not sentences or overlap_budget <= 0:
        return []

    result = []
    total = 0
    for sentence in reversed(sentences):
        if not result:
            result.append(sentence)
            total += len(sentence)
            continue
        if total + len(sentence) <= overlap_budget:
            result.append(sentence)
            total += len(sentence)
        else:
            break

    result.reverse()
    return result


def chunk_pages(pages, chunk_size=1200, overlap=200):
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    chunk_counter = 0

    for page in pages:
        cleaned = clean_text(page["text"])
        if not cleaned:
            continue

        sentences = _split_into_sentences(cleaned)
        current = []
        current_len = 0

        for sentence in sentences:
            sentence_len = len(sentence)

            if sentence_len > chunk_size:
                if current:
                    chunk_text = "".join(current).strip()
                    if chunk_text:
                        chunk_counter += 1
                        chunks.append({
                            "chunk_id": f"CH{chunk_counter:04d}",
                            "page_number": page["page_number"],
                            "text": chunk_text,
                        })
                    current = []
                    current_len = 0

                for piece in _split_long_text_on_whitespace(sentence, chunk_size):
                    piece_text = piece.strip()
                    if piece_text:
                        chunk_counter += 1
                        chunks.append({
                            "chunk_id": f"CH{chunk_counter:04d}",
                            "page_number": page["page_number"],
                            "text": piece_text,
                        })
                continue

            if current and current_len + sentence_len > chunk_size:
                chunk_text = "".join(current).strip()
                if chunk_text:
                    chunk_counter += 1
                    chunks.append({
                        "chunk_id": f"CH{chunk_counter:04d}",
                        "page_number": page["page_number"],
                        "text": chunk_text,
                    })

                overlap_sentences = _build_overlap_sentences(current, overlap)
                current = list(overlap_sentences)
                current_len = sum(len(s) for s in current)

            current.append(sentence)
            current_len += sentence_len

        if current:
            chunk_text = "".join(current).strip()
            if chunk_text:
                chunk_counter += 1
                chunks.append({
                    "chunk_id": f"CH{chunk_counter:04d}",
                    "page_number": page["page_number"],
                    "text": chunk_text,
                })

    return chunks
