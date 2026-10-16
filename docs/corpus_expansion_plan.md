# Corpus Expansion Plan

## 1. Current Corpus Summary

**Current number of papers**: 5 (P001–P005)

| paper_id | Title | primary_topic |
|---|---|---|
| P001 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Core RAG architectures |
| P002 | Dense Passage Retrieval for Open-Domain Question Answering | Retrieval methods |
| P003 | REALM: Retrieval-Augmented Language Model Pre-Training | Core RAG architectures |
| P004 | SELF-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection | Hallucination and grounded generation |
| P005 | Ragas: Automated Evaluation of Retrieval Augmented Generation | RAG evaluation |

**Current category distribution** (categories per `docs/dataset_scope.md`):

| Category | Current count |
|---|---|
| Core RAG architectures | 2 |
| Retrieval methods | 1 |
| Chunking and document processing | 0 |
| RAG evaluation | 1 |
| Hallucination and grounded generation | 1 |
| Knowledge Graph + RAG | 0 |
| Agentic RAG | 0 |

Three categories (Chunking/document processing, Knowledge Graph + RAG, Agentic RAG) currently have zero representation.

## 2. Target Total Corpus Size

**37 papers** (P001–P037), within the planned 30–40 range stated in `dataset_scope.md`.

## 3. Final Category Distribution (Verified)

| Category | Current (P001–P005) | New (P006–P037) | Final total |
|---|---|---|---|
| Core RAG architectures | 2 | 4 | 6 |
| Retrieval methods | 1 | 6 | 7 |
| Chunking and document processing | 0 | 4 | 4 |
| RAG evaluation | 1 | 4 | 5 |
| Hallucination and grounded generation | 1 | 4 | 5 |
| Knowledge Graph + RAG | 0 | 5 | 5 |
| Agentic RAG | 0 | 5 | 5 |
| **Total** | **5** | **32** | **37** |

All 32 new-paper entries below (P006–P037) have been individually verified directly against their official arXiv abstract pages (title, authors, year, arXiv ID). Official arXiv titles are used as the canonical `title` throughout; any commonly used method nickname (e.g. FLARE, RAGTruth) is noted only as an alias in the relevance reason, never substituted for the official title.

## 4. Final Verified Candidate List (P006–P037)

### Core RAG architectures (4 new — total 6)

| paper_id | Title | Authors | Year | arXiv ID | Reason |
|---|---|---|---|---|---|
| P006 | Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering | Gautier Izacard, Edouard Grave | 2020 | 2007.01282 | Landmark alternative RAG architecture (Fusion-in-Decoder; fuses many retrieved passages in the decoder); directly comparable to P001. |
| P007 | Atlas: Few-shot Learning with Retrieval Augmented Language Models | Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas Hosseini, Fabio Petroni, Timo Schick, Jane Dwivedi-Yu, Armand Joulin, Sebastian Riedel, Edouard Grave | 2022 | 2208.03299 | Influential large-scale retrieval-augmented LM, extends FiD-style architecture to few-shot settings. |
| P008 | Improving language models by retrieving from trillions of tokens | Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, et al. | 2021 | 2112.04426 | Major architecture (RETRO) showing retrieval at massive scale integrated directly into the LM, a key "core architecture" reference point. |
| P009 | In-Context Retrieval-Augmented Language Models | Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, Yoav Shoham | 2023 | 2302.00083 | Modern, simple RAG variant (retrieval prepended to context without fine-tuning); good contrast to the fine-tuned architectures already in the corpus. |

### Retrieval methods (6 new — total 7)

| paper_id | Title | Authors | Year | arXiv ID | Reason |
|---|---|---|---|---|---|
| P010 | ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT | Omar Khattab, Matei Zaharia | 2020 | 2004.12832 | Foundational late-interaction retrieval method, a major alternative to DPR's single-vector bi-encoder already in the corpus. |
| P011 | Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval | Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk | 2020 | 2007.00808 | Influential hard-negative-mining training method (ANCE) for dense retrievers, complements DPR's in-batch-negative approach. |
| P012 | ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction | Keshav Santhanam, Omar Khattab, Jon Saad-Falcon, Christopher Potts, Matei Zaharia | 2021 | 2112.01488 | Widely used, compressed/improved successor to ColBERT. |
| P013 | SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking | Thibault Formal, Benjamin Piwowarski, Stéphane Clinchant | 2021 | 2107.05720 | Represents the sparse-neural-hybrid retrieval family, broadening the corpus beyond pure dense retrieval. |
| P014 | Unsupervised Dense Information Retrieval with Contrastive Learning | Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, Edouard Grave | 2021 | 2112.09118 | Important unsupervised dense retriever (Contriever), contrasts with DPR/ANCE's supervised training. |
| P018 | Query Rewriting for Retrieval-Augmented Large Language Models | Xinbei Ma, Yeyun Gong, Pengcheng He, Hai Zhao, Nan Duan | 2023 | 2305.14283 | Query-side rewriting to close the gap between input text and needed retrieval knowledge. **Recategorized from "Chunking and document processing" to "Retrieval methods"** — it operates on the query before retrieval, not on how the corpus is chunked/processed. |

