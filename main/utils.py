import re
from transliterate import translit




def make_slug(text):
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'\s+', '-', text)
    text = translit(text, 'ru', reversed=True)
    text = re.sub(r'[^a-z0-9-]+', '', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')

    return text
