import unicodedata
import string

def normalize_text_for_id(text):
    return clean_text_no_whitespace(remove_accents(text))

def normalize_text(text):
    return clean_and_capitalized(remove_accents(text))

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))

def clean_text_no_whitespace(text):
    return ''.join(c for c in text.casefold() if c.isalnum())

def clean_and_capitalized(text):
    for char in string.punctuation:
        text = text.replace(char, " ")
    text = " ".join(text.split())
    return text.title()