### Chunking and document processing (4 new — total 4)

| paper_id | Title | Authors | Year | arXiv ID | Reason |
|---|---|---|---|---|---|
| P015 | Dense X Retrieval: What Retrieval Granularity Should We Use? | Tong Chen, Hongwei Wang, Sihao Chen, Wenhao Yu, Kaixin Ma, Xinran Zhao, Hongming Zhang, Dong Yu | 2023 | 2312.06648 | Directly studies chunk/retrieval-unit granularity (proposition-level vs passage-level), the most on-topic paper for this category. |
| P016 | RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval | Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, Christopher D. Manning | 2024 | 2401.18059 | Hierarchical/tree-based chunk organization and summarization, directly relevant to document-processing strategy. |
| P017 | Lost in the Middle: How Language Models Use Long Contexts | Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang | 2023 | 2307.03172 | Informs chunk size/ordering decisions by showing position-in-context effects on usage of retrieved text. |
| P037 | LongRAG: Enhancing Retrieval-Augmented Generation with Long-context LLMs | Ziyan Jiang, Xueguang Ma, Wenhu Chen | 2024 | 2406.15319 | Studies retrieval-unit granularity from the opposite direction of P015/P016 — processing whole documents as large ("long") units instead of small chunks, directly relevant to chunking/document-processing strategy. Added to backfill this category after P018 was recategorized out of it. |

### RAG evaluation (4 new — total 5)

| paper_id | Title | Authors | Year | arXiv ID | Reason |
|---|---|---|---|---|---|
| P019 | ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems | Jon Saad-Falcon, Omar Khattab, Christopher Potts, Matei Zaharia | 2023 | 2311.09476 | A direct peer/competitor evaluation framework to Ragas (P005), good for comparative evaluation-methodology coverage. |
| P020 | Benchmarking Large Language Models in Retrieval-Augmented Generation | Jiawei Chen, Hongyu Lin, Xianpei Han, Le Sun | 2023 | 2309.01431 | A dedicated RAG benchmark (RGB) covering noise robustness, negative rejection, and counterfactual robustness. |
| P021 | KILT: a Benchmark for Knowledge Intensive Language Tasks | Fabio Petroni, Aleksandra Piktus, Angela Fan, et al. | 2020 | 2009.02252 | Foundational knowledge-intensive-task benchmark widely used to evaluate RAG systems (including the original RAG paper, P001). |
| P022 | RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models | Cheng Niu, Yuanhao Wu, Juno Zhu, Siliang Xu, Kashun Shum, Randy Zhong, Juntong Song, Tong Zhang | 2024 | 2401.00396 | A hallucination benchmark built specifically for RAG systems (nearly 18,000 manually annotated RAG responses). **Replaces the originally proposed TruthfulQA entry**, which — despite being bibliographically correct — is a closed-book, no-retrieval benchmark and therefore a weak fit for the "RAG evaluation" category; RAGTruth is purpose-built for evaluating hallucination within RAG pipelines. |

### Hallucination and grounded generation (4 new — total 5)

| paper_id | Title | Authors | Year | arXiv ID | Reason |
|---|---|---|---|---|---|
| P023 | Survey of Hallucination in Natural Language Generation | Ziwei Ji, Nayeon Lee, Rita Frieske, et al. | 2022 | 2202.03629 | Broad, highly-cited survey framing the hallucination problem that grounded-generation methods (like SELF-RAG, P004) address. |
| P024 | RARR: Researching and Revising What Language Models Say, Using Language Models | Luyu Gao, Zhuyun Dai, Panupong Pasupat, Anthony Chen, Arun Tejasvi Chaganty, Yicheng Fan, Vincent Y. Zhao, Ni Lao, Hongrae Lee, Da-Cheng Juan, Kelvin Guu | 2022 | 2210.08726 | Post-hoc grounding/attribution-revision method, a different strategy than SELF-RAG's inline self-reflection. |
| P025 | Chain-of-Verification Reduces Hallucination in Large Language Models | Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, Xian Li, Asli Celikyilmaz, Jason Weston | 2023 | 2309.11495 | Self-verification method (nickname: CoVe), directly cited as concurrent work inside P004 (SELF-RAG); adds a comparable self-verification approach to the corpus. |
| P026 | FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, Wen-tau Yih, Pang Wei Koh, Mohit Iyyer, Luke Zettlemoyer, Hannaneh Hajishirzi | 2023 | 2305.14251 | The factuality metric already used to evaluate P004 (SELF-RAG) in its own results table — adds its source definition to the corpus. |

