import hashlib
import unicodedata
from helpers.normalize_text import normalize_text_for_id


def generate_id(title, author):
    clean_title = normalize_text_for_id(title)
    clean_author = normalize_text_for_id(author)
    text_to_hash = f"{clean_title}{clean_author}"
    return hashlib.md5(text_to_hash.encode()).hexdigest()