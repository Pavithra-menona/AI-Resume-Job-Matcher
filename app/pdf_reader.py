from pypdf import PdfReader


def extract_text_from_pdf(file):

    reader = PdfReader(file)

    text_parts = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text_parts.append(page_text)

    text = "\n".join(text_parts)

    return text.strip()