import re


def clean_text(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\x00", "")
    text = text.replace("\t", " ")

    lines = text.split("\n")
    cleaned_lines = [re.sub(r" {2,}", " ", line.strip()) for line in lines]
    text = "\n".join(cleaned_lines)

    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text
