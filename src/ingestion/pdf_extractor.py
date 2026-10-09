import pymupdf


def extract_pdf_pages(pdf_path):
    pages = []
    with pymupdf.open(pdf_path) as doc:
        for index, page in enumerate(doc):
            pages.append({
                "page_number": index + 1,
                "text": page.get_text(),
            })
    return pages
