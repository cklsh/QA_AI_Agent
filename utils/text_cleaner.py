import re

def clean_text(text):

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n", "\n", text)

    # Remove page numbers
    text = re.sub(r"Page\s+\d+\s+of\s+\d+", "", text, flags=re.IGNORECASE)

    # Remove standalone page numbers
    text = re.sub(r"^\d+$", "", text, flags=re.MULTILINE)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()