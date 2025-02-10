from pathlib import Path

DATA_DIR = Path("data")

BOOK_LIBRARY_FILE = DATA_DIR / "book_library.json"
PERSONAL_LIBRARY_FILE = DATA_DIR / "personal_library.json"
BOOK_GENRES_FILE = DATA_DIR / "book_genres.json"

def json_path(filename):
    return DATA_DIR / filename

LOG_FILE = Path("log.txt")