### Knowledge Graph + RAG (5 new — total 5)

| paper_id | Title | Authors | Year | arXiv ID | Reason |
|---|---|---|---|---|---|
| P027 | From Local to Global: A Graph RAG Approach to Query-Focused Summarization | Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, Jonathan Larson | 2024 | 2404.16130 | The most prominent recent "GraphRAG" work combining knowledge graphs with RAG for query-focused summarization. |
| P028 | Unifying Large Language Models and Knowledge Graphs: A Roadmap | Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, Xindong Wu | 2023 | 2306.08302 | Broad, well-cited survey bridging LLMs and knowledge graphs, good framing/context paper for this category. |
| P029 | Knowledge-Augmented Language Model Prompting for Zero-Shot Knowledge Graph Question Answering | Jinheon Baek, Alham Fikri Aji, Amir Saffari | 2023 | 2306.04136 | Concrete method (KAPING) for injecting KG facts into prompts for zero-shot QA. |
| P030 | Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph | Jiashuo Sun, Chengjin Xu, Lumingyuan Tang, Saizhuo Wang, Chen Lin, Yeyun Gong, Lionel M. Ni, Heung-Yeung Shum, Jian Guo | 2023 | 2307.07697 | LLM reasoning guided by KG traversal (ToG), a distinct agentic-style KG+RAG mechanism. |
| P031 | Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning | Linhao Luo, Yuan-Fang Li, Gholamreza Haffari, Shirui Pan | 2023 | 2310.01061 | Complements Think-on-Graph with a planning-retrieval-reasoning framework (RoG) focused on faithful, interpretable KG-grounded reasoning. |

### Agentic RAG (5 new — total 5)

| paper_id | Title | Authors | Year | arXiv ID | Reason |
|---|---|---|---|---|---|
| P032 | ReAct: Synergizing Reasoning and Acting in Language Models | Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao | 2022 | 2210.03629 | Foundational agentic-reasoning-plus-action framework underlying most later agentic RAG approaches. |
| P033 | Reflexion: Language Agents with Verbal Reinforcement Learning | Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao | 2023 | 2303.11366 | Self-reflective agent loop conceptually related to SELF-RAG but framed as general agentic self-improvement. |
| P034 | Active Retrieval Augmented Generation | Zhengbao Jiang, Frank F. Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie Callan, Graham Neubig | 2023 | 2305.06983 | Agentic, on-demand retrieval during generation (nickname: FLARE) — directly cited inside P004 (SELF-RAG) as related concurrent work. |
| P035 | Toolformer: Language Models Can Teach Themselves to Use Tools | Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom | 2023 | 2302.04761 | Agentic tool-use framework (retrieval as one tool among several), also referenced inside P004. |
| P036 | Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity | Soyeong Jeong, Jinheon Baek, Sukmin Cho, Sung Ju Hwang, Jong C. Park | 2024 | 2403.14403 | Agentic routing between retrieval strategies based on query complexity. |

## 5. Design Notes

- Every entry in the list above was individually verified against its official arXiv abstract page (title, authors, year, arXiv ID) before being finalized in this plan.
- Official arXiv titles are used as the canonical `title` field throughout. Where a method has a commonly used nickname (FLARE for P034, RAGTruth already being the official title for P022, CoVe for P025), the nickname appears only in the relevance-reason text, never replacing the official title.
- Candidates were chosen to be **well-known, directly relevant, peer-reviewed or widely-cited preprints** rather than loosely related work.
- No duplicate papers, no duplicate arXiv IDs, and no alternate versions of works already in the corpus (e.g., no second REALM/DPR/RAG variant papers) are included.
- Several candidates (CoVe/P025, FActScore/P026, FLARE/P034, Toolformer/P035) were deliberately chosen because they are **already referenced inside P004 (SELF-RAG)** as related/concurrent work — adding them lets the corpus capture genuine citation relationships that already exist between papers, which should be useful for later cross-paper retrieval testing.
- P018 was moved from "Chunking and document processing" to "Retrieval methods" after relevance review, since it operates on the query side, not the corpus-processing side.
- P022 was replaced (TruthfulQA → RAGTruth) after relevance review found the original candidate lacked any retrieval/RAG component.
- P037 (LongRAG) was added to restore "Chunking and document processing" to 4 papers after P018 was moved out of it.
