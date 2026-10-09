# Dataset Scope

## Project Domain

Retrieval-Augmented Generation (RAG) and related research.

## Planned Dataset Size

Approximately 30–40 research papers.

## Main Paper Categories

- Core RAG architectures
- Retrieval methods
- Chunking and document processing
- RAG evaluation
- Hallucination and grounded generation
- Knowledge Graph + RAG
- Agentic RAG

## Paper Metadata

For each research paper, we plan to store the following metadata:

- `paper_id`
- `title`
- `authors`
- `publication_year`
- `source`
- `paper_url`
- `pdf_filename`
- `primary_topic`
- `language`

## Chunk-Level Metadata (Future PDF Processing)

Later, during PDF processing, each extracted text chunk should preserve the following fields so that retrieval results can be traced back to their original context:

- `paper_id`
- `paper title`
- `page number`
- `section name` (when detectable)
- `chunk text`
- `chunk identifier`

This ensures that every chunk returned by the retrieval system remains linked to its source paper, page, and section, which supports citation, evaluation, and debugging of the RAG pipeline.
