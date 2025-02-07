import hashlib
import unicodedata


def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))

def clean_text(text):
    return ''.join(c for c in text.casefold() if c.isalnum())

def generate_id(title, author):
    clean_title = clean_text(remove_accents(title))
    clean_author = clean_text(remove_accents(author))
    text_to_hash = f"{clean_title}{clean_author}"
    return hashlib.md5(text_to_hash.encode()).hexdigest()