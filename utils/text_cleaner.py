import re

def clean_text(text):

    text = re.sub(r'\n+', '\n', text)

    text = re.sub(r'Page \d+ of \d+', '', text)

    return text.strip()