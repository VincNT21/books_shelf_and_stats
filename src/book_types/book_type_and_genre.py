from config import BOOK_GENRES_FILE
from helpers.logging_utils import log_error
from helpers.normalize_text import normalize_text
import json

class BookGenres:
    def __init__(self):
        self.genre_file = BOOK_GENRES_FILE
        self._valid_genres = self._load_file()

    def _load_file(self):
        try:
            with self.genre_file.open("r") as f:
                return json.load(f)
        except OSError as e:
            log_error(f"Error: Failed to read from {self.genre_file}. Reason: {e}")
        
    def _dump_file(self):
        try:
            with self.genre_file.open("w") as f:
                json.dump(self._valid_genres, f)
        except OSError as e:
            log_error(f"Error: Failed to write to {self.genre_file}. Reason: {e}")

    def add_main_genre(self, new_main_genre):
        normalized = normalize_text(new_main_genre)
        self._valid_genres[new_main_genre] = []
        self._dump_file()
        print(f"New main genre added : {new_main_genre}")
        return normalized
    
    def add_sub_genre(self, main_genre, new_sub_genre):
        if self.is_main_genre_exist(main_genre):
            normalized = normalize_text(new_sub_genre)
            self._valid_genres[main_genre].append(new_sub_genre)
            print(f"New sub genre added in {main_genre}: {new_sub_genre}")
            return normalized

    def is_main_genre_exist(self, main_genre):
        return main_genre in self._valid_genres
    
    def is_sub_genre_exist(self, main_genre, sub_genre):
        if self.is_main_genre_exist(main_genre) == False:
            raise KeyError("Main genre doesn't exist")
        else:
            return sub_genre in self._valid_genres[main_genre]
    
    def get_all_types(self):
        return self._valid_genres