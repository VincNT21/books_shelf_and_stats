
"""import os

current_dir = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(current_dir, "data")

ASSETS_DIR = os.path.join(current_dir, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
ICONS_DIR = os.path.join(IMAGES_DIR, "icons")


BOOK_LIBRARY_FILE = os.path.join(DATA_DIR, "book_library.json")
PERSONAL_LIBRARY_FILE = os.path.join(DATA_DIR, "personal_library.json")
BOOK_GENRES_FILE = os.path.join(DATA_DIR, "book_genres.json")

def file_path_in_data(filename):
    return os.path.join(DATA_DIR, filename)

def file_path_in_icons(icon_name):
    return os.path.join(ICONS_DIR, icon_name)

def file_path_in_images(image_name):
    return os.path.join(IMAGES_DIR, image_name)

LOG_FILE = os.path.abspath("log.txt")"""


from pathlib import Path

DATA_DIR = Path("data")

ASSETS_DIR = Path("assets")
IMAGES_DIR = ASSETS_DIR / "images"
ICONS_DIR = IMAGES_DIR / "icons"

BOOK_LIBRARY_FILE = DATA_DIR / "book_library.json"
PERSONAL_LIBRARY_FILE = DATA_DIR / "personal_library.json"
BOOK_GENRES_FILE = DATA_DIR / "book_genres.json"

def file_path_in_data(filename):
    return DATA_DIR / filename

def file_path_in_icons(icon_name):
    return ICONS_DIR / icon_name

def file_path_in_images(image_name):
    return (IMAGES_DIR / image_name)

LOG_FILE = Path("log.txt")