from pathlib import Path

DATA_DIR = Path("data")

ASSETS_DIR = Path("assets")
ICONS_DIR = ASSETS_DIR / "images" / "icons"

BOOK_LIBRARY_FILE = DATA_DIR / "book_library.json"
PERSONAL_LIBRARY_FILE = DATA_DIR / "personal_library.json"
BOOK_GENRES_FILE = DATA_DIR / "book_genres.json"

def file_path_in_data(filename):
    return DATA_DIR / filename

def file_path_in_icons(icon_name):
    return ICONS_DIR / icon_name

LOG_FILE = Path("log.txt")
